code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
books_path = var_call_40qGCZ5IEKOsg5pLcJ75aSst
reviews_path = var_call_9Hex92PY7nyl8SS105tzdu8k

with open(books_path, 'r', encoding='utf-8') as f:
    books_data = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Normalize ratings
reviews_df = reviews_df[reviews_df['rating'].notnull()].copy()
# Sometimes rating is string; convert to float
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df = reviews_df[reviews_df['rating'].notnull()]

# Map purchase_id -> book_id by numeric suffix
reviews_df['num'] = reviews_df['purchase_id'].astype(str).str.extract(r"(\d+)")[0]
reviews_df['book_id'] = 'bookid_' + reviews_df['num'].fillna('')

# Compute per-book average rating
book_avg = reviews_df.groupby('book_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

# Extract year from books details
def extract_year(s):
    if not isinstance(s, str):
        return None
    # find first 4-digit year between 1500 and 2023
    m = re.search(r"\b(1[5-9][0-9]{2}|20[0-2][0-9]|2023)\b", s)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
# Merge book averages with books
merged = pd.merge(book_avg, books_df[['book_id','year']], on='book_id', how='left')
# Keep only books with a year
merged = merged[merged['year'].notnull()].copy()
merged['year'] = merged['year'].astype(int)
# Compute decade label
merged['decade_start'] = (merged['year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# For each decade, require at least 10 distinct books that have been rated
decade_stats = merged.groupby('decade').agg(
    book_count=('book_id','nunique'),
    mean_avg_rating=('avg_rating','mean')
).reset_index()

# Filter decades with at least 10 books
eligible = decade_stats[decade_stats['book_count'] >= 10].copy()

if eligible.empty:
    result = None
else:
    # decade with highest mean_avg_rating
    best = eligible.sort_values(['mean_avg_rating','decade'], ascending=[False,True]).iloc[0]
    result = {
        'decade': best['decade'],
        'mean_average_rating': round(float(best['mean_avg_rating']), 4),
        'book_count': int(best['book_count'])
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hxniLgkKvNVs6sApUYyYlH9i': ['review'], 'var_call_NIvvehNbMU4MTBvM30GcjH7g': ['books_info'], 'var_call_40qGCZ5IEKOsg5pLcJ75aSst': 'file_storage/call_40qGCZ5IEKOsg5pLcJ75aSst.json', 'var_call_9Hex92PY7nyl8SS105tzdu8k': 'file_storage/call_9Hex92PY7nyl8SS105tzdu8k.json'}

exec(code, env_args)
