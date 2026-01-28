code = """import json
import pandas as pd
import re

# Load data from provided storage file paths
books_path = var_call_HrC8RRaITuE7rMfCQQq0jjdd
reviews_path = var_call_DORTvLmFhd2KKB1furIDd2XD

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize ratings to float
# Some ratings may be strings
df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()
try:
    df_reviews['rating'] = df_reviews['rating'].astype(float)
except:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Map purchase_id -> book_id by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')
else:
    df_reviews['book_id'] = None

# Extract year from details in books
year_list = []
for txt in df_books['details'].astype(str):
    years = re.findall(r"\b(\d{4})\b", txt)
    year = None
    for y in years:
        yi = int(y)
        if 1000 <= yi <= 2023:
            year = yi
            break
    year_list.append(year)

df_books['year'] = year_list

# Keep only books with a valid year
df_books_valid = df_books[df_books['year'].notnull()].copy()

# Compute per-book mean rating using reviews joined by book_id
# Only consider reviews with matching book_id present in books
merged = pd.merge(df_reviews, df_books_valid[['book_id','year']], on='book_id', how='inner')

# Compute per-book mean rating
book_means = merged.groupby('book_id', as_index=False).agg({'rating':'mean', 'year':'first'})
book_means.rename(columns={'rating':'mean_rating'}, inplace=True)

# Compute decade
book_means['decade_start'] = (book_means['year'] // 10) * 10
book_means['decade'] = book_means['decade_start'].astype(int).astype(str) + 's'

# Aggregate by decade: count distinct books and average of per-book mean ratings
decade_stats = book_means.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('mean_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10].copy()

# If none meet threshold, return empty
if decade_stats_filtered.empty:
    result = {'decade': None, 'average_rating': None, 'book_count': 0}
else:
    # Find decade with highest average rating; if tie, take the one with more books then lexicographically
    best = decade_stats_filtered.sort_values(['avg_rating','book_count','decade'], ascending=[False,False,True]).iloc[0]
    result = {'decade': best['decade'], 'average_rating': round(float(best['avg_rating']), 4), 'book_count': int(best['book_count'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YWZpvWKF1QbXS0qUsFALVbSm': ['books_info'], 'var_call_i05rlnL0fLX8K3aiJP4gekvf': ['review'], 'var_call_HrC8RRaITuE7rMfCQQq0jjdd': 'file_storage/call_HrC8RRaITuE7rMfCQQq0jjdd.json', 'var_call_DORTvLmFhd2KKB1furIDd2XD': 'file_storage/call_DORTvLmFhd2KKB1furIDd2XD.json'}

exec(code, env_args)
