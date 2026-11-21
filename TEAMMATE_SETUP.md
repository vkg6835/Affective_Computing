# Teammate setup and results

Repository updated on 21 November 2026 with the complete paper draft and the
technical delivery evaluated on 15 November. The existing project PDF remains
in the repository.

## Paper and Overleaf

The paper uses the original title, **Violence and Goon Detection in a Crowd
or Protest**, and omits running header text. Download the
[14-page PDF](output/pdf/paper_20261121/manuscript.pdf),
[complete LaTeX file](output/pdf/paper_20261121/complete_paper.tex), or
[Overleaf ZIP](output/pdf/paper_20261121/overleaf_single_file.zip).
Upload the ZIP through Overleaf's **New Project > Upload Project**, select
`main.tex` and pdfLaTeX, and edit the paper. The ZIP includes the class and
figures; all sections, tables, and references are inline in `main.tex`.
Use Overleaf's Share button to invite collaborators or share the ZIP and PDF
directly. Review [the author notes](paper/latex_20261121/REVIEW_NOTES.md).

## Final presentation

Open [the final technical deck](presentations/Final_Crowd_Violence_Presentation_20261119.pptx)
after cloning or extracting the repository. It has 16 main slides and four
appendix slides. Keep `presentations/media` beside the deck for the linked demos
on slides 13 and 14. The clips can also be opened directly in a video player.
See [opening instructions](presentations/FINAL_PRESENTATION.md).

## Start with the results

Read [PROJECT_STATUS.md](PROJECT_STATUS.md) and
[the final runbook](output/final_delivery_20261115/RUNBOOK.md).
The latest comparison, per-clip scores, protocols and four verified diagnostic
MP4s are committed. Clone the repository and open
`output/final_delivery_20261115/index.html` in a browser to play them. GitHub's
file view displays HTML source; it does not host these pages as a website.

```powershell
git clone https://github.com/vkg6835/Affective_Computing.git
cd Affective_Computing
Start-Process output/final_delivery_20261115/index.html
```

RWF evaluation accuracy is 84.0% for the frozen reference and 83.75% for the
fine-tuned model. Hockey Fight accuracy is 70.8% and 81.1%, respectively.
Fine-tuning catches more fights but also raises false alarms. RWF evaluation
footage was previously inspected; Hockey Fight is sports footage. Neither
experiment establishes surveillance deployment reliability.

## Install and test

The recorded environment uses Python 3.13, PyTorch 2.11.0 and torchvision
0.26.0. On Windows with a compatible NVIDIA GPU:

```powershell
py -3.13 -m venv .venv
& .venv/Scripts/python.exe -m pip install torch==2.11.0 torchvision==0.26.0 --index-url https://download.pytorch.org/whl/cu128
& .venv/Scripts/python.exe -m pip install -r requirements-verified.txt
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe scripts/verify_shared_results.py
```

For CPU-only tests, use the PyTorch `https://download.pytorch.org/whl/cpu`
index in the first install command. The CUDA gradient test skips on CPU. The
delivery inference command requires CUDA. The original verified local run
passed 60 tests. The repository copy also passed all 60 tests on 18 November;
the shared verifier reproduced all 3,800 model predictions.
`requirements-pilot.txt` remains available for an unpinned
development environment.

## Run a frozen video reference

The small trained logistic head and its sealed protocol are included. Download
the official pretrained encoder and verify its recorded SHA-256:

```powershell
& .venv/Scripts/python.exe scripts/prepare_shared_assets.py
& .venv/Scripts/python.exe scripts/predict_final_video.py --model frozen --video 'C:/path/to/video.mp4' --output-json output/my_video.json --render output/my_video.mp4
```

For the separate corrected crowd-pose model, its small trained checkpoint is
included. Download the matching pose detector, then select it explicitly:

```powershell
& .venv/Scripts/python.exe scripts/prepare_shared_assets.py --pose
& .venv/Scripts/python.exe scripts/predict_final_video.py --model pose --video 'C:/path/to/video.mp4' --output-json output/my_pose_video.json
```

## Run the retained fine-tuned model

The 132,762,051-byte fine-tuned checkpoint exceeds GitHub's normal per-file
limit and is kept in Vishal's local artifact archive. Obtain that file from
Vishal and place it at `output/rwf_finetune_v2_20261115/model.pt`. Its expected
SHA-256 is:

```text
04692366a21cd5469573733281d3124289e1584df6fdd7c175dd42aa558cab4f
```

The required protocol and selection records are already committed.
`scripts/predict_final_video.py --model fine` then uses the sealed epoch 2 and
threshold 0.23. The default active-model pointer selects this same model, so
use `--model frozen` until the checkpoint has been installed. Do not tune a
new threshold against the completed evaluation sets.

## Artifact scope and independent review

Raw datasets, pretrained/large weights, tensor/feature caches and local
environments are excluded. The committed reports are evidence from the full
local archive. Some historical report links and completion hashes refer to
excluded videos, weights or caches. `scripts/verify_shared_results.py` checks
the shared CSV metrics and hashes of included sealed artifacts;
`scripts/score_final_evaluations.py --verify-only` requires the full local
dataset/model/archive bundle and is not a clean-clone check.

Archived protocols retain their original paths and bytes. Use a new named
experiment/protocol for development on another machine instead of rewriting
sealed records. Obtain the datasets through their original distribution and
follow their usage terms.

Independent full-video label/difficulty review remains pending. Neutral review
videos and the coordinator mapping are kept with Vishal. The mapping is not
committed, so it is not exposed to prospective reviewers. A reviewer should
receive the neutral pack and complete labels before inspecting model results.
Paper drafting remains deferred.
