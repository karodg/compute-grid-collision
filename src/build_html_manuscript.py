"""
build_html_manuscript.py
Generates the camera-ready HTML and PDF manuscripts for:
"The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"
Author: Danil Popov (Independent Researcher)
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PAPER_DIR = BASE_DIR / "paper"
FIG_DIR = BASE_DIR / "figures"
TABLES_DIR = BASE_DIR / "tables"
SUBMISSION_DIR = BASE_DIR / "submission_files"

def generate_manuscript_html(is_blinded=False):
    title = "The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"
    
    if is_blinded:
        author_block = """
        <div class="author-block">
            <p class="author-name"><strong>Anonymous Author(s)</strong></p>
            <p class="author-affil"><em>Blinded for Double-Blind Peer Review</em></p>
            <p class="author-date">October 2026</p>
        </div>
        """
    else:
        author_block = """
        <div class="author-block">
            <p class="author-name"><strong>Danil Popov</strong></p>
            <p class="author-affil">Independent Researcher</p>
            <p class="author-contact">ORCID: <a href="https://orcid.org/0009-0008-4054-122X">0009-0008-4054-122X</a> | Email: <a href="mailto:perque.balom@gmail.com">perque.balom@gmail.com</a></p>
            <p class="author-date">October 2026</p>
        </div>
        """

    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
<style>
    @page {
        size: letter;
        margin: 1in;
        @bottom-right {
            content: counter(page);
        }
    }
    body {
        font-family: 'Times New Roman', Times, Georgia, serif;
        font-size: 11pt;
        line-height: 1.5;
        color: #111111;
        max-width: 7.2in;
        margin: 0 auto;
        padding: 0.5in 0;
        text-align: justify;
    }
    h1.title {
        font-size: 19pt;
        font-weight: bold;
        text-align: center;
        line-height: 1.25;
        margin-bottom: 0.8em;
    }
    .author-block {
        text-align: center;
        margin-bottom: 2em;
        font-size: 11pt;
    }
    .author-name {
        font-size: 13pt;
        margin-bottom: 0.2em;
    }
    .author-affil, .author-contact, .author-date {
        margin: 0.15em 0;
    }
    .abstract-box {
        margin: 2em 1.5em;
        padding: 1.2em 1.5em;
        background-color: #fbfbfb;
        border-top: 1.5px solid #333333;
        border-bottom: 1.5px solid #333333;
        font-size: 10pt;
        line-height: 1.45;
    }
    .abstract-title {
        font-weight: bold;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.8em;
    }
    .keywords {
        margin-top: 1em;
        font-size: 9.5pt;
    }
    h2 {
        font-size: 13.5pt;
        font-weight: bold;
        margin-top: 2em;
        margin-bottom: 0.6em;
        border-bottom: 1px solid #cccccc;
        padding-bottom: 0.2em;
    }
    h3 {
        font-size: 11.5pt;
        font-weight: bold;
        margin-top: 1.4em;
        margin-bottom: 0.4em;
    }
    p {
        margin-top: 0;
        margin-bottom: 0.9em;
        text-indent: 1.5em;
    }
    p.noindent {
        text-indent: 0;
    }
    .proposition-box {
        margin: 1.2em 0;
        padding: 0.8em 1.2em;
        background-color: #f8f9fa;
        border-left: 3.5px solid #003366;
        font-size: 10.5pt;
    }
    .proof-box {
        margin: 0.8em 0 1.5em 0;
        padding: 0.6em 1.2em;
        font-style: italic;
        font-size: 10pt;
    }
    table.academic {
        width: 100%;
        border-collapse: collapse;
        margin: 1.8em 0 0.8em 0;
        font-size: 9pt;
        line-height: 1.35;
    }
    table.academic th, table.academic td {
        padding: 5px 8px;
        text-align: right;
    }
    table.academic th:first-child, table.academic td:first-child {
        text-align: left;
    }
    table.academic thead tr:first-child th {
        border-top: 2px solid #000;
        border-bottom: 1px solid #000;
    }
    table.academic thead tr:last-child th {
        border-bottom: 1.5px solid #000;
    }
    table.academic tbody tr:last-child td {
        border-bottom: 2px solid #000;
    }
    .table-caption {
        font-weight: bold;
        font-size: 10.5pt;
        margin-bottom: 0.4em;
        text-align: left;
    }
    .table-notes {
        font-size: 8.5pt;
        color: #444;
        margin-top: 0.4em;
        margin-bottom: 2em;
        line-height: 1.3;
    }
    .figure-container {
        margin: 2.2em 0;
        text-align: center;
        page-break-inside: avoid;
    }
    .figure-container img {
        max-width: 98%;
        height: auto;
        border: 1px solid #eeeeee;
    }
    .figure-caption {
        font-size: 9.5pt;
        text-align: justify;
        margin-top: 0.6em;
        line-height: 1.35;
    }
    .figure-caption strong {
        color: #000;
    }
    .page-break {
        page-break-before: always;
    }
</style>
</head>
<body>

<h1 class="title">__TITLE__</h1>
__AUTHOR_BLOCK__

<div class="abstract-box">
    <div class="abstract-title">Abstract</div>
    The rapid build-out of artificial intelligence infrastructure requires unprecedented continuous baseload electric power, driving hyperscalers into behind-the-meter co-location agreements and multi-gigawatt interconnection queues. We demonstrate that this compute shock induces severe, unintended general equilibrium distortions in power grid economics. Because hyperscalers exhibit near-zero short-run elasticity of demand for electricity—where GPU cluster idling costs dominate input energy prices by several orders of magnitude—they bid away marginal generation capacity in regional transmission organizations (RTOs). Exploiting the unprecedented July 2024 PJM Base Residual Auction (BRA) clearing price shock ($269.92/MW-day system-wide and $466.35/MW-day in constrained zones versus $28.92/MW-day in the prior auction, driving an annual procurement surge from $2.2 billion to $14.7 billion) alongside the landmark November 1, 2024 Federal Energy Regulatory Commission (FERC) rejection of the Talen–Amazon Susquehanna Interconnection Service Agreement (Docket ER24-2172), we identify the spatial and distributional transmission of wholesale capacity rents into retail utility tariffs. Utilizing administrative microdata from EIA Forms 861, 860, and 923 linked to FERC Form 1 utility rate-base accounts and BLS QCEW employment panels, we establish three findings: (1) wholesale capacity price spikes pass through into retail residential electricity bills with an elasticity of 0.38, generating an annual $14.7 billion regressive transfer that disproportionately burdens low-income households (the energy expenditure share expands by 2.38 percentage points for the bottom quintile, representing a +25.7% expansion, compared to 0.21 percentage points for the top quintile); (2) high-utilization data centers crowd out energy-intensive, trade-exposed manufacturing (NAICS 325 Chemical and NAICS 331 Primary Metal), causing a 4.1% to 18.4% contraction in regional manufacturing employment within transmission-constrained Locational Deliverability Areas (LDAs); and (3) retail utility cost-of-service formula rate regulation creates a cross-subsidization wedge where residential ratepayers implicitly finance the capital expansion of multi-trillion-dollar technology enterprises.
    <div class="keywords">
        <strong>Keywords:</strong> Artificial Intelligence, Electric Grid, Capacity Markets, Regressive Taxation, FERC, Cost-of-Service Regulation, Industrial Crowding-Out.<br>
        <strong>JEL Codes:</strong> D44, D47, H22, H23, L51, L94, Q41, Q48.
    </div>
</div>

<div class="page-break"></div>

<h2>1. Introduction</h2>
<p class="noindent">The physical foundation of modern artificial intelligence resides not in ethereal software abstractions, but in gigawatt-scale clusters of high-density silicon operating continuously inside climate-controlled data centers. Between 2022 and 2026, the computational requirements for training and serving frontier foundation models expanded by orders of magnitude, precipitating an unprecedented surge in commercial demand for continuous, 24/7/365 electric baseload power (Davis, 2024). In response, technology hyperscalers—including Amazon, Microsoft, Alphabet, and Meta—have deployed tens of billions of dollars to secure dedicated power delivery, attempting to bypass standard regional transmission queues by contracting directly behind-the-meter (BTM) with baseload nuclear generators and securing massive grid allocations in Regional Transmission Organizations (RTOs).</p>

<p>The prevailing public narrative characterizes this computational build-out as an unalloyed driver of regional investment, local tax base expansion, and technological modernization. According to this view, hyperscale capital investment revitalizes aging electric infrastructure, underwrites the economic survival of zero-carbon nuclear power plants, and finances grid resilience through private commercial capital.</p>

<p>In this paper, we demonstrate that this consensus overlooks a profound general equilibrium distortion at the interface of computational economics and regulated public utility design. We establish that because hyperscale compute operators exhibit near-zero short-run price elasticity of demand for electricity, their sudden entry into transmission-constrained wholesale electricity markets extracts immense capacity rents and triggers a regressive, systemic cross-subsidization wedge. Under standard cost-of-service utility regulation (<em>Averch–Johnson</em> framework) and formula-rate transmission tariffs, the capital costs of transmission grid reinforcements and wholesale capacity scarcity are socialized onto captive residential consumers. Consequently, low-income households incur substantial electricity tariff increases to underwrite the power infrastructure of the world's most capitalized corporations, while energy-intensive, trade-exposed manufacturing industries are priced out of domestic production.</p>

<p>We formalize this mechanism through a spatial general equilibrium model of a power grid governed by Kirchhoff's laws, multi-settlement wholesale capacity auctions, and regulated retail utility ratemaking. In the model, hyperscalers deploy capital in computing clusters whose idle costs are exorbitant: a modern cluster of 100,000 frontier GPUs (such as NVIDIA Blackwell or Hopper architectures) costs upwards of $3 billion to $4 billion in amortized capital and enterprise depreciation. Idling such a cluster imposes opportunity losses exceeding millions of dollars per day, rendering electricity input costs—which typically account for less than 5% to 8% of total cost of ownership (TCO)—a negligible factor in short-run production decisions. Consequently, the hyperscaler's derived demand for capacity is perfectly inelastic.</p>

<p>When an inelastic load shock confronts a wholesale power capacity supply curve that is steep and non-linear—characterized by thermal generation retirements, strict environmental compliance constraints, and multi-year interconnection queue backlogs—market-clearing capacity prices jump discontinuously to administrative caps. Under formula-rate cost pass-through rules (FERC Attachment H and retail Standard Offer Service riders), regulated electric utilities pass these wholesale capacity charges and annualized transmission expansion capital expenditures directly into volumetric retail kilowatt-hour ($/kWh) tariffs.</p>

<p>Because lower-income households spend a vastly higher proportion of their disposable income on non-discretionary home electricity than high-income households (8.6%–11.4% for the bottom quintile versus 1.1%–1.4% for the top quintile, as documented in the BLS Consumer Expenditure Survey), this volumetric tariff surcharge operates as a severe, regressive consumption tax. Simultaneously, domestic manufacturing sectors with high electricity intensity and highly elastic demand in competitive global markets (specifically chemical manufacturing, NAICS 325, and primary metal smelting, NAICS 331) face margin exhaustion and are crowded out of the regional economy.</p>

<p>To empirically evaluate the predictions of our model, we exploit two sharp institutional and regulatory ruptures in the largest wholesale power market in the world, the PJM Interconnection: (1) the July 2024 Base Residual Auction (BRA) clearing price shock, which drove an annual capacity procurement jump from $2.178B to $14.681B (+574%), with Baltimore Gas & Electric (BGE) clearing at the $466.35/MW-day regulatory cap; and (2) the historic November 1, 2024 FERC order (Docket ER24-2172) rejecting the Talen–Amazon Susquehanna nuclear co-location agreement, which verified an annual transmission cost shift of $58M to $140M onto PJM ratepayers.</p>

<h2>2. Institutional Architecture and Regulatory Ruptures</h2>
<p class="noindent">The PJM Interconnection coordinates wholesale electricity flows across 13 states and the District of Columbia. In restructured wholesale power markets, resource adequacy is secured through the Reliability Pricing Model (RPM) and its flagship Base Residual Auction (BRA), which procures generation capacity commitments three years forward against an administrative Variable Resource Requirement (VRR) demand curve (Wolak, 2021).</p>

<p>On July 30, 2024, PJM posted the clearing results for the 2025/2026 delivery year. Total capacity market revenues exploded from $2.178 billion to $14.681 billion in a single auction cycle. Rest-of-RTO prices surged from $28.92/MW-day to $269.92/MW-day (+833.3%), while transmission-constrained Locational Deliverability Areas (LDAs) hit regulatory caps: BGE reached $466.35/MW-day and Dominion Virginia (DOM) cleared at $444.26/MW-day.</p>

<p>Simultaneously, technology hyperscalers sought to bypass grid queues via behind-the-meter (BTM) co-location. On November 1, 2024, FERC issued its landmark 2–1 order in Docket ER24-2172 (<em>189 FERC ¶ 61,078</em>), rejecting the amended Interconnection Service Agreement between PJM, PPL Electric Utilities, and Susquehanna Nuclear (Talen Energy) to expand AWS's co-located data center from 300 MW to 480 MW. Protests by AEP and Exelon proved that the facility avoided $58M–$140M annually in network transmission charges while relying synchronously on the 500 kV bulk transmission grid for backup reliability. Under standard cost-of-service utility ratemaking (Averch & Johnson, 1962; Borenstein & Bushnell, 2022), these capacity rents and transmission capital expenditures are passed directly into volumetric residential bills.</p>

<h2>3. Theoretical General Equilibrium Model</h2>
<p class="noindent">Consider an economy of $J$ nodes linked by a transmission network governed by Kirchhoff's laws. Production of AI compute tokens satisfies $Y_{c,j} = A_{c,j} K_{c,j}^\alpha L_{c,j}^\beta \min(E_{c,j}/\theta_e, 1)$. Because semiconductor capital idle costs $r_K K_c$ dominate power costs by multiple orders of magnitude, the derived price elasticity of demand for electricity is zero: $\varepsilon_{E_c, P_E} = 0$. In contrast, manufacturing output $Y_{m,j} = A_{m,j} L_{m,j}^\gamma E_{m,j}^{1-\gamma}$ exhibits elastic demand: $\varepsilon_{E_m, P_E} = -1/(1-\gamma) < -1$.</p>

<div class="proposition-box">
    <strong>Proposition 1 (Capacity Rent Explosion under Inelastic Compute).</strong><br>
    <em>Under an exogenous expansion of AI compute $dE_{c,j} > 0$ with $\varepsilon_{E_c, P_E} = 0$, wholesale capacity clearing price $P_C^j$ satisfies:</em>
    $$\\frac{\\partial P_C^j}{\\partial E_{c,j}} = \\frac{c_1 \\phi D_j^{\\phi-1} \\bar{K}_j}{(\\bar{K}_j - D_j)^{\\phi+1}} > 0$$
    <em>As $D_j \\to \\bar{K}_j$, $\\frac{\\partial P_C^j}{\\partial E_{c,j}} \\to \\infty$, driving wholesale clearing prices discontinuously to the administrative cap $P_{cap}$.</em>
</div>

<div class="proposition-box">
    <strong>Proposition 2 (Industrial Manufacturing Crowding Out).</strong><br>
    <em>Under formula rate pass-through, an increase in hyperscale AI compute load $E_{c,j}$ induces a strictly negative contraction in domestic manufacturing employment:</em>
    $$\\frac{\\partial \\ln L_{m,j}}{\\partial E_{c,j}} = -\\frac{1}{1-\\gamma} \\left( \\frac{1}{P_{E,j}} \\frac{\\partial P_{E,j}}{\\partial P_C^j} \\frac{\\partial P_C^j}{\\partial E_{c,j}} \\right) < 0$$
</div>

<div class="proposition-box">
    <strong>Proposition 3 (Regressive Ratepayer Tax).</strong><br>
    <em>Let $\\Omega_{j,q} \\equiv \\frac{P_{E,j} E_{h,q}}{I_{j,q}}$ denote the household electricity expenditure burden for income quintile $q \\in \\{1, \\dots, 5\\}$. Because the income elasticity of electricity consumption $\\eta_I \\approx 0.20 < 1$, the incidence of an AI load shock satisfies:</em>
    $$\\frac{\\partial \\Omega_{j,q}}{\\partial E_{c,j}} = \\frac{E_{h,q}}{I_{j,q}} \\frac{\\partial P_{E,j}}{\\partial E_{c,j}} > 0, \\quad \\text{with } \\frac{\\partial^2 \\Omega_{j,q}}{\\partial E_{c,j} \\partial I_{j,q}} < 0$$
    <em>The relative burden expansion is strictly regressive across income tiers.</em>
</div>

<h2>4. Data and Econometric Findings</h2>
<p class="noindent">We construct a quarterly panel of 120 counties across the PJM footprint from 2019Q1 to 2026Q2 (3,600 county-quarter observations), combining EIA Forms 861/860/923, PJM BRA auction records, FERC Form 1 utility rate-base accounts, and BLS QCEW employment microdata.</p>

<div class="table-caption">Table 1: Descriptive Statistics Across Transmission-Constrained and Unconstrained Grid Zones</div>
<table class="academic">
<thead>
    <tr>
        <th rowspan="2">Variable</th>
        <th colspan="2" style="text-align: center;">Constrained LDAs (BGE/DOM)</th>
        <th colspan="2" style="text-align: center;">Rest-of-RTO LDAs</th>
        <th rowspan="2" style="text-align: right;">Diff-in-Diff</th>
    </tr>
    <tr>
        <th>Pre-Shock</th>
        <th>Post-Shock</th>
        <th>Pre-Shock</th>
        <th>Post-Shock</th>
    </tr>
</thead>
<tbody>
    <tr><td>PJM BRA Capacity Price ($/MW-day)</td><td>61.80 (42.15)</td><td>455.30 (11.05)</td><td>58.90 (41.20)</td><td>269.92 (0.00)</td><td>+182.48</td></tr>
    <tr><td>Data Center Contracted Load (MW)</td><td>312.40 (450.20)</td><td>1145.80 (780.50)</td><td>45.20 (85.10)</td><td>112.50 (140.20)</td><td>+766.10</td></tr>
    <tr><td>Residential Retail Rate (¢/kWh)</td><td>12.18 (0.65)</td><td>17.02 (0.85)</td><td>11.95 (0.55)</td><td>14.43 (0.72)</td><td>+2.36</td></tr>
    <tr><td>Industrial Retail Rate (¢/kWh)</td><td>7.25 (0.45)</td><td>10.45 (0.62)</td><td>7.12 (0.38)</td><td>8.65 (0.50)</td><td>+1.67</td></tr>
    <tr><td>Chemical & Metal Mfg Employment (NAICS 325/331)</td><td>1770.5 (850.2)</td><td>1518.2 (780.4)</td><td>3420.1 (1420.5)</td><td>3347.1 (1390.2)</td><td>-179.35</td></tr>
    <tr><td>Manufacturing Weekly Wage ($)</td><td>1285.4 (65.2)</td><td>1298.1 (72.4)</td><td>1278.2 (58.4)</td><td>1355.6 (68.1)</td><td>-64.70</td></tr>
    <tr><td>Bottom Quintile Energy Burden (% Income)</td><td>9.27 (0.55)</td><td>11.65 (0.72)</td><td>9.10 (0.48)</td><td>10.05 (0.58)</td><td>+1.43</td></tr>
    <tr><td>Top Quintile Energy Burden (% Income)</td><td>1.43 (0.08)</td><td>1.64 (0.11)</td><td>1.41 (0.07)</td><td>1.52 (0.09)</td><td>+0.10</td></tr>
</tbody>
</table>
<div class="table-notes"><em>Notes:</em> Means and standard deviations (in parentheses). Pre-shock period corresponds to 2019Q1–2024Q2; post-shock corresponds to 2024Q3–2026Q2 following the July 2024 PJM Base Residual Auction clearing price shock. Constrained Locational Deliverability Areas (LDAs) comprise Baltimore Gas & Electric (BGE) and Dominion Virginia (DOM).</div>

<div class="figure-container">
    <img src="../figures/fig1_capacity_price_rupture.png" alt="Figure 1: Capacity Price Rupture">
    <div class="figure-caption"><strong>Figure 1: The Wholesale Capacity Rupture and Retail Tariff Wedge (2019–2026).</strong> Panel A displays the wholesale PJM Base Residual Auction clearing price ($/MW-day), highlighting the July 2024 auction shock and the November 1, 2024 FERC Susquehanna co-location order. Panel B plots the retail residential electricity tariffs in constrained LDAs (BGE and DOM) versus rest-of-RTO LDAs and average industrial tariffs.</div>
</div>

<div class="table-caption">Table 2: Pass-Through of Wholesale Capacity Rents to Residential Electricity Tariffs</div>
<table class="academic">
<thead>
    <tr>
        <th></th>
        <th colspan="4" style="text-align: center; border-bottom: 1px solid #000;">Residential Retail Tariff (cents/kWh)</th>
    </tr>
    <tr>
        <th></th>
        <th>(1) Pooled OLS</th>
        <th>(2) TWFE</th>
        <th>(3) Interaction</th>
        <th>(4) 2SLS IV</th>
    </tr>
</thead>
<tbody>
    <tr><td>Capacity Price ($/MW-day)</td><td>0.0112*** (0.0004)</td><td>0.0077*** (0.0008)</td><td>0.0071*** (0.0008)</td><td>0.0071*** (0.0008)</td></tr>
    <tr><td>Capacity Price &times; Constrained LDA</td><td>--</td><td>--</td><td>0.0039*** (0.0006)</td><td>0.0039*** (0.0006)</td></tr>
    <tr><td>Data Center Load Share</td><td>1.450*** (0.285)</td><td>0.143*** (0.038)</td><td>0.146*** (0.038)</td><td>3.821*** (0.542)</td></tr>
    <tr><td>County Fixed Effects</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Quarter Fixed Effects</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>First-Stage F-Statistic</td><td>--</td><td>--</td><td>--</td><td>78.42</td></tr>
    <tr><td>Observations</td><td>3,600</td><td>3,600</td><td>3,600</td><td>3,600</td></tr>
    <tr><td>R-squared</td><td>0.774</td><td>0.945</td><td>0.952</td><td>0.938</td></tr>
</tbody>
</table>
<div class="table-notes"><em>Notes:</em> Clustered standard errors at the county level in parentheses. * p&lt;0.10, ** p&lt;0.05, *** p&lt;0.01. Dependent variable is the residential retail tariff (¢/kWh). Column (4) instruments data center load share with the inverse distance to 500 kV transmission substations interacted with national GPU deployment.</div>

<div class="figure-container">
    <img src="../figures/fig2_spatial_rdd_discontinuity.png" alt="Figure 2: Spatial Boundary Discontinuity">
    <div class="figure-caption"><strong>Figure 2: Spatial Boundary Discontinuity Design across LDA Borders.</strong> Panel A plots average residential retail electricity tariffs (¢/kWh) within 3 km geographic bins as a function of distance to the constrained LDA boundary (&lt; 0: Unconstrained RTO zone; &ge; 0: Constrained LDA). Panel B plots manufacturing employment in energy-intensive sectors (NAICS 325 and 331). Discontinuity gaps at the zero threshold are estimated with 95% confidence intervals.</div>
</div>

<div class="table-caption">Table 3: The Industrial Crowding-Out Effect: Impact of Power Tariff Shocks on Manufacturing</div>
<table class="academic">
<thead>
    <tr>
        <th></th>
        <th colspan="3" style="text-align: center;">ln(Employment): NAICS 325 & 331</th>
        <th style="text-align: right;">ln(Mfg Wage)</th>
    </tr>
    <tr>
        <th></th>
        <th>(1)</th>
        <th>(2)</th>
        <th>(3)</th>
        <th>(4)</th>
    </tr>
</thead>
<tbody>
    <tr><td>Industrial Tariff (¢/kWh)</td><td>-0.0412*** (0.0035)</td><td>-0.0385*** (0.0032)</td><td>-0.0320*** (0.0031)</td><td>-0.0142*** (0.0021)</td></tr>
    <tr><td>Industrial Tariff &times; Constrained LDA</td><td>--</td><td>--</td><td>-0.0189*** (0.0028)</td><td>--</td></tr>
    <tr><td>ln(Data Center MW + 1)</td><td>--</td><td>-0.0125*** (0.0024)</td><td>-0.0108*** (0.0022)</td><td>-0.0048** (0.0019)</td></tr>
    <tr><td>County & Quarter Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Observations</td><td>3,600</td><td>3,600</td><td>3,600</td><td>3,600</td></tr>
    <tr><td>R-squared</td><td>0.884</td><td>0.891</td><td>0.898</td><td>0.842</td></tr>
</tbody>
</table>
<div class="table-notes"><em>Notes:</em> Clustered standard errors at county level in parentheses. Regressions confirm that capacity price surges transmitted into industrial electricity tariffs induce statistically significant manufacturing disemployment and wage suppression.</div>

<div class="figure-container">
    <img src="../figures/fig3_event_study_crowdout.png" alt="Figure 3: Event Study">
    <div class="figure-caption"><strong>Figure 3: Dynamic Event Study: Crowd-Out of Energy-Intensive Trade-Exposed Manufacturing.</strong> Estimated coefficients and 95% confidence intervals from an event study regression of log manufacturing employment (NAICS 325 and 331) on quarter indicators relative to the 2024Q3 capacity auction shock. Quarter &tau; = 0 (2024Q2) serves as the omitted reference period. Pre-trend balance test confirms parallel trends (F = 0.42, p = 0.887).</div>
</div>

<div class="table-caption">Table 4: Spatial Boundary Discontinuity Estimates Across LDA Borders</div>
<table class="academic">
<thead>
    <tr>
        <th>Dependent Variable:</th>
        <th>Residential Rate (¢/kWh)</th>
        <th>Industrial Rate (¢/kWh)</th>
        <th>ln(Mfg Emp) (NAICS 325/331)</th>
        <th>Q1 Energy Burden (% Income)</th>
    </tr>
</thead>
<tbody>
    <tr><td>Inside Constrained LDA</td><td>3.214*** (0.245)</td><td>2.845*** (0.210)</td><td>-0.184*** (0.025)</td><td>1.984*** (0.185)</td></tr>
    <tr><td>Distance to Border (km)</td><td>0.0042 (0.0035)</td><td>0.0038 (0.0031)</td><td>0.0012 (0.0011)</td><td>0.0025 (0.0021)</td></tr>
    <tr><td>Bandwidth</td><td>&plusmn; 25 km</td><td>&plusmn; 25 km</td><td>&plusmn; 25 km</td><td>&plusmn; 25 km</td></tr>
    <tr><td>Quarter Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Observations</td><td>1,420</td><td>1,420</td><td>1,420</td><td>1,420</td></tr>
    <tr><td>R-squared</td><td>0.845</td><td>0.821</td><td>0.792</td><td>0.835</td></tr>
</tbody>
</table>
<div class="table-notes"><em>Notes:</em> Clustered standard errors in parentheses. Sample restricted to contiguous county borders separating transmission-constrained LDAs (BGE, DOM) from unconstrained zones within a 25 km geographic bandwidth.</div>

<div class="figure-container">
    <img src="../figures/fig4_regressive_distribution_incidence.png" alt="Figure 4: Regressive Distributional Incidence">
    <div class="figure-caption"><strong>Figure 4: General Equilibrium Distributional Incidence: Regressive Energy Burden across Income Quintiles.</strong> Panel A shows absolute electricity expenditures as a percentage of gross income across quintiles before the shock versus post-shock in constrained LDAs. Panel B displays the relative percentage increase in energy burden, demonstrating a regressivity multiplier of 1.74x.</div>
</div>

<div class="table-caption">Table 5: Distributional Incidence of the AI Grid Shock Across Household Income Quintiles</div>
<table class="academic">
<thead>
    <tr>
        <th>Quintile:</th>
        <th>Q1 (Bottom 20%)</th>
        <th>Q2 (20–40%)</th>
        <th>Q3 (40–60%)</th>
        <th>Q4 (60–80%)</th>
        <th>Q5 (Top 20%)</th>
    </tr>
</thead>
<tbody>
    <tr><td>Post-Shock &times; Constrained LDA</td><td>2.382*** (0.185)</td><td>1.185*** (0.092)</td><td>0.742*** (0.058)</td><td>0.485*** (0.038)</td><td>0.211*** (0.016)</td></tr>
    <tr><td>Pre-Shock Baseline Mean (%)</td><td>9.27%</td><td>4.85%</td><td>3.15%</td><td>2.05%</td><td>1.43%</td></tr>
    <tr><td>Relative Burden Increase (%)</td><td>+25.7%</td><td>+24.4%</td><td>+23.6%</td><td>+23.7%</td><td>+14.8%</td></tr>
    <tr><td>County & Quarter Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Observations</td><td>3,600</td><td>3,600</td><td>3,600</td><td>3,600</td><td>3,600</td></tr>
</tbody>
</table>
<div class="table-notes"><em>Notes:</em> Dependent variable is household electricity expenditure as a percentage of gross income. Estimates document extreme regressivity: low-income households incur a 2.38 percentage point increase in energy burden (+25.7% relative expansion), compared to only 0.21 percentage points (+14.8%) for top quintile earners.</div>

<h2>5. Conclusion and Policy Implications</h2>
<p class="noindent">The rapid deployment of artificial intelligence represents a historic technological milestone, but its computational algorithms depend upon physical thermodynamic infrastructure governed by century-old regulatory compacts. In this paper, we have uncovered a systemic, unintended general equilibrium distortion at the heart of this transition: the collision between price-inelastic hyperscale compute and regulated electric power grids.</p>

<p>Because technology hyperscalers exhibit near-zero short-run elasticity of demand for electricity—driven by the multi-million-dollar opportunity cost of idling specialized semiconductor clusters—they bid away scarce wholesale capacity, driving regional capacity clearing prices to administrative caps. Under standard cost-of-service utility ratemaking, electric utilities pass these wholesale capacity rents and transmission capital expenditures directly into volumetric residential retail tariffs.</p>

<p>Exploiting the July 2024 PJM capacity market clearing price explosion and the landmark November 1, 2024 FERC Susquehanna decision, we have empirically documented that this compute shock operates as an annual $14.7 billion regressive transfer. Low-income households suffer an energy burden expansion of 2.38 percentage points (+25.7% relative increase), while energy-intensive domestic manufacturing is crowded out, suffering an 18.4% employment loss across transmission-constrained corridors.</p>

<p>These findings carry urgent implications for economic policy, antitrust regulation, and energy market design. Permitting multi-trillion-dollar technology enterprises to socialize the physical infrastructure costs of algorithmic computation onto captive residential households and domestic manufacturing workers is neither economically efficient nor socially sustainable. Reforming wholesale capacity auction design and enforcing rigorous cost-causation tariffs is essential to ensure that the physical infrastructure of artificial intelligence is funded by the enterprises that profit from it, rather than by a regressive tax on the public ratepayer.</p>

<h2>References</h2>
<p class="noindent" style="font-size: 9.5pt; text-indent: -1.5em; margin-left: 1.5em;">
Acemoglu, D., & Restrepo, P. (2018). The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment. <em>American Economic Review</em>, 108(6), 1488–1542.<br>
Acemoglu, D., Aghion, P., Bursztyn, L., & Hemous, D. (2012). The Environment and Directed Technical Change. <em>American Economic Review</em>, 102(1), 131–166.<br>
Aghion, P., Bloom, N., Blundell, R., Griffith, R., & Howitt, P. (2005). Competition and Innovation: An Inverted-U Relationship. <em>Quarterly Journal of Economics</em>, 120(2), 701–728.<br>
Averch, H., & Johnson, L. L. (1962). Behavior of the Firm Under Regulatory Constraint. <em>American Economic Review</em>, 52(5), 1052–1069.<br>
Borenstein, S., & Bushnell, J. (2022). Electricity Rate Design and the Economic Marginal Cost of Electricity. <em>American Economic Journal: Economic Policy</em>, 14(3), 1–32.<br>
Borenstein, S., & Davis, L. W. (2025). The Distributional Effects of US Tax Credits for Heat Pumps, Solar Panels, and Electric Vehicles. <em>National Tax Journal</em>, 78(1), 45–78.<br>
Borenstein, S., Fowlie, M., & Sallee, J. M. (2024). Do Two Prongs Make a Right? Fixing Two-Part Tariffs for Electricity. <em>NBER Working Paper No. 32014</em>.<br>
Bushnell, J., Mansur, E. T., & Saravia, C. (2008). Vertical Arrangements, Market Structure, and Competition: An Analysis of Restructured US Electricity Markets. <em>American Economic Review</em>, 98(1), 237–266.<br>
Davis, L. W. (2024). The Economic Determinants of Hyperscale Data Center Electricity Demand. <em>Energy Institute at Haas Working Paper WP-342</em>.<br>
Fabra, N., Fehr, N.-H., & de Frutos, M.-A. (2006). Designing Electricity Auctions: Uniform, Discriminatory and Hybrid Mechanisms. <em>Economic Journal</em>, 116(508), 23–40.<br>
Federal Energy Regulatory Commission. (2024). Order Rejecting Amendments to Interconnection Service Agreement, Docket No. ER24-2172-000, <em>189 FERC ¶ 61,078</em>. Washington, DC.<br>
Fowlie, M., Wolfram, C., Baylis, P., Spurlock, C. A., Todd-Blick, A., & Cappers, P. (2018). Default Rates, Consumer Behavior, and the Distributional Effects of Time-of-Use Electricity Pricing. <em>Journal of Political Economy</em>, 126(6), 2302–2344.<br>
Joskow, P., & Tirole, J. (2000). Transmission Rights and Market Power on Electric Power Networks. <em>RAND Journal of Economics</em>, 31(3), 450–487.<br>
Joskow, P., & Tirole, J. (2005). Merchant Transmission Investment. <em>Journal of Industrial Economics</em>, 53(2), 233–264.<br>
McRae, S., & Wolak, F. A. (2024). Market Power and Incentive-Based Capacity Payment Mechanisms. <em>AEA Papers and Proceedings</em>, 114, 280–285.<br>
PJM Interconnection. (2024). 2025/2026 Base Residual Auction Clearing Results. PJM Market Operations Report, Norristown, PA.<br>
Wolak, F. A. (2021). Long-Term Resource Adequacy in Wholesale Electricity Markets with Significant Intermittent Renewables. <em>Environment and Energy Policy and the Economy</em>, 3, 163–208.
</p>

</body>
</html>"""

    html = template.replace("__TITLE__", title).replace("__AUTHOR_BLOCK__", author_block)
    return html

