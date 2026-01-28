code = """import json
import pandas as pd
import re

# Load the query results from storage files
with open(var_call_h3KwakvfhuMMwf63BPIAw7NT, 'r') as f:
    books = json.load(f)
with open(var_call_jyexEf57U5sWqiFmXDU7ru5L, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize column names if needed
# Extract numeric id from book_id and purchase_id
def extract_numeric_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)$", s)
    return int(m.group(1)) if m else None

df_books['book_num'] = df_books['book_id'].apply(extract_numeric_id)
df_reviews['book_num'] = df_reviews['purchase_id'].apply(extract_numeric_id)

# Keep only rows with numeric ids
df_books = df_books[df_books['book_num'].notnull()].copy()
df_reviews = df_reviews[df_reviews['book_num'].notnull()].copy()

# Extract publication year from details using regex (first 4-digit year between 1000 and 2029)
def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(1[0-9]{3}|20[0-2][0-9])", s)
    return int(m.group(0)) if m else None

df_books['pub_year'] = df_books['details'].apply(extract_year)

# Drop books without a publication year
df_books = df_books[df_books['pub_year'].notnull()].copy()

# Compute decade string
df_books['decade_start'] = (df_books['pub_year'] // 10) * 10
df_books['decade'] = df_books['decade_start'].astype(int).astype(str) + 's'

# Convert ratings to float
# Some ratings may be strings; coerce errors
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
else:
    df_reviews['rating'] = pd.to_numeric(df_reviews.get('stars', None), errors='coerce')

# Drop reviews without valid rating
df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()

# Compute per-book average rating from reviews
book_avg = df_reviews.groupby('book_num', as_index=False).agg({'rating': 'mean'})
book_avg = book_avg.rename(columns={'rating': 'book_avg_rating'})

# Join with books to get publication decade
merged = pd.merge(book_avg, df_books[['book_num', 'book_id', 'title', 'pub_year', 'decade']], on='book_num', how='inner')

# For each decade, compute number of distinct books and average of book_avg_rating (unweighted per book)
decade_stats = merged.groupby('decade').agg(
    num_distinct_books=('book_id', 'nunique'),
    avg_of_book_avgs=('book_avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_distinct_books'] >= 10].copy()

# If no eligible decades, return None
if eligible.empty:
    result = {'decade': None, 'avg_rating': None, 'num_books': 0}
else:
    # Find decade with highest average
    top = eligible.sort_values(['avg_of_book_avgs', 'num_distinct_books'], ascending=[False, False]).iloc[0]
    result = {
        'decade': top['decade'],
        'avg_rating': round(float(top['avg_of_book_avgs']), 4),
        'num_books': int(top['num_distinct_books'])
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_p2f4kZc3sleUiV0OHSAYd2vo': ['review'], 'var_call_NJDGbBt5sVTpOiKRD5hGVnsK': ['books_info'], 'var_call_h3KwakvfhuMMwf63BPIAw7NT': 'file_storage/call_h3KwakvfhuMMwf63BPIAw7NT.json', 'var_call_jyexEf57U5sWqiFmXDU7ru5L': 'file_storage/call_jyexEf57U5sWqiFmXDU7ru5L.json'}

exec(code, env_args)
