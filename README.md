# Fashion Trends & Economic Indicators (Australia)

## Project Overview

This project explores the relationship between **Australian economic conditions** and **fashion trend adoption** using a combination of Google Trends data and official economic indicators. The goal is to understand whether fashion trends respond immediately to economic changes or whether they emerge with measurable delays, and to empirically test popular cultural theories such as the *Hemline Index*.

The analysis spans **2010–2024** and applies multiple time-series techniques, including correlation analysis, cross-correlation, lag analysis, Granger causality testing, and event-based analysis around COVID-19.

---

## Data Sources

### Economic Indicators (Australia)

* Unemployment Rate (%)
* Consumer Price Index (CPI)
* Seasonally Adjusted Retail Turnover ($m)

### Fashion Trend Indicators (Google Trends)

Keywords used:

* luxury
* quiet luxury
* silent luxury
* minimalist fashion
* timeless basics
* capsule wardrobe
* thrift store
* second hand clothing
* vintage clothing
* short skirts
* mini skirts
* fast fashion
* statement pieces

All Google Trends series were normalized and aligned to monthly frequency to match economic data.

---

## Methodology

The project uses multiple complementary analytical approaches:

* **Correlation Matrix**: Measures contemporaneous relationships between economic indicators and fashion trends.
* **Lagged Correlation Analysis**: Examines how correlations evolve across short-term (0–12 months) and long-term (up to 48 months) horizons.
* **Cross-Correlation Analysis**: Identifies the lag at which the relationship between an economic variable and a fashion trend is strongest.
* **Granger Causality Testing**: Tests whether past values of economic indicators statistically improve prediction of fashion interest.
* **Event Study (COVID-19)**: Evaluates behavioral shifts before, during, and after the pandemic shock (Jan 2020 – Dec 2021).

Together, these methods allow the analysis to capture **immediate reactions**, **behavioral adaptations**, and **long-term cultural shifts**.

---

## Key Results & Findings

### 1. Is there a measurable relationship between economic conditions and fashion trends?

**Yes, there is a strong and statistically significant relationship.** The correlation matrix and cross-correlation data reveal that fashion interest is deeply tied to economic health:

* **Inflation (CPI):** Shows some of the strongest ties, with a **0.86 correlation to fast fashion** and a **0.88 correlation to capsule wardrobes**.
* **Unemployment:** Has a **strong negative correlation with fast fashion (-0.63)** and thrift stores (-0.51), suggesting interest in these categories drops when unemployment is high.
* **Statistical Significance:** P-values for economic indicators driving interest in *fast fashion* and *quiet luxury* are frequently below 0.05, particularly for CPI’s influence on fast fashion, indicating a robust predictive relationship.

---

### 2. Do different fashion categories respond on different time horizons?

**Yes, fashion categories display distinct temporal sensitivities.**

* **Immediate (0–3 months):**

  * *Thrift stores* and *quiet luxury* respond immediately to inflation (0-month lag).
  * *Luxury* interest reacts quickly to CPI changes at a 2-month lag.

* **Medium-Term (12–24 months):**

  * *Fast fashion* peaks in correlation at approximately **12–13 months**, suggesting delayed behavioral adjustment rather than instant reaction.

* **Long-Term (36–48 months):**

  * *Capsule wardrobes* and *luxury* show their strongest relationship with retail turnover at **48 months** and **45 months** respectively, indicating slow-moving cultural normalization.

---

### 3. Are there lag effects between economic change and trend adoption?

**Yes, significant lag effects are present across multiple trends.**

* The **48-month lag analysis** shows that correlations often strengthen substantially over time.
* *Quiet luxury* begins with a modest **0.21 correlation at 0 months**, increasing to **0.52 after 48 months**.
* *Mini skirts* show almost no immediate relationship (0.01) but rise to **0.31 at the 48-month mark**.
* In contrast, *short skirts* maintain a strong negative correlation across timeframes, reaching **-0.52 after 48 months**.

These results indicate that many fashion trends respond to the **cumulative effects of economic cycles**, rather than short-term shocks.

---

### 4. Does the popular “Hemline Index” hold empirically?

**The results are mixed and highly dependent on terminology.**

The Hemline Index proposes that shorter skirts are more popular during economic booms.

* **Mini Skirts (Supports the Index):**

  * Negative correlation with unemployment (-0.21)
  * Positive correlation with retail turnover (0.14)
  * Suggests rising interest during economic expansion

* **Short Skirts (Contradicts the Index):**

  * Positive correlation with unemployment (0.37)
  * Strong negative correlation with turnover (-0.72)

This divergence suggests that **semantic differences in search behavior** materially affect empirical validation of cultural theories.

---

### 5. How did COVID-19 reshape fashion interest and consumer behavior?

The event analysis (Jan 2020 – Dec 2021) reveals a clear **shock-and-recovery pattern**:

* **Immediate Shock (Early 2020):**

  * Unemployment rose from **5.25% (Jan 2020) to 7.05% (May 2020)**
  * *Luxury* interest collapsed from **98 to 46**
  * *Fast fashion* interest surged from **18 to 52**

* **Budget & Sustainability Shift:**

  * *Vintage clothing* and *thrift stores* peaked during lockdowns (75 and 91 respectively)

* **Recovery Phase (2021):**

  * Unemployment fell to **4.2% by Dec 2021**
  * Retail turnover reached **$32,521.3m**
  * *Mini skirts* rebounded (peaks of 67–68)
  * *Statement pieces* experienced a one-time spike (88), signaling renewed consumer confidence

---

## Interpretation

Rather than contradicting each other, the analytical methods reveal **different layers of fashion response**:

* **Immediate reactions** reflect consumer sentiment and affordability constraints
* **Medium-term shifts** capture behavioral adaptation
* **Long-term trends** represent cultural normalization and aesthetic change

Together, these results support the conclusion that fashion trends are not merely reactive but evolve through **multi-stage economic and cultural processes**.

---

## Future Work

* Expand analysis to additional countries for cross-cultural comparison
* Incorporate social media engagement data
* Apply regime-switching or structural break models
* Develop forecasting models for fashion trend emergence

---

## Limitations

* Google Trends data reflects relative search interest, not actual sales.
* Retail sales data contains structural gaps in early years.
* Correlation and Granger causality do not imply true causal mechanisms.

## Future Work

* Incorporate social media data (Instagram, TikTok)
* Compare results across countries
* Segment fashion categories by price tiers
* Apply structural break tests for major economic events

## Author

Tanisha Thapa
