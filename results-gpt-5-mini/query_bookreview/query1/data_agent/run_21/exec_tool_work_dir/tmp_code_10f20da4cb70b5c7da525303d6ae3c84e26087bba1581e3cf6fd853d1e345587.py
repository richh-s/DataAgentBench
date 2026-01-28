code = """import json, re, pandas as pd
with open(var_call_5dwCE4tu8xQa66eB3wyRTBzu, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_V2MudqENPjmroLDcBNOyV1cj, 'r', encoding='utf-8') as f:
    avgs = json.load(f)

df_books = pd.DataFrame(books)
df_avgs = pd.DataFrame(avgs)

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

# add fields
if 'book_id' in df_books.columns:
    df_books['num_id'] = df_books['book_id'].apply(extract_num_id)
else:
    df_books['num_id'] = None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

if 'purchase_id' in df_avgs.columns:
    df_avgs['num_id'] = df_avgs['purchase_id'].apply(extract_num_id)
else:
    df_avgs['num_id'] = None

# samples
books_sample = df_books.head(10).to_dict(orient='records')
avgs_sample = df_avgs.head(10).to_dict(orient='records')

# stats
common_ids = set(df_books['num_id'].dropna().unique()) & set(df_avgs['num_id'].dropna().unique())

out = {
    'books_count': len(df_books),
    'avgs_count': len(df_avgs),
    'books_sample': books_sample,
    'avgs_sample': avgs_sample,
    'common_num_ids_sample': list(sorted(list(common_ids)))[:20]
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8TbuovrDdOB1xBpUtttDEP9A': ['review'], 'var_call_14ux0gRqZwo7087az28Kt6PP': ['books_info'], 'var_call_5dwCE4tu8xQa66eB3wyRTBzu': 'file_storage/call_5dwCE4tu8xQa66eB3wyRTBzu.json', 'var_call_V2MudqENPjmroLDcBNOyV1cj': 'file_storage/call_V2MudqENPjmroLDcBNOyV1cj.json', 'var_call_1fQyjP8cKJKxos6iWhcuzwV3': None, 'var_call_SjGHGFBt7k8lLJutROwDBk57': []}

exec(code, env_args)
