code = """import json, re, pandas as pd
with open(var_call_XTvE2u4u8fNfAT70SyBtj3lO, 'r') as f:
    reviews = json.load(f)
with open(var_call_WgirpVXkL6BEgT2yzTQt6Ktv, 'r') as f:
    books = json.load(f)

df_books = pd.DataFrame(books)

def extract_year(details):
    if not isinstance(details, str):
        return None
    years = re.findall(r"\b(\d{4})\b", details)
    for y in years:
        try:
            yi = int(y)
            if 1500 <= yi <= 2025:
                return yi
        except:
            continue
    return None

if 'details' in df_books.columns:
    df_books['pub_year'] = df_books['details'].apply(extract_year)
else:
    df_books['pub_year'] = None

# Diagnostics
total_books = len(df_books)
books_with_year = df_books['pub_year'].notnull().sum()
sample_with_year = df_books[df_books['pub_year'].notnull()].head(10).to_dict(orient='records')
sample_without_year = df_books[df_books['pub_year'].isnull()].head(10).to_dict(orient='records')

# Reviews diagnostics
df_rev = pd.DataFrame(reviews)
num_purchase_ids = df_rev['purchase_id'].nunique()
# extract numeric ids ranges
import math

def pid_to_int(pid):
    m = re.search(r"(\d+)", pid)
    return int(m.group(1)) if m else None

pnums = df_rev['purchase_id'].apply(pid_to_int).dropna().astype(int)
min_p = int(pnums.min()) if not pnums.empty else None
max_p = int(pnums.max()) if not pnums.empty else None

# book ids in books
bnums = df_books['book_id'].apply(lambda x: int(re.search(r"(\d+)", x).group(1)) if isinstance(x,str) and re.search(r"(\d+)", x) else None).dropna().astype(int)
min_b = int(bnums.min()) if not bnums.empty else None
max_b = int(bnums.max()) if not bnums.empty else None

# merged counts using earlier mapping

def purchase_to_book(pid):
    m = re.search(r"(\d+)", pid)
    if m:
        return f"bookid_{m.group(1)}"
    return None

df_rev['book_id'] = df_rev['purchase_id'].apply(purchase_to_book)
merged = pd.merge(df_rev, df_books[['book_id','pub_year']], on='book_id', how='inner')
merged_count = len(merged)
merged_unique_books = merged['book_id'].nunique()

res = {
    'total_books': total_books,
    'books_with_year': int(books_with_year),
    'sample_with_year': sample_with_year,
    'sample_without_year': sample_without_year,
    'num_purchase_ids': int(num_purchase_ids),
    'purchase_id_min': min_p,
    'purchase_id_max': max_p,
    'book_id_min': min_b,
    'book_id_max': max_b,
    'merged_count': int(merged_count),
    'merged_unique_books': int(merged_unique_books)
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_HMpLhDV5JN6U08VwosCXQpgv': ['review'], 'var_call_tm06RGmquUHZ4WBzlNs8BZRv': ['books_info'], 'var_call_XTvE2u4u8fNfAT70SyBtj3lO': 'file_storage/call_XTvE2u4u8fNfAT70SyBtj3lO.json', 'var_call_WgirpVXkL6BEgT2yzTQt6Ktv': 'file_storage/call_WgirpVXkL6BEgT2yzTQt6Ktv.json', 'var_call_RdSLEQzUUDJbC5EcyEKWN7Ms': {'best_decade': None, 'avg_rating': None, 'n_books': 0, 'decades': []}}

exec(code, env_args)
