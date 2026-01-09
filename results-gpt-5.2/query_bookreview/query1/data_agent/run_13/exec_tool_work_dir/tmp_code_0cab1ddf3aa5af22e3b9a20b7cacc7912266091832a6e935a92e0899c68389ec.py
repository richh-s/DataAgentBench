code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_udp5uxHOeuJJMs5wpyX11aoG)
books_details = load_records(var_call_1hnd3BAjJRy1eLvCicF64SzO)

pat = re.compile(r'\b(17\d{2}|18\d{2}|19\d{2}|20\d{2})\b')
rows=[]
for r in books_details:
    bid = r.get('book_id')
    det = r.get('details') or ''
    m = pat.search(det)
    if bid is not None and m:
        rows.append({'book_id': bid, 'year': int(m.group(1))})
books_df = pd.DataFrame(rows)

rev_df = pd.DataFrame(reviews)
rev_df['rating']=pd.to_numeric(rev_df.get('rating'), errors='coerce')
rev_df['book_id'] = rev_df.get('purchase_id').astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

merged = rev_df.merge(books_df, on='book_id', how='inner')
merged = merged.dropna(subset=['rating','year'])

out = {
    'books_year_rows': int(len(books_df)),
    'books_with_year': int(books_df['book_id'].nunique()) if not books_df.empty else 0,
    'reviews_rows': int(len(rev_df)),
    'joined_reviews': int(len(merged)),
    'joined_books': int(merged['book_id'].nunique()) if not merged.empty else 0,
}
if not merged.empty:
    merged['decade'] = ((merged['year']//10)*10).astype(int)
    out['top_decades_by_distinct_books'] = merged.groupby('decade')['book_id'].nunique().sort_values(ascending=False).head(20).to_dict()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1hnd3BAjJRy1eLvCicF64SzO': 'file_storage/call_1hnd3BAjJRy1eLvCicF64SzO.json', 'var_call_Ju0rflhBZZCI0gaSIDNbn0i9': 'file_storage/call_Ju0rflhBZZCI0gaSIDNbn0i9.json', 'var_call_7lsT6uyUTXIHzv7aZ4ejmCo0': [{'n_books': '200'}], 'var_call_NU4QC8lFewmA6eAgXwb8aZVC': ['review'], 'var_call_udp5uxHOeuJJMs5wpyX11aoG': 'file_storage/call_udp5uxHOeuJJMs5wpyX11aoG.json', 'var_call_UEhZhdP7Fe049y6chbtuhFpz': {'decade': None, 'avg_rating': None, 'distinct_books': 0}}

exec(code, env_args)
