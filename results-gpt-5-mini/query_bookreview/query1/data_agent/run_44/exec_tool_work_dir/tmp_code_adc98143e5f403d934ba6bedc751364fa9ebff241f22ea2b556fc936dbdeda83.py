code = """import pandas as pd
import re
import json

# Load full results from storage keys
with open(var_call_DiCNNhhARGb9RUVdW7hkMvTu, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_BOd223WfRMgrp9QW6NpCUa7y, 'r', encoding='utf-8') as f:
    books = json.load(f)

# DataFrames
df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Clean ratings
if 'rating' in df_rev.columns:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
else:
    df_rev['rating'] = None

# Map purchase_id to book_id by replacing prefix
import numpy as np

def map_purchase_to_book(pid):
    if not isinstance(pid, str):
        return None
    # If already bookid, keep
    if pid.startswith('bookid_'):
        return pid
    if pid.startswith('purchaseid_'):
        return 'bookid_' + pid.split('_',1)[1]
    # handle other possible formats
    m = re.search(r"(\d+)$", pid)
    if m:
        return 'bookid_' + m.group(1)
    return None

df_rev['book_id'] = df_rev['purchase_id'].apply(map_purchase_to_book)

# Extract year from books.details

def extract_year(detail):
    if not isinstance(detail, str):
        return None
    # find plausible years 1000-2023
    matches = re.findall(r"\b(1[0-9]{3}|20[0-9]{2})\b", detail)
    if not matches:
        return None
    # choose first <=2023
    for m in matches:
        y = int(m)
        if y <= 2023:
            return y
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# drop books without year
df_books_year = df_books[df_books['year'].notna()].copy()
# decade label
df_books_year['decade_start'] = (df_books_year['year'].astype(int) // 10) * 10
df_books_year['decade'] = df_books_year['decade_start'].astype(int).astype(str) + 's'

# Merge reviews with books on book_id
merged = pd.merge(df_rev, df_books_year[['book_id','year','decade']], on='book_id', how='inner')

# Stats
unique_books_in_books = df_books['book_id'].nunique()
unique_books_with_year = df_books_year['book_id'].nunique()
unique_books_in_reviews = df_rev['book_id'].nunique()
unique_books_merged = merged['book_id'].nunique()
merged_rows = len(merged)

# Per-book average rating
book_avg = merged.groupby('book_id', as_index=False)['rating'].mean()
# attach decade
book_decade = merged[['book_id','decade']].drop_duplicates()
book_avg = pd.merge(book_avg, book_decade, on='book_id', how='left')

# Per-decade stats: count distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()
# filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10].copy()

result = {
    'unique_books_in_books': int(unique_books_in_books),
    'unique_books_with_year': int(unique_books_with_year),
    'unique_books_in_reviews': int(unique_books_in_reviews) if not pd.isna(unique_books_in_reviews) else None,
    'unique_books_merged': int(unique_books_merged),
    'merged_rows': int(merged_rows),
    'decade_stats_total_count': len(decade_stats),
    'decade_stats_filtered_count': len(decade_stats_filtered)
}

if not decade_stats_filtered.empty:
    top = decade_stats_filtered.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    result['top_decade'] = {
        'decade': top['decade'],
        'avg_rating': round(float(top['avg_rating']),4),
        'book_count': int(top['book_count'])
    }
    # include full filtered list
    result['decade_stats_filtered'] = decade_stats_filtered.sort_values('decade').to_dict(orient='records')
else:
    # include decade_stats for debugging
    result['decade_stats'] = decade_stats.sort_values('decade').to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M1DMCPupp3B3jq0ziCIFVhMR': ['review'], 'var_call_Ttpgp7VClBs4EFDnJI7zL5JZ': ['books_info'], 'var_call_C7Ry03Y3bUL3b7zqHTJQEPHL': 'file_storage/call_C7Ry03Y3bUL3b7zqHTJQEPHL.json', 'var_call_1vj3Aot5CQEWtRMQQm0uCbif': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}, {'purchase_id': 'purchaseid_188', 'rating': '1'}, {'purchase_id': 'purchaseid_23', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '3'}, {'purchase_id': 'purchaseid_99', 'rating': '2'}, {'purchase_id': 'purchaseid_190', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_169', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_194', 'rating': '4'}, {'purchase_id': 'purchaseid_81', 'rating': '5'}, {'purchase_id': 'purchaseid_199', 'rating': '1'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_200', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '1'}, {'purchase_id': 'purchaseid_20', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_159', 'rating': '2'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_67', 'rating': '3'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_58', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_95', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_136', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_38', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_31', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_7', 'rating': '5'}, {'purchase_id': 'purchaseid_4', 'rating': '5'}, {'purchase_id': 'purchaseid_104', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_162', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '3'}, {'purchase_id': 'purchaseid_158', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_165', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_6', 'rating': '5'}, {'purchase_id': 'purchaseid_158', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_86', 'rating': '5'}, {'purchase_id': 'purchaseid_174', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_177', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_63', 'rating': '2'}, {'purchase_id': 'purchaseid_33', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '4'}, {'purchase_id': 'purchaseid_157', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_185', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_13', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_72', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_42', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_73', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '4'}, {'purchase_id': 'purchaseid_97', 'rating': '5'}, {'purchase_id': 'purchaseid_59', 'rating': '5'}, {'purchase_id': 'purchaseid_192', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_99', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_163', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_106', 'rating': '5'}, {'purchase_id': 'purchaseid_130', 'rating': '5'}, {'purchase_id': 'purchaseid_118', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '1'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '2'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_161', 'rating': '4'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}, {'purchase_id': 'purchaseid_36', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_124', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_197', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}], 'var_call_BOd223WfRMgrp9QW6NpCUa7y': 'file_storage/call_BOd223WfRMgrp9QW6NpCUa7y.json', 'var_call_PB0DWjw0IUu32aUWXkeb15Oy': None, 'var_call_DiCNNhhARGb9RUVdW7hkMvTu': 'file_storage/call_DiCNNhhARGb9RUVdW7hkMvTu.json'}

exec(code, env_args)
