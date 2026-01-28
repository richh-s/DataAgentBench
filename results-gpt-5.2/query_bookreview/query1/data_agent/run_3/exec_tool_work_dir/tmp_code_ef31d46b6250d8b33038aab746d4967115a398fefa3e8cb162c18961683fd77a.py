code = """import json, re, pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

reviews = load_records(var_call_wowwCZGfQ7zT5OJYGvNtbqnl)
books = load_records(var_call_FG60Nzk157HkRruUbOxqJjk9)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# map purchaseid_X -> bookid_X
m = df_r['purchase_id'].astype(str).str.extract(r'(\d+)', expand=False)
df_r['book_id'] = 'bookid_' + m.fillna('')
df_r = df_r[df_r['book_id'] != 'bookid_']

# parse year from details
_df_b = pd.DataFrame(books)
_df_b = _df_b.dropna(subset=['book_id','details'])

years = _df_b['details'].astype(str).str.extract(r'\b(19\d{2}|20\d{2})\b', expand=False)
_df_b['year'] = pd.to_numeric(years, errors='coerce')
_df_b = _df_b.dropna(subset=['year'])
_df_b['decade_start'] = (_df_b['year']//10)*10
_df_b['decade'] = _df_b['decade_start'].astype(int).astype(str) + 's'

# join
merged = df_r.merge(_df_b[['book_id','decade']], on='book_id', how='inner')

# compute per-decade stats; require at least 10 distinct books rated
stats = merged.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique)
).reset_index()

eligible = stats[stats['distinct_books'] >= 10].copy()
if eligible.empty:
    result = {"decade": None}
else:
    top = eligible.sort_values(['avg_rating','distinct_books','decade'], ascending=[False, False, True]).iloc[0]
    result = {"decade": str(top['decade'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FFpdUdeRLFcDrDo1kzhXUDnA': ['review'], 'var_call_wowwCZGfQ7zT5OJYGvNtbqnl': 'file_storage/call_wowwCZGfQ7zT5OJYGvNtbqnl.json', 'var_call_FG60Nzk157HkRruUbOxqJjk9': 'file_storage/call_FG60Nzk157HkRruUbOxqJjk9.json'}

exec(code, env_args)
