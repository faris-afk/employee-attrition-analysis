'''
====================================================
Milestone 7

Nama: Muhammad Fariz Firdaus
Batch: SBY002
Objective: This file was made to create a table in a postgre database, then insert the employee dataset into it.
====================================================
'''


-- Start a transaction
BEGIN;

-- Create a new table
CREATE TABLE employee (
    Attrition VARCHAR(255),
    "Business Travel" VARCHAR(255),
    "CF_age band" VARCHAR(255),
    "CF_attrition label" VARCHAR(255),
    Department VARCHAR(255),
    "Education Field" VARCHAR(255),
    "emp no" VARCHAR(255),
    "Employee Number" INT,
    Gender VARCHAR(255),
    "Job Role" VARCHAR(255),
    "Marital Status" VARCHAR(255),
    "Over Time" VARCHAR(255),
    Over18 VARCHAR(255),
    "Training Times Last Year" INT,
    "-2" INT,
    "0" INT,
    Age INT,
    "CF_current Employee" INT,
    "Daily Rate" INT,
    "Distance From Home" INT,
    Education VARCHAR(255),
    "Employee Count" INT,
    "Environment Satisfaction" INT,
    "Hourly Rate" INT,
    "Job Involvement" INT,
    "Job Level" INT,
    "Job Satisfaction" INT,
    "Monthly Income" INT,
    "Monthly Rate" INT,
    "Num Companies Worked" INT,
    "Percent Salary Hike" INT,
    "Performance Rating" INT,
    "Relationship Satisfaction" INT,
    "Standard Hours" INT,
    "Stock Option Level" INT,
    "Total Working Years" INT,
    "Work Life Balance" INT,
    "Years At Company" INT,
    "Years In Current Role" INT,
    "Years Since Last Promotion" INT,
    "Years With Curr Manager" INT
);

-- Insert data from a CSV file into the table
COPY employee 
FROM 'C:\Users\FARIS\Documents\GitHub\milestone\p2-ftds002-sby-m3-faris-afk\airflow\data\P2M3_MuhammadFariz_data_raw.csv'
DELIMITER ','
CSV HEADER;

-- Commit the transaction
COMMIT;