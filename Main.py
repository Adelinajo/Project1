import streamlit as st
import pandas as pd



# Set up the Streamlit app
st.header("Police Log Project")
options = st.sidebar.radio("Go to", ["Dataset","Prerequisite Dataset"])

# Home page

if options == "Dataset":
       st.subheader(" RAW DATASET")
       df=pd.read_csv(r"C:\Users\sugan\Downloads\ctraffic_stops.csv")
       st.write(df)

      
if options == "Prerequisite Dataset": 
       st.subheader("CLEANED DATASET")
    
       df=pd.read_csv(r"C:\Users\sugan\Downloads\ctraffic_stops.csv")

       df["stop_date"] = pd.to_datetime(df["stop_date"]).dt.strftime("%Y-%m-%d") 
       
       boolean_columns = ['search_conducted','is_arrested','drugs_related_stop']
       df[boolean_columns] = df[boolean_columns].astype(str)  # Convert  boolean to string formatting
       df = df.dropna(subset=['search_type'])
  
       # Remove columns with all NaN or whitespace-only values
       df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Strip whitespace from strings
       df = df.dropna(axis=1, how='all')  # Drop columns where all values are NaN
       df = df.loc[:, (df != '').any(axis=0)] 


      
       st.write(df)
       df_csv=df.to_csv(index=False,date_format="%Y-%m-%d").encode('utf-8')
       st.subheader("Download Cleaned Dataset")
       st.download_button(
       label="Download CSV",
       data=df_csv,
       file_name="Ctrafficdata1.csv",
       mime="text/csv"
)
