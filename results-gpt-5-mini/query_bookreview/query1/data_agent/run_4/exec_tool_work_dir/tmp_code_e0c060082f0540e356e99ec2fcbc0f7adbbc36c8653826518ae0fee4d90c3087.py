code = """import json
import pandas as pd
import re

# Load books data
books_source = var_call_QAfj9WBTnljXCGB8V0Gl5hfy
if isinstance(books_source, str):
    # it's a filepath to JSON
    with open(books_source, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_source

# Load reviews data
reviews_source = var_call_lEd9iNj3hU7BAb9DQ8AtXeXJ
if isinstance(reviews_source, str):
    with open(reviews_source, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = reviews_source

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Clean and extract publication year from details
def extract_year(details):
    if not isinstance(details, str):
        return None
    # match years from 1500 to 2023
    m = re.search(r"(?<!\d)(1[5-9]\d{2}|20[0-1]\d|202[0-3])(?!\d)", details)
    if m:
        return int(m.group(0))
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)
# drop books without pub_year
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)
books_df['decade'] = (books_df['pub_year'] // 10 * 10).astype(int).astype(str) + 's'

# Prepare reviews: map purchase_id to book_id
reviews_df = reviews_df.copy()
# Some ratings may be strings; coerce to float
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
# map purchaseid_### -> bookid_###
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Merge reviews with books on book_id
merged = reviews_df.merge(books_df[['book_id','decade']], on='book_id', how='left')
# drop rows without decade
merged = merged.dropna(subset=['decade','rating'])

# For each decade, count distinct books that have been rated and compute average rating across reviews
group = merged.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()
# Filter decades with at least 10 distinct books
eligible = group[group['distinct_books'] >= 10]

if eligible.empty:
    result = {"best_decade": None, "avg_rating": None, "distinct_books": 0}
else:
    # choose decade with highest avg_rating; in case of tie choose the one with more distinct_books then earliest decade
    eligible = eligible.sort_values(by=['avg_rating','distinct_books','decade'], ascending=[False, False, True])
    best = eligible.iloc[0]
    result = {"best_decade": best['decade'], "avg_rating": round(float(best['avg_rating']), 4), "distinct_books": int(best['distinct_books'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gxdy5bEZHOv037eeJt2kIu4X': ['review'], 'var_call_7DdI8Fs2bsPDZU5zPny59KzA': ['books_info'], 'var_call_QAfj9WBTnljXCGB8V0Gl5hfy': 'file_storage/call_QAfj9WBTnljXCGB8V0Gl5hfy.json', 'var_call_lEd9iNj3hU7BAb9DQ8AtXeXJ': 'file_storage/call_lEd9iNj3hU7BAb9DQ8AtXeXJ.json'}

exec(code, env_args)
