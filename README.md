# Police Post Log
Digital Ledger for Police Post Logs
    This project aim to streamline vehicle logging and tracking at police check posts.With Streamlite dashboard helps to Predict the insights about datasets and outcome of the violations. 
1. Main.py contains 2 tabs. First tab displays Raw dataset and Second Tab represent Prerequisite or cleaned data from the raw dataset. Cleaning is done by checking for NAN/Null 
   values,striping of whitespaces from strings,Stop_date column is converted into standardized date format, converted boolean columns to string format.this helps to clean 
   dataset and it is displayed as tabular form in streamlit. This tabular format is downloaded using download button and saved as csv file(Ctrafficdata1.csv) with formatted 
   date.
2. Establish db connection and use the CSV file as input and insert the cleaned data into db using insert query by specifying placeholder values by mapping pandas datatype with
   MYSQL datatype.The table is created and the data are inserted baased on columns and datatype.
3. Once the table CPolice1 is created. Simple and complex queries are written and it is displayed in streamlit using selection box.
4. A input form is created to fill the necessary details like stop_date,stop_time,driver_age,race and prediction is made based on the input from the form. ie. This gives
   the prediction about violation and outcome of the violation and the summary is displayed based on the form and predicted values.
5. Using matplotlib.pyplot a graph is plotted against violation and its count.
