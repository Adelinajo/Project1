import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

# df=pd.read_csv(r"C:\Users\sugan\Downloads\ctrafficdata1.csv")
# if df.isnull().any().any():
#         st.write("There are missing values in the file.")
#         st.write("Missing Values Count by Column:")
#         st.write(df.isnull().sum())
# else:
#         st.write("✅ No missing values detected!")


# Database connection
db_connection = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="12345",  
    database="police_log"  
)

cursor = db_connection.cursor()

# Path to the CSV file
csv_file_path = r"C:\Users\sugan\Downloads\Ctrafficdata1.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Function to map Pandas dtypes to MySQL data types
def map_dtype_to_sql(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "DATETIME"

    else:
        return "VARCHAR(255)"  # Default to VARCHAR for strings or unknown types

# Generate the CREATE TABLE query dynamically based on the CSV columns and datatypes
table_name = "cpolice1"
columns = ", ".join([f"{col} {map_dtype_to_sql(dtype)}" for col, dtype in zip(data.columns, data.dtypes)])

create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
cursor.execute(create_table_query)

# Insert data into the table
for _, row in data.iterrows():
    placeholders = ", ".join(["%s"] * len(row))
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(row))

# Commit the transaction and close the connection
db_connection.commit()
cursor.close()
db_connection.close()

print("Data uploaded successfully!")