code = """import json
import pandas as pd
import re

with open(var_call_v4Qs3F5BbtONXcuyiUrFTqZk, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_MzN91tOr8xrMKRPLFMLDuBal, 'r', encoding='utf-8') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize ratings
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Extract publication year from details
pattern = re.compile(r"(\d{4})")

def extract_year(detail):
    if not isinstance(detail, str):
        return None
    matches = pattern.findall(detail)
    for m in matches:
        y = int(m)
        if 1000 <= y <= 2023:
            return y
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Merge
merged = rev_df.merge(books_df[['book_id','pub_year']], on='book_id', how='left')
merged = merged[merged['pub_year'].notna() & merged['rating'].notna()].copy()
merged['pub_year'] = merged['pub_year'].astype(int)

# per-book average rating
book_avg = merged.groupby(['book_id','pub_year'], as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
book_avg['decade_start'] = (book_avg['pub_year'] // 10) * 10
book_avg['decade'] = book_avg['decade_start'].astype(int).astype(str) + 's'

# decade stats
decade_stats = book_avg.groupby('decade').agg(distinct_books=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()
valid_decades = decade_stats[decade_stats['distinct_books'] >= 10]

if valid_decades.empty:
    result = None
else:
    best = valid_decades.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': best['decade'],
        'decade_avg_rating': float(best['decade_avg_rating']),
        'distinct_books': int(best['distinct_books'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YLjPOkHQrNjMcLg8AQ0CN4zU': ['review'], 'var_call_PCJA205YfJGXnXYCx0XEM9Ol': ['books_info'], 'var_call_v4Qs3F5BbtONXcuyiUrFTqZk': 'file_storage/call_v4Qs3F5BbtONXcuyiUrFTqZk.json', 'var_call_MzN91tOr8xrMKRPLFMLDuBal': 'file_storage/call_MzN91tOr8xrMKRPLFMLDuBal.json', 'var_call_Ff97s3lidt1pAM1LUbqpWQQo': {'reviews_columns': ['purchase_id', 'rating', 'title'], 'books_columns': ['book_id', 'title', 'details'], 'reviews_sample0': {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!'}, 'books_sample0': {'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, 'reviews_len': 1833, 'books_len': 200}}

exec(code, env_args)
