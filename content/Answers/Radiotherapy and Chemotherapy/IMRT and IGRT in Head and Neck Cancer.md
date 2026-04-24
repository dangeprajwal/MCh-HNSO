---
title: "IMRT and IGRT in Head and Neck Cancer"
tags:
  - Radiotherapy
  - Diagnostics
  - Evidence-Based
---

> [!question] MCh Exam Questions
> - **Q2** IMRT in head and neck cancer (AIIMS 2020)
> - **Q13** IGRT (AMRITA 2010)
> - **Q17** IMRT (AMRITA 2016)
> - **Q21** IGRT (AMRITA 2018)
> - **Q33** Role of IGRT in HNC (TMH 2017)
> - **Q38** IMRT and IGRT in laryngeal/hypopharyngeal cancers (TMH 2018)
> - **Q39** IMRT in management of HNC (TMH 2018)
> - **Q50** Intensity modulated radiation techniques (TMH 2020)

## Source

Harrison LB, Sessions RB, Kies MS. *Head and Neck Cancer: A Multidisciplinary Approach*. 4th ed. Lippincott Williams & Wilkins; 2014. Ch22, Ch23; Halperin EC, Wazer DE, Perez CA, Brady LW. *Perez & Brady's Principles and Practice of Radiation Oncology*. 7th ed. Wolters Kluwer; 2019. Ch39, Ch40; Shah JP. *Head and Neck Surgery and Oncology*. 5th ed. Elsevier; 2019. Ch14

> [!cite]- Landmark Articles
>
> Nutting et al. (2011) conducted the PARSPORT trial, a landmark phase 3 multicentre RCT demonstrating that parotid-sparing IMRT significantly reduced grade 2 or worse xerostomia from 83% to 29% at 24 months compared with conventional radiotherapy in head and neck cancer, establishing IMRT as the standard of care. Kam et al. (2007) performed a prospective randomised study comparing IMRT with two-dimensional RT in early-stage NPC, showing that IMRT significantly reduced severe xerostomia (39% vs 82%) and preserved higher stimulated parotid flow rates. Gupta et al. (2012) conducted an RCT comparing 3D-CRT versus IMRT in head and neck squamous cell carcinoma, finding that IMRT significantly reduced grade 2+ acute salivary gland toxicity (59% vs 89%). Jaffray (2007) published a comprehensive review of image-guided radiation therapy, outlining the technologies enabling real-time treatment verification and adaptive strategies. Wu et al. (2003) reported the dosimetric results of simultaneous integrated boost IMRT for locally advanced HNSCC, demonstrating the feasibility of dose escalation to gross tumour volumes while maintaining organ-at-risk constraints. Gregoire et al. (2003) published the landmark CT-based consensus guidelines for delineation of lymph node levels and related CTVs in the node-negative neck, providing the standardised framework adopted internationally for conformal and IMRT planning.
>
> | Study | Journal | Year | Key Finding |
> |---|---|---|---|
> | Nutting — Parotid-Sparing Intensity Modulated Versus Conventional Radiotherapy in Head and Neck Cancer (PARSPORT): A Phase 3 Multicentre Randomised Controlled Trial | Lancet Oncol | 2011 | IMRT reduced grade 2+ xerostomia from 83% to 29% at 24 months |
> | Kam — Prospective Randomized Study of Intensity-Modulated Radiotherapy on Salivary Gland Function in Early-Stage Nasopharyngeal Carcinoma Patients | J Clin Oncol | 2007 | IMRT reduced severe xerostomia (39% vs 82%) with superior parotid flow preservation |
> | Gupta — Three-Dimensional Conformal Radiotherapy (3D-CRT) Versus Intensity Modulated Radiation Therapy (IMRT) in Squamous Cell Carcinoma of the Head and Neck: A Randomized Controlled Trial | Radiother Oncol | 2012 | IMRT reduced grade 2+ salivary toxicity (59% vs 89%, p=0.009) |
> | Jaffray — Review of Image-Guided Radiation Therapy | Expert Rev Anticancer Ther | 2007 | Comprehensive framework for IGRT technologies including CBCT and adaptive strategies |
> | Wu — Simultaneous Integrated Boost Intensity-Modulated Radiotherapy for Locally Advanced Head-and-Neck Squamous Cell Carcinomas: Dosimetric Results | Int J Radiat Oncol Biol Phys | 2003 | SIB-IMRT feasible for dose escalation up to 73.8 Gy in 30 fractions to GTV |
> | Gregoire — CT-Based Delineation of Lymph Node Levels and Related CTVs in the Node-Negative Neck: DAHANCA, EORTC, GORTEC, NCIC, RTOG Consensus Guidelines | Radiother Oncol | 2003 | International consensus standardising nodal CTV delineation for conformal/IMRT planning |

