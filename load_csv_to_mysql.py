import os 
import pandas as pd 
from sqlalchemy import create_engine 

USERNAME = ""
PASSWORD = ""
HOST = ""
DATABASE = ""

engine = create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
)

DATA_FOLDER = "data"
#Note: The CSVs in the data folder are the datasets of Animal crossing that I got from kaggle 

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in csv_files:
    file_path = os.path.join(DATA_FOLDER, file)

    # EXTRACT
    df = pd.read_csv(file_path)

    # TRANSFORM (implicit)
    table_name = file.replace(".csv", "")

    # LOAD
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",  # replace / append
        index=False
    )

    print(f"Loaded {file} → table '{table_name}'")