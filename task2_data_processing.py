print("Task 2 - Data Processing started")

import pandas as pd
import os

# JSON file path (change date if needed)
file_path = "data/trends_20260409.json"

# check if file exists
if os.path.exists(file_path):

    print("Reading JSON file...")

    # load data into dataframe
    df = pd.read_json(file_path)

    # show sample data
    print(df.head())

    # -------- cleaning --------

    # remove rows where title or category is missing
    df = df.dropna(subset=["title", "category"])

    # remove duplicate rows
    df = df.drop_duplicates()

    print("Cleaning completed")

    # -------- save CSV --------

    csv_file_path = "data/cleaned_trends.csv"

    df.to_csv(csv_file_path, index=False)

    print("CSV file saved")

    # show total rows
    print("Total records:", len(df))

else:
    print("File not found. Check file path.")