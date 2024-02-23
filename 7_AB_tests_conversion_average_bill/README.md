# 7. AB Test: 2 Landing Page Variants for a Travel Agency

## Table of Contents
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results
6. Conclusions

### Project Description

AB-test based on two criteria — purchase conversion and daily average check.

### Problem Statement

Analyze the effectiveness of 2 landing page variants for a travel agency 

**Competition Conditions:**
Which of the 2 landing page variants provides better conversion and average check metrics, and how stable are the metrics.

**Quality Metric:**
Conversion, daily average check, as well as cumulative metrics.

**Practiced Techniques:**
Feature engineering, AB tests, hypothesis testing, statistical tests, confidence intervals.

### Brief Data Overview

The data consists of a CSV table with the following fields:

- user_id — identifier of the user who visited the site;
- date — date of site visit;
- group — test group (control — A or experimental — B);
- purchase — purchase indicator: did the user make a tour purchase (1 — yes, 0 — no);
- price — price of the purchased tour (if the purchase did not occur, the price is 0).

The company offers the following tour options (in the "price" category):

- Thailand — 100,000 rubles;
- Turkey — 60,000 rubles;
- Maldives — 200,000 rubles;
- St. Petersburg — 10,000 rubles;
- Kamchatka — 150,000 rubles.

### Project Workflow

1. Data structure analysis and preprocessing.
2. Calculation of key metrics for A/B tests.
3. Preliminary results.
4. Checking the stabilization of metrics.
5. Statistical analysis of A/B test results.
6. Conclusion: which landing page variant is more preferable in terms of conversion and daily average check.

### Results

Conversion-A generally remained higher than Conversion-B except for a few days in the middle when they converged. Then the metrics stabilized, but the difference between them turned out to be insignificant. Average check B consistently remains higher than the average check of group A, and over time, this difference became even more apparent. Check B, according to point tests, statistically significantly exceeds the average check in group A. The difference in conversions turned out to be insignificant.

In group A, more tours to Turkey were purchased, which is cheaper than Thailand, the preference of clients in the second group. This means that in group B, more expensive tours were sold.

### Conclusions

Changing the landing page to variant B makes sense if the company's goal is to increase the average check by shifting the focus from tours to Turkey to tours to Thailand. Such a change is possible, and the difference in the average check is noticeable and statistically significant. If the goal is to increase conversion, changing the landing page will not lead to the desired results, as the difference in conversion is not statistically significant, both in point and interval estimates.
