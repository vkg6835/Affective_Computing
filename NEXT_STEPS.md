# Technical project priorities

Updated 21 November 2026 after completing the checked 14-page IEEE TAI paper
draft. Local GPU work has completed all currently authorized computation and
demonstration tasks. The next writing step is author and professor review of
the title, author details, interpretation, and appendix placement.

[Review PDF](output/pdf/paper_20261121/manuscript.pdf) |
[Overleaf source ZIP](output/pdf/paper_20261121/overleaf_source.zip) |
[Concrete review notes](paper/latex_20261121/REVIEW_NOTES.md)

The local GPU evaluation and delivery work is complete. Independent human
label/difficulty review remains pending because no reviewer is available.
The paper draft is complete for review. Completion describes work delivered and does
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

## Remaining required work

An independent person must review the existing neutral 40-clip full-video pack
and export labels/difficulty notes before seeing predictions or the coordinator
mapping. No reviewer is available at present. Preserve the experiment labels;
later corrections require a versioned dataset. This diagnostic subset does not
establish dataset-wide label accuracy.

## Optional later research

New surveillance sources, longer videos, occlusion and difficult lighting would
support a more relevant transfer study. Freeze any new protocol before scoring.
Do not tune the retained epoch, threshold or model against these completed
evaluation sets. Source independence, pretraining overlap, calibrated scores,
person-level attribution and streaming evaluation require separate work.

Paper drafting resumed and the checked 14-page review copy was completed on
21 November. The previous requirement was at least 12 pages before 20 November,
with an internal target of 19 November. The review-copy date is not evidence
of on-time submission. The final group date remains unconfirmed.

## Previous work order (paper drafting deferred)

1. Turn the working methods/results notes into the complete manuscript of at
   least 12 pages in the supplied TAI LaTeX template. Add an abstract,
   introduction, related work, discussion and conclusion; integrate the existing
   methods, repeated evaluation, controls and coverage ablation. Verify every
   citation and keep the exploratory nature of the results explicit. Target a
   finished, checked draft on 19 November, before the 20 November deadline.
2. Complete independent label/difficulty review. Inspect full clips for
   occlusion, crowd density, nonviolent high motion, camera movement and tracking
   failures with a documented rubric. The source audit fully decoded 245 clips
   and visually reviewed 20 sampled candidate sheets. Thirteen source links
   reduced known groups from 215 to 204. [The review](output/source_review_20261107/REVIEW.md)
   records its evidence; it cannot rule out all shared footage or validate labels.
3. Measure full-pipeline latency on specified hardware. Cached-feature fitting
   and classifier-only timings do not measure the complete video pipeline.
4. Add a stronger RGB/video baseline or a separately defined supervised RWF
   experiment when college GPU access and a fixed protocol are available.
   The requested one-time saved-model RWF transfer evaluation is complete.
   The released evaluation clips have now been scored; preserve suitable
   uninspected evidence for subsequent development and report reuse honestly.
   This is a conditional extension; manuscript completion proceeds with the
   verified experiments already available.

## Previous paper schedule (deferred)

| Date | Work | Concrete output |
|---|---|---|
| 15 November | Assemble the full paper structure, write abstract/introduction/related work, and verify bibliography entries against the original sources. | Complete LaTeX manuscript structure with existing methods and results integrated. |
| 16 November | Prepare a model-blind review rubric and have an independent group member review full clips for label ambiguity, occlusion, crowd density, high nonviolent motion, camera movement and pose/tracking failures. Write failure analysis alongside the review. | Review records with reviewer identity and scope, plus representative failure examples. |
| 17 November | Benchmark raw-video execution on the laptop using a fixed clip list and settings. Separate model initialization, decode/pose extraction, feature construction and classification; record overlay/export separately. | Hardware/settings record, per-clip timings and median/p95 runtime over the declared sample. |
| 18 November | Incorporate completed review and timing evidence, write discussion/limitations/conclusion, and compile the full paper. | Complete draft with at least 12 substantive pages in the supplied template. |
| 19 November | Check all reported numbers against saved artifacts, verify citations, inspect every rendered page, and rehearse the demo and project explanation. | Checked manuscript PDF and source files, plus a stable demonstration package. |

The independent reviewer should not see model predictions during label review.
Record ambiguous cases and disagreements. Preserve the original experiment
labels; any later relabeling belongs to a separate versioned dataset and
experiment. A reviewed subset must be described as a subset, with its selection
rule and size recorded.

Fix the latency sample before measuring, include both labels and varied clip
lengths, and report the exact measurement boundary. Raw-video decoding and pose
extraction must be included in the full-pipeline number. Keep cold-start and
warmed runs distinct. These offline timings do not establish streaming
real-time behavior.

The paper should explain the measured finding: reliability has a small mean
advantage among skeleton variants, the combined additions show no established
benefit, and quality-only remains competitive even after the direct coverage
ablation. Further detection-cue dependence, independent labels, source overlap
and external generalization remain open questions.

