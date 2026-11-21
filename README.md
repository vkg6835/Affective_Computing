# Crowd violence and Goon detection

This project runs raw crowd videos through multi-person pose extraction, within-clip tracking, motion/interaction features, a small temporal convolutional network, and binary clip prediction. It implements the four configurations described in `presentations/Stage1_Crowd_Violence_Detection.pptx`.

## Complete paper draft: 21 November 2026

**Violence and Goon Detection in a Crowd or Protest**

The checked IEEE TAI draft is 14 pages, with nine tables, seven figures,
and 18 references. The original project title is restored, and running
header text is removed.

- [Read or download the paper PDF](output/pdf/paper_20261121/manuscript.pdf)
- [Download the complete editable LaTeX file](output/pdf/paper_20261121/complete_paper.tex)
- [Download the single-file Overleaf project ZIP](output/pdf/paper_20261121/overleaf_single_file.zip)
- [Download the sectioned Overleaf project ZIP](output/pdf/paper_20261121/overleaf_source.zip)
- [Author and professor review notes](paper/latex_20261121/REVIEW_NOTES.md)

In Overleaf, choose **New Project > Upload Project**, upload either ZIP, and
use `main.tex` with the pdfLaTeX compiler. The single-file version includes
all sections, tables, and references in `main.tex`. Both ZIPs include the
class and figures and have been compiled independently. On GitHub, use the
file's download button to save a ZIP or LaTeX file.

This is an author-review draft. Independent label review remains pending,
and the paper retains the exploratory qualifications of the saved results.

## Final presentation

The [final technical deck](presentations/Final_Crowd_Violence_Presentation_20261119.pptx)
contains 16 main slides and four appendix slides, with completed results,
limitations and speaker notes. Slides 13 and 14 link to the four saved MP4s in
`presentations/media`. Keep that folder beside the deck when sharing it.
[Opening instructions](presentations/FINAL_PRESENTATION.md) explain playback.
The original Stage 1 deck is preserved. The complete paper draft is linked
above; independent label review remains pending.

## Instructions for teammates

Start with [TEAMMATE_SETUP.md](TEAMMATE_SETUP.md) for cloning, dependencies,
checking the shared results and running the frozen-video reference. The current
code, tests, selected experiment evidence and four diagnostic demo MP4s are
included. The original [project PDF](Affective_computing_project.pdf) is preserved.

Clone this repository and open `output/final_delivery_20261115/index.html`
locally to view the results and play the demos. The large fine-tuned checkpoint,
pretrained weights, raw datasets and caches are separate from Git. The setup
guide explains the required assets and their checksums. Independent review is
still pending, and the coordinator mapping is not published.

## Final technical delivery

The local GPU evaluation and delivery work is complete. Independent human
label/difficulty review remains pending because no reviewer is available.
The complete paper draft is linked above. Completion describes work delivered and does
not imply reliable deployment.

The retained video model is the layer-4 fine-tuned R3D-18 candidate. Validation
alone selected epoch 2 and threshold 0.23 before either evaluation was scored.
Validation accuracy is 86.4%, macro-F1 0.864, and AUC
0.939. Validation Fight misses fell from 42 to 13 and false alarms
increased from 15 to 30. The original frozen-video reference is preserved and
remains the predeclared primary model for the external experiment.

| Evaluation | Model | Clips | Accuracy | Macro-F1 | AUC | False alarms | Misses |
|---|---|---:|---:|---:|---:|---:|---:|
| RWF released evaluation | rwf_frozen_video | 400 | 84.00% | 0.840 | 0.900 | 21 | 43 |
| RWF released evaluation | rwf_finetuned_video | 400 | 83.75% | 0.837 | 0.929 | 40 | 25 |
| Hockey Fight external | rwf_frozen_video | 1000 | 70.80% | 0.686 | 0.886 | 14 | 278 |
| Hockey Fight external | rwf_finetuned_video | 1000 | 81.10% | 0.810 | 0.893 | 57 | 132 |
| Hockey Fight external | crowd_pose_interactions | 1000 | 40.90% | 0.361 | 0.420 | 432 | 159 |

