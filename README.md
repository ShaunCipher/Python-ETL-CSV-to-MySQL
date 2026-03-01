# Python-ETL-CSV-to-MySQL

Python ETL (Extract-Transform-Load) scripts to extract data from CSV files, transform it as needed, and load it into a MySQL database. This repository demonstrates a simple workflow for handling CSV data and automating database insertion.

# Note to User

1. Upload your csv files to the data folder (and delete my sample csv files)
2. Run the script inside the requirements.txt
3. Input your username, password, host, and database 

# Algorithm

1. Import required modules
Import os for file handling, pandas for data processing, and sqlalchemy for database connectivity.

2. Define database connection credentials
Specify the MySQL username, password, host, and database name.

3. Create a database engine
Initialize a SQLAlchemy engine to establish a connection to the MySQL database.

4. Specify the folder containing CSV files
Set the path of the directory where the CSV files are stored.

5. List all CSV files in the folder
Retrieve all filenames ending with .csv from the specified directory.

6. Iterate through each CSV file
Loop through the list of CSV files one by one.

7. Read each CSV file into a DataFrame
Use pandas.read_csv() to load the CSV file into memory.

8. Generate the table name
Derive the MySQL table name from the CSV filename (remove .csv).

9. Load the DataFrame into MySQL
Use DataFrame.to_sql() to write the data into MySQL
- Replace the table if it already exists
- Do not include the DataFrame index

10. Print a confirmation message
Display a message in the terminal indicating that the file was successfully loaded.

## ⚖️ License & Copyright
© 2026 Charlene Jusgado / ShaunCipher. All rights reserved.  
**Viewing allowed, copying or reuse prohibited.**