The explicit coverage ablation is complete. Baseline, reliability and combined
mean accuracy are unchanged; interactions decrease by 0.14 percentage points.
This isolated scalar does not explain the competitive quality-only control.
Masks, missing joints, confidence/validity channels and neighbor counts remain
available. Further detection-cue controls should change one component at a time
in a new named experiment after clarifying the data's labels and difficulty.

The cached-input stage completed locally on the RTX 3050 Laptop GPU. All 60 TCN
fits and 10 control fits are finished and verified. [The results page](output/cross_validation_20261107/index.html)
and [paper notes](paper/METHODS_AND_PILOT_RESULTS.md) record the findings.
Server access is useful for larger subsequent experiments; data review and
writing can continue locally. The active next task is the feature-consistency correction and diagnostic case review.

## Prepared cross-validation workflow

Use `--no-coverage` to freeze a coverage-disabled plan. It keeps classifier
dimensions and initialization while replacing the explicit scalar with zero.
Omitting the flag retains the original behavior. Choose a new named output
directory for subsequent experiments.

`prepare-cv` copies immutable poses and motion descriptors once into a separate experiment directory.
It canonicalizes known truncated source IDs, assigns whole source groups with
StratifiedGroupKFold, and reserves the preceding outer fold for validation.
Three folds train, one validates and one tests in the default five-fold setup.
Each clip is tested once per seed. The supplied dataset fold remains recorded
in the manifest; these custom folds are a different evaluation protocol.

No pilot training statistics or checkpoints are reused. Configuration, code,
fold manifests and cache hashes are frozen. Completed runs resume only when
their artifacts match. Quality descriptors and source-review evidence are also
frozen. The default configuration requires 60 TCN fits and 10 control fits.
Controls use fresh training-only scaling and validation-only choices in every fold;
their identical deterministic fits are not repeated for each TCN seed.
Existing footage has already been inspected, so these remain exploratory
development results. Running this script does not certify source independence
or full-video label correctness.

For a subsequent experiment, prepare a new named plan from PowerShell in the
project folder. Include any new ablation settings once implemented:

```powershell
& '.\.venv\Scripts\python.exe' -m affective.cli --out output/cross_validation_v2 prepare-cv --source output/pilot --source-merges output/source_review_20261107/source_merges.json --source-review output/source_review_20261107/review.json
& '.\.venv\Scripts\python.exe' -m affective.cli --out output/cross_validation_v2 run-cv --device cuda
& '.\.venv\Scripts\python.exe' -m affective.cli --out output/cross_validation_v2 summarize-cv
& '.\.venv\Scripts\python.exe' -m affective.cli --out output/cross_validation_v2 report-cv --date 2026-11-14 --verification-device cuda
```

For additional reviewed source links, pass `--source-merges source_merges.json`
when preparing a new plan. The file is a JSON list of clip-ID lists, for example
`[["first_clip_id", "second_clip_id"], ["second_clip_id", "third_clip_id"]]`.
Merges are transitive and cannot split known groups. Do not change a frozen plan
after inspecting its results. Prepare a new named experiment when code,
grouping or model settings change, and report the development sequence honestly.

`summary.json` reports per-fold/per-seed scores and an equal-weight mean with
descriptive standard deviation. It marks missing runs as incomplete. Folds and
seeds are dependent; the standard deviation is not a confidence interval.

## College server preparation

Ask for the SSH hostname/alias and username, authentication method, GPU model
and VRAM, scheduler/queue instructions, maximum job duration, storage quota,
and available Python/PyTorch/CUDA environment. These determine the exact setup
and launch command. An SSH host alone does not establish permission to train
on a login node.

For cached TCN/control evaluation, transfer `affective/`, `requirements-pilot.txt` and
the newly prepared experiment directory. Raw videos and YOLO weights
are not required for this cached stage. They are needed for source review, new
extraction, RGB baselines and demos. Reuse a supported server PyTorch environment
or install the wheel compatible with its driver. Do not copy the Windows venv.
The runner records package versions for each completed fit. Stored motion extraction
provenance is retained when the server's OpenCV version differs; optical flow is not
recomputed during cached evaluation.

Within an allocated Linux GPU session, from the transferred project folder:

```bash
python -m affective.cli --out output/cross_validation_v2 run-cv --device cuda
python -m affective.cli --out output/cross_validation_v2 summarize-cv
```

`run-cv --folds 1` can run a single fold in a scheduler job. Different fold jobs
can use separate allocated GPUs; never launch two jobs for the same fold.
Run `summarize-cv` after all jobs finish. After a forced interruption, a fold's
`.running` directory can be stale. Verify no job is active for that fold before
removing that empty lock and resuming. Completed models are reused after hash
verification; an unfinished fit restarts from the beginning.

