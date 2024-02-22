# Statistical Tests in the Context of Salary Analysis in Data Science

## Table of Contents
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results
6. Conclusions

### Project Description

An HR agency is studying labor market trends in IT. The company wants to conduct research based on salary data in the Data Science field from 2020 to 2022 and draw some conclusions.

### Problem Statement

Answer questions regarding Data Science vacancies and determine if the statistically obtained answers are significant:

- Is there an annual increase in salaries for Data Scientists?
- Does work experience ('experience_level') influence the salary of Data Scientists?
- Does employment type ('employment_type') impact the salary of Data Scientists?
- Does the proportion of remote work ('remote_ratio') affect the salary of Data Scientists?
- Does the company size ('company_size') influence the salary of Data Scientists?
- Does the employee's location (same region as the employer or not) impact their salary?
- Does the employee's location influence the amount of remote work?
- How do salaries of Data Scientists and Data Engineers in different companies compare?
- Is there a correlation between the presence of Data Scientist and Data Engineer positions and the company size?

**Practiced Techniques:**
Statistical data analysis, hypothesis testing, tests for normality.

### Brief Data Overview

Original dataset: “Data Science Job Salaries” (kaggle.com)

Table:
- work_year: The year in which the salary was paid.
- experience_level: Work experience in years with possible values: EN (Entry-level/Junior), MI (Mid-level/Intermediate), SE (Senior-level/Expert), EX (Executive-level/Director).
- employment_type: Employment type for the role: PT (part-time), FT (full-time), CT (contract), FL (freelance).
- job_title: Role in which the applicant worked during the year.
- salary: Total gross salary paid.
- salary_currency: Currency of the salary in ISO 4217 currency code.
- salary_in_usd: Salary in US dollars (exchange rate divided by the average USD exchange rate for the corresponding year).
- employee_residence: Employee's main country of residence during the working year in ISO 3166 country code.
- remote_ratio: Overall volume of remote work: 0 (no remote work, less than 20%), 50 (partially remote work), 100 (fully remote work, more than 80%).
- company_location: Country of the employer's main office or branch by contract in ISO 3166 country code.
- company_size: Average number of people working in the company during the year: S (less than 50 employees), M (50 to 250 employees), L (more than 250 employees).

### Project Workflow
1. Exploratory Data Analysis (EDA)
2. Statistical Data Analysis

### Results

- **Is there an annual increase in salaries for Data Scientists?**
  Salary varies from year to year, but there is no clear growth from 2020 to 2021. However, there is a noticeable increase in Data Science salaries from 2021 to 2022.

- **Does work experience ('experience_level') influence the salary of Data Scientists?**
  As the level of expertise in Data Science increases, salaries of specialists indeed grow.

- **Does employment type ('employment_type') impact the salary of Data Scientists?**
  It can be confidently stated that for full-time and part-time employment, salaries differ, with lower salaries for part-time employment. No definite conclusion can be drawn for other types of employment.

- **Does the proportion of remote work ('remote_ratio') affect the salary of Data Scientists?**
  It can be concluded that the volume of remote work is indeed related to the salary, but the relationship is nonlinear. The highest salaries are observed for those working 100% remotely, followed by those with minimal remote work. Employees with half of their work remote have the lowest salary.

- **Does the company size ('company_size') influence the salary of Data Scientists?**
  It can be concluded that the company size does influence employee salaries. Small companies pay less than medium and large ones. However, it is uncertain which size between M (50-250 employees) and L (more than 250 employees) leads in terms of salaries.

- **Does the employee's location (same region as the employer or not) impact their salary?**
  Indeed, if the company and the employee are located in the same region, the employee may receive a higher salary compared to when they are in different regions.

- **Does the employee's location influence the amount of remote work?**
  There is no statistically significant correlation between the employee's location relative to the employer and the amount of remote work.

- **How do salaries of Data Scientist and Data Engineer in different companies compare?**
  Salaries in the fields of Data Scientist and Data Engineer do not show statistically significant differences.

- **Is there a correlation between the presence of Data Scientist and Data Engineer positions and the company size?**
  There is no statistically significant correlation between the presence of Data Scientist and Data Engineer positions and the company size.

### Conclusions

Successfully answered each question and assessed the statistical significance of the initial responses.