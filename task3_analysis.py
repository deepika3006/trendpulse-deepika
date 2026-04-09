print("Task 3 - Analysis started")

import pandas as pd
import numpy as np

# load csv file
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

# -------- basic info --------

print("Data loaded:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

# average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", avg_score)
print("Average comments:", avg_comments)

# -------- numpy analysis --------

print("\n--- NumPy Stats ---")

scores = df["score"].values

print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))

print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# category with most stories
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print("\nMost stories in:", top_category, "(", count, "stories )")

# most commented story
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(max_comments_row["title"], "-", max_comments_row["num_comments"], "comments")

# -------- new columns --------

# engagement = comments per score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = score > average
df["is_popular"] = df["score"] > avg_score

print("\nNew columns added")

# -------- save file --------

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print("Saved to", output_file)
