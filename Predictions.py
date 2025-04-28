import streamlit as st
import pandas as pd
import mysql.connector

# Function to connect to the database
def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="police_log"
    )

# Streamlit form for user input
with st.form("query_form"):
    st.subheader("📝 Add Police Log and Predict Outcome:")
    stop_date = st.date_input("Stop Date")
    stop_time = st.text_input("Stop Time", value="00:00:00")
    country_name = st.text_input("Country Name")
    driver_gender = st.selectbox("Driver Gender", ["M", "F"])
    driver_age = st.number_input("Driver Age", min_value=0, max_value=100, format="%d")
    driver_race = st.text_input("Driver Race")
    search_conducted = st.selectbox("Was Search Conducted?", ["1", "0"])
    search_type = st.text_input("Search Type")
    drugs_related_stop = st.selectbox("Was Drug Related?", ["1", "0"])
    stop_duration = st.selectbox("Stop Duration", ["0-15min", "16-30 Min", "30-60min", "30+ Min"])
    vehicle_number = st.text_input("Vehicle Number")
    click = st.form_submit_button("Predict Violation & Outcome")

if click:
    try:
        # Connect to the database
        mydb = db_connect()
        mycursor = mydb.cursor(buffered=True)

        # SQL query with placeholders for parameters
        qstring = """
            SELECT violation, stop_outcome 
            FROM cpolice1 
            WHERE stop_date = %s AND
                  stop_time = %s AND 
                  country_name = %s AND 
                  driver_gender = %s AND
                  driver_age = %s AND 
                  driver_race = %s AND
                  search_conducted = %s AND
                  search_type = %s AND 
                  drugs_related_stop = %s AND
                  stop_duration = %s AND 
                  vehicle_number = %s;
        """

        # Execute the query with parameters
        mycursor.execute(qstring, (
            stop_date.strftime("%Y-%m-%d"),  # Format date as string
            stop_time,  # Format time as string
            country_name,
            driver_gender,
            driver_age,
            driver_race,
            search_conducted,
            search_type,
            drugs_related_stop,
            stop_duration,
            vehicle_number
        ))
        
        # Fetch the result
        data = mycursor.fetchone()
        
        # Close the cursor and connection
        mycursor.close()
        mydb.close()

        # Display the result
        if data:
            violation, stop_outcome = data
            st.text(f"Predicted Violation: {violation}")
            st.text(f"Predicted Outcome: {stop_outcome}")
            st.write(f"""
                A {driver_age} year old {driver_gender} driver was stopped on 📅 {stop_date} at ⌚ {stop_time}.
                {search_type} was conducted and the stop was related to drugs ({drugs_related_stop}).
                The driver received a {stop_outcome}. The stop lasted for {stop_duration} with the 🚗 {vehicle_number} in {country_name}.
            """)
        else:
            st.warning("No matching records found.")

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")