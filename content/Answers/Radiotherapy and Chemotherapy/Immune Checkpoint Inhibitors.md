---
tags:
  - Radiotherapy-and-Chemotherapy
  - Molecular-Biology
  - Systemic-Therapy
---

> [!question] Questions Covered
> - **Chemo Q2:** Immune checkpoint inhibitors (AIIMS 2020)
> - **Chemo Q18:** Concept of immune gatekeepers (AMRITA 2019)
> - **Chemo Q26:** Immune checkpoint inhibitors (AMRITA 2021)

## Source
**Shah JP. Head and Neck Surgery and Oncology, 5th Ed. Elsevier, 2019**; De Vita VT et al. Cancer: Principles and Practice of Oncology. 11th ed. Wolters Kluwer, 2019; Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science, 2017; Colevas AD et al. NCCN Guidelines Head and Neck Cancers.

> [!cite] Landmark Articles
>
> Allison and Honjo were awarded the 2018 Nobel Prize in Physiology or Medicine for their discovery of cancer therapy by inhibition of negative immune regulation. Allison's group described CTLA-4 as an inhibitory T-cell receptor in 1987, and demonstrated in 1996 that CTLA-4 blockade caused tumour rejection in murine models (Leach et al., Science 1996). Honjo's group identified PD-1 as an apoptosis-inducing gene in 1992 and later established its role as a peripheral tolerance checkpoint; Freeman et al. (2000) cloned PD-L1 and defined the PD-1/PD-L1 axis. These discoveries directly enabled the development of ipilimumab (anti-CTLA-4, approved 2011), nivolumab, and pembrolizumab (both anti-PD-1, 2014–2016).
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Leach DR, Krummel MF, Allison JP — Enhancement of Antitumor Immunity by CTLA-4 Blockade | Science | 1996 | [10.1126/science.271.5256.1734](https://doi.org/10.1126/science.271.5256.1734) |
> | Freeman GJ et al. — Engagement of the PD-1 Immunoinhibitory Receptor by a Novel B7 Family Member Leads to Negative Regulation of Lymphocyte Activation | J Exp Med | 2000 | [10.1084/jem.192.7.1027](https://doi.org/10.1084/jem.192.7.1027) |

---

## Immune Checkpoint Inhibitors

### Background — Why Checkpoints Exist

The immune system evolved **two checkpoints** to prevent self-destruction:

1. **Central tolerance** (in the thymus): autoreactive T cells are deleted by clonal deletion during T-cell development
2. **Peripheral tolerance** (in peripheral tissues): residual autoreactive T cells are silenced by inhibitory co-receptors — the **immune checkpoints**

The key peripheral tolerance molecules are:
- **CTLA-4** — regulates T-cell activation in **lymph nodes** (central control)
- **PD-1** — regulates T-cell function in **peripheral tissues** (local control)

Cancer cells hijack these checkpoints to evade immune destruction. Blocking these checkpoints with monoclonal antibodies — **immune checkpoint inhibitors (ICIs)** — restores anti-tumour T-cell activity.

---

### Concept of Immune Gatekeepers

The term **"immune gatekeepers"** (coined in the oncology context) refers to checkpoint molecules that act as physiological "brakes" on immune activation. In the normal state, they are essential — preventing autoimmune disease. In cancer, their overexpression or exploitation by tumour cells constitutes a mechanism of **immune evasion**.

The Nobel-prize analogy: the immune system has an **accelerator** (T-cell receptor activation, co-stimulatory CD28) and a **brake** (CTLA-4, PD-1). Cancer applies the brake. ICIs release the brake — not by adding a new signal, but by removing an inhibitory one.

---

### Major Immune Checkpoints in HNSCC

#### 1. PD-1 / PD-L1 Axis

**PD-1 (Programmed Death-1; CD279)**
- Expressed on: activated CD8+ and CD4+ T cells, NK cells, B cells, Tregs
- Upregulated by: chronic antigen stimulation (drives exhaustion), IL-2, IFN-γ
- **Intracellular domain:** contains ITIM (immunoreceptor tyrosine-based inhibitory motif) and ITSM (switch motif) → on PD-L1 binding, recruits **SHP-2** (phosphatase)

**Molecular mechanism:**
1. Antigen presented via MHC class I → TCR activates ZAP-70 → downstream signalling → T-cell activation
2. PD-L1 on tumour cell binds PD-1 on T cell → SHP-2 activation → ZAP-70 dephosphorylation → PI3K/AKT and Ras/MAPK pathways inhibited → T-cell **functional exhaustion**
3. Exhausted T cells: reduced IFN-γ, IL-2, TNF-α production; reduced cytotoxic granule release (perforin, granzyme B); upregulate co-inhibitory receptors (TIM-3, LAG-3, TIGIT)

**Adaptive immune resistance:**
IFN-γ released by tumour-infiltrating T cells upregulates PD-L1 on tumour cells via JAK/STAT1 signalling. This is paradoxical — the immune response that attempts to kill tumours simultaneously enhances the tumour's ability to block T cells. This is why PD-L1 expression is induced by the immune microenvironment, not just by oncogenic drivers.

**PD-L1 (CD274; B7-H1):**
- Expressed on: tumour cells, tumour-associated macrophages (M2), dendritic cells, endothelium
- Induced by: IFN-γ, IL-4, IL-13, NF-κB, HIF-1α
- Prevalence in HNSCC: positive in 50–80% of tumours; higher in HPV+ oropharyngeal cancer

**PD-L2 (CD273; B7-DC):**
- Expressed primarily on dendritic cells and macrophages
- Binds PD-1 with ~3× higher affinity than PD-L1; less studied in HNSCC
- Also engages RGMb (repulsive guidance molecule b) — role in lung tolerance

**Approved anti-PD-1 agents in HNSCC:**
- **Nivolumab** (Opdivo): fully human IgG4; CheckMate 141 (2nd-line R/M HNSCC)
- **Pembrolizumab** (Keytruda): humanised IgG4; KEYNOTE-048 (1st-line R/M HNSCC); KEYNOTE-040 (2nd-line)

**Approved anti-PD-L1 agents (not currently HNSCC-specific):**
- Atezolizumab (IgG1, non-FcR binding), Durvalumab (IgG1), Avelumab (IgG1) — HNSCC trials (CONDOR, EAGLE, JAVELIN) were negative

---

#### 2. CTLA-4 (Cytotoxic T-Lymphocyte Antigen-4; CD152)

**Expression:** Activated CD4+ and CD8+ T cells (surface); constitutively on Tregs (intracellular pool)

**Mechanism:**
1. T-cell activation requires **two signals:**
   - Signal 1: TCR + MHC-peptide
   - Signal 2 (co-stimulatory): **CD28** binds **CD80/CD86** (B7 ligands) on APCs
2. After T-cell activation, CTLA-4 is rapidly upregulated on the surface
3. CTLA-4 binds CD80/CD86 with **20× higher affinity** than CD28 → **outcompetes CD28** → signal 2 is lost
4. CTLA-4 on Tregs actively sequesters CD80/CD86 via trans-endocytosis → strips B7 from APCs → dampens CD28 co-stimulation for neighbouring T cells

**Where it acts:** Primarily in **lymph nodes** during the priming phase (antigen presentation stage)

**Ipilimumab (Yervoy; BMS):** Fully human IgG1 anti-CTLA-4 antibody; FDA-approved for melanoma (2011); no approval in HNSCC
- CheckMate 651 (ipilimumab + nivolumab 1st-line R/M HNSCC): **negative** — did not improve OS

**CTLA-4 vs PD-1 — the complementary model:**

| Feature | CTLA-4 | PD-1 |
|---|---|---|
| Site of action | Lymph node (priming phase) | Tumour microenvironment (effector phase) |
| Stage | Early T-cell activation | Late — T-cell exhaustion in periphery |
| Physiological role | Central peripheral tolerance | Peripheral tolerance |
| Immune cells affected | CD4+ T cells, Tregs (primarily) | CD8+ cytotoxic T cells (primarily) |
| Combo benefit | Synergistic with PD-1 blockade | — |
| HNSCC data | Negative (no approval) | Strong evidence |

---

#### 3. TIM-3 (T-cell Immunoglobulin and Mucin domain-3)

- Expressed on: exhausted CD8+ T cells (co-expressed with PD-1 at highest levels in deeply exhausted TILs), Th1 cells, Tregs, NK cells, macrophages
- **Ligands:** Galectin-9, CEACAM-1, HMGB1, Phosphatidylserine
- Marks the most exhausted T-cell phenotype in HNSCC — co-expression of PD-1+TIM-3+ predicts non-response to anti-PD-1 monotherapy
- **Rationale for combination blockade:** PD-1+TIM-3 co-blockade rescues deeply exhausted T cells; this is the next frontier after PD-1 monotherapy failure
- Agents in trials: Sabatolimab (MBG453), Cobolimab, LY3321367

---

#### 4. LAG-3 (Lymphocyte Activation Gene-3; CD223)

- Expressed on: activated and exhausted T cells, Tregs, NK cells
- **Ligand:** MHC class II (binds with higher affinity than CD4)
- Mechanism: inhibits T-cell activation by reducing TCR signalling through MHC class II binding on APCs
- **Relatlimab (anti-LAG-3)** + nivolumab (RELATIVITY-047): approved for unresectable/metastatic melanoma (2022) — the first LAG-3 inhibitor approval
- HNSCC-specific trials with anti-LAG-3 + anti-PD-1 combinations: ongoing

---

#### 5. TIGIT (T-cell Immunoreceptor with Ig and ITIM Domains)

- Expressed on: activated T cells, Tregs, NK cells; upregulated during exhaustion
- **Ligands:** CD155 (PVR) and CD112 (Nectin-2) on APCs and tumour cells
- Competes with co-stimulatory **CD226** (DNAM-1) for CD155 binding; TIGIT wins → inhibitory signal
- Double function: inhibits T cells directly AND promotes Treg activity
- Anti-TIGIT agents: Tiragolumab, Vibostolimab — in combination with atezolizumab/pembrolizumab; early-phase HNSCC trials

---

### Biomarkers for ICI Response

| Biomarker | Assay | Role |
|---|---|---|
| **PD-L1 CPS** | IHC (22C3 PharmDx clone) | Pembrolizumab 1st-line approval: CPS ≥1 (mono), CPS ≥20 (best OS) |
| **PD-L1 TPS** | IHC | Less discriminatory than CPS in HNSCC; used in some nivolumab analyses |
| **TMB-H** (≥10 mut/Mb) | NGS | FDA pan-tumour approval for pembrolizumab (KEYNOTE-158) |
| **MSI-H / dMMR** | IHC + PCR | FDA pan-tumour pembrolizumab; rare in HNSCC (<5%) |
| **HPV/p16 status** | p16 IHC / HPV ISH | HPV+ HNSCC has higher TIL density; greater nivolumab benefit (HR 0.55 in CheckMate 141) |
| **IFN-γ gene expression signature** | RNA-seq / NanoString | Investigational; high expression = inflamed phenotype = better response |
| **TIL density (CD8+)** | IHC | Higher intratumoral CD8+ TIL → better ICI response |
| **PD-L1 on TILs / TAMs** | IHC | Component of CPS calculation; immune cell PD-L1 highly predictive |

---

### Immune-Related Adverse Events (irAEs)

Loss of peripheral tolerance (the intended effect of ICIs) can cause inflammatory injury to any organ — this is the price of releasing the immune brake.

**Epidemiology:**
- Anti-PD-1 (nivolumab, pembrolizumab): any-grade irAEs ~55–70%; grade 3–4 ~13–15%
- Anti-CTLA-4 (ipilimumab): any-grade ~80%; grade 3–4 ~25–30%
- Combination (anti-PD-1 + anti-CTLA-4): any-grade ~95%; grade 3–4 ~55%

**Organ-specific irAEs and management:**

| Organ | irAE | Grade 3–4 Incidence | First-line Management |
|---|---|---|---|
| Skin | Rash, pruritus, vitiligo | 1–2% | Topical/oral steroids |
| Endocrine — thyroid | Hypo or hyperthyroidism | 1–2% | TSH replacement; beta-blockers |
| Endocrine — pituitary | Hypophysitis (headache, fatigue, hypogonadism) | 1% | High-dose prednisone; hormone replacement |
| Endocrine — adrenal | Primary adrenal insufficiency | <1% | Hydrocortisone replacement (lifelong) |
| GI | Diarrhoea, colitis | 2–5% (anti-PD-1); 10–15% (anti-CTLA-4) | Hold ICI; prednisone 1–2 mg/kg; infliximab 5 mg/kg if refractory |
| Liver | Hepatitis (↑ALT/AST) | 2–3% | Hold ICI; prednisone; mycophenolate if refractory |
| Lung | Pneumonitis | 2–4% | Hold ICI; methylprednisolone 1–2 mg/kg IV; CT chest; BAL |
| Kidney | Nephritis (↑creatinine) | <1% | Hold ICI; prednisone |
| Cardiac | Myocarditis | <0.5% | **PERMANENTLY DISCONTINUE; IV steroids; urgent cardiology** |
| Musculoskeletal | Arthritis, myositis | 1–2% | NSAIDs; steroids |
| Neurological | Peripheral neuropathy, encephalitis | <1% | Hold ICI; high-dose steroids; IVIG |
| Ocular | Uveitis, episcleritis | <1% | Topical/systemic steroids; ophthalmology |

**CTCAE grading — action:**
| Grade | Definition | Action |
|---|---|---|
| 1 | Mild; asymptomatic | Continue ICI; close monitoring |
| 2 | Moderate; limiting instrumental ADL | **Hold ICI**; oral prednisone 0.5–1 mg/kg; resume after recovery to ≤G1 |
| 3 | Severe; limiting self-care ADL | **Hold ICI**; IV methylprednisolone 1–2 mg/kg; consider permanent discontinuation |
| 4 | Life-threatening | **Permanently discontinue ICI**; IV steroids; urgent specialist input |
| 5 | Death | — |

**Key principles:**
- Never use prophylactic immunosuppression — irAEs are not predictable by timing and prophylaxis reduces efficacy
- Steroids are the backbone for most irAEs — taper slowly over ≥4 weeks to prevent rebound
- Refractory irAEs: infliximab (TNF-α blockade) for colitis; mycophenolate for hepatitis; IVIG/plasmapheresis for neurological irAEs
- Endocrine irAEs (hypothyroidism, adrenal insufficiency): DO NOT resolve with steroids — lifelong hormone replacement needed; ICI can often be continued

---

> [!example] Examiner's Summary
> Immune checkpoints (PD-1, CTLA-4, TIM-3, LAG-3, TIGIT) are physiological brakes that prevent autoimmunity but are co-opted by tumours to evade immune destruction — hence the term "immune gatekeepers." PD-1/PD-L1 operates in the tumour microenvironment: PD-L1 on tumour cells engages PD-1 on T cells → SHP-2 activation → ZAP-70 dephosphorylation → T-cell exhaustion. Adaptive immune resistance (IFN-γ–driven PD-L1 upregulation) explains why the immune response paradoxically fuels immune evasion. CTLA-4 operates earlier, competing with CD28 in the lymph node to block co-stimulation. Both nivolumab (anti-PD-1, CheckMate 141) and pembrolizumab (anti-PD-1, KEYNOTE-048) are approved in R/M HNSCC. irAEs result from loss of peripheral tolerance and are managed with organ-specific corticosteroids; grade 4 events require permanent ICI discontinuation.

> [!tip] Clinical Pearls
> 1. CTLA-4 acts in the lymph node (priming); PD-1 acts in the tumour (effector) — they regulate different phases of the T-cell response and are synergistic when co-blocked.
> 2. CTLA-4 binds CD80/CD86 with 20× higher affinity than CD28 — it wins the competition and shuts down co-stimulation.
> 3. Adaptive immune resistance: IFN-γ from TILs upregulates PD-L1 on tumour cells via JAK1/2–STAT1 → the immune attack creates its own blockade — this is why ICI therapy is needed to sustain T-cell activity.
> 4. PD-L1 CPS (counts tumour cells AND immune cells in the numerator) is more predictive than TPS (counts only tumour cells) in HNSCC.
> 5. TIM-3 co-expression with PD-1 marks deeply exhausted T cells — anti-PD-1 monotherapy may not rescue these; this is the rationale for TIM-3 + PD-1 co-blockade in the next generation of trials.
> 6. Myocarditis is rare (<0.5%) but has ~50% case fatality rate — permanent discontinuation is mandatory; no rechallenge.
> 7. Endocrine irAEs (hypothyroidism, adrenal insufficiency): the endocrine gland is permanently destroyed — hormone replacement is needed lifelong; ICI can usually be continued because the condition is manageable.
> 8. IFN-γ upregulates PD-L1 through JAK1/2–STAT1 pathway — JAK inhibitors (ruxolitinib) are being studied as a way to reduce adaptive PD-L1 upregulation in tumours.
> 9. TIGIT competes with DNAM-1 (CD226) for CD155 — both bind the same ligand; TIGIT has immunoinhibitory ITIM; DNAM-1 has co-stimulatory function — TIGIT tilts the balance toward T-cell inhibition.
> 10. The Nobel Prize analogy for exam: Allison (CTLA-4) + Honjo (PD-1) shared the 2018 Nobel Prize in Physiology or Medicine — mention this to examiners when asked about the discovery of checkpoint blockade.

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/Radiotherapy and Chemotherapy/index|Radiotherapy and Chemotherapy]]
>
> **Related Notes:**
> - [[Answers/Radiotherapy and Chemotherapy/Nivolumab in HNSCC|Nivolumab in HNSCC]] — CheckMate 141; clinical application of anti-PD-1 in 2nd-line R/M HNSCC
> - [[Answers/Radiotherapy and Chemotherapy/Pembrolizumab in HNSCC|Pembrolizumab in HNSCC]] — KEYNOTE-048; clinical application and PD-L1 CPS biomarker
> - [[Answers/Radiotherapy and Chemotherapy/Immunotherapy in HNC|Immunotherapy in HNC]] — clinical role overview, irAE management algorithm, future directions
>
> **See Also:**
> - [[Answers/General/Apoptosis|Apoptosis]] — T-cell exhaustion vs apoptosis; co-inhibitory receptor signalling converges on pro-apoptotic pathways
> - [[Answers/Radiotherapy and Chemotherapy/Adoptive Cell Immunotherapy|Adoptive Cell Immunotherapy]] — TIL therapy and CAR-T as alternatives when checkpoint blockade fails
