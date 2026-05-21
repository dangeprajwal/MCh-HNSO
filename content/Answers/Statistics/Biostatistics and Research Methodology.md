---
tags:
  - Statistics
  - Research Methodology
  - Evidence Based Medicine
---

# Biostatistics and Research Methodology in Head and Neck Oncology

> [!question] Questions Covered
> - Forest graph (KIDWAI 2020)
> - Randomised control trial. What are the different phases? Explain in detail (KIDWAI 2020)
> - Null hypothesis (AMRITA 2008)
> - Non inferiority clinical trials (AMRITA 2016)
> - Levels of evidence in evidence based medicine (AMRITA 2016)
> - P value (AMRITA 2018)
> - Meta-analysis (AMRITA 2018)
> - Elaborate on the concept of lead time bias in cancer screening (AMRITA 2019)
> - Alpha error (AMRITA 2020, 2021; TMH 2020)
> - Enumerate levels and sublevels of evidence (TMH 2019)
> - Write briefly on case control and cohort studies (TMH 2020)
> - Write briefly on Meta Analysis (TMH 2020)
> - What are the factors causing bias in retrospective and prospective study? Advantages of a randomised controlled design (TMH 2021)
> - What are Type I and Type II errors (TMH 2021)

**Source:** Scott-Brown's Otorhinolaryngology Vol 3, Chapter 13 (Evidence Base in OPSCC); Stell and Maran's Head and Neck Surgery, Chapter 5 (Evidence-Based Practice); Harrison — Head and Neck Cancer: A Multidisciplinary Approach, Chapter 6 (Clinical Trials); Greenhalgh T, How to Read a Paper, BMJ Books

