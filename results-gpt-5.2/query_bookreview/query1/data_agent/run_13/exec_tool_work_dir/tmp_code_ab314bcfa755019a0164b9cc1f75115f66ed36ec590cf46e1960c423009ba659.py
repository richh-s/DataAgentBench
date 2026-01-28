code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_udp5uxHOeuJJMs5wpyX11aoG)
books_details = load_records(var_call_1hnd3BAjJRy1eLvCicF64SzO)

# Parse year from details text (first 4-digit year)
pat = re.compile(r'\b(17\d{2}|18\d{2}|19\d{2}|20\d{2})\b')
rows = []
for r in books_details:
    bid = r.get('book_id')
    det = r.get('details') or ''
    m = pat.search(det)
    year = int(m.group(1)) if m else None
    rows.append({'book_id': bid, 'year': year})
books_df = pd.DataFrame(rows).dropna(subset=['book_id','year'])

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# fuzzy join: purchaseid_### -> bookid_###
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
merged = rev_df.merge(books_df, on='book_id', how='inner').dropna(subset=['rating','year'])

merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# compute avg rating per decade with >=10 distinct books (rated)
g = merged.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id','nunique')
).reset_index()

g2 = g[g['distinct_books']>=10].sort_values(['avg_rating','distinct_books'], ascending=[False, False])
if g2.empty:
    out = {'decade': None, 'avg_rating': None, 'distinct_books': 0}
else:
    top = g2.iloc[0]
    out = {'decade': top['decade'], 'avg_rating': float(top['avg_rating']), 'distinct_books': int(top['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1hnd3BAjJRy1eLvCicF64SzO': 'file_storage/call_1hnd3BAjJRy1eLvCicF64SzO.json', 'var_call_Ju0rflhBZZCI0gaSIDNbn0i9': 'file_storage/call_Ju0rflhBZZCI0gaSIDNbn0i9.json', 'var_call_7lsT6uyUTXIHzv7aZ4ejmCo0': [{'n_books': '200'}], 'var_call_NU4QC8lFewmA6eAgXwb8aZVC': ['review'], 'var_call_udp5uxHOeuJJMs5wpyX11aoG': 'file_storage/call_udp5uxHOeuJJMs5wpyX11aoG.json'}

exec(code, env_args)
