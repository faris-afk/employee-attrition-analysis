'''
====================================================
Milestone 7

Nama: Muhammad Fariz Firdaus
Batch: SBY002
Objective: This file was made to schedule a set of jobs that fetch the employee dataset, clean the dataset, and finally post the cleaned dataset into elastic search
====================================================
'''

import pandas as pd 
import psycopg2 as db
import numpy as np 
from elasticsearch import Elasticsearch

import datetime as dt  
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator 

def getData():
    '''
    Description:
        This function make a connection to the PostgreSQL database, and read data from postgres.
    
    Parameters:
        None
    
    Returns:
        None
    
    Usage Example:
        getData()
    '''

    # Define the connection string
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port=5432" 
    
    # Establish the connection
    conn = db.connect(conn_string)

    # Read to CSV
    df = pd.read_sql("select * from employee", conn)
    df.to_csv('/opt/airflow/data/P2M3_MuhammadFariz_data_fetched.csv', index=False)


def cleanData():
    '''
    Description:
        This function reads a CSV file into a pandas DataFrame, removes duplicates and null values, 
        and then writes the cleaned data back to a new CSV file.
    
    Parameters:
        None
    
    Returns:
        None
    
    Usage Example:
        cleanData()
    '''

    # Read the raw data
    df = pd.read_csv('/opt/airflow/data/P2M3_MuhammadFariz_data_fetched.csv', index_col=False)
    
    # Remove duplicates
    if df.duplicated().sum() > 0: df.drop_duplicates(inplace=True)
    
    # Remove null values
    if df.isnull().sum().sum() > 0: df.dropna(inplace=True)

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace whitespaces with underscores in column names
    df.columns = df.columns.str.replace(' ', '_')

    # List of columns to drop
    columns_to_drop = ['over18', '-2', '0', 'employee_count', 'standard_hours'] # These columns only has 1 unique values, so I will drop them as they don't give much information

    # Drop the specified columns
    df = df.drop(columns=columns_to_drop)
    
    # Write the cleaned data to a new CSV file
    df.to_csv('/opt/airflow/data/P2M3_MuhammadFariz_data_clean.csv', index=False)

def postData():
    '''
    Description:
        This function reads the cleaned data from a CSV file into a pandas DataFrame, 
        deletes the old data from the Elasticsearch index, 
        and then posts each row of the DataFrame as a document to the Elasticsearch index.
    
    Parameters:
        None
    
    Returns:
        None
    
    Usage Example:
        postData()
    '''

    # Read the cleaned data
    df = pd.read_csv('/opt/airflow/data/P2M3_MuhammadFariz_data_clean.csv', index_col=False)

    # Establish the connection to Elasticsearch
    es = Elasticsearch("Elasticsearch")
    es.ping()

    # Check if the "hr_data" index exists
    if es.indices.exists(index="hr_data"):
        # Delete all documents in the "hr_data" index
        es.delete_by_query(index="hr_data", body={"query": {"match_all": {}}})

    # Post each row of the DataFrame as a document to the Elasticsearch index
    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="hr_data", body=doc)

# Default arguments for the DAG
default_args = {
    'owner': 'Fariz',
    'start_date': dt.datetime(2024, 1, 11, 18, 25, 0) - dt.timedelta(hours=7) 
}

# Define the DAG
with DAG('hr_dag',
        default_args=default_args,
        schedule_interval='30 23 * * *',  # Run daily at 6:30 AM Jakarta time 
        catchup=False
        ) as dag:
    
    # Define the tasks in the DAG
    getdatatask = PythonOperator(task_id='getdatatask', python_callable=getData)
    cleandatatask = PythonOperator(task_id='cleandatatask', python_callable=cleanData)
    postdatatask = PythonOperator(task_id='postdatatask', python_callable=postData)

# Define the task dependencies
getdatatask >> cleandatatask >> postdatatask 