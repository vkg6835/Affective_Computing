# Manuscript experiment index

All paths below are relative to the project root. They identify the existing
local archive; the Overleaf ZIP does not bundle datasets or model checkpoints.
The manuscript uses the supplied labels and preserves the exploratory status
of previously inspected footage.

| Manuscript study | Archive directory | Principal records |
|---|---|---|
| Corrected CPU pose fits | `output/centering_corrected_cpu_20261115` | `summary.json`, `audit.json` |
| Matched legacy CPU fits | `output/centering_reference_cpu_20261115` | `summary.json`, `audit.json` |
| Centering comparison | `output/centering_corrected_cpu_20261115` | `centering_comparison.json` |
| Corrected GPU input controls | `output/input_controls_20261115` | `summary.json` |
| Historical coverage-enabled GPU reference | `output/cross_validation_20261107` | `summary.json` |
| Historical explicit coverage ablation | `output/coverage_ablation_20261114` | `summary.json`, `coverage_comparison.json` |
| Frozen crowd video heads | `output/video_baseline_v2_20261115` | `summary.json` |
| Crowd video heads transferred to RWF | `output/video_transfer_20261115` | `metrics.json` |
| Legacy combined pose transferred to RWF | `output/rwf_transfer_20261115` | `metrics.json` |
| Supervised frozen RWF video | `output/rwf_supervised_20261115` | `model.json`, `metrics.json`, `selection.json`, `source_audit.json` |
| Rejected temporal candidate | `output/rwf_temporal_20261115` | `selection.json`, `paired_comparison.json`, `promotion.json`; no released-evaluation scoring |
| Retained layer4 fine-tuning | `output/rwf_finetune_v2_20261115` | `model.pt`, `promotion.json`, `training_history.json` |
| Fixed RWF evaluation | `output/final_delivery_20261115/rwf_evaluation` | `metrics.json` |
| Fixed external Hockey evaluation | `output/external_validation_20261115` | `metrics.json` |
| Offline pose runtime | `output/runtime_20261115` | `summary.json` |
| Final RGB diagnostic videos | `output/final_delivery_20261115` | `demo_audit.json`, `demos/` |

The corrected pose transfer checkpoint is
`output/centering_corrected_cpu_20261115/fold_1/runs/interactions_seed42/model.pt`.
Its threshold is 0.62. The video thresholds are 0.50 for the frozen RWF head
and 0.23 for the epoch-2 fine-tuned checkpoint.

`evidence_manifest.json` records full SHA-256 hashes for the source metrics,
diagnostic posters, and three selected model artifacts. The asset generator
reads these archive records without running inference or training.
