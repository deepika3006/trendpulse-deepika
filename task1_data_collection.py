# Starting message
print("Starting TrendPulse Task 1...")

import requests
import json
import os
import time
from datetime import datetime

# API links
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# header for request
headers = {"User-Agent": "TrendPulse/1.0"}

# categories with keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# function to find category
def get_category(title):
    title = title.lower()
    for cat in categories:
        for word in categories[cat]:
            if word in title:
                return cat
    return None


# get top story ids
try:
    response = requests.get(top_stories_url, headers=headers)
    all_ids = response.json()[:500]
except:
    print("Error while getting story ids")
    all_ids = []

# list to store final data
my_final_data = []

# count how many per category
count = {c: 0 for c in categories}

print("Getting Data from API")

# loop through ids
for sid in all_ids:
    try:
        res = requests.get(item_url.format(sid), headers=headers)
        story = res.json()

        # skip if no title
        if not story or "title" not in story:
            continue

        # find category
        cat = get_category(story["title"])

        # check limit
        if cat is None:
             cat = "technology"   # default category

        if count[cat] < 40:

            one_story = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": cat,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            my_final_data.append(one_story)
            count[cat] += 1

    except:
        print("Error in story:", sid)
        continue

    # stop when all categories full
    if len(my_final_data) >= 150:
        break
# small delay (requirement)
time.sleep(2)

# create data folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# file name with date
file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

# save file
with open(file_name, "w") as f:
    json.dump(my_final_data, f, indent=4)

print("Done collecting stories")
print("Total stories:", len(my_final_data))
print("Saved to:", file_name)