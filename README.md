# Employee Attrition Analysis

## Introduction
A client company is facing a problem with a 16% annual employee attrition rate, leading to reduced productivity, increased workload for remaining staff, and high costs associated with hiring and training new employees. This project aims to identify the employees leaving the company and understand why.

## Data Engineering Pipeline
The project uses a data pipeline built using **Airflow**. The pipeline consists of three main jobs:

1. **Fetch Data**: The first job fetches data from a **PostgreSQL** database, ensuring the most recent and relevant data is used for analysis.
2. **Clean Data**: The fetched data is then cleaned using a Python script, preparing it for further analysis.
3. **Post Data**: The cleaned data is posted to **Elasticsearch**, a powerful search and analytics engine.

This pipeline is scheduled to run weekly, ensuring the analysis is based on the most up-to-date data. The use of Airflow, PostgreSQL, and Elasticsearch highlights my skills in data engineering and management.

## Analysis
The analysis was conducted in **Kibana**, a data visualization and exploration tool connected to Elasticsearch. This allowed for interactive and real-time analysis of the data.

## Findings and Recommendations
### Based on Age
- **Findings**: Employees in the age group of 25 to 30 have the highest attrition rate.
- **Recommendations**: Maintain a youngster-friendly environment and implement mentorship programs to make them feel connected to the company.

### Based on Department
- **Findings**: The Sales Department has the highest attrition rate.
- **Recommendations**: Conduct a department-focused survey and review sales department policies based on the survey.

### Based on Job Roles
- **Findings**: Laboratory Technicians have the highest attrition rate.
- **Recommendations**: Invest more in their projects, providing challenging work and opportunities for them to improve their skills.

### Based on Job Satisfaction
- **Findings**: The lower the job satisfaction, the higher the attrition rate.
- **Recommendations**: Create a safe, supportive, and positive work environment. Research what resources, tools, and benefits matter the most to the employees to fulfill their expectations.

### Based on Work-Life Balance
- **Findings**: Employees struggling to balance their work and personal lives might seek employment elsewhere.
- **Recommendations**: Make better working arrangements, such as remote work or flexible working hours.

### Based on Salary
- **Findings**: Employees who leave have a lower average monthly income than those who stay.
- **Recommendations**: Offer a more competitive compensation based on trends in the industry or location. Offer performance-based rewards to make employees feel rewarded.

## Conclusion
Younger employees, specifically those in the age group of 20 to 30, are more likely to leave the company. In terms of job roles, sales roles, and lab technicians show the highest attrition rates. The data also shows that low job satisfaction, poor work-life balance, and lower income are significant factors contributing to attrition.

This project demonstrates the power of data engineering and analysis in addressing real-world business challenges and informing strategic decision-making.
