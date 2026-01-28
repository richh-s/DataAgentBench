code = """import pandas as pd
import json
import re

# Load query results from storage variables (they may be file paths)
data_reviews = var_call_05expxCW64So2lMoYCMVbOtc
data_books = var_call_rhVkob30qCS7mrNQXm9ZyNk0

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str):
        # assume it's a file path to a .json file
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return path_or_obj

reviews = load_json_maybe(data_reviews)
books = load_json_maybe(data_books)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize ratings
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Map purchase_id to book_id by replacing prefix
def purchase_to_book(pid):
    if pd.isna(pid):
        return None
    return pid.replace('purchaseid_', 'bookid_')

df_reviews['book_id'] = df_reviews['purchase_id'].apply(purchase_to_book)

# Extract year from books 'details' field using regex
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    years = re.findall(r"(19\d{2}|20\d{2})", detail)
    if not years:
        return None
    # pick the earliest plausible publication year? Use the first occurrence
    try:
        y = int(years[0])
        return y
    except:
        return None

# Apply
if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# Merge reviews with books on book_id
merged = pd.merge(df_reviews, df_books[['book_id','year']], on='book_id', how='inner')

# Drop rows without year or rating
merged = merged.dropna(subset=['year','rating'])
merged['year'] = merged['year'].astype(int)

# Compute per-book average rating
book_avg = merged.groupby('book_id', as_index=False).agg({'rating':'mean','year':'first'})

# Compute decade
book_avg['decade_start'] = (book_avg['year'] // 10) * 10
book_avg['decade'] = book_avg['decade_start'].astype(str) + 's'

# For each decade, require at least 10 distinct books that have been rated
decade_stats = book_avg.groupby('decade').agg(
    avg_rating_across_books = ('rating','mean'),
    distinct_books = ('book_id','nunique')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['distinct_books'] >= 10]

# If no decade meets requirement, return None
if decade_stats_filtered.empty:
    result = None
else:
    # find decade with highest avg_rating_across_books
    best = decade_stats_filtered.sort_values(['avg_rating_across_books','decade'], ascending=[False,True]).iloc[0]
    result = {
        'decade': best['decade'],
        'average_rating': round(float(best['avg_rating_across_books']), 4),
        'distinct_books': int(best['distinct_books'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_agEhyXtkJqx1WQbcbfLWibu8': ['review'], 'var_call_05expxCW64So2lMoYCMVbOtc': 'file_storage/call_05expxCW64So2lMoYCMVbOtc.json', 'var_call_VCNYJrQs7Sx9JWlVk8xXmptn': ['books_info'], 'var_call_rhVkob30qCS7mrNQXm9ZyNk0': 'file_storage/call_rhVkob30qCS7mrNQXm9ZyNk0.json'}

exec(code, env_args)
