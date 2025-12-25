import sqlite3
import pandas as pd
import numpy as np
import os

SEED = 42
np.random.seed(SEED)

RAW_CSV = "/home/ruiying/DataAgentBench/query_music_brainz_20k/musicbrainz-20-A01.csv"
SQLITE_DB = "/home/ruiying/DataAgentBench/query_music_brainz_20k/query_dataset/tracks.db"

os.makedirs(os.path.dirname(SQLITE_DB), exist_ok=True)

df = pd.read_csv(RAW_CSV)

sqlite_conn = sqlite3.connect(SQLITE_DB)
cur = sqlite_conn.cursor()

cur.execute("""
CREATE TABLE tracks (
    track_id INTEGER PRIMARY KEY,
    source_id INTEGER,
    source_track_id TEXT,
    title TEXT,
    artist TEXT,
    album TEXT,
    year TEXT,
    length TEXT,
    language TEXT
)
""")

for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO tracks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        int(row["TID"]),
        int(row["SourceID"]),
        row["id"],
        row["title"],
        row["artist"],
        row["album"],
        row["year"],
        row["length"],
        row["language"]
    ))

sqlite_conn.commit()
sqlite_conn.close()

import duckdb

DUCKDB_DB = "/home/ruiying/DataAgentBench/query_music_brainz_20k/query_dataset/sales.duckdb"
os.makedirs(os.path.dirname(DUCKDB_DB), exist_ok=True)

duck = duckdb.connect(DUCKDB_DB)

duck.execute("""
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    track_id INTEGER,
    country TEXT,
    store TEXT,
    units_sold INTEGER,
    revenue_usd DOUBLE
)
""")

countries = ["USA", "UK", "Canada", "Germany", "France"]
stores = ["iTunes", "Spotify", "Apple Music", "Amazon Music", "Google Play"]

sales_rows = []
sale_id = 1

for tid in df["TID"]:
    for _ in range(np.random.randint(1, 6)):
        units = np.random.randint(1, 500)
        sales_rows.append((
            sale_id,
            int(tid),
            np.random.choice(countries),
            np.random.choice(stores),
            units,
            round(units * np.random.uniform(0.99, 1.29), 2)
        ))
        sale_id += 1

sales_df = pd.DataFrame(
    sales_rows,
    columns=[
        "sale_id",
        "track_id",
        "country",
        "store",
        "units_sold",
        "revenue_usd"
    ]
)

duck.register("sales_df", sales_df)

duck.execute("""
INSERT INTO sales
SELECT * FROM sales_df
""")