No server connection, upload or training job has been performed.

## Setup verification on 25 October

The full test suite passed (13 tests), including a synthetic training/resume
check and training-only normalization. After the atomic artifact-write update,
all four cross-validation tests passed again.
Preparation was also verified against the real 245 cached clips: 215 known
source groups, with 147 training, 49 validation and 49 test clips in each custom
rotation. The preparation check is stored in
`tmp/cv_preparation_check_20261025/`; no real-dataset TCN fits were launched.
Create the experiment intended for analysis after full-video source review.

## Completed and verified: 7 November

Cross-fold control integration and source-overlap triage are implemented. Twenty
tests pass, including control fitting, training-only scaling, test-data invariance,
resume protection, cached-motion provenance, reviewed-link agreement, and complete
out-of-fold prediction coverage in the results verifier.

The frozen 204-group plan completed all 70 fits. The report verifier reproduced
all saved decisions, training-only normalization and validation-selected
thresholds. The maximum CPU score drift was 0.0002628565, within the 0.0003
tolerance. The report and comparison figure are complete; the older pilot
artifacts are preserved. These remain exploratory results on previously
inspected footage, with descriptive variation rather than significance claims.

The completed run includes a verified training-code snapshot. Use its helper
for future inspection after source changes:

```powershell
& '.\.venv\Scripts\python.exe' output/cross_validation_20261107/run_snapshot.py summarize-cv
& '.\.venv\Scripts\python.exe' output/cross_validation_20261107/run_snapshot.py report-cv --date 2026-11-07
```

## Completed and verified: 14 November

`output/coverage_ablation_20261114/` contains 60 freshly fitted coverage-disabled
TCNs and ten unchanged linear controls on the November 7 folds, groups and seeds.
All 140 reference/new fits reproduced saved scores exactly on the RTX 3050.
Training-only normalization and validation-selected decisions were verified.
The paired accuracy changes are 0.00 pp for baseline, reliability and combined,
and -0.14 pp for interactions. Only 19 of 2,940 repeated TCN test decisions
changed across all variants and seeds. These are dependent observations.

The strict CPU report initially failed on one of 5,880 scores, with maximum
absolute drift 0.00033545 above the unchanged 0.0003 tolerance. CPU decisions
and validation-selected thresholds still match. A separately archived GPU
verifier records score reproduction, and the supplemental CPU audit preserves
the numerical limitation. No models were refitted to address this audit issue.
All 947 reference files are unchanged, and 24 tests pass.

Use these helpers from the project root:

```powershell
& '.\.venv\Scripts\python.exe' output/coverage_ablation_20261114/run_snapshot.py summarize-cv
& '.\.venv\Scripts\python.exe' output/coverage_ablation_20261114/run_verification.py report-cv --date 2026-11-14
& '.\.venv\Scripts\python.exe' output/coverage_ablation_20261114/run_verification.py compare-coverage --reference output/cross_validation_20261107 --date 2026-11-14
```

[The paired report](output/coverage_ablation_20261114/coverage_ablation.html),
[experiment guide](output/coverage_ablation_20261114/README.md) and
[paper section](paper/METHODS_AND_PILOT_RESULTS.md#12-explicit-coverage-ablation-14-november-2026)
record the evidence and limitations. The working manuscript is still not the
complete 12-page submission. College SSH details and the final presentation
date remain unconfirmed; no server job or submission has been performed.


## Completed one-time local-GPU evaluation: 15 November

At Vishal's request, the saved source-corrected combined crowd model was
applied once to all 400 released RWF evaluation clips on the RTX 3050.
The threshold remains 0.54 and crowd-training normalization is reused.
Accuracy is 56.0%, macro-F1 is 0.506 and ROC-AUC is 0.578. The confusion matrix
is [[46, 154], [22, 178]], showing many false positives on NonFight footage.
This is weak exploratory transfer, which the paper should discuss explicitly.

The run took about 3 minutes 10 seconds; all 400 full decodes and frozen
source/cache checks passed. One known previously inspected demo clip is
included, with a supplementary 399-clip result. The completed-run verifier
returns saved results without additional extraction or inference. No RWF
model fitting or threshold tuning was performed. The test suite passed 26 tests.

[The result](output/rwf_transfer_20261115/index.html),
[experiment guide](output/rwf_transfer_20261115/README.md) and manuscript
section 13 record the study. [PROJECT_STATUS.md](PROJECT_STATUS.md) gives a
rough 70% overall completion estimate: core pipeline complete, experiments
approximately 85%, and full manuscript approximately 40%. These are planning
estimates, separate from the measured 56.0% transfer accuracy.

Paper drafting is deferred. The next technical work is feature consistency,
independent label/difficulty review, controlled comparisons and pipeline timing. Larger new training experiments
remain conditional on a separate scope and suitable compute.
