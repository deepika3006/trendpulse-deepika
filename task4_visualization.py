print("Task 4 - Visualization started")

import pandas as pd
import matplotlib.pyplot as plt

# load data
file_path = "data/cleaned_trends.csv"
df = pd.read_csv(file_path)

print("Data ready")

# graph 1
category_count = df["category"].value_counts()

plt.figure()
category_count.plot(kind="bar")
plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Count")

# graph 2
avg_score = df.groupby("category")["score"].mean()

plt.figure()
avg_score.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Score")

plt.show()