## Intensity Modulated Radiation Therapy (IMRT)

### Principles and Rationale

Intensity modulated radiation therapy (IMRT) represents a fundamental advance over conventional and 3D-CRT techniques by modulating the intensity of each radiation beam across the treatment field. This allows creation of highly conformal dose distributions that closely conform to irregular target volumes while simultaneously sparing adjacent organs at risk (OARs).

**Key principles:**

1. **Inverse planning** -- unlike forward planning (3D-CRT), the clinician specifies the desired dose to targets and OAR dose limits; the optimisation algorithm then determines optimal beam fluence patterns
2. **Multi-leaf collimator (MLC) modulation** -- each beam is divided into multiple segments (beamlets) with varying intensities, delivered via dynamic MLC (sliding window) or step-and-shoot (segmental) techniques
3. **Dose painting** -- ability to deliver different dose levels to different target volumes simultaneously
4. **Simultaneous integrated boost (SIB)** -- delivers higher dose per fraction to gross disease (GTV) and lower dose per fraction to elective volumes in a single treatment session

### IMRT Delivery Techniques

| Technique | Mechanism | Advantages |
|---|---|---|
| Step-and-shoot (segmental) | MLC shapes discrete segments per beam angle | Simple QA, widely available |
| Dynamic (sliding window) | MLC leaves move continuously during irradiation | Smoother fluence, faster delivery |
| VMAT/RapidArc | Gantry rotates continuously with dynamic MLC and dose rate modulation | Fastest delivery (2-5 min), fewer MU |
| Helical (TomoTherapy) | Fan beam rotates helically around patient | 360-degree optimisation, built-in MVCT |

### Target Volume Delineation for IMRT

Accurate target delineation is the critical first step in IMRT planning. The International Commission on Radiation Units (ICRU) framework defines:

**Gross Tumour Volume (GTV):**
- Macroscopic tumour visible on imaging and clinical examination
- Delineated on planning CT fused with MRI and/or PET-CT
- GTV-P (primary) and GTV-N (nodal) defined separately

**Clinical Target Volume (CTV):**
- GTV plus margin for microscopic disease extension
- High-risk CTV (CTV-HR): GTV + 5-10 mm margin, adapted to anatomic barriers
- Low-risk CTV (CTV-LR): elective nodal regions at risk of subclinical spread
- Nodal CTV delineation follows the Gregoire et al. consensus guidelines (levels I-VII)

**Planning Target Volume (PTV):**
- CTV plus margin for setup uncertainty and organ motion
- Typically 3-5 mm margin; can be reduced with IGRT (to 2-3 mm)
- PTV-HR receives 70 Gy (2.12 Gy/fraction in 33 fractions with SIB)
- PTV-intermediate: 59.4-63 Gy
- PTV-LR (elective): 54-56 Gy

### Dose Prescriptions in SIB-IMRT

