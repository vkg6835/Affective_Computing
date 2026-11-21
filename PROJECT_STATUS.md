# Project status

Updated 21 November 2026 after completion of the checked 14-page IEEE TAI
author-review draft. The sealed fine-tuned evaluations and technical delivery
remain unchanged. Earlier percentage estimates were rough planning judgments.

[Paper PDF](output/pdf/paper_20261121/manuscript.pdf) |
[Overleaf ZIP](output/pdf/paper_20261121/overleaf_source.zip) |
[Review notes](paper/latex_20261121/REVIEW_NOTES.md)

The local GPU evaluation and delivery work is complete. Independent human
label/difficulty review remains pending because no reviewer is available.
The full draft is complete for author review. Completion describes work delivered and does
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

The core clip-level implementation, controlled experiments, bounded fine-tuning,
external scoring and demo/runbook delivery are complete. Independent full-video
label/difficulty review is still required for the broader technical completion
claim. No review has been fabricated or replaced by assistant inspection.
The full manuscript is complete as a checked draft. Professor and author review
remain pending; manuscript completion does not imply submission approval.
