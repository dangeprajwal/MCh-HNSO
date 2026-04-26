---
tags:
  - Radiotherapy-and-Chemotherapy
  - Systemic-Therapy
  - Molecular-Biology
---

> [!question] Questions Covered
> - **Chemo Q8:** Mechanism of action of taxanes and platinum compounds (KIDWAI 2020)

## Source
**Shah JP. Head and Neck Surgery and Oncology, 5th Ed. Elsevier, 2019**; Harrison LB et al. Head and Neck Cancer: A Multidisciplinary Approach. 4th ed. 2014; De Vita VT et al. Cancer: Principles and Practice of Oncology. 11th ed. 2019; Stell & Maran's Textbook of Head and Neck Surgery and Oncology. 5th ed. 2012.

> [!cite] Landmark Articles
>
> The clinical use of cisplatin in HNSCC was established through multiple seminal trials. Vermorken et al. (2008) published the EXTREME trial in the New England Journal of Medicine, establishing first-line cetuximab + platinum + 5-FU as standard for recurrent/metastatic HNSCC — platinum compounds remain the backbone of R/M treatment. Calvert et al. (1989) published the original pharmacokinetically guided formula for carboplatin dosing (AUC-based), now universally adopted to replace body surface area dosing for carboplatin. The taxane contribution to HNSCC was established through induction chemotherapy trials: Posner et al. (2007) and Vermorken et al. (2007) independently reported the TAX 323 and TAX 324 trials demonstrating that docetaxel-cisplatin-5-FU (TPF) induction chemotherapy significantly improved survival over cisplatin-5-FU (PF) in locally advanced HNSCC. Blanchard et al. (2013) confirmed this in a meta-analysis of five TPF vs PF trials.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Vermorken JB et al. (EXTREME) — Cisplatin, Fluorouracil, and Cetuximab in Head and Neck Cancer | N Engl J Med | 2008 | [10.1056/NEJMoa0802656](https://doi.org/10.1056/NEJMoa0802656) |
> | Calvert AH et al. — Carboplatin Dosage: Prospective Evaluation of a Simple Formula Based on Renal Function | J Clin Oncol | 1989 | [10.1200/JCO.1989.7.11.1748](https://doi.org/10.1200/JCO.1989.7.11.1748) |
> | Posner MR et al. (TAX 324) — Cisplatin and Fluorouracil Alone or with Docetaxel in Head and Neck Cancer | N Engl J Med | 2007 | [10.1056/NEJMoa070956](https://doi.org/10.1056/NEJMoa070956) |
> | Vermorken JB et al. (TAX 323) — Docetaxel Plus Cisplatin and Fluorouracil Versus Cisplatin and Fluorouracil in Head and Neck Cancer | N Engl J Med | 2007 | [10.1056/NEJMoa071028](https://doi.org/10.1056/NEJMoa071028) |

---

## PART A: Platinum Compounds

Platinum-based compounds are the cornerstone of HNSCC chemotherapy — used in concurrent CRT (cisplatin), adjuvant CRT (cisplatin), induction chemotherapy (cisplatin as part of TPF), and recurrent/metastatic HNSCC (cisplatin or carboplatin + 5-FU ± cetuximab or pembrolizumab).

### Cisplatin (cis-Diamminedichloroplatinum II)

#### Mechanism of Uptake

Cisplatin is a neutral inorganic platinum complex at physiological plasma chloride concentrations (approximately 100 mM). It enters cells via:
- **Passive diffusion** (primary, down concentration gradient)
- **Active transport** via **CTR1** (copper transporter 1, SLC31A1) — the major active uptake transporter; CTR1 downregulation is a mechanism of acquired resistance

#### Intracellular Activation (Aquation)

Inside the cell, intracellular chloride concentration is low (~4 mM). This chloride-deficient environment promotes **aquation**: the two chloride ligands are displaced by water molecules, generating highly reactive **monoaqua** and **diaqua** platinum species (aquaplatin). These aquaplatin species are the cytotoxic form — they carry a positive charge and react avidly with electron-rich sites on DNA and proteins.

#### DNA Adduct Formation and Cytotoxicity

Cisplatin reacts preferentially with guanine N7 atoms, forming:

| Adduct Type | Frequency | Location |
|---|---|---|
| 1,2-d(GpG) intrastrand crosslink (adjacent guanines, same strand) | ~65% | Major groove |
| 1,2-d(ApG) intrastrand crosslink | ~25% | Major groove |
| 1,3-intrastrand crosslink (d(GpXpG)) | ~5–6% | Major groove |
| Interstrand crosslink (G:G on opposite strands) | ~1–2% | |
| Protein–DNA crosslinks | rare | |

The **1,2-d(GpG) intrastrand crosslink** is the most abundant and biologically relevant adduct. These bulky adducts:
1. Distort the DNA helix (bend and unwind), recognisable by damage-sensing proteins
2. **Block DNA replication fork progression** — polymerases stall at the adduct
3. Activate **nucleotide excision repair (NER)** — the predominant repair pathway for Pt-DNA adducts; involves XPC-RAD23B (damage recognition), TFIIH (helicase), XPA/RPA (verification), followed by dual incision by ERCC1-XPF (5' cut) and XPG (3' cut), removing a ~30-nucleotide oligonucleotide containing the adduct

When NER is overwhelmed or the replication fork stall is irresolvable, the cell activates **ATR/ATM kinase cascade** → CHK1/CHK2 → p53 stabilisation → cell cycle arrest at G1/S or G2/M → apoptosis via intrinsic (mitochondrial) pathway.

#### Cell Cycle Effects

Cisplatin is considered **cell cycle non-specific** (can form adducts in any phase), but **S-phase cells** are most sensitive because active replication maximises the probability of a fork colliding with an unrepaired adduct. Cisplatin also causes accumulation in **G2/M**, which is the cell cycle phase of maximum radiosensitivity.

#### Radiosensitisation Mechanisms

Cisplatin potentiates radiation injury through multiple mechanisms:
1. **Inhibition of sublethal damage repair (SLD repair)**: cisplatin adducts consume NER machinery, reducing capacity to repair radiation-induced base damage and single-strand breaks
2. **Cell cycle synchronisation**: accumulation of cells in radiosensitive G2/M phase
3. **Damage fixation**: cisplatin adducts at radiation-induced base damage sites prevent repair, converting sublethal to lethal lesions
4. **Hypoxic cell sensitisation**: some radiosensitisation independent of oxygen level

#### Resistance Mechanisms

| Mechanism | Detail |
|---|---|
| Reduced uptake | CTR1 downregulation; MRP2 (ABCC2) upregulation (efflux) |
| Increased efflux | P-glycoprotein (MDR1/ABCB1), MRP2, MVP (major vault protein) |
| Sequestration | Metallothionein and glutathione bind platinum before it reaches DNA |
| Enhanced NER | ERCC1/XPF overexpression — faster repair of Pt-DNA adducts; ERCC1 expression correlates inversely with cisplatin sensitivity in HNSCC |
| Tolerance of adducts | Upregulated translesion synthesis (TLS) polymerases (pol η, pol ζ) bypass adducts without triggering apoptosis |
| Apoptosis pathway loss | p53 mutation, MDM2 amplification, Bcl-2 overexpression |
| Drug inactivation | Increased intracellular thiol levels (glutathione, cysteine) chemically inactivate platinum |

#### Toxicity Profile

| Toxicity | Mechanism / Notes | Management |
|---|---|---|
| **Nephrotoxicity** (dose-limiting) | Proximal tubular damage; Na⁺ and Mg²⁺ wasting; AKI; avoid CrCl <60 mL/min | 2–3 L IV hydration pre and post; mannitol diuresis; magnesium supplementation; avoid nephrotoxic co-medications |
| **Ototoxicity** (irreversible) | High-frequency sensorineural hearing loss (4–8 kHz); damage to cochlear outer hair cells | Baseline and periodic audiometry; irreversible; amifostine may partially protect (limited evidence) |
| **Peripheral neuropathy** | Sensory > motor; stocking-glove distribution; cumulative | Dose reduction; no established preventive agent |
| **Nausea/vomiting** | Most emetogenic single agent in oncology (highly emetogenic); acute (0–24h) and delayed (24–120h) | Mandatory: 5-HT₃ antagonist (ondansetron) + NK₁ antagonist (aprepitant) + dexamethasone; lorazepam for anticipatory emesis |
| Myelosuppression | Moderate; nadir at Day 10–14 | Monitor CBC; G-CSF if febrile neutropenia |
| Alopecia | Mild–moderate | |
| Electrolyte disturbances | Hypomagnesaemia, hypocalcaemia, hypokalaemia | Regular monitoring and supplementation |

#### Standard Doses in HNSCC

- **Concurrent CRT (definitive)**: 100 mg/m² IV q21d × 3 cycles (standard high-dose); or 40 mg/m² IV weekly × 6–7 cycles (lower toxicity, equivalent efficacy — widely used)
- **TPF induction chemotherapy**: cisplatin 75 mg/m² D1 + docetaxel 75 mg/m² D1 + 5-FU 750 mg/m²/day D1–5, q21d
- **RADPLAT**: 150 mg/m² IA weekly (with STS neutralisation — see RADPLAT file)

---

### Carboplatin

Carboplatin replaces the two chloride leaving groups with a cyclobutane-1,1-dicarboxylate (CBDCA) bidentate ligand. This makes carboplatin more stable, slower to activate by aquation, and **less reactive with plasma proteins** — reducing non-renal clearance and making renal excretion the dominant elimination pathway.

**Same MOA as cisplatin**: forms the same Pt-DNA intrastrand crosslinks after aquation; equivalent anti-tumour activity to cisplatin at equimolar doses.

**Pharmacokinetic-based dosing (Calvert formula)**:
> Total dose (mg) = Target AUC × (GFR + 25)

Where GFR is measured or estimated (Cockcroft-Gault), and target AUC is typically 5–6 mg/mL·min for combination regimens. This formula was derived and validated by Calvert et al. (1989) and accounts for renal drug clearance directly.

**Toxicity differences from cisplatin:**

| Toxicity | Carboplatin | Cisplatin |
|---|---|---|
| Nephrotoxicity | Substantially less | Dose-limiting |
| Ototoxicity | Less | Significant |
| Neuropathy | Less | Significant |
| Nausea/vomiting | Moderate (moderately emetogenic) | Severe (highly emetogenic) |
| **Myelosuppression** | **Dose-limiting** (thrombocytopenia > neutropenia) | Moderate |
| Alopecia | Mild | Mild–moderate |

**Clinical use in HNSCC**: used as **substitute for cisplatin** in patients with: CrCl <60 mL/min, pre-existing Grade ≥2 neuropathy, Grade ≥2 hearing loss, poor performance status precluding high-dose cisplatin. Carboplatin (AUC 5) + 5-FU is the standard backbone for R/M HNSCC (EXTREME/KEYNOTE-048 regimens) in cisplatin-ineligible patients.

---

### Oxaliplatin

Third-generation platinum; trans-R,R-diaminocyclohexane (DACH) carrier ligand. Forms bulky Pt-DACH-DNA adducts that are poorly recognised by mismatch repair — active in colorectal cancer (oxaliplatin + 5-FU: FOLFOX). Limited use in HNSCC. Characteristic toxicity: **acute cold-triggered peripheral neuropathy** (laryngopharyngeal dysaesthesia on cold exposure) and chronic sensory neuropathy.

---

## PART B: Taxanes

Taxanes are **antimicrotubule agents** that work by stabilising microtubules rather than depolymerising them — the opposite mechanism to vinca alkaloids (which inhibit polymerisation). They are used in HNSCC in induction chemotherapy (TPF: docetaxel + cisplatin + 5-FU) and, as single agents or in combinations, in recurrent/metastatic HNSCC.

### Microtubule Biology (Background)

Microtubules are polymers of α/β-tubulin heterodimers. They exist in **dynamic instability** — rapidly interconverting between phases of growth (polymerisation) and shrinkage (depolymerisation). This dynamic behaviour is essential for:
- **Mitotic spindle formation**: spindle fibres attach to kinetochores on chromosomes; dynamic instability allows chromosomes to be pulled to opposite poles during anaphase
- Intracellular transport
- Cell shape and motility

Interference with dynamic instability — in either direction (prevention of polymerisation by vinca alkaloids, or prevention of depolymerisation by taxanes) — arrests cells in mitosis, preventing chromosome segregation and triggering apoptosis.

---

### Paclitaxel (Taxol)

Paclitaxel is a diterpenoid natural product originally isolated from the Pacific yew tree (*Taxus brevifolia*); now semi-synthesised from *Taxus baccata* needles.

#### Mechanism of Action

Paclitaxel binds to a specific binding site on the **N-terminal region of β-tubulin** within assembled microtubules (the taxane-binding pocket). This binding:
1. **Stabilises microtubules against depolymerisation** — prevents the GDP-bound tubulin conformation from causing filament shrinkage
2. Creates abnormally stable, non-dynamic microtubules — the spindle cannot function because it cannot dynamically attach and detach from kinetochores
3. **Arrests cells in G2/M phase** (mitotic arrest) — cells cannot complete chromosome segregation and proceed to anaphase
4. Prolonged G2/M arrest → activation of the **spindle assembly checkpoint** (SAC; MAD2, BubR1) → mitotic catastrophe → apoptosis (intrinsic pathway via Bcl-2 phosphorylation and BAX/BAK activation)

The cell cycle specificity is **G2/M** — paclitaxel is most cytotoxic to cells in S-phase transit leading to mitosis or already in G2/M.

#### Formulation Issues

Paclitaxel is highly hydrophobic and insoluble in aqueous solvents. The original formulation uses **Cremophor EL** (polyoxyethylated castor oil) as solubilising vehicle. Cremophor EL itself can cause severe **acute hypersensitivity reactions** (anaphylactoid), including bronchospasm, urticaria, and haemodynamic compromise.

- **Mandatory premedication**: dexamethasone 20 mg IV (12h and 6h before, or 30 min before) + diphenhydramine (H1 blocker) + ranitidine or famotidine (H2 blocker) — given before every infusion
- Infused over 3 hours (slow infusion reduces hypersensitivity risk)

#### Resistance

| Mechanism | Detail |
|---|---|
| P-glycoprotein (MDR1/ABCB1) | Efflux pump that expels paclitaxel from cells; classical multidrug resistance |
| β-tubulin mutations | Mutations in paclitaxel-binding domain prevent binding |
| Altered tubulin isotype expression | Increased β-III tubulin (TUBB3) associated with taxane resistance in HNSCC and other cancers |

#### Toxicity Profile

| Toxicity | Notes |
|---|---|
| **Peripheral neuropathy** (dose-limiting) | Sensory > motor; length-dependent stocking-glove; cumulative; can be severe and irreversible at high cumulative doses; paclitaxel causes more neuropathy than docetaxel |
| Hypersensitivity | Cremophor EL-related; prevented by premedication |
| Myelosuppression | Neutropenia (nadir Day 8–11) |
| Alopecia | Universal; reversible |
| Myalgia/arthralgia | Common, especially with weekly regimens |
| Cardiac | Bradyarrhythmia (rare); heart block (rare) |

---

### Docetaxel (Taxotere)

Semi-synthetic analogue of paclitaxel; same β-tubulin taxane-pocket binding mechanism; **higher binding affinity** than paclitaxel.

**Key differences from paclitaxel:**

| Feature | Paclitaxel | Docetaxel |
|---|---|---|
| Formulation | Cremophor EL (polysorbate ethanol) | Polysorbate 80 (also causes hypersensitivity but different pattern) |
| Myelosuppression | Moderate | **More severe neutropenia** — G-CSF prophylaxis required with TPF |
| Peripheral neuropathy | More severe | Less severe |
| Fluid retention | Not characteristic | **Docetaxel-specific fluid retention** — pleural effusion, ascites, peripheral oedema; prevented by mandatory dexamethasone pre-treatment 3 days before and after each cycle (dexamethasone 8 mg BD × 3 days starting Day -1) |
| Premedication | Dexamethasone + H1 + H2 | Dexamethasone × 3 days (different rationale — both hypersensitivity prevention AND fluid retention prevention) |
| Dose in TPF | — | 75 mg/m² D1 q21d |

**Docetaxel use in HNSCC:**
- **TPF induction**: docetaxel 75 mg/m² + cisplatin 75 mg/m² + 5-FU 750 mg/m²/d × 5 days, q21d × 3 cycles (TAX 323, TAX 324 regimens) — superior to PF induction; G-CSF support is **mandatory** between cycles
- Weekly docetaxel: 35 mg/m² weekly; used in R/M HNSCC or as radiosensitiser
- **Scalp cooling** and **G-CSF** recommendations differ between paclitaxel and docetaxel regimens

---

### Nab-Paclitaxel (Abraxane)

Albumin-nanoparticle–bound paclitaxel (nab-paclitaxel): paclitaxel bound to human albumin nanoparticles (130 nm); no Cremophor EL required.

**Advantages over conventional paclitaxel:**
- No Cremophor → no HSR from vehicle; **no premedication required**
- Higher maximum tolerated dose possible (260 mg/m² vs 175 mg/m²)
- Exploits **SPARC** (secreted protein acidic and rich in cysteine) — overexpressed in tumour stroma — to concentrate albumin-bound drug in tumour microenvironment

**Status in HNSCC**: Phase II data in R/M HNSCC show activity; no Phase III regulatory approval for HNSCC; used in clinical trials and some institutional protocols.

---

## Combined Platinum + Taxane Synergy

The combination of cisplatin and paclitaxel/docetaxel is synergistic rather than merely additive:

| Mechanism of Synergy | Detail |
|---|---|
| Complementary DNA damage + mitotic arrest | Cisplatin causes DNA adducts → G2/M arrest; paclitaxel stabilises microtubules → G2/M arrest → cells trapped in G2/M when both agents present |
| Sequential enhancement | Cisplatin-induced G2/M arrest synchronises cells in the phase most sensitive to paclitaxel's anti-mitotic effect |
| Separate resistance pathways | Different efflux pumps and resistance mechanisms → less cross-resistance |
| Radiosensitisation from both | Both agents independently sensitise cells to radiation at G2/M checkpoint |

In the TPF induction regimen (docetaxel + cisplatin + 5-FU), all three drugs target different molecular mechanisms — platinum (DNA crosslinks), taxane (mitotic arrest), and 5-FU (nucleotide synthesis inhibition) — creating a highly effective anti-tumour combination.

---

> [!example] Examiner's Summary
> Platinum compounds (cisplatin, carboplatin) act by forming covalent intra-strand DNA crosslinks at guanine N7, predominantly 1,2-d(GpG) adducts (65%), after intracellular aquation; these stall DNA replication forks, activate NER repair (rate-limited by ERCC1-XPF), and trigger p53-mediated apoptosis when repair is overwhelmed. Cisplatin's dose-limiting toxicities are nephrotoxicity (requiring aggressive hydration) and ototoxicity (irreversible high-frequency sensorineural loss); carboplatin substitutes the CBDCA ligand, causing less nephrotoxicity/neurotoxicity but more myelosuppression, and is dosed by the Calvert AUC formula. Taxanes (paclitaxel, docetaxel) bind the taxane pocket on β-tubulin and stabilise microtubules against depolymerisation — the opposite of vinca alkaloids — causing G2/M mitotic arrest and apoptosis; paclitaxel causes more peripheral neuropathy while docetaxel causes more myelosuppression and characteristic fluid retention (prevented by 3-day dexamethasone). The TPF induction regimen (docetaxel + cisplatin + 5-FU) was established by the TAX 323 and TAX 324 trials as superior to PF induction for locally advanced HNSCC.

> [!tip] Clinical Pearls
> 1. Cisplatin aquation (replacement of chloride ligands by water) is the activation step producing the cytotoxic aquaplatin species — it occurs preferentially in low-chloride intracellular environments.
> 2. The dominant Pt-DNA adduct (65%) is the **1,2-d(GpG) intrastrand crosslink** (adjacent guanines, same strand).
> 3. ERCC1 (nucleotide excision repair) is the key resistance mediator — high ERCC1 expression correlates with cisplatin resistance in HNSCC.
> 4. Carboplatin is dosed by the **Calvert formula**: Total dose (mg) = AUC × (GFR + 25); not body surface area — this is the key pharmacokinetic principle.
> 5. Taxanes **stabilise** microtubules; vinca alkaloids **destabilise** them — both arrest cells in G2/M but by opposite mechanisms.
> 6. Mandatory premedication before every paclitaxel infusion: **dexamethasone + diphenhydramine + H2 blocker** — prevents Cremophor EL-induced hypersensitivity.
> 7. Mandatory premedication before every docetaxel infusion: **dexamethasone 8 mg BD × 3 days** (starting Day -1) — prevents both hypersensitivity AND docetaxel-specific fluid retention (pleural effusion, oedema).
> 8. **G-CSF support is mandatory** with TPF (docetaxel + cisplatin + 5-FU) induction chemotherapy to prevent febrile neutropenia.
> 9. Nab-paclitaxel (Abraxane) eliminates Cremophor — no premedication required; higher MTD; validated in Phase II HNSCC trials.
> 10. Cisplatin's most emetogenic profile requires **5-HT₃ antagonist + NK₁ antagonist + dexamethasone** as triple antiemetic premedication — single-agent cisplatin (100 mg/m²) is the most highly emetogenic chemotherapy agent in clinical use.

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/Radiotherapy and Chemotherapy/index|Radiotherapy and Chemotherapy]]
>
> **Related Notes:**
> - [[Answers/Radiotherapy and Chemotherapy/Chemoradiation Principles and Applications|Chemoradiation Principles and Applications]] — concurrent CRT regimens and platinum use
> - [[Answers/Radiotherapy and Chemotherapy/Selective Intra-arterial Chemotherapy and RADPLAT|Selective Intra-arterial Chemotherapy and RADPLAT]] — cisplatin pharmacokinetics in IA delivery
> - [[Answers/Radiotherapy and Chemotherapy/Mucositis Management with Targeted Therapies|Mucositis Management with Targeted Therapies]] — toxicity management
>
> **See Also:**
> - [[Answers/Larynx/Landmark Trials and Organ Preservation Strategies|Landmark Trials and Organ Preservation Strategies]] — TPF induction evidence (TAX 323, TAX 324)
> - [[Answers/Radiotherapy and Chemotherapy/Pembrolizumab in HNSCC|Pembrolizumab in HNSCC]] — KEYNOTE-048; platinum + 5-FU backbone combined with pembrolizumab
