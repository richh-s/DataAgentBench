import os
import sqlite3
from bson import encode
import pandas as pd
import os

# Read the dataset from the parquet file
PARQUET_PATH = "/home/ruiying/DataAgentBench/query_agnews/agnews_gt.parquet"
df = pd.read_parquet(PARQUET_PATH)

DATASET_FOLDER = "/home/ruiying/DataAgentBench/query_agnews/query_dataset"
os.makedirs(DATASET_FOLDER, exist_ok=True)

# Create dump as bson for MongoDB
# db_name: articles_db
BSON_PATH = os.path.join(DATASET_FOLDER, "agnews_articles", "articles_db", "articles.bson")
os.makedirs(os.path.dirname(BSON_PATH), exist_ok=True)
with open(BSON_PATH, "wb") as f:
    cnt = 0
    for _, row in df.iterrows():
        doc = {
            "article_id": int(row["article_id"]),
            "title": row["title"],
            "description": row["description"],
        }
        cnt += 1
        f.write(encode(doc))

print(f"BSON file written: {BSON_PATH}")
print(f"Total articles written: {cnt}")

# Create SQLite database (3 tables)

SQLITE_PATH = os.path.join(DATASET_FOLDER, "metadata.db")

assert not os.path.exists(SQLITE_PATH), "SQLite database already exists!"

# -------------------------------------------------------------
# SETUP SQLITE
# -------------------------------------------------------------
conn = sqlite3.connect(SQLITE_PATH)
cur = conn.cursor()

# Create a table for authors
cur.execute("""
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY,
    name TEXT
);
""")
conn.commit()
# Populate authors table
author_set = set()
for _, row in df.iterrows():
    author_id = int(row["author_id"])
    author_name = row["author_name"]
    if author_id not in author_set:
        cur.execute("INSERT INTO authors (author_id, name) VALUES (?, ?)", (author_id, author_name))
        author_set.add(author_id)
conn.commit()
print(f"Inserted {len(author_set)} authors into authors table.")

# Create a table for article metadata
cur.execute("""
CREATE TABLE article_metadata (
    article_id INTEGER PRIMARY KEY,
    author_id INTEGER,
    region TEXT,
    publication_date TEXT,
    FOREIGN KEY(author_id) REFERENCES authors(author_id)
);
""")
conn.commit()
# Populate article_metadata table
for _, row in df.iterrows():
    article_id = int(row["article_id"])
    author_id = int(row["author_id"])
    region = row["region"]
    publication_date = row["publication_date"]
    cur.execute("""
    INSERT INTO article_metadata (article_id, author_id, region, publication_date)
    VALUES (?, ?, ?, ?)
    """, (article_id, author_id, region, publication_date))
conn.commit()
print(f"Inserted {len(df)} records into article_metadata table.")
conn.close()
print(f"SQLite database created at: {SQLITE_PATH}")