| Target | Total Dose | Dose per Fraction | Indication |
|---|---|---|---|
| PTV-70 (GTV + margin) | 70 Gy | 2.12 Gy | Gross disease |
| PTV-63 (high-risk CTV) | 63 Gy | 1.91 Gy | High-risk subclinical |
| PTV-56 (low-risk CTV) | 56 Gy | 1.70 Gy | Elective nodal regions |
| PTV-54 (prophylactic) | 54 Gy | 1.64 Gy | Low-risk prophylactic |

All delivered in 33 fractions over 6.5 weeks.

### OAR Constraints (Dose-Volume Histogram Parameters)

| Organ at Risk | Constraint | Clinical Rationale |
|---|---|---|
| Spinal cord | D_max < 45 Gy (absolute < 50 Gy) | Myelopathy prevention |
| Brainstem | D_max < 54 Gy | Neurological injury |
| Parotid gland | Mean dose < 26 Gy (at least one); or V30 < 50% | Xerostomia reduction |
| Submandibular gland | Mean dose < 35 Gy | Saliva production |
| Oral cavity | Mean dose < 40 Gy | Mucositis, dysgeusia |
| Cochlea | Mean dose < 45 Gy | Sensorineural hearing loss |
| Brachial plexus | D_max < 66 Gy | Plexopathy prevention |
| Mandible | D_max < 70 Gy | Osteoradionecrosis |
| Larynx (if not target) | Mean dose < 40-45 Gy | Voice preservation |
| Pharyngeal constrictors | Mean dose < 50 Gy | Dysphagia reduction |
| Optic nerves/chiasm | D_max < 54 Gy | Visual impairment |

### Clinical Benefits of IMRT

**1. Parotid Sparing and Xerostomia Reduction:**
- The PARSPORT trial (Nutting et al., 2011) demonstrated reduction in grade 2+ xerostomia from 83% to 29% at 24 months
- Kam et al. (2007) showed preserved stimulated parotid flow rates with IMRT in NPC
- Meaningful improvement in patient-reported quality of life

**2. Dose Conformality and Escalation:**
- Superior target coverage (conformity index closer to 1.0)
- Ability to deliver simultaneous different dose levels
- Potential for dose escalation to resistant subvolumes (dose painting by numbers using PET)

**3. Reduced Normal Tissue Toxicity:**
- Lower rates of dysphagia through pharyngeal constrictor sparing (DARS approach)
- Reduced feeding tube dependence
- Lower rates of hypothyroidism (thyroid sparing)
- Submandibular gland transfer feasibility enhanced

**4. Treatment of Complex Anatomy:**
- Concave dose distributions wrapping around spinal cord
- Bilateral neck irradiation with midline sparing
- Re-irradiation scenarios with tight margins

## Image-Guided Radiation Therapy (IGRT)

### Rationale for IGRT

Head and neck cancers present unique challenges for treatment delivery accuracy:

1. **Interfraction motion** -- day-to-day changes in patient positioning, weight loss (up to 10% during treatment), tumour shrinkage, anatomical deformation
2. **Intrafraction motion** -- swallowing, breathing, involuntary movements during treatment
3. **Setup uncertainty** -- despite thermoplastic mask immobilisation, residual setup errors of 3-5 mm are common
4. **Anatomic changes** -- progressive weight loss causes parotid gland migration medially, altering dosimetry

IGRT enables verification and correction of patient position immediately before or during each treatment fraction, ensuring the planned dose distribution matches the actual delivered dose.

### IGRT Technologies

**1. Cone-Beam CT (CBCT):**
- Most widely used IGRT modality in H&N cancer
- kV CBCT mounted on the linear accelerator gantry (on-board imager)
- 3D volumetric image acquired in treatment position before each fraction
- Registered to planning CT for translational and rotational corrections
- Soft tissue visualisation enables target and OAR verification
- Typical acquisition time: 60-120 seconds

**2. Kilovoltage (kV) Planar Imaging:**
- 2D orthogonal kV images compared with digitally reconstructed radiographs (DRRs)
- Bony anatomy matching for setup correction
- Fast (seconds), low dose
- Limited soft tissue information

