import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector     



db_connection = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="12345",  
    database="police_log"  
)
cursor = db_connection.cursor()

query="SELECT violation, COUNT(*)AS count FROM `cpolice1` group by stop_outcome,violation"
#query = "SELECT violation,COUNT(*) as count FROM cpolice1 GROUP BY violation;"
cursor.execute(query)

data =pd.DataFrame(cursor.fetchall(),columns=["violation", "count"])

st.dataframe(data)
cursor.close()
db_connection.close()


# category_column = st.selectbox("Select the category column (x-axis):", df.columns)
# value_column = st.selectbox("Select the value column (y-axis):", df.columns)




st.title("Violation Rates vs Count ")

#plt.scatter(df['violation'],df['stop_time'],cmap='viridis', s=100, alpha=0.5)

#plt.bar(s, df['stop_time'], align='edge', alpha=0.8, width=0.8, hatch='*')
plt.figure(figsize=(8, 5)) 

plt.bar(data["violation"],data["count"], color="pink")
plt.xticks(rotation=45) 
plt.tight_layout()

plt.xlabel('violation')
plt.ylabel('count')
plt.title('violation Rates vs count')
plt.legend(["violation Rates"])
st.pyplot(plt)
plt.close()