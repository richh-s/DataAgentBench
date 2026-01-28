code = """import json, re, pandas as pd
with open(var_call_5dwCE4tu8xQa66eB3wyRTBzu, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_V2MudqENPjmroLDcBNOyV1cj, 'r', encoding='utf-8') as f:
    avgs = json.load(f)

df_books = pd.DataFrame(books)
df_avgs = pd.DataFrame(avgs)

import re

def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)", s)
    return int(m.group(1)) if m else None

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"\b(19|20)\d{2}\b", s)
    if m:
        return int(m.group(0))
    return None

# apply
if 'book_id' not in df_books.columns:
    df_books['book_id'] = None
if 'details' not in df_books.columns:
    df_books['details'] = None

df_books['num_id'] = df_books['book_id'].apply(extract_num_id)
df_books['year'] = df_books['details'].apply(extract_year)
df_books['decade'] = df_books['year'].apply(lambda y: f"{(y//10)*10}s" if pd.notnull(y) else None)

if 'purchase_id' not in df_avgs.columns:
    df_avgs['purchase_id'] = None

df_avgs['num_id'] = df_avgs['purchase_id'].apply(extract_num_id)
df_avgs['avg_rating'] = pd.to_numeric(df_avgs['avg_rating'], errors='coerce')

# merge
from pandas import merge

df_merged = merge(df_books, df_avgs, on='num_id', how='inner', suffixes=('_book','_avg'))
df_merged = df_merged[['book_id','purchase_id','num_id','year','decade','avg_rating']]
df_merged = df_merged[df_merged['decade'].notnull() & df_merged['avg_rating'].notnull()]

grp = df_merged.groupby('decade').agg(book_count=('num_id', lambda x: int(x.nunique())),
                                       mean_avg_rating=('avg_rating', 'mean')).reset_index()
# sort
grp = grp.sort_values('decade')
# convert to list of dicts
out = grp.to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8TbuovrDdOB1xBpUtttDEP9A': ['review'], 'var_call_14ux0gRqZwo7087az28Kt6PP': ['books_info'], 'var_call_5dwCE4tu8xQa66eB3wyRTBzu': 'file_storage/call_5dwCE4tu8xQa66eB3wyRTBzu.json', 'var_call_V2MudqENPjmroLDcBNOyV1cj': 'file_storage/call_V2MudqENPjmroLDcBNOyV1cj.json', 'var_call_1fQyjP8cKJKxos6iWhcuzwV3': None}

exec(code, env_args)