**3. Megavoltage (MV) Portal Imaging:**
- Electronic portal imaging device (EPID) using treatment beam
- Bony anatomy verification
- Higher dose than kV imaging; lower soft tissue contrast

**4. Surface-Guided Radiation Therapy (SGRT):**
- Optical surface monitoring systems (e.g., AlignRT, Catalyst)
- Real-time tracking of patient surface during treatment
- Non-ionising, no additional dose
- Useful for intrafraction motion monitoring

**5. ExacTrac and Stereoscopic kV Imaging:**
- Floor- or ceiling-mounted kV X-ray tubes with flat-panel detectors
- Stereoscopic imaging for 6-degree-of-freedom (6DoF) correction
- Particularly useful for stereotactic applications (SBRT for recurrent H&N)

**6. Electromagnetic Tracking (Calypso):**
- Implanted transponders tracked in real time
- Sub-millimetre accuracy
- Limited use in H&N due to implantation challenges

### IGRT Workflow in Head and Neck Cancer

1. **Immobilisation** -- thermoplastic mask (5-point or 7-point), custom head rest, shoulder retraction
2. **Pre-treatment imaging** -- daily CBCT (recommended) or weekly CBCT with daily kV orthogonal imaging
3. **Registration** -- automatic or manual registration of CBCT to planning CT
4. **Correction** -- online correction applied via couch shifts (translational +/- rotational with 6DoF couch)
5. **Threshold** -- action level typically 1-2 mm; systematic errors corrected immediately
6. **Treatment delivery** -- proceed with corrected position
7. **Post-treatment verification** -- optional MV portal or CBCT for quality assurance

### Benefits of IGRT

- **PTV margin reduction** -- from 5 mm to 2-3 mm, enabling further OAR sparing
- **Improved target coverage** -- detection and correction of geographic miss
- **Detection of anatomic changes** -- triggers for adaptive replanning
- **Quality assurance** -- documentation of treatment delivery accuracy
- **Dose tracking** -- accumulated dose estimation using deformable image registration

## Adaptive Radiation Therapy (ART)

### Rationale

During a 6-7 week course of H&N radiotherapy, significant anatomic changes occur:

- **Weight loss** -- average 5-10% body weight; alters external contour and internal anatomy
- **Tumour shrinkage** -- GTV regression leads to normal tissue moving into high-dose region
- **Parotid gland migration** -- medial shift of 3-5 mm; increases parotid dose beyond planned
- **Muscle/fat loss** -- changes body habitus and fit of immobilisation mask

### Triggers for Replanning

| Trigger | Threshold | Action |
|---|---|---|
| Weight loss | > 5% or > 3 kg | Rescan and replan |
| Significant tumour regression | Visual on CBCT | Rescan, recontour, replan |
| Mask fit deterioration | Loose fit, visible gaps | New mask, rescan, replan |
| Dosimetric deviation | OAR dose exceeds constraint on accumulated dose | Replan with updated anatomy |

### ART Workflow

1. Monitor anatomy on daily/weekly CBCT
2. Identify trigger for replanning (typically weeks 3-4)
3. Resimulation with new planning CT
4. Re-delineation of targets and OARs
5. Re-optimisation of IMRT plan
6. Quality assurance of new plan
7. Resume treatment with adapted plan

## Volumetric Modulated Arc Therapy (VMAT)

VMAT represents an evolution of IMRT where the gantry rotates continuously around the patient while simultaneously modulating MLC positions, dose rate, and gantry speed.

### Advantages Over Fixed-Field IMRT

- **Treatment time** -- 2-5 minutes vs 15-20 minutes for step-and-shoot IMRT
- **Monitor units** -- typically 20-30% fewer MU, reducing peripheral dose
- **Plan quality** -- comparable or superior conformity and homogeneity
- **Patient comfort** -- shorter treatment improves compliance and reduces intrafraction motion
- **Throughput** -- more patients treated per linear accelerator per day

