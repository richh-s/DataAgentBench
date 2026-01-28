code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_v4Qs3F5BbtONXcuyiUrFTqZk, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_MzN91tOr8xrMKRPLFMLDuBal, 'r', encoding='utf-8') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize ratings
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
# Map purchase_id to book_id by replacing prefix
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Extract publication year from details using regex for 4-digit years
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    # find all 4-digit numbers
    matches = re.findall(r"(\d{4})", detail)
    for m in matches:
        y = int(m)
        if 1000 <= y <= 2023:
            return y
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Merge reviews with books on book_id
merged = rev_df.merge(books_df[['book_id','title','pub_year']], on='book_id', how='left', suffixes=('_rev','_book'))

# Keep only rows with pub_year and rating
merged = merged[merged['pub_year'].notna() & merged['rating'].notna()].copy()
merged['pub_year'] = merged['pub_year'].astype(int)

# Compute per-book average rating and ensure distinct books
book_avg = merged.groupby(['book_id','title','pub_year'], as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

# Compute decade string
book_avg['decade_start'] = (book_avg['pub_year'] // 10) * 10
book_avg['decade'] = book_avg['decade_start'].astype(int).astype(str) + 's'

# For each decade, count distinct books and compute average of per-book averages
decade_stats = book_avg.groupby('decade').agg(distinct_books=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
valid_decades = decade_stats[decade_stats['distinct_books'] >= 10]

if valid_decades.empty:
    result = None
else:
    # Find decade with highest average rating; if tie, pick the one with highest avg then smallest decade string
    best = valid_decades.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = best['decade']

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YLjPOkHQrNjMcLg8AQ0CN4zU': ['review'], 'var_call_PCJA205YfJGXnXYCx0XEM9Ol': ['books_info'], 'var_call_v4Qs3F5BbtONXcuyiUrFTqZk': 'file_storage/call_v4Qs3F5BbtONXcuyiUrFTqZk.json', 'var_call_MzN91tOr8xrMKRPLFMLDuBal': 'file_storage/call_MzN91tOr8xrMKRPLFMLDuBal.json'}

exec(code, env_args)
