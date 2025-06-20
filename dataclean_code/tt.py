import sqlite3
import pandas as pd

conn = sqlite3.connect("../amazonreview_query\origin_dataset/review_query.db")

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

df = pd.read_sql("SELECT * FROM meta;", conn)
print(df.head())

conn.close()
