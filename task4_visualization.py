print("Task 4 - Visualization started")

import pandas as pd
import matplotlib.pyplot as plt
import os

# load data
file_path = "data/trends_analysed.csv"

if not os.path.exists(file_path):
    print("File not found")
    exit()

df = pd.read_csv(file_path)
print("Data loaded")

# create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------- Chart 1 --------
try:
    top10 = df.sort_values(by="score", ascending=False).head(10)

    top10["title"] = top10["title"].apply(
        lambda x: x[:50] + "..." if len(x) > 50 else x
    )

    plt.figure()
    plt.barh(top10["title"], top10["score"])
    plt.title("Top 10 Stories by Score")
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.gca().invert_yaxis()

    plt.savefig("outputs/chart1_top_stories.png")
    print("Chart 1 saved")

except Exception as e:
    print("Error in chart 1:", e)

# -------- Chart 2 --------
try:
    category_count = df["category"].value_counts()

    plt.figure()
    category_count.plot(kind="bar")
    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig("outputs/chart2_categories.png")
    print("Chart 2 saved")

except Exception as e:
    print("Error in chart 2:", e)

# -------- Chart 3 --------
try:
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure()
    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

    plt.title("Score vs Comments")
    plt.xlabel("Score")
    plt.ylabel("Comments")
    plt.legend()

    plt.savefig("outputs/chart3_scatter.png")
    print("Chart 3 saved")

except Exception as e:
    print("Error in chart 3:", e)

# -------- Dashboard --------
try:
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    axes[0, 0].barh(top10["title"], top10["score"])
    axes[0, 0].set_title("Top Stories")
    axes[0, 0].invert_yaxis()

    axes[0, 1].bar(category_count.index, category_count.values)
    axes[0, 1].set_title("Categories")

    axes[1, 0].scatter(popular["score"], popular["num_comments"])
    axes[1, 0].set_title("Score vs Comments")

    axes[1, 1].axis("off")

    fig.suptitle("TrendPulse Dashboard")

    plt.tight_layout()
    plt.savefig("outputs/dashboard.png")

    print("Dashboard saved")

except Exception as e:
    print("Error in dashboard:", e)

plt.show()

print("All done")
