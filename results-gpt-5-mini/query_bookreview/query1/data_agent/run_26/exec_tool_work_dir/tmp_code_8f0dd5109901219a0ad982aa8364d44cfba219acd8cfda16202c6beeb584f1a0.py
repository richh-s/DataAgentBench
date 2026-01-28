code = """import json
import re
import pandas as pd

# Load data from previous query results
# Variables provided by tool results
books_path = var_call_QSjyrvIxhBlGVpdirNH7y338
reviews_path = var_call_S2ZqOFWrtqE48XpYvJwhEpwl

# helper to load
def load_json(path_or_obj):
    if isinstance(path_or_obj, str):
        # path to json file
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

books = load_json(books_path)
reviews = load_json(reviews_path)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Extract numeric id
def extract_num_id(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)$", str(s))
    return int(m.group(1)) if m else None

df_books['num_id'] = df_books['book_id'].apply(extract_num_id)
df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num_id)

# Convert rating to float
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Merge on num_id
df_merged = pd.merge(df_reviews, df_books, on='num_id', how='inner', suffixes=('_rev','_book'))

# Extract year from details (first 4-digit year between 1000 and 2099)
def extract_year(text):
    if pd.isna(text):
        return None
    m = re.search(r"(19|20)\d{2}", str(text))
    return int(m.group(0)) if m else None

# Try details then description then categories
if 'details' in df_merged.columns:
    df_merged['year'] = df_merged['details'].apply(extract_year)
else:
    df_merged['year'] = None

# For missing years, try description
mask_missing = df_merged['year'].isna()
if mask_missing.any():
    df_merged.loc[mask_missing, 'year'] = df_merged.loc[mask_missing, 'description'].apply(extract_year)

# If still missing, try categories and book_id etc
mask_missing = df_merged['year'].isna()
if mask_missing.any():
    df_merged.loc[mask_missing, 'year'] = df_merged.loc[mask_missing, 'categories'].apply(extract_year)

# Drop rows without year or without rating
df_merged = df_merged.dropna(subset=['year','rating','book_id'])

df_merged['year'] = df_merged['year'].astype(int)
# Determine decade label
df_merged['decade'] = df_merged['year'].apply(lambda y: f"{(y//10)*10}s")

# Compute per-book average rating
book_avg = df_merged.groupby('book_id').agg({'rating':'mean','decade':'first'}).reset_index()
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# For each decade, compute number of distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(book_count=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count']>=10]

result = None
if not decade_stats_filtered.empty:
    top = decade_stats_filtered.sort_values(['decade_avg_rating','decade'], ascending=[False,True]).iloc[0]
    result = {
        'decade': top['decade'],
        'average_rating': round(float(top['decade_avg_rating']),4),
        'book_count': int(top['book_count'])
    }
else:
    result = {'error': 'No decade has at least 10 distinct rated books.'}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QSjyrvIxhBlGVpdirNH7y338': 'file_storage/call_QSjyrvIxhBlGVpdirNH7y338.json', 'var_call_WQ716E3yupAX7m0B03ev6lB0': ['review'], 'var_call_S2ZqOFWrtqE48XpYvJwhEpwl': 'file_storage/call_S2ZqOFWrtqE48XpYvJwhEpwl.json'}

exec(code, env_args)
