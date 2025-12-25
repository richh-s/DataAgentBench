import os
from datasets import load_dataset
import random
import datetime
import pandas as pd
from faker import Faker

# ===============================
# Paths
# ===============================

PARQUET_PATH = os.path.join("/home/ruiying/DataAgentBench/query_agnews", "agnews_gt.parquet")

AUTHORS = list(set([
    Faker().name() for i in range(1000)
]))
print("Generated", len(AUTHORS), "unique author names.")

REGIONS = ["North America", "Europe", "Asia", "Africa", "South America"]

def random_publication_date():
    year = random.randint(2004, 2022)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    return datetime.date(year, month, day).isoformat()

# ===============================
# Load AGNews and union train + test
# ===============================

dataset = load_dataset("sh0416/ag_news")
train = dataset["train"]
test = dataset["test"]

combined = []
current_id = 0

for split_name, split_data in [("train", train), ("test", test)]:
    for item in split_data:
        author_id = random.randint(0, len(AUTHORS) - 1)
        combined.append({
            "article_id": current_id,
            "label": item["label"], # 1: World 2: Sports 3: Business 4: Sci/Tech
            "split": split_name,
            "title": item["title"],
            "author_id": author_id,
            "author_name": AUTHORS[author_id],
            "publication_date": random_publication_date(),
            "region": random.choice(REGIONS),
            "description": item["description"],   # preserved raw text
        })
        current_id += 1


# store in parquet for easy querying
df = pd.DataFrame(combined)
df.to_parquet(PARQUET_PATH, index=False)
# print the first few rows
print(df.head(n=5))