The RWF evaluation clips were previously inspected, so their scores remain
exploratory supervised development evidence. Hockey Fight was pinned and its
protocol frozen before external scoring. All 1,000 mirror clips were retained,
including three duplicate files, with 997 unique byte hashes. No byte-identical
overlap was found with the compared 2,245-file crowd/RWF inventory. Byte hashes
do not establish independent source games or rule out near-duplicates and
Kinetics pretraining overlap. Sports broadcasts differ from surveillance.
Supplied labels remain unchanged and independently unreviewed.

Four diagnostic raw-video MP4s cover correct positive/negative decisions,
a false alarm and a miss. They reproduce saved scores and decode completely.
The bounded decoder reproduces the original uniform 32-frame samples. Single
video calls preserve the validation batch shape to match CUDA score rounding.
A closed-window interface accounts for every frame in a longer-video smoke
check; event localization and real-time streaming accuracy are unvalidated.
All 8,474 files in ten previous completed experiments are preserved byte-exact.
All 60 project tests pass, including exact bounded sampling, window-tail
accounting, sealed-protocol rejection and the validation batch-shape check.

[Final results and demos](output/final_delivery_20261115/index.html) |
[Runbook](output/final_delivery_20261115/RUNBOOK.md) |
[RWF evaluation](output/final_delivery_20261115/rwf_evaluation/index.html) |
[External evaluation](output/external_validation_20261115/index.html) |
[Preservation audit](output/final_delivery_20261115/preservation_audit.json) |
[Independent review pack](output/blind_review_20261115/index.html)

## Earlier technical progress:

At this earlier stage, paper drafting was deferred and technical work was
roughly 85 to 90% complete as a planning estimate, separate from prediction accuracy.

The separate supervised RWF reference is now complete: 82.0% validation accuracy
and 84.0% released-evaluation accuracy, macro-F1 0.840 and AUC 0.900. Its fresh
head uses 1,271 training clips and 317 source-grouped validation clips; all 400
evaluation clips are retained. Six train/evaluation byte-duplicate pairs were
found and linked training sources excluded. C=0.01 and threshold=0.50 were
selected using validation before evaluation arrays were loaded. These are
supervised development results on already-inspected evaluation footage,
separate from crowd-only transfer. All 48 tests pass.

The focused temporal follow-up is complete. Four short local video windows
were added to the global features in one frozen candidate. Validation accuracy
was 81.7%, compared with 82.0% for the retained reference. It fixed 12 old errors
and introduced 13 new errors, with 40 Fight misses and 18 false alarms. It failed
the predeclared validation rule, so no evaluation features or predictions were
produced for this candidate. The original supervised model remains the retained
reference. All 53 current project tests pass; four raw validation demonstrations
reproduce cached scores and all nine earlier completed experiments are preserved.

[Temporal comparison](output/rwf_temporal_20261115/index.html) |
[Validation diagnosis](output/rwf_validation_review_20261115/index.html)

[Supervised RWF results](output/rwf_supervised_20261115/index.html) |
[Raw-video demonstrations](output/rwf_supervised_20261115/demos/index.html)

- The centering correction is tested and evaluated with 140 matched CPU fits.
  Interactions improve from 76.5% to 78.6% mean accuracy; reliability improves
  by 0.95 percentage points. Baseline and combined do not improve.
- A frozen pretrained R3D-18 video reference reaches 91.0% mean crowd accuracy,
  macro-F1 0.909 and AUC 0.979 on the same 245 clips and source-grouped folds.
  Its fixed fold-1 head reaches 63.25% accuracy and 0.712 AUC on RWF transfer;
  the predeclared ensemble reaches 63.75% and 0.743 AUC. Transfer remains weak.
