print("Task 2 - Data Processing started")

import pandas as pd
import os

# file path (change date if needed)
file_path = "data/trends_20260409.json"

# check file exists
if not os.path.exists(file_path):
    print("File not found")
else:
    # load json
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from file")

    # -------- cleaning --------

    # 1. remove duplicates based on post_id
    df = df.drop_duplicates(subset=["post_id"])
    print("After removing duplicates:", len(df))

    # 2. remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print("After removing nulls:", len(df))

    # 3. fix data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # 4. remove low quality (score < 5)
    df = df[df["score"] >= 5]
    print("After removing low scores:", len(df))

    # 5. remove extra spaces in title
    df["title"] = df["title"].str.strip()

    print("Cleaning completed")

    # -------- save csv --------

    output_path = "data/trends_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} rows to {output_path}")

    # -------- summary --------

    print("\nStories per category:")
    print(df["category"].value_counts())