> [!cite] Landmark Articles
> Greenhalgh (1997) published the landmark series "How to Read a Paper" in the BMJ, establishing practical frameworks for critical appraisal. Sackett et al. (1996) formalised evidence-based medicine in the JAMA. The Cochrane Collaboration (Chalmers 1993) established systematic review methodology as the highest level of clinical evidence.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Greenhalgh T — How to read a paper: the basics of evidence based medicine | BMJ | 1997 | [10.1136/bmj.315.7110.672](https://doi.org/10.1136/bmj.315.7110.672) |
> | Sackett DL — Evidence based medicine: what it is and what it isn't | BMJ | 1996 | [10.1136/bmj.312.7023.71](https://doi.org/10.1136/bmj.312.7023.71) |
> | Moher D — PRISMA statement for reporting systematic reviews and meta-analyses | BMJ | 2009 | [10.1136/bmj.b2535](https://doi.org/10.1136/bmj.b2535) |
> | Altman DG — Practical statistics for medical research | Chapman & Hall | 1991 | — |

---

## Part A: Levels of Evidence

### Oxford Centre for Evidence-Based Medicine (OCEBM) Hierarchy

Evidence is graded from highest (most reliable) to lowest (least reliable):

| Level | Type of Evidence | Example in HNC |
|-------|-----------------|----------------|
| **1a** | Systematic review of RCTs (with homogeneity) | MACH-NC meta-analysis of CRT in HNSCC |
| **1b** | Individual RCT (narrow confidence intervals) | KEYNOTE-048 (pembrolizumab in R/M HNSCC) |
| **1c** | All-or-none case series | Historical: laryngectomy transforming laryngeal cancer outcome |
| **2a** | Systematic review of cohort studies | Systematic review of HPV+ OPC outcomes |
| **2b** | Individual cohort study or low-quality RCT | De Almeida 2015 multicentre TORS cohort |
| **2c** | "Outcomes" research; ecological studies | Cancer registry data on incidence trends |
| **3a** | Systematic review of case-control studies | Systematic review of risk factors for OSCC |
| **3b** | Individual case-control study | HPV as risk factor for oropharyngeal cancer (Gillison 2000) |
| **4** | Case-series, poor quality cohort/case-control | Surgical series without controls |
| **5** | Expert opinion, bench research | Anatomy textbook descriptions |

### Grades of Recommendation (OCEBM)

| Grade | Based on | Meaning |
|-------|----------|---------|
| **A** | Level 1 evidence | Consistent RCTs or systematic reviews |
| **B** | Level 2–3 evidence | Consistent cohort or case-control studies |
| **C** | Level 4 evidence | Case series, poor cohorts |
| **D** | Level 5 evidence | Expert opinion only |

---

## Part B: Study Designs

### Hierarchy of Study Designs

```
Systematic Review & Meta-analysis (highest)
         ↓
 Randomised Controlled Trial (RCT)
         ↓
    Cohort Study
         ↓
   Case-Control Study
         ↓
     Cross-sectional Study
         ↓
  Case Report / Case Series (lowest)
```

### Randomised Controlled Trial (RCT)

The **gold standard** for evaluating treatment efficacy.

**Key Features:**
| Feature | Detail |
|---------|--------|
| **Randomisation** | Patients allocated to treatment/control by chance — eliminates selection bias |
| **Control group** | Concurrent comparison arm (placebo, standard treatment) |
| **Blinding** | Single (patient), double (patient + investigator), triple (+ statistician) |
| **Prospective** | Data collected prospectively from enrolment |
| **Parallel group** | Most common; crossover RCTs possible for chronic conditions |

**Advantages:**
- Eliminates selection bias (randomisation)
- Controls for confounders (known and unknown)
- Establishes causality (not just association)
- Allows calculation of absolute and relative risk reduction

**Disadvantages:**
- Expensive and time-consuming
- Ethical issues (equipoise required)
- May not reflect real-world clinical practice (strict inclusion/exclusion criteria)
- Long follow-up needed in HNC (OS endpoint)

**Phases of Clinical Trials:**
- **Phase I:** Safety, dose-finding; 15–30 patients
- **Phase II:** Preliminary efficacy; 30–100 patients
- **Phase III:** Definitive efficacy vs standard; hundreds to thousands of patients
- **Phase IV:** Post-marketing surveillance; real-world safety

### Cohort Study

Follows a group (cohort) exposed to a risk factor or intervention and compares outcomes with unexposed controls over time.

| Feature | Prospective Cohort | Retrospective Cohort |
|---------|-------------------|---------------------|
| **Direction** | Forward in time | Backward using records |
| **Strength** | Controls exposure measurement; less recall bias | Cheaper, faster |
| **Weakness** | Expensive, long follow-up; attrition | Relies on existing records; selection bias |
| **Example in HNC** | SEER database prospective follow-up of thyroid cancer | Retrospective review of surgical margins in oral SCC |

**Outcome measure:** Relative risk (RR) = Incidence in exposed ÷ Incidence in unexposed

### Case-Control Study

Compares patients **with disease** (cases) vs **without disease** (controls) and looks backward for exposure.

| Feature | Detail |
|---------|--------|
| **Direction** | Retrospective (backward) |
| **Outcome** | Odds Ratio (OR) — not RR |
| **Best for** | Rare diseases (rare tumours); quick, cheap |
| **Weakness** | Recall bias; selection of controls; cannot measure incidence |
| **Example** | HPV exposure in oropharyngeal cancer vs controls |

**Odds Ratio (OR):** Odds of exposure in cases ÷ Odds of exposure in controls
- OR >1: exposure associated with disease
- OR <1: exposure protective
- OR approximates RR when disease is rare (<10%)

### Bias in Observational Studies

| Bias Type | Definition | Example in HNC |
|-----------|-----------|----------------|
| **Selection bias** | Cases/controls not representative of population | Hospital-based controls over-represent sick people |
| **Recall bias** | Cases remember exposure better than controls | Patients with tongue cancer recall tobacco use more accurately |
| **Information bias** | Differential data quality between groups | Retrospective records may be incomplete for older cases |
| **Confounding** | Third variable associated with both exposure and outcome | Smoking confounds the alcohol-OSCC relationship |
| **Lead time bias** | Earlier detection appears to improve survival without changing natural history | Screening program detects cancer earlier — patients appear to survive longer |
| **Length bias** | Screening preferentially detects slow-growing tumours | Mammography screen detects more indolent cancers |
| **Observer bias** | Investigator's knowledge of patient's exposure influences outcome assessment | Unblinded surgeon assesses wound healing differently in trial groups |

### Advantages of RCT over Observational Studies

| Feature | RCT | Observational |
|---------|-----|---------------|
| **Selection bias** | Eliminated by randomisation | Present |
| **Confounding** | Controlled (known + unknown) | Only known confounders controlled |
| **Causality** | Can establish | Association only |
| **Ethical constraints** | Required (equipoise) | Fewer restrictions |
| **Cost/time** | High | Lower |
| **External validity** | Sometimes limited | Often better (real-world) |

---

## Part C: Statistical Concepts

### Null Hypothesis and Hypothesis Testing

**Null hypothesis (H₀):** "There is no difference between groups" (no treatment effect)
**Alternative hypothesis (H₁):** "There is a difference between groups"

Statistical testing calculates the probability of observing results at least as extreme as those observed, **assuming H₀ is true** — this probability is the **p-value**.

### P-value

The **p-value** is the probability of obtaining results at least as extreme as those observed, assuming the null hypothesis is true.

- **p < 0.05:** Conventional threshold for "statistical significance" — probability of false positive < 5%
- **p < 0.01:** Highly significant
- **p ≥ 0.05:** Fail to reject null hypothesis (does NOT mean H₀ is true — may be underpowered)

**Misinterpretations of p-value:**
- p-value is NOT the probability that H₀ is true
- p-value does NOT indicate clinical importance
- p < 0.05 does NOT mean the result is clinically meaningful
- p-value depends heavily on sample size — large trials can detect tiny, clinically irrelevant differences

### Type I Error (Alpha Error — False Positive)

**Definition:** Rejecting the null hypothesis when it is actually true — concluding a treatment works when it doesn't.

- **α = 0.05:** Willing to accept 5% chance of type I error
- Called **"false positive"** or **"alpha error"**
- A positive trial may be wrong 1 in 20 times by chance alone

**In HNC context:** A trial reports CRT superiority over RT alone with p=0.04, but this could be a Type I error — the treatment may actually be no better.

### Type II Error (Beta Error — False Negative)

**Definition:** Failing to reject the null hypothesis when it is actually false — concluding a treatment doesn't work when it does.

- **β = 0.20:** Conventional; willing to accept 20% chance of Type II error
- Called **"false negative"** or **"beta error"**
- Usually caused by **inadequate sample size** (underpowered study)

### Statistical Power

**Power = 1 − β** = the probability of correctly detecting a true difference (true positive)

- Standard: **Power = 80–90%** (β = 0.10–0.20)
- Power depends on: sample size, effect size, α level, variability of outcome
- Larger sample size → more power → less Type II error

| Error Type | Definition | Conventional Rate | Cause | Clinical Impact |
|-----------|-----------|------------------|-------|-----------------|
| **Type I (α)** | False positive — reject true H₀ | α ≤ 0.05 | Chance | Adopt ineffective treatment |
| **Type II (β)** | False negative — fail to reject false H₀ | β ≤ 0.20 | Underpowering | Miss effective treatment |

---

## Part D: Meta-analysis and Systematic Review

### Definitions

**Systematic review:** Comprehensive, reproducible search and critical appraisal of all relevant studies addressing a specific clinical question.

**Meta-analysis:** Quantitative pooling of results from multiple studies using statistical methods to produce a single combined estimate.

### Steps in Meta-analysis

1. **Clinical question formulation:** PICO framework (Population, Intervention, Comparison, Outcome)
2. **Comprehensive literature search:** Multiple databases (MEDLINE, EMBASE, Cochrane), no language restriction
3. **Inclusion/exclusion criteria:** Defined a priori; applied independently by two reviewers
4. **Quality assessment:** Risk of bias tools (Cochrane RoB 2.0 for RCTs; Newcastle-Ottawa for observational)
5. **Data extraction:** Outcomes, sample sizes, follow-up, effect measures
6. **Statistical pooling:**
   - Test for **heterogeneity** (I² statistic): I² < 25% = low, 25–75% = moderate, >75% = high
   - **Fixed effects model:** Assumes all studies estimate same true effect (low heterogeneity)
   - **Random effects model:** Assumes studies estimate different but related effects (high heterogeneity — DerSimonian and Laird)
7. **Summary estimate:** Pooled OR, RR, or mean difference with 95% CI
8. **Publication bias assessment:** Funnel plot; Egger's test; Begg's test

### Forest Plot

A graphical display of meta-analysis results showing:

| Element | Meaning |
|---------|---------|
| **Each horizontal line** | Individual study result with 95% confidence interval |
| **Square on line** | Point estimate; size proportional to study weight |
| **Diamond at bottom** | Pooled estimate from meta-analysis; width = 95% CI |
| **Vertical line of no effect** | RR or OR = 1.0 (or Mean Difference = 0) |
| **Position relative to no-effect line** | Left = favours intervention; right = favours control (for RR/OR) |
| **Heterogeneity statistics** | I² value and p for heterogeneity shown below |

**Reading a forest plot:**
- If diamond crosses the vertical line → result is NOT statistically significant
- Wide confidence intervals → imprecise estimate (small study)
- Studies scattered widely on x-axis → high heterogeneity

### Example — MACH-NC Meta-analysis (Pignon 2000)
- 63 trials, 10,741 patients
- Concurrent CRT (vs RT alone): HR 0.81, p<0.0001
- 8% absolute OS benefit at 5 years
- Forest plot showed consistent benefit across most trials
- I² moderate — some heterogeneity due to different chemotherapy regimens

### Advantages and Limitations of Meta-analysis

| Advantages | Limitations |
|-----------|-----------|
| Increased statistical power | "Garbage in, garbage out" — quality of included studies |
| More precise effect estimate | Publication bias — negative trials less likely published |
| Resolves conflicting results | Heterogeneity — pooling apples and oranges |
| Identifies subgroup effects | Cannot control for confounders of included studies |
| Systematic, reproducible | Time-consuming; requires statistical expertise |

---

## Part E: Lead Time Bias

### Definition

**Lead time bias** is a systematic error in survival analysis that occurs when screening detects disease **earlier** in its natural history, leading to an apparent improvement in survival time even when the natural history is unchanged.

### Mechanism

```
Without screening:  Diagnosis ──────────────────── Death
                    (symptomatic)  5 years survival

With screening:     Diagnosis ──────────────────────── Death
                    (screen-detected) 7 years survival
                         ↑
                    Lead time (2 years)
                    Disease detected 2 years earlier
                    but patient still dies at same time
```

**The "lead time"** is the interval between screen detection and when the disease would have been diagnosed symptomatically. Adding this interval creates an illusion of improved survival.

### Examples in HNC

1. **Oral cancer screening:** If dysplasia detected by brush biopsy in asymptomatic patient, the time from diagnosis to death is longer than a patient who presented with a lump — but only because diagnosis was earlier, not because outcome changed
2. **Thyroid incidentalomas on PET:** Screen-detected thyroid cancers appear to have better survival partly due to lead time bias
3. **HPV serology screening for OPC:** Earlier HPV detection doesn't necessarily translate to improved survival — may represent lead time bias

### How to Correct for Lead Time Bias

- **Disease-specific mortality rate** rather than survival time — if mortality rate unchanged, benefit is lead time bias
- **Randomised screening trials** — compare screened vs unscreened populations for cause-specific mortality
- **Adjust for lead time** using mathematical models

### Length Bias (Related Concept)

Screening disproportionately detects **slow-growing tumours** (longer sojourn time) because they are more likely to be present and detectable during a screening round. Aggressive fast-growing tumours arise and become symptomatic between screens.

This creates an apparent survival advantage for screen-detected tumours that is not due to screening efficacy but to preferential detection of biologically indolent tumours.

---

## Part F: Non-Inferiority Trials

### Rationale

In clinical oncology, a new treatment may be:
- **Less effective** in terms of tumour control
- But **superior** in terms of toxicity, cost, convenience, or QOL

A **non-inferiority (NI) trial** tests whether the new treatment is "not unacceptably worse" than the standard, within a pre-specified margin (δ).

### Non-inferiority Margin (δ)

- Pre-specified clinically meaningful threshold of "acceptable inferiority"
- Example: 5% reduction in 5-year OS is acceptable if toxicity is significantly reduced
- Determined from prior studies of active control (must preserve proportion of standard treatment effect)

### Hypothesis Testing in NI Trials

- **H₀ (null):** New treatment is inferior by more than δ (new is inferior)
- **H₁ (alternative):** New treatment is not inferior by more than δ
- **One-sided test** at α = 0.025 (equivalent to two-sided 0.05)
- **Confidence interval approach:** Lower bound of 95% CI must be above −δ for NI to be declared

### HNC Examples of Non-Inferiority Trials

| Trial | Standard | Experimental | NI Margin | Status |
|-------|----------|-------------|-----------|--------|
| **ECOG 3311** | 60 Gy adjuvant RT post-TORS | 50 Gy (low-risk patients: observation) | 10% 2-yr PFS | Ongoing |
| **PATHOS** | 60 Gy post-TORS | 50 Gy (intermediate risk) | Swallowing QOL (MDADI) | Ongoing |
| **NRG-HN002** | CRT (60 Gy + cisplatin) | RT alone (60 Gy) in HPV+ OPC | PFS | Reported — RT alone inferior |
| **RTOG 1016** | CRT with cisplatin | CRT with cetuximab | 5-yr OS | Cetuximab INFERIOR — negative |

### Key Principle: NI ≠ Equivalence

- NI only establishes that new treatment is not worse beyond δ
- Does not claim equal efficacy
- Assay sensitivity required — must demonstrate the active control was superior to placebo in prior studies

---

> [!abstract] Key Points
> 1. Levels of evidence: 1a (systematic review of RCTs) → 1b (single RCT) → 2 (cohort) → 3 (case-control) → 4 (case series) → 5 (expert opinion)
> 2. RCT is the gold standard for evaluating treatment efficacy; randomisation eliminates selection bias and controls for known + unknown confounders
> 3. **Type I error (α):** False positive — reject H₀ when true; p-value threshold conventionally 0.05 (5% chance of false positive)
> 4. **Type II error (β):** False negative — fail to reject H₀ when false; caused by underpowering; β conventionally ≤ 0.20
> 5. **Power = 1 − β:** Probability of detecting true difference; conventionally 80–90%; increases with larger sample size
> 6. **p-value:** Probability of results this extreme assuming H₀ is true; NOT the probability H₀ is true; does NOT indicate clinical importance
> 7. **Meta-analysis:** Pools results of multiple studies for a single estimate; forest plot displays individual and pooled results; I² measures heterogeneity
> 8. **Forest plot:** Each line = one study; diamond = pooled estimate; if diamond crosses line of no effect = NS
> 9. **Lead time bias:** Screening appears to improve survival but only because diagnosis made earlier — natural history unchanged
> 10. **Non-inferiority trials:** Test whether new treatment is not unacceptably worse than standard; key in de-escalation studies in HPV+ OPC

> [!tip] Clinical Pearls
> - A statistically significant result (p<0.05) does NOT mean the result is clinically meaningful — always quote the absolute difference and confidence intervals
> - RTOG 1016 showed cetuximab was **inferior** to cisplatin in HPV+ OPC CRT — a critical negative NI trial result; cetuximab should NOT replace cisplatin
> - NRG-HN002 showed RT alone inferior to CRT even in HPV+ OPC — de-escalation of chemotherapy is not yet proven safe
> - Lead time bias is the key confounder in all cancer screening outcome studies — screen-detected thyroid cancers and their "excellent" survival partly reflect this
> - Forest plot reading: diamond to the left of 1.0 = intervention better (for OR/RR); wide CI = imprecise; I² > 75% = do not pool
> - Type I error = crying wolf (false alarm); Type II error = missing the wolf (missed diagnosis)
> - In head and neck exams, knowing MACH-NC (meta-analysis showing 8% OS benefit for CRT) is essential

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/Statistics/index|Statistics]]
>
> **Related Notes:**
> - [[Answers/General/Phase III Clinical Trials|Phase III Clinical Trials]]
> - [[Answers/General/Non-Inferiority Clinical Trials|Non-Inferiority Clinical Trials]]
> - [[Answers/General/RECIST Criteria|RECIST Criteria]]
> - [[Answers/HPV/De-escalation in HPV+ OPC|De-escalation in HPV+ OPC]]
