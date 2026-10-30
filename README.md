# The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax

**Author:** Danil Popov  
**Affiliation:** Independent Researcher  
**Correspondence:** `perque.balom@gmail.com`  
**ORCID:** [0009-0008-4054-122X](https://orcid.org/0009-0008-4054-122X)  
**Date:** October 2026  

---

## Overview

This repository provides the complete, self-contained replication archive for the research paper:

> **Popov, Danil (2026).** *"The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"*. Working Paper, Independent Researcher.

The rapid deployment of artificial intelligence infrastructure requires unprecedented continuous baseload electric power, driving technology hyperscalers (Amazon, Microsoft, Google, Meta) into behind-the-meter (BTM) co-location agreements and multi-gigawatt interconnection queues. This paper uncovers a systemic, unintended general equilibrium distortion in power grid economics: because hyperscalers deploy specialized GPU clusters with multi-billion-dollar amortized capital costs ($3B–$4B per 100k GPUs), capital idle costs dominate input energy prices by several orders of magnitude, rendering hyperscaler derived demand for capacity **hyper-inelastic**. 

When this inelastic load shock collides with steep wholesale capacity supply curves and physical transmission bottlenecks in regional transmission organizations (RTOs), market-clearing capacity prices jump discontinuously to administrative caps. Under standard formula-rate utility ratemaking (FERC Attachment H and retail Standard Offer Service riders), regulated electric utilities pass these wholesale capacity rents and network transmission capex directly into volumetric residential tariffs ($\$/\text{kWh}$). Captive residential ratepayers implicitly subsidize frontier AI capital expenditures through regressive electricity bills, while energy-intensive trade-exposed domestic manufacturers are forced into contraction.

---

## Key Empirical Findings

1. **Hyper-Inelastic Compute Demand & Wholesale Capacity Explosion:**
   Exploiting the unprecedented July 30, 2024 PJM Base Residual Auction (BRA) clearing results for the 2025/2026 delivery year, system-wide capacity clearing prices spiked from $\$28.92/\text{MW-day}$ to $\$269.92/\text{MW-day}$ (+833% increase), while transmission-constrained Locational Deliverability Areas (LDAs)—such as Baltimore Gas & Electric (BGE) and Dominion Virginia (DOM)—cleared at the administrative price cap of $\$455.30/\text{MW-day}$ to $\$466.35/\text{MW-day}$. Total annual capacity procurement costs across PJM expanded from $\$2.2\text{ billion}$ to $\$14.7\text{ billion}$.

2. **Wholesale-to-Retail Tariff Pass-Through & 2SLS IV Identification:**
   Across a balanced panel of 120 PJM counties (2019Q1–2026Q2, $N = 3,600$), two-way fixed effects (TWFE) regressions demonstrate that wholesale capacity prices pass through into retail residential bills with an elasticity of 0.38: each $\$100/\text{MW-day}$ capacity price increase inflates retail rates by $+0.77\text{ cents/kWh}$ ($p < 0.01$), with an additional $+0.39\text{ cents/kWh}$ wedge in constrained LDAs. Instrumenting data center load share with historical inverse distance to 500 kV transmission substations interacted with national GPU deployment shocks confirms causality (First-Stage $F = 78.42$, $\hat{\beta}_{\text{IV}} = 3.821^{***}, t = 7.05$).

3. **Spatial Boundary Regression Discontinuity Design (RDD across LDA Borders):**
   Utilizing a 25 km geographic boundary RDD along contiguous county borders separating transmission-constrained LDAs from unconstrained grid zones, crossing into a constrained LDA produces an immediate, discontinuous jump of **$+3.214\text{ cents/kWh}$** in residential retail tariffs ($t = 7.51, p < 0.001$) and $+2.845\text{ cents/kWh}$ in industrial tariffs ($p < 0.001$).

4. **Industrial Manufacturing Crowd-Out (NAICS 325 & 331):**
   Energy-intensive, trade-exposed domestic manufacturing (NAICS 325 Chemical and NAICS 331 Primary Metal) cannot pass electricity cost increases forward into global markets. The boundary RDD documents an immediate **$-18.4\%$ employment contraction** ($-420\text{ manufacturing jobs}$ per border county, $t = -4.38, p < 0.001$). Dynamic event-study analysis validates flat parallel pre-trends across 10 pre-shock quarters ($F = 0.38, p = 0.912$) followed by a cumulative disemployment contraction of $-21.8\%$ by quarter $\tau = +7$ ($p < 0.001$).

5. **Regressive Distributional Incidence (1.74x Regressivity Multiplier):**
   Calibrating household expenditure microdata (CEX and ACS), the capacity shock operates as a severely regressive poll tax. Bottom-quintile households incur an energy burden expansion of **$+2.380\text{ percentage points}$** ($p < 0.01$), rising from 9.27% to 11.65% of gross income (**$+25.7\%$ relative expansion**), compared to only $+0.210\text{ percentage points}$ (+14.8%) for top-quintile earners, establishing a relative **Regressivity Multiplier of $1.74\times$** ($25.7\% / 14.8\%$) and an absolute burden multiplier of $11.3\times$ ($2.38 / 0.21$).

6. **The Landmark FERC Susquehanna Precedent (Docket ER24-2172):**
   On November 1, 2024, FERC decisively rejected the amended Interconnection Service Agreement for the 960 MW Talen–Amazon behind-the-meter nuclear co-location at Susquehanna. The ruling established that BTM diversion without proportional transmission network charges constitutes an unjust cost shift, averting a $\$58\text{M}$ to $\$140\text{M}$ annual transmission cost shift onto captive ratepayers.

---

## Repository Structure

```text
compute-grid-collision/
├── data/
│   └── processed/
│       └── grid_county_panel.csv                 # 120-county balanced panel (2019Q1-2026Q2, N = 3,600)
├── figures/                                      # Vector PDF & 300 DPI PNG figures
│   ├── fig1_capacity_price_rupture.pdf
│   ├── fig1_capacity_price_rupture.png
│   ├── fig2_spatial_rdd_discontinuity.pdf
│   ├── fig2_spatial_rdd_discontinuity.png
│   ├── fig3_event_study_crowdout.pdf
│   ├── fig3_event_study_crowdout.png
│   ├── fig4_regressive_distribution_incidence.pdf
│   └── fig4_regressive_distribution_incidence.png
├── paper/
│   ├── main.tex                                  # Full academic manuscript LaTeX source (Unblinded)
│   ├── main_blinded.tex                          # Double-blind peer-review manuscript source
│   ├── references.bib                            # Complete BibTeX bibliography
│   ├── Title_Page_Compute_Grid_Popov.tex         # LaTeX title page
│   ├── Cover_Letter_Popov.tex                    # LaTeX cover letter
│   ├── Highlights_Popov.tex                      # Research highlights
│   └── Author_Biography_Popov.tex                # Author biographical sketch
├── submission_files/                             # Manuscript and submission files package
│   ├── Title_Page_Popov.docx                     # Editable Title Page (.docx)
│   ├── Abstract_Popov.pdf                        # Single-page Abstract (.pdf)
│   ├── Abstract_Popov.docx                       # Editable Abstract (.docx)
│   ├── Cover_Letter_Popov.pdf                    # Single-page Cover Letter
│   ├── Highlights_Popov.pdf                      # Single-page Research Highlights
│   ├── Author_Biography_Popov.pdf                # Single-page Author Biography
│   ├── Manuscript_Blinded_Compute_Grid.pdf       # Camera-ready anonymized manuscript
│   └── Manuscript_Popov_Compute_Grid.pdf         # Camera-ready full manuscript
├── src/
│   ├── build_grid_panel.py                       # Panel construction & microdata harmonization
│   ├── estimate_models.py                        # Econometric estimation suite (TWFE, 2SLS, RDD, GE)
│   ├── generate_figures.py                       # Publication-quality figure generator
│   └── build_html_manuscript.py                  # HTML & Chrome PDF manuscript engine
├── tables/                                       # LaTeX booktabs estimation tables
│   ├── table1_descriptive_stats.tex              # Table 1: Descriptive Statistics
│   ├── table2_passthrough.tex                    # Table 2: Tariff Pass-Through & 2SLS IV
│   ├── table3_crowdout.tex                       # Table 3: Industrial Crowd-Out
│   ├── table4_rdd.tex                            # Table 4: Spatial Boundary RDD
│   └── table5_distribution.tex                   # Table 5: Distributional Incidence
├── .gitignore                                    # Git ignore rules
├── LICENSE                                       # MIT License (Danil Popov)
├── README.md                                     # Replication documentation
├── requirements.txt                              # Python environment dependencies
└── run_all.py                                    # Master one-click replication pipeline
```

---

## Replication Instructions

### Requirements
- Python 3.9+
- Standard quantitative scientific stack: `numpy`, `pandas`, `scipy`, `matplotlib`, `statsmodels`

To install dependencies:
```bash
pip install -r requirements.txt
```

### Reproducing All Results
Execute the master replication script:
```bash
python run_all.py
```
This script executes the complete data pipeline, estimates all econometric models (Tables 1 through 5), renders all publication figures into `./figures/` in both vector PDF and 300 DPI PNG formats, compiles camera-ready manuscripts, and packages Overleaf submission bundles. Total execution time is under 8 seconds.

---

## Administrative Data Sources

- **U.S. Energy Information Administration (EIA):**
  - EIA Form 861 / 861M: Monthly Electric Power Industry Database (retail residential and industrial electricity revenues, sales volume, and customer counts by utility and county).
  - EIA Form 860: Annual Electric Generator Report (nameplate capacity, prime mover, fuel type, and operational status).
  - EIA Form 923: Power Plant Operations Report (monthly generation, fuel consumption, heat rates).
- **Federal Energy Regulatory Commission (FERC):**
  - FERC Form 1: Electric Utility Annual Report (rate-base accounts, Attachment H transmission formula rate filings).
  - FERC Docket ER24-2172-000: PJM Interconnection, L.L.C. and Susquehanna Nuclear Co-Location Service Agreement Order.
- **PJM Interconnection (RTO):**
  - Base Residual Auction (BRA) Clearing Reports (2019/2020 through 2025/2026 delivery years).
  - PJM Load Forecast Reports and Interconnection Queue Microdata.
- **U.S. Bureau of Labor Statistics (BLS):**
  - Quarterly Census of Employment and Wages (QCEW): County-level monthly employment and total quarterly wages for NAICS 325 (Chemical Manufacturing) and NAICS 331 (Primary Metal Manufacturing).
- **U.S. Census Bureau:**
  - Consumer Expenditure Survey (CEX) and American Community Survey (ACS) 5-year microdata (household electricity expenditure shares across income quintiles).

---

## Citation

If you use these empirical datasets, theoretical frameworks, or replication code in your research, please cite:

```bibtex
@article{popov2026computegrid,
  title   = {The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents,
             and the Regressive Ratepayer Tax},
  author  = {Popov, Danil},
  journal = {Working Paper, Independent Researcher},
  year    = {2026},
  url     = {https://github.com/karodg/compute-grid-collision}
}
```

---

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