### VMAT Planning Considerations

- Typically 2-3 full or partial arcs used for H&N
- Avoidance sectors can be programmed to reduce dose to specific OARs
- Collimator rotation between arcs improves MLC coverage of targets
- Comparable target coverage and OAR sparing to 7-9 field IMRT

## Site-Specific Applications

### Nasopharyngeal Carcinoma

- IMRT is the standard of care (Kam et al., 2007; Lee et al., RTOG 0225)
- Complex target geometry adjacent to brainstem, optic apparatus, temporal lobes
- SIB technique preferred: 70 Gy to GTV, 59.4 Gy to high-risk CTV, 54 Gy to low-risk CTV
- Bilateral retropharyngeal nodes always included in CTV
- IGRT essential due to tumour regression during treatment

### Oropharyngeal Cancer

- IMRT enables bilateral neck irradiation with parotid and pharyngeal constrictor sparing
- Dysphagia-Aspiration Related Structures (DARS) sparing approach
- HPV-positive: potential for dose de-escalation trials
- Submandibular gland sparing feasible with contralateral sparing techniques

### Laryngeal and Hypopharyngeal Cancer

- IMRT indicated for advanced (T3-T4) tumours treated with concurrent chemoradiation
- Carotid-sparing IMRT to reduce cerebrovascular events (emerging concept)
- For early glottic cancer, conventional opposed lateral fields remain standard (simple geometry)
- Larynx-sparing IMRT in hypopharyngeal cancer preserves non-involved laryngeal structures
- IGRT critical for detecting tumour regression and laryngeal oedema changes

### Oral Cavity (Post-operative)

- Adjuvant IMRT for close/positive margins, perineural invasion, nodal extracapsular extension
- Sparing of contralateral parotid and oral cavity mucosa
- Mandible dose constraint critical for osteoradionecrosis prevention

## Quality Assurance in IMRT/IGRT

### Patient-Specific QA

1. **Pre-treatment verification** -- each IMRT plan verified before first treatment
2. **Phantom measurements** -- plan delivered to phantom; measured dose compared with calculated dose
3. **Gamma analysis** -- point-by-point comparison using gamma index (criteria: 3%/3 mm or 3%/2 mm)
4. **Pass rate** -- typically > 95% of points must meet gamma criteria
5. **Independent MU calculation** -- second check of monitor units by independent software

### Machine QA

- Daily output checks (constancy within 3%)
- Monthly MLC positional accuracy verification (< 1 mm)
- Annual comprehensive commissioning checks
- CBCT imaging quality checks (spatial resolution, contrast, geometric accuracy)

### Plan Quality Metrics

| Metric | Definition | Target |
|---|---|---|
| Conformity index (CI) | V_Rx / V_PTV | 1.0 (ideal) |
| Homogeneity index (HI) | (D2% - D98%) / D50% | < 0.10 |
| Gradient index (GI) | V_50%Rx / V_Rx | As low as possible |
| Mean dose to OAR | Average dose in OAR volume | Below constraint |

## Special Considerations

### IMRT in Re-irradiation

Re-irradiation for recurrent or second primary H&N cancers presents unique challenges where IMRT/IGRT are indispensable:

- Prior dose distributions must be overlaid on the re-irradiation plan (composite dose assessment)
- Cumulative spinal cord dose must remain below tolerance (consider BED correction for time elapsed)
- Smaller PTV margins with IGRT are critical to minimise overlap with previously irradiated tissues
- Stereotactic body radiotherapy (SBRT) using IMRT principles increasingly used for small-volume recurrences
- Typical re-irradiation dose: 60 Gy in 30 fractions or hypofractionated SBRT (35-40 Gy in 5 fractions)

### Proton Therapy vs Photon IMRT

