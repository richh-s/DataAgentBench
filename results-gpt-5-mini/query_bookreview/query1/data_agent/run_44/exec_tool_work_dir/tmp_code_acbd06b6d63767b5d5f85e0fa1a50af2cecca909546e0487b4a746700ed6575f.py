code = """import pandas as pd
import re
import json

# Data from previous tool calls
reviews = var_call_1vj3Aot5CQEWtRMQQm0uCbif
books = None
# var_call_BOd223WfRMgrp9QW6NpCUa7y may be a file path or list
if isinstance(var_call_BOd223WfRMgrp9QW6NpCUa7y, str):
    # it's a file path to JSON
    import io
    with open(var_call_BOd223WfRMgrp9QW6NpCUa7y, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = var_call_BOd223WfRMgrp9QW6NpCUa7y

# Create dataframes
df_rev = pd.DataFrame(reviews)
# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
# Map purchase_id -> book_id by replacing prefix
def map_purchase_to_book(pid):
    if not isinstance(pid, str):
        return None
    return re.sub(r'^purchaseid_', 'bookid_', pid)

df_rev['book_id'] = df_rev['purchase_id'].apply(map_purchase_to_book)

# Load books dataframe
df_books = pd.DataFrame(books)

# Extract year from details using regex (first match between 1000 and 2023)
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    # find all 4-digit numbers
    matches = re.findall(r"\b(1[0-9]{3}|20[0-9]{2})\b", detail)
    if not matches:
        return None
    # convert and filter <=2023
    for m in matches:
        try:
            y = int(m)
            if y <= 2023:
                return y
        except:
            continue
    return None

# Apply
df_books['year'] = df_books['details'].apply(extract_year)
# Drop rows without year
df_books = df_books[df_books['year'].notna()].copy()
# Compute decade label
df_books['decade_start'] = (df_books['year'].astype(int) // 10) * 10
df_books['decade'] = df_books['decade_start'].astype(int).astype(str) + 's'

# Merge reviews with books on book_id
df_merged = pd.merge(df_rev, df_books[['book_id','year','decade']], on='book_id', how='inner')

# Compute per-book average rating (only include valid ratings)
book_avg = df_merged.groupby('book_id', as_index=False)['rating'].mean()
# attach decade to book_avg
book_decade = df_merged[['book_id','decade']].drop_duplicates()
book_avg = pd.merge(book_avg, book_decade, on='book_id', how='left')

# Per-decade: count distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()
# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10]

result = None
if not decade_stats_filtered.empty:
    # find decade with highest avg_rating
    top = decade_stats_filtered.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {'decade': top['decade'], 'avg_rating': round(float(top['avg_rating']), 4), 'book_count': int(top['book_count'])}
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M1DMCPupp3B3jq0ziCIFVhMR': ['review'], 'var_call_Ttpgp7VClBs4EFDnJI7zL5JZ': ['books_info'], 'var_call_C7Ry03Y3bUL3b7zqHTJQEPHL': 'file_storage/call_C7Ry03Y3bUL3b7zqHTJQEPHL.json', 'var_call_1vj3Aot5CQEWtRMQQm0uCbif': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}, {'purchase_id': 'purchaseid_188', 'rating': '1'}, {'purchase_id': 'purchaseid_23', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '3'}, {'purchase_id': 'purchaseid_99', 'rating': '2'}, {'purchase_id': 'purchaseid_190', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_169', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_194', 'rating': '4'}, {'purchase_id': 'purchaseid_81', 'rating': '5'}, {'purchase_id': 'purchaseid_199', 'rating': '1'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_200', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '1'}, {'purchase_id': 'purchaseid_20', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_159', 'rating': '2'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_67', 'rating': '3'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_58', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_95', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_136', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_38', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_31', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_7', 'rating': '5'}, {'purchase_id': 'purchaseid_4', 'rating': '5'}, {'purchase_id': 'purchaseid_104', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_162', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '3'}, {'purchase_id': 'purchaseid_158', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_165', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_6', 'rating': '5'}, {'purchase_id': 'purchaseid_158', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_86', 'rating': '5'}, {'purchase_id': 'purchaseid_174', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_177', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_63', 'rating': '2'}, {'purchase_id': 'purchaseid_33', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '4'}, {'purchase_id': 'purchaseid_157', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_185', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_13', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_72', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_42', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_73', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '4'}, {'purchase_id': 'purchaseid_97', 'rating': '5'}, {'purchase_id': 'purchaseid_59', 'rating': '5'}, {'purchase_id': 'purchaseid_192', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_99', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_163', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_106', 'rating': '5'}, {'purchase_id': 'purchaseid_130', 'rating': '5'}, {'purchase_id': 'purchaseid_118', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '1'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '2'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_161', 'rating': '4'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}, {'purchase_id': 'purchaseid_36', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_124', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_197', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}], 'var_call_BOd223WfRMgrp9QW6NpCUa7y': 'file_storage/call_BOd223WfRMgrp9QW6NpCUa7y.json'}

exec(code, env_args)
