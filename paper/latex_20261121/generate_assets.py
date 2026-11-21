"""Generate manuscript tables and figures from immutable experiment records."""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIG = HERE / 'figures'
FIG.mkdir(exist_ok=True)
sources = {}
def read(rel):
    p = ROOT / rel
    sources[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text(encoding='utf-8'))
pose = read('output/centering_corrected_cpu_20261115/summary.json')
center = read('output/centering_corrected_cpu_20261115/centering_comparison.json')
controls = read('output/input_controls_20261115/summary.json')
rgb = read('output/video_baseline_v2_20261115/summary.json')
frozen = read('output/rwf_supervised_20261115/metrics.json')
promotion = read('output/rwf_finetune_v2_20261115/promotion.json')
history = read('output/rwf_finetune_v2_20261115/training_history.json')
rwf = read('output/final_delivery_20261115/rwf_evaluation/metrics.json')
hockey = read('output/external_validation_20261115/metrics.json')
runtime = read('output/runtime_20261115/summary.json')
audit = read('output/final_delivery_20261115/demo_audit.json')
coverage = read('output/coverage_ablation_20261114/coverage_comparison.json')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'ps.fonttype':42})
names = {'baseline':'Baseline','reliability':'Reliability','interactions':'Interactions','combined':'Combined','motion_linear':'Motion linear','pose_quality_only':'Quality only'}
def table(filename, caption, label, header, rows, cols, wide=False, note=''):
    env = 'table*' if wide else 'table'
    s = f'\\begin{{{env}}}[t]\n\\caption{{{caption}}}\n\\label{{{label}}}\\centering\n'
    s += '\\begin{tabular}{'+cols+'}\n\\toprule\n'+' & '.join(header)+'\\\\\n\\midrule\n'
    s += '\n'.join(' & '.join(str(x) for x in row)+'\\\\' for row in rows)
    s += '\n\\bottomrule\n\\end{tabular}\n'
    if note:s += '\\par\\smallskip\\parbox{'+('\\textwidth' if wide else '\\columnwidth')+'}{\\footnotesize '+note+'}\n'
    s += f'\\end{{{env}}}\n'
    (HERE/'sections'/filename).write_text(s,encoding='utf-8')
def percent(v, digits=1):return f'{100*v:.{digits}f}\\%'
def dec(v):return f'{v:.3f}'
pose_rows=[]
for m in pose['models']:
    z=m['fold_seed_mean']
    pose_rows.append([names[m['variant']],m['completed_runs'],f"{100*z['accuracy']['mean']:.1f} $\\pm$ {100*z['accuracy']['descriptive_std']:.1f}",dec(z['macro_f1']['mean']),dec(z['roc_auc']['mean'])])
table('table_pose.tex','Corrected CPU crowd results. Accuracy is in percent. The spread is descriptive fold/seed standard deviation.','tab:pose',['Model','Fits','Accuracy','F1','AUC'],pose_rows,'lrrrr',note='F1 denotes macro-F1. TCNs have 15 fits per variant; deterministic controls have five fits. Dependent runs do not provide confidence intervals.')
table('table_center.tex','Matched CPU centering comparison. Changes use unrounded source values and percentage points (pp).','tab:center',['Variant','Legacy','Corrected','Change'],[[names[m['variant']],percent(m['original']['accuracy']['mean']),percent(m['corrected']['accuracy']['mean']),f"{100*m['paired_delta']['accuracy']['mean']:+.2f} pp"] for m in center['models']],'lrrr')
table('table_controls.tex','Matched corrected combined-TCN GPU input controls. Accuracy is mean percent with descriptive standard deviation.','tab:controls',['Condition','Accuracy','F1','AUC'],[[{'full':'Full','detection_only':'Detection only','shuffled_time':'Shuffled time'}[m['condition']],f"{100*m['fold_seed_mean']['accuracy']['mean']:.1f} $\\pm$ {100*m['fold_seed_mean']['accuracy']['descriptive_std']:.1f}",dec(m['fold_seed_mean']['macro_f1']['mean']),dec(m['fold_seed_mean']['roc_auc']['mean'])] for m in controls['models']],'lrrr')
val=promotion['candidate_validation']['validation']
table('table_validation.tex','RWF validation comparison on 317 clips. The chosen fine-tuned checkpoint is epoch 2.','tab:validation',['Metric','Frozen','Fine-tuned'],[['Log loss','0.393','0.337'],['Accuracy',percent(frozen['validation']['accuracy']),percent(val['accuracy'])],['Macro-F1',dec(frozen['validation']['macro_f1']),dec(val['macro_f1'])],['Fight recall',percent(frozen['validation']['recall_violent']),percent(val['recall_violent'])],['Threshold','0.50','0.23']],'lrr')
eval_rows=[]
for dataset,record in [('RWF',rwf),('Hockey',hockey)]:
    for key,model in record['models'].items():
        m=model['all_clips'];cm=m['confusion_matrix']
        assert sum(map(sum,cm)) == m['n']
        assert abs((cm[0][0]+cm[1][1])/m['n']-m['accuracy'])<1e-10
        short={'rwf_frozen_video':'Frozen video','rwf_finetuned_video':'Fine-tuned video','crowd_pose_interactions':'Crowd pose'}[key]
        eval_rows.append([dataset,short,m['n'],f"{model['threshold']:.2f}",percent(m['accuracy'],2),dec(m['macro_f1']),dec(m['roc_auc']),percent(m['precision_violent']),percent(m['recall_violent']),cm[0][1],cm[1][0]])