- Proton therapy offers superior dose conformality due to the Bragg peak (no exit dose)
- Potential advantage in reducing low-dose bath and integral dose to normal tissues
- Currently under investigation in randomised trials (e.g., NRG-HN002 for oropharyngeal cancer)
- Limited availability and higher cost restrict widespread adoption
- Photon IMRT remains the global standard for the vast majority of H&N cases

### IMRT and Concurrent Systemic Therapy

- IMRT planning must account for enhanced mucosal toxicity with concurrent cisplatin or cetuximab
- Pharyngeal constrictor and swallowing structure sparing is particularly important during chemoradiation
- Weekly cisplatin (40 mg/m2) regimens may have lower acute toxicity than 3-weekly high-dose cisplatin with IMRT
- Treatment breaks should be avoided; IMRT plan should be robust enough to maintain schedule adherence

## Limitations of IMRT/IGRT

1. **Cost** -- higher capital and operational costs (linear accelerator upgrades, planning systems, QA equipment, physics staffing)
2. **Planning complexity** -- inverse planning requires experienced dosimetrists and physics team; longer planning time (hours to days)
3. **Low-dose bath** -- IMRT distributes low doses over larger volumes; theoretical concern for second malignancies (particularly relevant in younger patients)
4. **Marginal miss risk** -- highly conformal plans have steeper dose gradients; geographic miss if setup errors exceed PTV margins
5. **Interobserver variability** -- target delineation inconsistency remains the weakest link; contouring guidelines and peer review essential
6. **Imaging dose** -- daily CBCT adds 1-3 cGy per fraction; cumulative dose over treatment course (approximately 1-2 Gy)
7. **Resource intensive** -- requires dedicated physics team, contouring time, plan optimisation, and patient-specific QA
8. **Not always necessary** -- simple target geometries (T1 glottic cancer) do not benefit from IMRT complexity

> [!tip] Clinical Pearls
> 1. **IMRT is the standard of care** for the majority of head and neck cancers requiring radiotherapy, supported by Level 1 evidence from the PARSPORT trial demonstrating significant xerostomia reduction
> 2. **SIB-IMRT** delivers 70 Gy, 63 Gy, and 56 Gy simultaneously in 33 fractions -- avoiding the need for field changes and cone-downs used in sequential boost techniques
> 3. **Parotid mean dose < 26 Gy** is the critical threshold for meaningful saliva recovery; achieving this in at least one parotid is the minimum goal
> 4. **IGRT with daily CBCT** allows PTV margin reduction from 5 mm to 2-3 mm, translating to further OAR dose reduction
> 5. **Adaptive replanning** should be triggered by weight loss > 5%, significant tumour regression, or mask fit deterioration -- typically required in weeks 3-4 of treatment
> 6. **VMAT** achieves comparable plan quality to fixed-field IMRT with significantly shorter treatment times (2-5 min vs 15-20 min), making it the preferred delivery technique
> 7. **Inverse planning** is the defining feature of IMRT -- the planner specifies dose objectives and the computer optimises beam fluences, unlike forward planning in 3D-CRT
> 8. **Early glottic cancer (T1)** is the exception where conventional opposed lateral fields remain appropriate; IMRT offers no advantage for this simple target geometry
> 9. **Low-dose bath** is the trade-off of IMRT conformality -- larger volumes receive low doses, a theoretical concern for radiation-induced second malignancies
> 10. **Target delineation** remains the weakest link in the IMRT chain; adherence to consensus guidelines (Gregoire et al.) and institutional peer review are essential for quality

> [!compass]- Navigate
> **Parent:** [[Answers/Radiotherapy and Chemotherapy/index|Radiotherapy]]
>
> **Related Notes:**
> - [[Answers/Larynx/Radiation Therapy Techniques and Complications|RT Techniques in Laryngeal Cancer]]
> - [[Answers/Oropharynx/DARS-Sparing Radiation in OPC|DARS-Sparing RT]]
> - [[Answers/Oropharynx/Submandibular Gland Sparing RT in OPC|SMG-Sparing RT]]
