# IEEE TAI paper draft

Completed and checked on 21 November 2026. The review PDF is 14 pages and
contains nine tables, seven figures, and 18 cited references. The compiled
draft and Overleaf source ZIP are in `output/pdf/paper_20261121` relative to
the project root. This is an author-review draft; independent label review
and professor approval remain pending.

This manuscript uses the professor's `IEEEtai.cls` without modifying it.
The original extracted template remains in `TAI_LaTex_Template`.

## Open in Overleaf

Create a new project by uploading the supplied source ZIP. Set `main.tex` as
the main document and select the standard pdfLaTeX compiler. The project
includes the class file, bibliography, sections, and all referenced PDF figures.
Overleaf runs the bibliography and cross-reference passes automatically.

## Compile locally

With a TeX installation:

```text
latexmk -pdf main.tex
```

With Tectonic:

```text
tectonic -X compile main.tex
```

The first Tectonic run downloads its standard TeX resources. The supplied PDF
is a compiled review copy; edit the LaTeX sources for revisions.

## Authors

The draft follows the order supplied by Vishal:

1. Sudhakar Mishra, sudhakarm@aid.svnit.ac.in
2. Vishal Gautam, u23ai127@coed.svnit.ac.in
3. Ishat Shivhare, u23ai071@coed.svnit.ac.in
4. Parth Parmar, u23ai084@coed.svnit.ac.in
5. Hanmant Jajulwar, u23ai098@coed.svnit.ac.in
6. Tanu Meena, u23ai076@coed.svnit.ac.in
7. Prakriti Manhar, u23ai114@coed.svnit.ac.in

All affiliations use the Department of Artificial Intelligence, SVNIT Surat.
No IEEE memberships, funding, submission dates, or editor information have
been invented.

## Evidence and figures

`evidence_manifest.json` records source result hashes and the three selected
checkpoint hashes. `generate_assets.py` reads the existing repository outputs
to regenerate tables and figures. It requires NumPy, Matplotlib, and Pillow.
It performs no inference, fitting, or threshold selection.
Run the generator from its original project location with the full experiment
archive available. The ZIP is self-contained for LaTeX compilation, while
regenerating assets requires the archive listed in `EXPERIMENT_INDEX.md`.

The manuscript separates corrected CPU pose fits, GPU input controls, the
crowd frozen RGB reference, supervised RWF video fitting, the rejected temporal
candidate, bounded layer4 fine-tuning, and fixed external scoring. Older
experiments remain in the archive.

Read `REVIEW_NOTES.md` before submission. `VERIFICATION.json` records the
evidence hashes and compilation checks for this review copy. Independent
label review remains pending, and the results retain their exploratory
qualifications.