- The 45-fit GPU control study reaches 75.4% for full combined input, 72.5%
  for detection-only input and 75.4% for shuffled derived time slices.
  Shuffling retains velocity vectors; detection cues remain predictive.
- Raw-video warmed runtime has a 0.270-second median and 0.390-second p95 on
  ten fixed crowd clips. Cold process median is 8.36 seconds. Four diagnostic
  demonstrations are refreshed and fully decoded. The latest 53 implementation tests pass.

These remain exploratory results on previously inspected footage. The RGB
encoder's pretraining/source overlap is unaudited. Independent label review
remains, with a neutral 40-clip review pack prepared. Historical fitted artifacts
are preserved, and older checkpoints retain their legacy feature semantics.

[Centering comparison](output/centering_corrected_cpu_20261115/centering_ablation.html) |
[Video baseline](output/video_baseline_v2_20261115/index.html) |
[Video transfer](output/video_transfer_20261115/index.html) |
[Input controls](output/input_controls_20261115/index.html) |
[Runtime](output/runtime_20261115/RESULTS.md) |
[Demonstrations](output/demo_20261115/index.html) |
[Completion estimate](PROJECT_STATUS.md)

## One-time RWF-2000 transfer:

The saved source-corrected combined crowd model was evaluated once on the local
RTX 3050 GPU using all 400 released RWF-2000 evaluation clips: 200 Fight and
200 NonFight. Its threshold remains 0.54, and its crowd-training normalization
is reused. Fresh pose extraction uses the recorded settings; RWF data does not
select weights, normalization or a new threshold.

| Evaluation | Clips | Accuracy | Macro-F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| All released RWF evaluation clips | 400 | 56.0% | 0.506 | 0.578 |
| Excluding the known prior demo clip | 399 | 56.1% | 0.508 | 0.577 |

The model detects 178 of 200 Fight clips but also flags 154 of 200 NonFight
clips. This is weak transfer to surveillance footage under the frozen protocol.
The run took about 3 minutes 10 seconds. All 400 videos decoded completely,
their frame counts matched, and metrics reproduce from saved scores. These
results measure transfer, which differs from supervised training on RWF.
They remain exploratory after known prior inspection of one clip.

Open [the transfer results](output/rwf_transfer_20261115/index.html),
[the experiment guide](output/rwf_transfer_20261115/README.md), or
[the completion estimate](PROJECT_STATUS.md). The 26-test suite passed.
The current project is roughly 70% complete overall; the core pipeline is
complete and the full manuscript is approximately 40% complete. These are
planning estimates, separate from classification accuracy.

## Explicit coverage ablation:

The next focused experiment is complete: 60 new TCN fits and 10 control fits on
the same 245 clips, 204 reviewed source groups, five folds and three seeds as
November 7. The explicit observed-track coverage scalar was replaced with zero.
Network dimensions and initialization were preserved; normalization, fitting,
checkpoints and thresholds were recomputed using training and validation data.

| Model | Coverage on accuracy | Coverage off accuracy | Paired change (pp) |
|---|---:|---:|---:|
| Skeleton baseline | 76.1% | 76.1% | 0.00 |
| Reliability | 76.9% | 76.9% | 0.00 |
| Interactions | 76.1% | 75.9% | -0.14 |
| Combined | 74.8% | 74.8% | 0.00 |

This scalar has little effect under these settings. Masks, missing joints,
confidence channels and neighbor counts still expose detection behavior, so
the result does not establish that the remaining signal comes from body motion.
The unchanged quality-only control still reaches 77.6% mean accuracy.
These are descriptive exploratory comparisons on previously inspected footage.