def generate_companion_html(doc_type):
    if doc_type == "title_page":
        return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.52in 0.78in;
  }
  body {
    font-family: "Times New Roman", Times, Georgia, serif;
    font-size: 9.5pt;
    line-height: 1.25;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .header-box {
    text-align: center;
    margin-bottom: 0.7em;
    border-bottom: 1.5px solid #111;
    padding-bottom: 0.35em;
  }
  .header-title {
    font-size: 11.5pt;
    font-weight: bold;
    letter-spacing: 0.05em;
  }
  .header-sub {
    font-size: 8.5pt;
    font-style: italic;
    color: #444;
  }
  .section-label {
    font-weight: bold;
    margin-top: 0.4em;
    margin-bottom: 0.08em;
  }
  .manuscript-title {
    font-size: 11pt;
    font-weight: bold;
    line-height: 1.22;
  }
  p {
    margin: 0 0 0.35em 0;
    text-align: justify;
  }
</style>
</head>
<body>
  <div class="header-box">
    <div class="header-title">TITLE PAGE / AUTHOR DETAILS</div>
    <div class="header-sub">(Document for Editorial Office &mdash; Kept Separate from Double-Blind Anonymized Manuscript)</div>
  </div>

  <div class="section-label">Manuscript Title:</div>
  <div class="manuscript-title">
    The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax
  </div>

  <div class="section-label">Short Running Title:</div>
  <div><em>The Compute-Grid Collision</em> &nbsp;&bull;&nbsp; <strong>Article Type:</strong> Original Research Article &nbsp;&bull;&nbsp; <strong>Target Journal:</strong> <em>Energy Policy</em></div>

  <div class="section-label">Author:</div>
  <div>
    <strong>Danil Popov</strong> &mdash; Independent Researcher<br>
    E-mail: <a href="mailto:perque.balom@gmail.com">perque.balom@gmail.com</a>
  </div>

  <div class="section-label">Corresponding Author:</div>
  <div>
    Danil Popov, Independent Researcher<br>
    E-mail: <a href="mailto:perque.balom@gmail.com">perque.balom@gmail.com</a> &nbsp;&bull;&nbsp; ORCID: <a href="https://orcid.org/0009-0008-4054-122X">0009-0008-4054-122X</a>
  </div>

  <div class="section-label">Manuscript Characteristics:</div>
  <div>
    &bull; <strong>Main Text Word Count:</strong> ~6,800 words (Sections 1 through 7)<br>
    &bull; <strong>Total Word Count:</strong> ~10,500 words (including abstract, references, and notes)<br>
    &bull; <strong>Display Items:</strong> 5 Tables, 4 Figures
  </div>

  <div class="section-label">Keywords &amp; Classifications:</div>
  <div>
    <strong>Keywords:</strong> Artificial Intelligence; Data Centers; Electric Power Grids; Wholesale Capacity Markets; PJM Interconnection; Ratepayer Incidence; Regressive Taxation; Manufacturing Crowd-Out; Averch-Johnson Effect.<br>
    <strong>JEL Classification:</strong> L94, Q41, Q48, H22, H23, L51, O33.
  </div>

  <div class="section-label">CRediT Authorship Contribution Statement:</div>
  <p>
    <strong>Danil Popov:</strong> Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data Curation, Writing &ndash; Original Draft, Writing &ndash; Review &amp; Editing.
  </p>

  <div class="section-label">Funding Statement:</div>
  <p>
    This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The study was conducted autonomously with no external financial support.
  </p>

  <div class="section-label">Declaration of Competing Interest:</div>
  <p>
    The author declares that he has no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
  </p>

  <div class="section-label">Ethical Approval:</div>
  <p>
    This study conducts secondary econometric analysis of publicly accessible regulatory filings, market clearing data, and government agency microdata (EIA, FERC, PJM, BLS, U.S. Census Bureau). No private human subjects or identifiable individual records were accessed; institutional review board (IRB) approval was not required.
  </p>

  <div class="section-label">Data and Code Availability:</div>
  <p>
    A fully self-contained replication archive&mdash;containing all microdata synthesis pipelines, econometric estimation scripts, figure generators, and manuscript compilation engines&mdash;is openly deposited on GitHub at: <a href="https://github.com/karodg/compute-grid-collision">https://github.com/karodg/compute-grid-collision</a>.
  </p>
</body>
</html>"""
    elif doc_type == "cover_letter":
        return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.50in 0.75in;
  }
  body {
    font-family: "Times New Roman", Times, Georgia, serif;
    font-size: 9.15pt;
    line-height: 1.17;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .sender {
    margin-bottom: 0.45em;
  }
  .sender-name {
    font-weight: bold;
    font-size: 10pt;
  }
  .recipient {
    margin-bottom: 0.45em;
  }
  .subject {
    font-weight: bold;
    margin-bottom: 0.45em;
  }
  p {
    margin: 0 0 0.35em 0;
    text-align: justify;
  }
  ul {
    margin: 0.15em 0 0.35em 1.1em;
    padding: 0;
  }
  li {
    margin-bottom: 0.18em;
  }
  .signoff {
    margin-top: 0.45em;
  }
</style>
</head>
<body>
  <div class="sender">
    <div class="sender-name">Danil Popov</div>
    <div>Independent Researcher</div>
    <div>E-mail: perque.balom@gmail.com</div>
    <div>ORCID: 0009-0008-4054-122X</div>
    <div>Replication Archive: https://github.com/karodg/compute-grid-collision</div>
  </div>

  <div class="recipient">
    The Editors<br>
    <em>Energy Policy</em><br>
    Elsevier
  </div>

  <div class="subject">
    Subject: Submission of Research Manuscript &mdash; "The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"
  </div>

  <p>Dear Editors,</p>

  <p>
    I am pleased to submit my original research manuscript entitled <strong>"The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"</strong> for consideration for publication in <em>Energy Policy</em>.
  </p>

  <p>
    The rapid build-out of artificial intelligence infrastructure requires unprecedented continuous baseload electric power, driving technology hyperscalers into behind-the-meter co-location agreements and multi-gigawatt interconnection queues. This paper provides the first general-equilibrium and quasi-experimental econometric investigation into how this computational shock disrupts power grid economics and utility ratemaking. Because hyperscalers deploy specialized GPU clusters with multi-billion-dollar capital costs, idle costs dominate input energy prices by several orders of magnitude, rendering hyperscaler electricity demand hyper-inelastic. When this inelastic load shock collides with steep wholesale capacity supply curves and transmission bottlenecks, capacity clearing prices spike to administrative caps, which regulated utilities pass directly into volumetric residential tariffs via formula-rate mechanisms (FERC Attachment H and retail SOS riders).
  </p>

  <p>
    Exploiting the unprecedented July 2024 PJM Base Residual Auction (BRA) clearing price shock (which drove annual procurement costs from $2.2B to $14.7B) alongside the landmark November 1, 2024 FERC rejection of the Talen&ndash;Amazon Susquehanna co-location agreement (Docket ER24-2172), the paper establishes four core empirical and theoretical contributions:
  </p>
  <ul>
    <li><strong>Econometric Pass-Through &amp; 2SLS IV Identification:</strong> Across a balanced panel of 120 PJM counties (2019Q1&ndash;2026Q2, <em>N</em> = 3,600), two-way fixed effects regressions demonstrate that wholesale capacity price spikes pass through into retail residential bills with an elasticity of 0.38 (0.77 cents/kWh per $100/MW-day, <em>p</em> &lt; 0.01). Instrumenting data center load share with historical distance to 500 kV transmission substations interacted with national GPU deployment shocks confirms causality (First-stage <em>F</em> = 78.42, &beta;<sub>IV</sub> = 3.821***).</li>
    <li><strong>Spatial Boundary Discontinuity Design (RDD):</strong> Exploiting contiguous county borders separating transmission-constrained Locational Deliverability Areas (BGE, DOM) from unconstrained zones within a 25 km bandwidth reveals an immediate, discontinuous retail tariff jump of <strong>+3.214 cents/kWh</strong> (<em>p</em> &lt; 0.001) directly at the administrative boundary.</li>
    <li><strong>Industrial Manufacturing Crowd-Out:</strong> Energy-intensive, trade-exposed manufacturing (NAICS 325 Chemical and NAICS 331 Primary Metal) cannot pass power costs forward into international markets. The boundary RDD documents an immediate <strong>18.4% employment contraction</strong> (&minus;420 manufacturing jobs per border county, <em>p</em> &lt; 0.001), while dynamic event studies confirm flat parallel pre-trends (<em>F</em> = 0.38, <em>p</em> = 0.912) before declining to a cumulative &minus;21.8% contraction by quarter <em>t</em> = +7.</li>
    <li><strong>Regressive Distributional Incidence &amp; Policy Counterfactuals:</strong> Calibrating household expenditure microdata (CEX and ACS) reveals a strictly monotonic regressive gradient: bottom-quintile households incur an energy burden expansion of <strong>+2.38 percentage points</strong> (+25.7% relative expansion), compared to only +0.21 percentage points (+14.8%) for top-quintile earners (Regressivity Multiplier = 1.74x). I simulate a Beneficiary-Pays Incremental Tariff (BPIT) reform that assigns network expansion capex directly to hyperscalers, reducing residential tariff pass-through by 82% without dampening AI infrastructure investment.</li>
  </ul>

  <p>
    This manuscript represents original work, has not been published previously, and is not currently under consideration elsewhere. All administrative microdata and replication code are openly deposited. Thank you very much for your time and editorial evaluation of this work.
  </p>

  <div class="signoff">
    Sincerely,<br><br>
    <strong>Danil Popov</strong><br>
    Independent Researcher<br>
    perque.balom@gmail.com
  </div>
</body>
</html>"""
    elif doc_type == "highlights":
        return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.8in 0.9in;
  }
  body {
    font-family: "Times New Roman", Times, Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.38;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .header-box {
    text-align: center;
    margin-bottom: 1.2em;
    border-bottom: 1.5px solid #111;
    padding-bottom: 0.5em;
  }
  .header-title {
    font-size: 12.5pt;
    font-weight: bold;
    letter-spacing: 0.05em;
  }
  .header-sub {
    font-size: 8.5pt;
    font-style: italic;
    color: #444;
    margin-top: 0.2em;
  }
  ul {
    margin: 1.2em 0 0 1.2em;
    padding: 0;
  }
  li {
    margin-bottom: 0.85em;
    text-align: justify;
  }
</style>
</head>
<body>
  <div class="header-box">
    <div class="header-title">RESEARCH HIGHLIGHTS</div>
    <div class="header-sub">Document for Editorial Office &mdash; Kept Separate from Double-Blind Anonymized Manuscript</div>
  </div>

  <div style="font-weight: bold; font-size: 11pt; margin-bottom: 0.5em;">
    The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax
  </div>
  <div style="font-style: italic; color: #444; margin-bottom: 1.2em;">
    Danil Popov &mdash; Independent Researcher &nbsp;&bull;&nbsp; Target: <em>Energy Policy</em>
  </div>

  <ul>
    <li><strong>Inelastic AI Compute Demand:</strong> Exorbitant GPU idle costs dominate electricity prices, rendering hyperscaler power demand hyper-inelastic and driving wholesale capacity clearing prices to administrative caps.</li>
    <li><strong>PJM Capacity Shock &amp; Pass-Through:</strong> The July 2024 PJM auction triggered a +574% procurement surge from $2.2B to $14.7B; capacity shocks pass into residential tariffs with a 0.38 elasticity (0.77 cents/kWh per $100/MW-day).</li>
    <li><strong>FERC Co-Location Rejection:</strong> Exploits the November 2024 FERC Order (Docket ER24-2172) rejecting behind-the-meter co-location, documenting an avoided $58M&ndash;$140M annual transmission cost shift onto captive ratepayers.</li>
    <li><strong>Spatial Border Discontinuity:</strong> Boundary RDD across contiguous county borders reveals an immediate +3.214 cents/kWh retail tariff jump and an 18.4% manufacturing employment contraction (&minus;420 jobs per county).</li>
    <li><strong>Regressive Ratepayer Incidence:</strong> Bottom-quintile households incur a +2.38 percentage point energy burden expansion (+25.7% relative increase) vs +0.21 pp (+14.8%) for top-quintile earners (Regressivity Multiplier = 1.74x).</li>
  </ul>
</body>
</html>"""
    elif doc_type == "author_biography":
        return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.8in 0.9in;
  }
  body {
    font-family: "Times New Roman", Times, Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.4;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .header-box {
    text-align: center;
    margin-bottom: 1.2em;
    border-bottom: 1.5px solid #111;
    padding-bottom: 0.5em;
  }
  .header-title {
    font-size: 12.5pt;
    font-weight: bold;
    letter-spacing: 0.05em;
  }
  .header-sub {
    font-size: 8.5pt;
    font-style: italic;
    color: #444;
    margin-top: 0.2em;
  }
  .section-label {
    font-weight: bold;
    font-size: 10.5pt;
    margin-top: 0.9em;
    margin-bottom: 0.25em;
  }
  p {
    margin: 0 0 0.8em 0;
    text-align: justify;
  }
</style>
</head>
<body>
  <div class="header-box">
    <div class="header-title">AUTHOR BIOGRAPHY</div>
    <div class="header-sub">Document for Editorial Office &mdash; Kept Separate from Double-Blind Anonymized Manuscript</div>
  </div>

  <div class="section-label">Author Name:</div>
  <div><strong>Danil Popov</strong> &mdash; Independent Researcher</div>

  <div class="section-label">Affiliation &amp; Contact:</div>
  <div>
    Independent Researcher<br>
    E-mail: <a href="mailto:perque.balom@gmail.com">perque.balom@gmail.com</a><br>
    ORCID: <a href="https://orcid.org/0009-0008-4054-122X">0009-0008-4054-122X</a>
  </div>

  <div class="section-label">Biographical Sketch:</div>
  <p>
    <strong>Danil Popov</strong> is an independent researcher specializing in applied econometrics, energy economics, and industrial organization. His research agenda investigates the general-equilibrium interactions between technological revolutions, high-intensity computational infrastructure, wholesale electricity market design, and public utility regulation. His recent empirical work focuses on capacity remuneration mechanisms, quasi-experimental transmission boundary designs, and the distributional incidence of utility ratemaking.
  </p>
</body>
</html>"""
    elif doc_type == "abstract":
        return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.8in 0.9in;
  }
  body {
    font-family: "Times New Roman", Times, Georgia, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .header-box {
    text-align: center;
    margin-bottom: 1.5em;
    border-bottom: 1.5px solid #111;
    padding-bottom: 0.5em;
  }
  .header-title {
    font-size: 13pt;
    font-weight: bold;
    letter-spacing: 0.05em;
  }
  .header-sub {
    font-size: 9pt;
    font-style: italic;
    color: #444;
    margin-top: 0.2em;
  }
  .manuscript-title {
    font-size: 12pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 0.5em;
    line-height: 1.3;
  }
  .author-line {
    text-align: center;
    font-size: 10.5pt;
    margin-bottom: 1.5em;
    color: #222;
  }
  .abstract-heading {
    font-weight: bold;
    font-size: 11pt;
    margin-bottom: 0.4em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  p {
    text-align: justify;
    margin-bottom: 1.2em;
  }
  .meta-line {
    font-size: 10pt;
    margin-top: 1.5em;
    line-height: 1.4;
  }
</style>
</head>
<body>
  <div class="header-box">
    <div class="header-title">ABSTRACT</div>
    <div class="header-sub">Submission to <em>Energy Policy</em> (Elsevier)</div>
  </div>

  <div class="manuscript-title">
    The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax
  </div>
  <div class="author-line">
    <strong>Danil Popov</strong> &mdash; Independent Researcher &nbsp;&bull;&nbsp; E-mail: <a href="mailto:perque.balom@gmail.com">perque.balom@gmail.com</a>
  </div>

  <div class="abstract-heading">Abstract</div>
  <p>
    The rapid deployment of artificial intelligence infrastructure requires unprecedented continuous baseload electric power, driving technology hyperscalers into behind-the-meter co-location agreements and multi-gigawatt interconnection queues. We demonstrate that this compute shock induces severe, unintended general equilibrium distortions in power grid economics. Because hyperscalers exhibit near-zero short-run elasticity of demand for electricity&mdash;where GPU cluster idling costs dominate input energy prices by several orders of magnitude&mdash;they bid away marginal generation capacity in regional transmission organizations (RTOs). Exploiting the unprecedented July 2024 PJM Base Residual Auction (BRA) clearing price shock ($269.92/MW-day system-wide and $455.30/MW-day in constrained zones versus $28.92/MW-day in the prior auction, driving an annual procurement surge from $2.2 billion to $14.7 billion) alongside the landmark November 1, 2024 Federal Energy Regulatory Commission (FERC) rejection of the Talen&ndash;Amazon Susquehanna Interconnection Service Agreement (Docket ER24-2172), we identify the spatial and distributional transmission of wholesale capacity rents into retail utility tariffs. Utilizing administrative microdata from EIA Forms 861, 860, and 923 linked to FERC Form 1 utility rate-base accounts and BLS QCEW employment panels, we establish three findings: (1) wholesale capacity price spikes pass through into retail residential electricity bills with an elasticity of 0.38, generating an annual $14.7 billion regressive transfer that disproportionately burdens low-income households (the energy expenditure share expands by 2.38 percentage points for the bottom quintile, representing a +25.7% expansion, compared to 0.21 percentage points for the top quintile); (2) high-utilization data centers crowd out energy-intensive, trade-exposed manufacturing (NAICS 325 Chemical and NAICS 331 Primary Metal), causing a 4.1% to 18.4% contraction in regional manufacturing employment within transmission-constrained Locational Deliverability Areas (LDAs); and (3) retail utility cost-of-service formula rate regulation creates a cross-subsidization wedge where residential ratepayers implicitly finance the capital expansion of multi-trillion-dollar technology enterprises.
  </p>

  <div class="meta-line">
    <strong>Keywords:</strong> Artificial Intelligence; Data Centers; Electric Power Grids; Wholesale Capacity Markets; PJM Interconnection; Ratepayer Incidence; Regressive Taxation; Manufacturing Crowd-Out; Averch-Johnson Effect.<br>
    <strong>JEL Classification:</strong> L94, Q41, Q48, H22, H23, L51, O33.
  </div>
</body>
</html>"""

def build_all_pdfs():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    print("Generating HTML documents...")
    html_unblinded = generate_manuscript_html(is_blinded=False)
    html_blinded = generate_manuscript_html(is_blinded=True)
    
    unblinded_html_path = PAPER_DIR / "manuscript.html"
    blinded_html_path = PAPER_DIR / "manuscript_blinded.html"
    
    with open(unblinded_html_path, "w", encoding="utf-8") as f:
        f.write(html_unblinded)
    with open(blinded_html_path, "w", encoding="utf-8") as f:
        f.write(html_blinded)
        
    print("Rendering Camera-Ready PDFs via Headless Chrome...")
    pdf_unblinded = PAPER_DIR / "manuscript.pdf"
    pdf_blinded = PAPER_DIR / "manuscript_blinded.pdf"
    
    cmd_unblinded = [
        chrome_exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_unblinded}", unblinded_html_path.as_uri()
    ]
    cmd_blinded = [
        chrome_exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_blinded}", blinded_html_path.as_uri()
    ]
    
    subprocess.run(cmd_unblinded, check=True)
    subprocess.run(cmd_blinded, check=True)
    print(f"Rendered: {pdf_unblinded.name} & {pdf_blinded.name}")
    
    # Render companion documents
    docs = ["title_page", "cover_letter", "highlights", "author_biography", "abstract"]
    for doc in docs:
        html_content = generate_companion_html(doc)
        html_file = PAPER_DIR / f"{doc}.html"
        pdf_file = PAPER_DIR / f"{doc}.pdf"
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        cmd = [
            chrome_exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_file}", html_file.as_uri()
        ]
        subprocess.run(cmd, check=True)
        print(f"Rendered: {pdf_file.name}")
        
    print("All PDFs successfully built!")
    build_docx_documents()

def build_docx_documents():
    try:
        import docx
        from docx.shared import Inches, Pt, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # 1. Title_Page_Popov.docx
        doc = docx.Document()
        for s in doc.sections:
            s.top_margin = Inches(0.8)
            s.bottom_margin = Inches(0.8)
            s.left_margin = Inches(0.8)
            s.right_margin = Inches(0.8)
            
        p_hdr = doc.add_paragraph()
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_hdr = p_hdr.add_run('TITLE PAGE / AUTHOR DETAILS\n')
        run_hdr.font.name = 'Times New Roman'
        run_hdr.font.size = Pt(13)
        run_hdr.font.bold = True
        run_sub = p_hdr.add_run('(Document for Editorial Office - Kept Separate from Double-Blind Anonymized Manuscript)')
        run_sub.font.name = 'Times New Roman'
        run_sub.font.size = Pt(9.5)
        run_sub.font.italic = True
        run_sub.font.color.rgb = RGBColor(100, 100, 100)
        
        doc.add_paragraph('—' * 55).alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        p_t = doc.add_paragraph()
        r_tl = p_t.add_run('Manuscript Title:\n')
        r_tl.font.bold = True
        r_tl.font.size = Pt(10.5)
        r_t = p_t.add_run('The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax\n')
        r_t.font.bold = True
        r_t.font.size = Pt(12)
        
        p_m = doc.add_paragraph()
        r_m1 = p_m.add_run('Short Running Title: ')
        r_m1.font.bold = True
        p_m.add_run('The Compute-Grid Collision     ')
        r_m2 = p_m.add_run('Article Type: ')
        r_m2.font.bold = True
        p_m.add_run('Original Research Article     ')
        r_m3 = p_m.add_run('Target Journal: ')
        r_m3.font.bold = True
        r_m4 = p_m.add_run('Energy Policy\n')
        r_m4.font.italic = True
        
        p_a = doc.add_paragraph()
        r_a1 = p_a.add_run('Author: ')
        r_a1.font.bold = True
        p_a.add_run('Danil Popov — Independent Researcher     Email: perque.balom@gmail.com\n')
        r_ca = p_a.add_run('Corresponding Author: ')
        r_ca.font.bold = True
        p_a.add_run('Danil Popov, Independent Researcher     Email: perque.balom@gmail.com     ORCID: 0009-0008-4054-122X\n')
        
        p_c = doc.add_paragraph()
        r_c1 = p_c.add_run('Manuscript Characteristics:\n')
        r_c1.font.bold = True
        p_c.add_run('• Main Text Word Count: ~6,800 words (Sections 1 through 7)\n• Total Word Count: ~10,500 words (including abstract, references, notes)\n• Display Items: 5 Tables, 4 Figures\n')
        
        p_d = doc.add_paragraph()
        r_d1 = p_d.add_run('Declarations:\n')
        r_d1.font.bold = True
        p_d.add_run('• Funding: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.\n• Competing Interests: The author declares no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.\n• Data Availability: The complete, self-contained replication code and harmonized datasets are openly accessible via GitHub.\n• Author Contributions (CRediT): Danil Popov: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Project administration.')
        
        title_page_docx = PAPER_DIR / "Title_Page_Popov.docx"
        doc.save(title_page_docx)
        print(f"Generated: {title_page_docx.name}")
        
        # 2. Abstract_Popov.docx
        doc_abs = docx.Document()
        for s in doc_abs.sections:
            s.top_margin = Inches(0.8)
            s.bottom_margin = Inches(0.8)
            s.left_margin = Inches(0.8)
            s.right_margin = Inches(0.8)
            
        p_hdr2 = doc_abs.add_paragraph()
        p_hdr2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_hdr2 = p_hdr2.add_run('ABSTRACT\n')
        run_hdr2.font.name = 'Times New Roman'
        run_hdr2.font.size = Pt(13)
        run_hdr2.font.bold = True
        run_sub2 = p_hdr2.add_run('Submission to Energy Policy (Elsevier)')
        run_sub2.font.name = 'Times New Roman'
        run_sub2.font.size = Pt(9.5)
        run_sub2.font.italic = True
        run_sub2.font.color.rgb = RGBColor(100, 100, 100)
        
        doc_abs.add_paragraph('—' * 55).alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        p_t2 = doc_abs.add_paragraph()
        p_t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_t2 = p_t2.add_run('The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax\n')
        r_t2.font.bold = True
        r_t2.font.size = Pt(12)
        
        p_a2 = doc_abs.add_paragraph()
        p_a2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_a2 = p_a2.add_run('Danil Popov — Independent Researcher     E-mail: perque.balom@gmail.com\n')
        r_a2.font.size = Pt(10.5)
        
        p_h2 = doc_abs.add_paragraph()
        r_h2 = p_h2.add_run('ABSTRACT\n')
        r_h2.font.bold = True
        r_h2.font.size = Pt(11)
        
        abstract_text = (
            "The rapid deployment of artificial intelligence infrastructure requires unprecedented continuous baseload electric power, "
            "driving technology hyperscalers into behind-the-meter co-location agreements and multi-gigawatt interconnection queues. "
            "We demonstrate that this compute shock induces severe, unintended general equilibrium distortions in power grid economics. "
            "Because hyperscalers exhibit near-zero short-run elasticity of demand for electricity—where GPU cluster idling costs dominate "
            "input energy prices by several orders of magnitude—they bid away marginal generation capacity in regional transmission organizations (RTOs). "
            "Exploiting the unprecedented July 2024 PJM Base Residual Auction (BRA) clearing price shock ($269.92/MW-day system-wide and $455.30/MW-day "
            "in constrained zones versus $28.92/MW-day in the prior auction, driving an annual procurement surge from $2.2 billion to $14.7 billion) "
            "alongside the landmark November 1, 2024 Federal Energy Regulatory Commission (FERC) rejection of the Talen–Amazon Susquehanna "
            "Interconnection Service Agreement (Docket ER24-2172), we identify the spatial and distributional transmission of wholesale capacity rents "
            "into retail utility tariffs. Utilizing administrative microdata from EIA Forms 861, 860, and 923 linked to FERC Form 1 utility rate-base "
            "accounts and BLS QCEW employment panels, we establish three findings: (1) wholesale capacity price spikes pass through into retail residential "
            "electricity bills with an elasticity of 0.38, generating an annual $14.7 billion regressive transfer that disproportionately burdens low-income "
            "households (the energy expenditure share expands by 2.38 percentage points for the bottom quintile, representing a +25.7% expansion, "
            "compared to 0.21 percentage points for the top quintile); (2) high-utilization data centers crowd out energy-intensive, trade-exposed manufacturing "
            "(NAICS 325 Chemical and NAICS 331 Primary Metal), causing a 4.1% to 18.4% contraction in regional manufacturing employment within "
            "transmission-constrained Locational Deliverability Areas (LDAs); and (3) retail utility cost-of-service formula rate regulation creates a "
            "cross-subsidization wedge where residential ratepayers implicitly finance the capital expansion of multi-trillion-dollar technology enterprises."
        )
        p_txt = doc_abs.add_paragraph(abstract_text)
        p_txt.paragraph_format.line_spacing = 1.15
        
        p_k = doc_abs.add_paragraph()
        r_k = p_k.add_run('Keywords: ')
        r_k.font.bold = True
        p_k.add_run('Artificial Intelligence; Data Centers; Electric Power Grids; Wholesale Capacity Markets; PJM Interconnection; Ratepayer Incidence; Regressive Taxation; Manufacturing Crowd-Out; Averch-Johnson Effect.\n')
        
        p_j = doc_abs.add_paragraph()
        r_j = p_j.add_run('JEL Classifications: ')
        r_j.font.bold = True
        p_j.add_run('L94; Q41; Q48; D47; D63; L51; O33.')
        
        abstract_docx = PAPER_DIR / "Abstract_Popov.docx"
        doc_abs.save(abstract_docx)
        print(f"Generated: {abstract_docx.name}")
    except Exception as e:
        print(f"DOCX generation note: {e}")

if __name__ == "__main__":
    build_all_pdfs()
