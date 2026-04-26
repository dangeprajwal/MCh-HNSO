---
tags:
  - Radiotherapy-and-Chemotherapy
  - Molecular-Biology
  - Oncology
---

> [!question] Questions Covered
> - **Chemo Q6:** Adoptive cell immunotherapy (KIDWAI 2020)

## Source
**Shah JP. Head and Neck Surgery and Oncology, 5th Ed. Elsevier, 2019**; Harrison LB et al. Head and Neck Cancer: A Multidisciplinary Approach. 4th ed. 2014; De Vita VT et al. Cancer: Principles and Practice of Oncology. 11th ed. 2019; Stell & Maran's Textbook of Head and Neck Surgery and Oncology. 5th ed. 2012.

> [!cite] Landmark Articles
>
> Adoptive cell immunotherapy has its foundational evidence in melanoma, largely from the work of Rosenberg and colleagues at the National Cancer Institute (NCI). Sarnaik et al. (2021) published the pivotal phase II trial of lifileucel (LN-144), a cryopreserved autologous TIL therapy, in 66 patients with advanced melanoma who had progressed through prior checkpoint inhibition, reporting a 36.4% objective response rate and demonstrating the clinical viability of TIL therapy in heavily pre-treated solid tumour patients. This led to the FDA accelerated approval of lifileucel (brand name Amtagvi) in February 2024 — the first cellular therapy approved for any solid (non-haematological) malignancy. The application of these principles to HNSCC remains investigational, though the principles of TIL manufacture, lymphodepletion conditioning, and IL-2 support established in melanoma directly inform ongoing HNSCC TIL trials. In the field of chimeric antigen receptor T cells, the demonstration of durable remissions in haematological malignancies has motivated intensive investigation of CAR-T in solid tumours, though the immunosuppressive tumour microenvironment of HNSCC presents substantial barriers.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Sarnaik AA et al. — Lifileucel, a Tumor-Infiltrating Lymphocyte Therapy, in Metastatic Melanoma | J Clin Oncol | 2021 | [10.1200/JCO.21.00612](https://doi.org/10.1200/JCO.21.00612) |

## Definition and Distinction from Checkpoint Inhibitors

**Adoptive cell immunotherapy (ACT)** is the ex vivo expansion or engineering of immune cells followed by their infusion into a patient to mediate anti-tumour immunity. It is fundamentally distinct from immune checkpoint inhibitors (ICI):

- **Checkpoint inhibitors** (pembrolizumab, nivolumab): small molecules or antibodies that remove inhibitory signals from the patient's own endogenous T cells, allowing pre-existing tumour-reactive T cells to be unleashed in vivo
- **Adoptive cell therapy**: bypasses endogenous T-cell activation entirely; immune cells are removed from the patient (or a donor), expanded or engineered to very large numbers ex vivo with specific anti-tumour properties, and then re-infused in massive quantities

The conceptual advantage is that ACT delivers a large, pre-activated, tumour-specific immune force that does not depend on the patient's ability to generate a de novo anti-tumour immune response — which is frequently impaired in advanced cancer.

---

## Types of Adoptive Cell Immunotherapy

### 1. Tumour-Infiltrating Lymphocyte (TIL) Therapy

TIL therapy is the oldest and most clinically validated ACT modality in solid tumours.

**Manufacturing process:**
1. Resect a tumour fragment (surgical specimen, excision biopsy, or core biopsy of accessible lesion)
2. Fragment tumour and co-culture in high-dose IL-2 to selectively expand TILs — the tumour microenvironment TILs contain a subset of tumour-reactive T cells (both CD4+ and CD8+)
3. Expand to >10¹⁰ cells over 4–6 weeks in a GMP (Good Manufacturing Practice) facility using rapid expansion protocols (REP): anti-CD3 antibody (OKT3) + irradiated feeder cells + IL-2
4. Prior to infusion: patient undergoes **lymphodepletion conditioning** with cyclophosphamide (60 mg/kg × 2 days) + fludarabine (25 mg/m² × 5 days) to create immunological space by depleting regulatory T cells (Tregs) and endogenous lymphocytes that would otherwise compete for homeostatic cytokines
5. Re-infuse TILs intravenously
6. Administer high-dose IL-2 (600,000 IU/kg IV q8h × up to 15 doses) to support TIL survival and expansion in vivo — this IL-2 regimen carries significant toxicity (vascular leak syndrome)

**Clinical status in melanoma:**
- Proof-of-concept established by Rosenberg group (NCI) — response rates of 40–70% in highly pre-treated patients
- **Lifileucel (Amtagvi, Iovance Biotherapeutics)**: FDA accelerated approval February 2024 for unresectable or metastatic melanoma progressed on anti-PD-1 ± BRAF-targeted therapy; first cellular therapy approved for any solid tumour; ORR 31.5% in pivotal C-144-01 trial

**Status in HNSCC:**
- TILs from HNSCC tumours contain tumour-reactive T cells (particularly HPV E6/E7-specific T cells in HPV+ tumours)
- Expansion of HNSCC TILs is technically feasible but more challenging than melanoma (lower TIL density, immunosuppressive TME)
- Multiple Phase I/II trials ongoing; no approved TIL product for HNSCC

---

### 2. CAR-T Cell Therapy (Chimeric Antigen Receptor T Cells)

CAR-T cells are T lymphocytes genetically engineered to express a synthetic receptor that directs tumour cell killing independent of HLA restriction.

**CAR construct structure:**
- **Extracellular domain**: single-chain variable fragment (scFv) — an antibody-derived antigen-binding domain targeting a tumour surface antigen; does not require antigen processing or HLA presentation (unlike native TCR recognition)
- **Hinge/transmembrane domain**: anchors receptor to T-cell membrane
- **Intracellular signalling domain(s)**: activates T-cell effector functions upon antigen engagement

**Generations of CAR-T:**

| Generation | Intracellular Domain | Properties |
|---|---|---|
| 1st generation | CD3ζ only | Limited persistence; poor in vivo expansion |
| 2nd generation | CD3ζ + 1 co-stimulatory (CD28 or 4-1BB) | Current clinical standard; improved persistence |
| 3rd generation | CD3ζ + 2 co-stimulatory domains | Enhanced activation; possible toxicity |
| 4th generation (TRUCKs) | 2nd gen + inducible cytokine payload (e.g., IL-12) | Armoured CAR; remodel TME; investigational |

**Approved CAR-T products (haematological malignancies only):**
Tisagenlecleucel, axicabtagene ciloleucel, lisocabtagene maraleucel, ciltacabtagene autoleucel (myeloma), idecabtagene vicleucel — all for B-cell lymphoma, ALL, or myeloma; none approved for solid tumours.

**Investigational CAR-T targets in HNSCC:**

| Target | Rationale | Clinical Status |
|---|---|---|
| EGFR | Universally expressed in HNSCC (>90%) | Phase I/II trials; toxicity from normal tissue expression |
| HER2 (ErbB2) | Overexpressed in subset | Phase I trials |
| EpCAM | Expressed on epithelial cancers | Early phase |
| B7-H3 (CD276) | Overexpressed on HNSCC cells and vasculature | Preclinical/Phase I |
| CD44v6 | Expressed on HNSCC CSC-like cells | Investigational |
| Mesothelin | Expressed in some HNSCC | Investigational |

All HNSCC CAR-T targets remain **investigational**; no approved product exists for HNSCC.

**Toxicities of CAR-T therapy:**
- **Cytokine release syndrome (CRS)**: fever, hypotension, hypoxia — mediated by massive cytokine release (IL-6, IFN-γ, IL-1) after CAR-T activation; managed with tocilizumab (anti-IL-6R) ± corticosteroids; graded 1–4
- **ICANS (immune effector cell-associated neurotoxicity syndrome)**: confusion, aphasia, seizure, cerebral oedema — managed with corticosteroids; potentially life-threatening
- On-target off-tumour toxicity: antigens like EGFR are expressed on normal epithelial cells, potentially causing mucosal toxicity

---

### 3. TCR-T Cell Therapy (T-Cell Receptor-Engineered T Cells)

Patient T cells are transduced with a high-affinity T-cell receptor (αβ heterodimer) recognising a specific peptide–HLA complex.

**Key advantage over CAR-T**: can target **intracellular antigens** (because TCRs recognise peptide fragments presented on MHC I/II) — CAR-T cells can only target surface antigens.

**Application in HNSCC:**
- **HPV E6 and E7 TCR-T** in HPV+ oropharyngeal cancer: HPV oncoproteins are tumour-specific antigens expressed only in HPV-transformed cells (not in normal tissues); high-affinity TCRs against HLA-A*02:01-restricted E6/E7 peptides are in Phase I/II trials; considered one of the most promising ACT approaches for HNSCC
- Limitation: HLA-restricted (requires specific HLA type, typically HLA-A*02:01, present in ~45% of White populations)

---

### 4. NK Cell Therapy

Natural killer (NK) cells kill targets that have lost MHC I expression (a common mechanism of tumour immune escape from T-cell recognition) via their **missing-self** recognition pathway (inhibitory KIRs and NKG2A/NKG2D receptors).

**Relevance to HNSCC:**
- NK cells mediate **antibody-dependent cellular cytotoxicity (ADCC)** via CD16 (FcγRIII) — this is a key mechanism by which cetuximab (anti-EGFR antibody) exerts anti-tumour effects in HNSCC; cetuximab-coated tumour cells are lysed by NK cells via CD16 engagement
- **Ex vivo-expanded allogeneic NK cell therapy** combined with cetuximab has been explored in HNSCC to amplify ADCC; allogeneic NK cells carry lower graft-versus-host risk than allogeneic T cells
- Clinical data in HNSCC: early phase only

---

### 5. Dendritic Cell (DC) Vaccines

Dendritic cells are the most potent antigen-presenting cells; loaded ex vivo with tumour antigens and injected to stimulate anti-tumour CD8+ cytotoxic T-cell responses.

**Manufacturing:**
- Monocytes isolated from patient peripheral blood
- Differentiated into immature DCs with GM-CSF + IL-4
- Loaded with tumour antigens (tumour lysate, peptide pools, mRNA)
- Matured with TLR agonists or TNF-α
- Re-injected subcutaneously or intratumorally

**Status:**
- Sipuleucel-T (Provenge): autologous DC-based vaccine; FDA-approved for prostate cancer — the only approved therapeutic DC vaccine
- In HNSCC: multiple small trials, limited objective responses; DC vaccines have generally produced immunological responses (detectable anti-tumour T-cell immunity by assays) but modest clinical responses in Phase II trials; no approved product for HNSCC

---

## Challenges in Solid Tumours (HNSCC Specifically)

The success of CAR-T and TIL therapy in haematological malignancies has not been replicated in solid tumours, including HNSCC. The barriers are both physical and immunological:

| Challenge | Mechanism | Potential Solution |
|---|---|---|
| Immunosuppressive TME | Tregs, MDSCs, TGF-β, PD-L1, IDO | Combine ACT with ICI; armoured CAR-T secreting IL-12 |
| T-cell trafficking | Circulating ACT cells fail to home to solid tumour | Intratumoural delivery; engineer chemokine receptors on ACT cells (e.g., CXCR2 for CXCL8-rich HNSCC) |
| Antigen heterogeneity | Tumour antigen downregulation under CAR selection pressure | Multi-antigen CARs; TCR-T targeting clonal antigens (e.g., HPV E7) |
| T-cell exhaustion | Chronic antigen exposure → T-cell exhaustion (TOX+ PD-1+ Lag3+) | Co-stimulatory domain optimisation (4-1BB); gene-edited (TET2 KO, TOX KO) T cells |
| Physical barriers | Dense stroma, poor vascularisation — impedes ACT trafficking | Tumour normalisation (anti-VEGF), hylauronidase co-injection |
| On-target off-tumour toxicity | EGFR and other targets expressed on normal epithelium | Dual-antigen logic gates (CAR only activated when both antigens expressed) |

---

## Future Directions

- **Armoured/4th-generation CAR-T** (TRUCKs): secrete IL-12, IL-15, or anti-PD-1 locally within the tumour to remodel the immunosuppressive TME
- **Gene-edited universal allogeneic CAR-T**: TCR-deleted, MHC I-deleted allogeneic T cells — "off-the-shelf" products eliminating the need for autologous manufacture; HLA-editing prevents rejection
- **CAR-NK cells**: allogeneic NK cells expressing CARs — potentially off-the-shelf, lower GvHD risk
- **ACT + ICI combinations**: rationale for combining with pembrolizumab (PD-1 blockade prevents TIL exhaustion after infusion); multiple trials ongoing
- **HPV E6/E7 TCR-T in HPV+ OPC**: most clinically advanced HNSCC-specific ACT approach

---

> [!example] Examiner's Summary
> Adoptive cell immunotherapy encompasses the ex vivo manufacture of immune cells (TILs, CAR-T, TCR-T, NK cells, or dendritic cell vaccines) and their infusion to mediate anti-tumour immunity, fundamentally distinct from checkpoint inhibitors which work by unleashing endogenous T cells. TIL therapy is the most clinically advanced form for solid tumours, with lifileucel (Amtagvi) receiving FDA accelerated approval in February 2024 for advanced melanoma — the first cellular therapy approved for any solid tumour. CAR-T cells carry synthetic antigen receptors targeting tumour surface antigens and are transformative in haematological malignancies, but no CAR-T product is approved for HNSCC; key barriers include the immunosuppressive tumour microenvironment, poor T-cell trafficking into solid tumours, antigen heterogeneity, and on-target off-tumour toxicity. HPV E6/E7 TCR-T cells are the most HNSCC-specific ACT approach under investigation, targeting viral oncoproteins expressed exclusively in HPV-transformed cells. All ACT modalities in HNSCC remain investigational as of 2025.

> [!tip] Clinical Pearls
> 1. TIL therapy differs from CAR-T in that TILs are naturally tumour-reactive T cells harvested from the tumour itself — no genetic engineering; CAR-T cells are normal T cells engineered with a synthetic receptor.
> 2. Lymphodepletion conditioning (cyclophosphamide + fludarabine) is required before TIL infusion — it depletes regulatory T cells and creates immunological space for homeostatic expansion of infused cells.
> 3. **Lifileucel (Amtagvi)** was FDA-approved in February 2024 — the first approved cellular therapy for a solid tumour; approved for advanced melanoma, not HNSCC.
> 4. CAR-T cells recognise surface antigens directly without HLA restriction; TCR-T cells recognise intracellular peptide antigens presented on HLA — giving TCR-T the advantage of targeting intracellular oncoproteins (like HPV E6/E7).
> 5. **CRS (cytokine release syndrome)** is the most common serious CAR-T toxicity; managed with tocilizumab (anti-IL-6 receptor antibody); corticosteroids used for ICANS.
> 6. EGFR-targeted CAR-T in HNSCC risks on-target off-tumour toxicity to normal epithelium — a key safety concern.
> 7. NK cell ADCC is the primary mechanism by which **cetuximab** kills HNSCC cells; NK cell depletion or NK-cell dysfunction reduces cetuximab efficacy.
> 8. HPV E6/E7-specific TCR-T is the most HNSCC-specific ACT approach — targets tumour-exclusive viral antigens that cannot be downregulated without loss of oncogenic driver function.
> 9. All HNSCC ACT approaches remain **investigational** — no approved cellular therapy exists for HNSCC as of 2025.
> 10. The key barriers to solid tumour ACT are: immunosuppressive TME (Tregs, MDSCs, TGF-β), poor T-cell homing, antigen heterogeneity, and T-cell exhaustion — all more pronounced in solid tumours than in haematological malignancies.

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/Radiotherapy and Chemotherapy/index|Radiotherapy and Chemotherapy]]
>
> **Related Notes:**
> - [[Answers/Radiotherapy and Chemotherapy/Immune Checkpoint Inhibitors|Immune Checkpoint Inhibitors]] — checkpoint inhibitor mechanism and evidence; PD-1/PD-L1, CTLA-4 biology
> - [[Answers/Radiotherapy and Chemotherapy/Chemoradiation Principles and Applications|Chemoradiation Principles and Applications]] — concurrent CRT regimens
>
> **See Also:**
> - [[Answers/Oropharynx/DARS-Sparing Radiation in OPC|DARS-Sparing Radiation in OPC]] — HPV+ OPC treatment context
> - [[Answers/Larynx/Landmark Trials and Organ Preservation Strategies|Landmark Trials and Organ Preservation Strategies]] — treatment landscape for advanced HNSCC