table('table_evaluation.tex','Fixed all-clip evaluation. Fight is positive. FP counts nonviolent clips flagged violent, and FN counts missed violent clips.','tab:evaluation',['Set','Model','$n$','$\\tau$','Accuracy','F1','AUC','Precision','Recall','FP','FN'],eval_rows,'llrrrrrrrrr',wide=True,note='RWF results use previously inspected footage. All 1,000 Hockey mirror clips remain. The frozen video reference is the predeclared primary external model; fine-tuning is supplementary and crowd pose is diagnostic.')
table('table_runtime.tex','Offline pose timing on ten fixed clips. Overlay generation and export are excluded.','tab:runtime',['Measurement','Median (s)','p95 (s)'],[['Warm pipeline (30 runs)',f"{runtime['warm_pipeline_seconds']['median']:.3f}",f"{runtime['warm_pipeline_seconds']['p95']:.3f}"],['Cold external process (10)',f"{runtime['cold_external_process_seconds']['median']:.3f}",f"{runtime['cold_external_process_seconds']['p95']:.3f}"]],'lrr')
def save(fig,name):
    fig.savefig(FIG/(name+'.pdf'),bbox_inches='tight',pad_inches=.04)
    fig.savefig(FIG/(name+'.png'),dpi=220,bbox_inches='tight',pad_inches=.04)
    plt.close(fig)

fig,ax=plt.subplots(figsize=(7.16,2.55));ax.set_xlim(0,10.2);ax.set_ylim(0,4.2);ax.axis('off')
boxes=[(.25,1.65,1.8,.9,'Full clip\nDecode\n32 samples'),(2.55,2.8,2.1,.9,'Pretrained pose\nClip-local tracks'),(5.0,2.8,2.05,.9,'Corrected features\nReliability and\ninteraction variants'),(7.55,2.8,2.1,.9,'Shared person TCN\nMasked pooling\nClip score'),(2.55,.45,2.1,.9,'Two windows\n16 frames each\nFrozen R3D-18'),(5.0,.45,2.05,.9,'Train-only scaling\nLogistic head\nClip score'),(7.55,.45,2.1,.9,'RWF layer4 tuning\nValidation selection\nClip score')]
for x,y,w,h,t in boxes:
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03',facecolor='#f0f0f0',edgecolor='#555'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=8)
for a,b in [((2.05,2.35),(2.55,3.25)),((2.05,1.85),(2.55,.9)),((4.65,3.25),(5.0,3.25)),((7.05,3.25),(7.55,3.25)),((4.65,.9),(5.0,.9)),((7.05,.9),(7.55,.9))]:ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'#444'})
ax.text(6.05,2.05,'Whole-clip scores with fixed decision thresholds',ha='center',va='center',fontsize=8.5)
save(fig,'pipeline')

fig,ax=plt.subplots(figsize=(3.5,2.65));fig.subplots_adjust(left=.29,right=.98,bottom=.2,top=.97);models=pose['models'];means=[100*m['fold_seed_mean']['accuracy']['mean'] for m in models];std=[100*m['fold_seed_mean']['accuracy']['descriptive_std'] for m in models]
labels=[names[m['variant']] for m in models]
ax.barh(np.arange(len(models)),means,xerr=std,capsize=2,color=['#9a9a9a']*4+['#c9c9c9']*2,edgecolor='#444',linewidth=.5)
ax.set_yticks(np.arange(len(models)),labels,fontsize=8);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('Accuracy (%)');ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
save(fig,'pose_results')

