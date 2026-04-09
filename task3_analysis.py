print("Task 3 - Analysis started")

import pandas as pd

# load csv file
file_path = "data/cleaned_trends.csv"

df = pd.read_csv(file_path)

print("CSV file read successfully")

# -------- analysis --------

# 1. count of posts per category
category_count = df["category"].value_counts()
print("\nPosts per category:")
print(category_count)

# 2. average score per category
avg_score = df.groupby("category")["score"].mean()
print("\nAverage score per category:")
print(avg_score)

# 3. top 5 posts by score
top_posts = df.sort_values(by="score", ascending=False).head(5)

print("\nTop 5 posts:")
print(top_posts[["title", "category", "score"]])