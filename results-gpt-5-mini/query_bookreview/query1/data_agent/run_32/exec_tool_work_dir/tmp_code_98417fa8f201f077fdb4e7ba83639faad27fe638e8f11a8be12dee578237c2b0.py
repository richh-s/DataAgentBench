code = """import json
import pandas as pd

with open(var_call_uoQBgM6xZLvCULtDUAjY1i45, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_3TFu4u2EsLD3NZx9UVOjCJLb, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# map id
df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

import re

def extract_year(detail):
    if not isinstance(detail, str):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", detail)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# basic stats
stats = {}
stats['num_books_rows'] = len(df_books)
stats['num_reviews_rows'] = len(df_reviews)
stats['num_unique_books_in_books'] = int(df_books['book_id'].nunique())
stats['num_unique_books_in_reviews'] = int(df_reviews['book_id'].nunique())
stats['num_books_with_year'] = int(df_books['year'].notna().sum())

# merged
df_merged = pd.merge(df_reviews, df_books[['book_id','year']], on='book_id', how='inner')
stats['merged_rows'] = len(df_merged)
stats['unique_books_in_merged'] = int(df_merged['book_id'].nunique())
stats['unique_years_in_merged'] = sorted(list(map(int, sorted(df_merged['year'].dropna().unique()))) ) if df_merged['year'].notna().any() else []

# year counts per book
book_year_counts = df_books.groupby('year').agg(count_books=('book_id','nunique')).reset_index().sort_values('year')
book_year_counts_list = []
for _,r in book_year_counts.iterrows():
    yr = None if pd.isna(r['year']) else int(r['year'])
    book_year_counts_list.append({'year': yr, 'book_count': int(r['count_books'])})

# decade grouping for merged
if df_merged['year'].notna().any():
    df_merged['decade_start'] = (df_merged['year'].astype(int) // 10) * 10
    df_merged['decade'] = df_merged['decade_start'].astype(int).astype(str) + 's'
    grp = df_merged.groupby('decade').agg(distinct_books=('book_id', lambda x: x.nunique()), avg_rating=('rating','mean')).reset_index()
    grp_list = grp.sort_values('decade').to_dict(orient='records')
else:
    grp_list = []

out = {'stats': stats, 'book_year_counts': book_year_counts_list, 'decade_groups': grp_list}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TmxbjPq0NdaugFpHVwIbt13H': ['books_info'], 'var_call_qtfordLX0oPiqP3bTJAZLsTQ': ['review'], 'var_call_uoQBgM6xZLvCULtDUAjY1i45': 'file_storage/call_uoQBgM6xZLvCULtDUAjY1i45.json', 'var_call_3TFu4u2EsLD3NZx9UVOjCJLb': 'file_storage/call_3TFu4u2EsLD3NZx9UVOjCJLb.json', 'var_call_gbfV8WSCwCdXgmhfDxEEK8nr': {'decade': None, 'average_rating': None, 'distinct_books_in_decade_with_ratings': None}}

exec(code, env_args)