fig,ax=plt.subplots(figsize=(3.5,2.3));epochs=[z['epoch'] for z in history];loss=[z['validation_log_loss'] for z in history]
ax.plot(epochs,loss,'o-',color='#333',markersize=3,label='Fine-tuning validation')
ax.axhline(.39298102478645885,color='#888',linestyle='--',label='Frozen reference')
ax.plot(2,loss[1],'o',color='#087f83',markersize=6);ax.set_xlabel('Epoch');ax.set_ylabel('Validation log loss');ax.set_xticks(epochs);ax.legend(fontsize=7,frameon=False);ax.grid(alpha=.2)
save(fig,'validation_loss')

fig,axes=plt.subplots(1,2,figsize=(7.16,2.55))
for ax,(key,model) in zip(axes,rwf['models'].items()):
    cm=np.array(model['all_clips']['confusion_matrix']);ax.imshow(cm,cmap='Greys',vmin=0,vmax=200)
    for i in range(2):
        for j in range(2):ax.text(j,i,str(cm[i,j]),ha='center',va='center',color='white' if cm[i,j]>100 else 'black',fontsize=13)
    ax.set_xticks([0,1],['NonFight','Fight']);ax.set_yticks([0,1],['NonFight','Fight']);ax.set_xlabel('Predicted label');ax.set_ylabel('Supplied label');ax.set_title(('Frozen video' if key=='rwf_frozen_video' else 'Fine-tuned video')+f" ($\\tau={model['threshold']:.2f}$)")
save(fig,'rwf_confusion')

fig,ax=plt.subplots(figsize=(3.5,2.6));keys=list(hockey['models']);x=np.arange(len(keys));w=.34
ax.bar(x-w/2,[100*hockey['models'][k]['all_clips']['accuracy'] for k in keys],w,color='#666',label='Accuracy')
ax.bar(x+w/2,[100*hockey['models'][k]['all_clips']['recall_violent'] for k in keys],w,color='#bbb',edgecolor='#666',label='Fight recall')
ax.set_xticks(x,['Frozen\nvideo','Fine-tuned\nvideo','Crowd\npose']);ax.set_ylim(0,100);ax.set_ylabel('Percent');ax.legend(fontsize=7,frameon=False);ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
save(fig,'external_results')

fig,axes=plt.subplots(1,2,figsize=(7.16,2.5))
fig.subplots_adjust(wspace=.45)
for ax,vals,title,unit in [(axes[0],[1000*z['pipeline_seconds'] for z in runtime['warm']],'Warm pipeline, 30 runs','Milliseconds'),(axes[1],[z['external_process_wall_seconds'] for z in runtime['cold']],'Cold external process, 10 runs','Seconds')]:
    ax.plot(np.arange(1,len(vals)+1),vals,'o',markersize=3,color='#555');ax.axhline(np.median(vals),color='#087f83',linestyle='--');ax.set_xlabel('Recorded run');ax.set_ylabel(unit);ax.set_title(title);ax.grid(alpha=.2)
save(fig,'runtime_runs')

fig,axes=plt.subplots(1,2,figsize=(7.16,2.9))
for ax,key in zip(axes,['false_positive','false_negative']):
    rel='output/final_delivery_20261115/demos/'+key+'.jpg';p=ROOT/rel;sources[rel]=hashlib.sha256(p.read_bytes()).hexdigest();im=Image.open(p).crop((55,120,746,620));ax.imshow(im);ax.axis('off');ax.set_title(key.replace('_',' ').capitalize(),fontsize=10)
save(fig,'failure_examples')

checkpoints={}
for rel in ['output/centering_corrected_cpu_20261115/fold_1/runs/interactions_seed42/model.pt','output/rwf_supervised_20261115/model.json','output/rwf_finetune_v2_20261115/model.pt']:
    checkpoints[rel]=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
facts={'sources':sources,'checkpoints':checkpoints,'pose_accuracy':means,'rgb_accuracy':100*rgb['fold_mean']['accuracy']['mean'],'selected_epoch':promotion['chosen_epoch'],'selected_threshold':promotion['candidate_validation']['threshold'],'evaluation_rows':eval_rows}
(HERE/'evidence_manifest.json').write_text(json.dumps(facts,indent=2),encoding='utf-8')
print('Generated six tables and seven figures from',len(sources),'source artifacts')