Open [the paired comparison](output/coverage_ablation_20261114/coverage_ablation.html),
[the experiment guide](output/coverage_ablation_20261114/README.md), or
[the manuscript section](paper/METHODS_AND_PILOT_RESULTS.md#12-explicit-coverage-ablation-14-november-2026).
All 140 reference/new fits reproduced their scores exactly on the training GPU;
all 947 reference files were preserved. The updated suite passed 24 tests.

The first CPU report exceeded its unchanged 0.0003 score tolerance on one of
5,880 scores, with maximum drift 0.00033545. No binary decisions or
validation-selected thresholds changed. The [GPU audit](output/coverage_ablation_20261114/audit.json)
and [supplemental CPU audit](output/coverage_ablation_20261114/cpu_precision_audit.json)
record both outcomes. The improved verifier is archived separately from the
frozen training implementation.

## Repeated source-grouped evaluation:

The five-fold experiment is complete: 245 unique clips, 204 known source groups,
60 TCN fits and 10 linear-control fits. Each rotation uses 147 training,
49 validation and 49 test clips. The four TCN variants use seeds 42, 123 and
2026; each deterministic control is fitted once per fold. Scaling uses training
data, and checkpoints, motion regularization and thresholds use validation data.

| Model | Fits | Accuracy mean | Accuracy SD (pp) | Macro-F1 mean | ROC-AUC mean |
|---|---:|---:|---:|---:|---:|
| Skeleton baseline | 15 | 76.1% | 4.8 | 0.756 | 0.860 |
| Reliability | 15 | 76.9% | 5.5 | 0.766 | 0.864 |
| Interactions | 15 | 76.1% | 6.0 | 0.755 | 0.854 |
| Combined | 15 | 74.8% | 6.1 | 0.739 | 0.860 |
| Adjacent-frame motion control | 5 | 75.1% | 5.3 | 0.748 | 0.798 |
| Pose-quality-only control | 5 | 77.6% | 6.1 | 0.773 | 0.861 |

SD describes variation across dependent fold/seed runs; pp means percentage
points. These are not confidence intervals or significance tests. Reliability
has a small mean advantage among skeleton models. The combined additions show
no consistent benefit, and quality-only remains competitive without joint
coordinates or trajectories. Detection cues therefore need further ablation.

Open [the verified results page](output/cross_validation_20261107/index.html),
[the detailed results](output/cross_validation_20261107/RESULTS.md), or
[the saved-fit audit](output/cross_validation_20261107/audit.json).
All 70 saved fits reproduced their decisions, training-only normalization and
validation-selected thresholds. The implementation test suite passed 20 tests.

[Source review](output/source_review_20261107/REVIEW.md) fully decoded every clip
and visually inspected sampled evidence for 20 candidate pairs. Thirteen source
links reduced the known group count from 215 to 204. Labels were preserved and
not independently re-annotated; unknown shared footage remains possible.
Existing clips have been inspected previously, so these are exploratory results.
The custom folds differ from the supplied Violent-Flows protocol and the older
holdout. Their scores should not be presented as a direct improvement over that
pilot.

The experiment includes an implementation snapshot. Use it to inspect the
completed run after later source changes:

```powershell
& '.\.venv\Scripts\python.exe' output/cross_validation_20261107/run_snapshot.py summarize-cv
& '.\.venv\Scripts\python.exe' output/cross_validation_20261107/run_snapshot.py report-cv --date 2026-11-07
```

[The experiment guide](output/cross_validation_20261107/README.md) records its
artifacts and reproduction commands. [The next-stage plan](NEXT_STEPS.md)
prioritizes detection-cue ablations, label/difficulty review, a stronger RGB
reference, RWF-2000 evaluation and full-pipeline latency.

## Source grouping corrected: 

**After the presentation, 25 October:** the professor requested no changes;
college GPU access is expected through SSH, with credentials pending.
Portable source-grouped TCN and control evaluation is now complete locally.
College server access remains useful for the larger RGB/RWF experiments.

**24 October demonstration requirement.** The professor requested the proposed framework running end to end; high accuracy was optional at that discussion stage. [The demonstration guide](output/oct24/DEMO_GUIDE.md), [the requirements record](PROFESSOR_REQUIREMENTS.md), and `scripts/show_pipeline.ps1` preserve that milestone. [Methods and results](paper/METHODS_AND_PILOT_RESULTS.md) now include the repeated evaluation. The complete manuscript must be at least 12 pages before 20 November.

Review found three training/validation candidate pairs that the original exact filename grouping missed because source IDs were truncated. Matching footage is visible in the two Preston crowd pairs. The source grouping rule now links matching titles/uploaders with prefix-compatible IDs and excludes related training clips. The corrected pilot uses 147 training, 48 validation and the original 47 test clips. All models were retrained with fresh training normalization and validation-selected checkpoints/thresholds.

| Model | Test accuracy | Macro-F1 | ROC-AUC |
|---|---:|---:|---:|
| Baseline | 68.1% | 0.680 | 0.808 |
| Reliability | 63.8% | 0.638 | 0.781 |
| Interactions | 68.1% | 0.679 | 0.850 |
| Combined | 66.0% | 0.658 | 0.786 |
| Adjacent-frame motion control | 74.5% | 0.744 | 0.766 |
| Pose-quality-only control | 76.6% | 0.764 | 0.873 |

Open [the corrected results page](output/source_corrected/index.html), [the correction comparison](output/source_corrected/CORRECTION.md), or [the saved-artifact audit](output/source_corrected/AUDIT.md). The archived pilot remains in `output/pilot/` with its source-overlap warning and source review.

The seven-feature quality-only control uses detection counts and coverage, without joint positions or trajectories. It exceeds the skeleton variants on this split, suggesting scene or detection cues may explain part of the result. The 80-feature motion control uses adjacent-frame differences and optical flow. Both controls use training-only scaling/fitting and validation-selected decisions.

All four corrected checkpoints, both linear controls and six complete demo video decodes passed verification. At this milestone, nine tests passed, including the truncated-ID regression test. No known exact or prefix-compatible source-ID overlaps remained; filenames and sparse image hashes can miss other shared footage. This correction followed prior test inspection and remains exploratory, with one seed and one split.

To reproduce the correction from the archived feature caches, use `scripts/run_source_corrected.py --date 2026-10-22` with the pilot Python environment. It refuses to overwrite an existing completed corrected run. Use `--out output/source_corrected` with the CLI to inspect or regenerate its reports:

```powershell
& '.\.venv\Scripts\python.exe' -m affective.cli --out output/source_corrected report --date 2026-10-22
& '.\.venv\Scripts\python.exe' scripts/audit_pilot.py --out output/source_corrected
```

## Archived pilot: 

All 245 unique crowd clips have cached poses. Four models were trained on the local RTX 3050 with seed 42, using 150 training clips, 48 validation clips, and 47 test clips. Checkpoints and thresholds use validation data only.

| Variant | Test accuracy | Macro-F1 | ROC-AUC |
|---|---:|---:|---:|
| Baseline | 66.0% | 0.658 | 0.810 |
| Reliability | 63.8% | 0.638 | 0.792 |
| Interactions | 70.2% | 0.701 | 0.864 |
| Combined | 68.1% | 0.681 | 0.777 |

The majority-class baseline is 51.1%. Mean usable pose coverage is 74.0%; 32 clips fall below 25% coverage, including 9 test clips. Models overfit quickly, so the saved checkpoints come from epochs 3-8. Small differences between variants are not established as significant.

Open [the archived results page](output/pilot/index.html) for six held-out videos, including abstentions and a missed violent clip. [The artifact audit](output/pilot/AUDIT.md) includes uncertainty intervals, a pose-quality breakdown and the source-overlap warning. All source hashes, saved scores, reported metrics, and complete demo video decoding passed verification. Source independence was not established by that consistency check.

The new-video inference path was also checked on one RWF-2000 non-fight clip. The combined model produced a false positive at score 0.887. This is an implementation check and a documented failure, not an external accuracy estimate. Its video is included in the results page.

## Setup and run on Windows

Python 3.13 is used in an isolated environment. CUDA PyTorch runs on the local NVIDIA GPU; use `-CpuOnly` for a CPU installation.

```powershell
.\scripts\setup_pilot.ps1
.\scripts\run_pilot.ps1
```

The pose weights are downloaded on first extraction. Later runs use local weights and cached poses. Open `output/pilot/index.html` for the results and video demonstrations.

## Individual stages

```powershell
$pilotPython = '.\.venv\Scripts\python.exe'
& $pilotPython -m affective.cli prepare
& $pilotPython -m affective.cli extract --frames 32 --max-people 8 --image-size 640
& $pilotPython -m affective.cli train --epochs 180
& $pilotPython -m affective.cli demo --count 6
& $pilotPython -m affective.cli motion
& $pilotPython -m affective.cli analyze
& $pilotPython scripts/audit_pilot.py
& $pilotPython -m affective.cli report
& $pilotPython -m pytest tests -q
```

For a new video, run the saved combined model on newly extracted poses:

```powershell
& '.\.venv\Scripts\python.exe' -m affective.cli demo --video 'C:\path\to\video.mp4'
```

The annotated MP4 is saved in `output/pilot/demos/`, with inference details in `output/pilot/new_video_demo.json`.

## Historical pilot protocol

The pilot uses Violent-Flows folds 1-3 for training, fold 4 for validation, and fold 5 for final pilot scoring. Byte-identical duplicates are removed. Filename-derived source groups appearing in a holdout are excluded from earlier partitions. Matching crowd titles/uploaders with source IDs of at least two characters are grouped when one ID prefixes another. This conservative rule handles known truncation cases; near-duplicates and other incomplete source identifiers still require manual inspection. The manifest records every clip and partition.

All variants share pose caches, splits, placeholder policy, hidden size, epoch budget, and seed. The four variants are baseline; confidence and validity handling; relative interactions; and combined. Input channels change parameter count, so this is reported. Training observations alone define feature normalization; validation loss selects the checkpoint and validation macro-F1 selects the threshold. The test set does not select these decisions.

The pose estimator is pretrained YOLO11n-pose with COCO's 17 joints. The project temporal model is trained locally from the supplied binary clip labels. It uses a shared per-person TCN, masks padded observations, pools over time and people, and emits a clip score. Interaction distances are computed in common image coordinates before individual body centering. Track IDs last for one clip only.

Caches include the source digest, model digest, extraction signature, shape, frame indices and pose-quality information. Extraction is resumable and rejects mismatched settings during training/inference.

## Limits of the experiments

- The historical pilot used one holdout and one seed. The newer custom source-grouped evaluation adds folds and seeds, but previously inspected videos and dependent runs do not establish untouched benchmark performance or significance of small differences.
- Crowded low-resolution clips can have unreliable or absent poses, fragmented tracks, and more people than the retained track cap.
- All selected clips remain in the reported test metrics. The demo flags insufficient pose evidence below 25% usable sampled frames. That cutoff is an initial operational rule, not a validated abstention model.
- Predictions use the entire clip offline. Sampled pose overlays use the nearest sampled frame. The demo does not establish real-time performance or temporal localization.
- The output is a clip score, not calibrated probability or person-level violent-action attribution.
- The original privacy scripts use industrial gestures. Their scores do not measure violence-detection accuracy.

## Data and references

`data/movies` contains Violent-Flows crowd videos and the five supplied folds. `data/RWF-2000` contains 2,000 surveillance clips. `data/FederatedHAR` supplies preliminary gesture/privacy experiments. Third-party reference notebooks and weights are in `reference/`; these are not project-trained models.

Sources: [Violent-Flows](https://www.openu.ac.il/home/hassner/data/violentflows/), [RWF-2000](https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection), [Ultralytics pose models](https://docs.ultralytics.com/tasks/pose/). Keep each source's license and dataset usage terms with any future redistribution.
