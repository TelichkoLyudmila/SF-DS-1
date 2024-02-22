# 2. Analysis of HH Vacancies using Python, SQL

## Table of Contents  
1. Project Description
2. Problem Statement
3. Brief Data Overview 
4. Project Workflow
5. Results 
6. Conclusions

### Project Description    
It is necessary to connect to the database (DB) and retrieve all information about HH vacancies. PostgreSQL integrated into Python using the Pandas library was used for database connection. After retrieving the data, their analysis was conducted with a focus on DS-related vacancies.

### Problem Statement    
1. Preliminary data analysis
2. Detailed data analysis
3. Employers' analysis
4. Subject analysis
5. Additional analysis

**Competition Conditions:**  
The data in the DB is not structured, and queries need to be wrapped around them to get results suitable for analysis.

**Quality Metric**     
Conclusions can be drawn about vacancies and employers presented on HH.

**Practiced Techniques**     
Learn to use SQL in working with a database, integrating queries into VS.

### Brief Data Overview
SkillFactory DB

### Project Workflow  
1. Preliminary data analysis (familiarization with quantitative features of available data columns)
2. Detailed data analysis (deepening the understanding of salary and experience concepts)
3. Employers' analysis (highlighting tops, regional and industrial coverage, using API)
4. Subject analysis (analysis with a focus on DS vacancies)
5. Additional analysis (additional research beyond the required)

### Results:  
Data has been retrieved using queries, available for analysis. Conclusions have been made about qualitative and quantitative metrics, including a focus on DS.

### Conclusions:  
Most employers prefer employees to be present in the office. Despite the fact that DS work can be completely remote, more than 60% of vacancies in this area imply the presence of employees in the office. At first glance, this applies to young specialists without experience, but no, among 319 vacancies in DS for full-time and full day, only 33 vacancies are for juniors.

On average across all vacancies, employers are looking for specialists with a salary of about 100 thousand, among DS, the average salary is significantly higher (over 170 thousand), and there is a growth corresponding to the increase in experience.

In general, 90% of vacancies indicate the expected salary, but among DS vacancies, only a third indicate the salary range.

The TOP-3 areas of activity by the number of vacancies (which is half of the entire database) are somehow related to the IT sector. The first place is software development (12.5 thousand vacancies).