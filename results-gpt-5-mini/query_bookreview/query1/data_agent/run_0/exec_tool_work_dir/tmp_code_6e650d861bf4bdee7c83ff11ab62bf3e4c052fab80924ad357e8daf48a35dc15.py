code = """import json
import pandas as pd
import re

books_path = var_call_HrC8RRaITuE7rMfCQQq0jjdd
reviews_path = var_call_DORTvLmFhd2KKB1furIDd2XD

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# ratings
try:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
except:
    pass

# map purchase to book
df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')

# extract years
years = []
for txt in df_books['details'].astype(str):
    ys = re.findall(r"\b(\d{4})\b", txt)
    y = None
    for yi in ys:
        yi = int(yi)
        if 1000 <= yi <= 2023:
            y = yi
            break
    years.append(y)

df_books['year'] = years

# stats
total_books = df_books['book_id'].nunique()
books_with_year = df_books['year'].notnull().sum()
unique_books_in_reviews = df_reviews['book_id'].nunique()

# merge
merged = pd.merge(df_reviews, df_books[['book_id','year']], on='book_id', how='inner')
unique_merged_books = merged['book_id'].nunique()

# per-book means
book_means = merged.groupby('book_id', as_index=False).agg({'rating':'mean','year':'first'})
book_means['decade'] = ((book_means['year']//10)*10).astype('Int64').astype(str) + 's'

decade_counts = book_means['decade'].value_counts().to_dict()

decade_stats = book_means.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()

# prepare result
res = {
    'total_books_in_books_db': int(total_books),
    'books_with_extracted_year': int(books_with_year),
    'unique_books_in_reviews': int(unique_books_in_reviews),
    'unique_books_in_merged': int(unique_merged_books),
    'decade_counts_sample': decade_counts,
    'decade_stats_top': decade_stats.sort_values('avg_rating', ascending=False).head(20).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_YWZpvWKF1QbXS0qUsFALVbSm': ['books_info'], 'var_call_i05rlnL0fLX8K3aiJP4gekvf': ['review'], 'var_call_HrC8RRaITuE7rMfCQQq0jjdd': 'file_storage/call_HrC8RRaITuE7rMfCQQq0jjdd.json', 'var_call_DORTvLmFhd2KKB1furIDd2XD': 'file_storage/call_DORTvLmFhd2KKB1furIDd2XD.json', 'var_call_fGwlWs1gvftkop7S9HmxTK3M': {'decade': None, 'average_rating': None, 'book_count': 0}}

exec(code, env_args)
