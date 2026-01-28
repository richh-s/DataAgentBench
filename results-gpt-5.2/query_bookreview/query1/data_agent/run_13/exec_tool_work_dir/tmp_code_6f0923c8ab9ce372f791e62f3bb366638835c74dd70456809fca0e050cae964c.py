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
    m = pat.search((r.get('details') or ''))
    if m:
        rows.append({'book_id': r.get('book_id'), 'year': int(m.group(1))})
books_df = pd.DataFrame(rows).dropna(subset=['book_id','year'])
rev_df = pd.DataFrame(reviews)
rev_df['rating']=pd.to_numeric(rev_df['rating'], errors='coerce')

# map purchaseid_### -> bookid_### but handle cases without prefix
rev_df['book_id'] = rev_df['purchase_id'].astype(str)
rev_df['book_id'] = rev_df['book_id'].str.replace('purchaseid_', 'bookid_', regex=False)

merged = rev_df.merge(books_df, on='book_id', how='inner').dropna(subset=['rating','year'])

out = {
    'n_reviews_total': int(len(rev_df)),
    'n_books_rated': int(rev_df['book_id'].nunique()),
    'n_books_with_year': int(books_df['book_id'].nunique()),
    'n_joined_reviews': int(len(merged)),
    'n_joined_books': int(merged['book_id'].nunique()),
    'decade_counts_distinct_books': merged.assign(decade=((merged['year']//10)*10).astype(int)).groupby('decade')['book_id'].nunique().sort_values(ascending=False).head(20).to_dict()
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1hnd3BAjJRy1eLvCicF64SzO': 'file_storage/call_1hnd3BAjJRy1eLvCicF64SzO.json', 'var_call_Ju0rflhBZZCI0gaSIDNbn0i9': 'file_storage/call_Ju0rflhBZZCI0gaSIDNbn0i9.json', 'var_call_7lsT6uyUTXIHzv7aZ4ejmCo0': [{'n_books': '200'}], 'var_call_NU4QC8lFewmA6eAgXwb8aZVC': ['review'], 'var_call_udp5uxHOeuJJMs5wpyX11aoG': 'file_storage/call_udp5uxHOeuJJMs5wpyX11aoG.json', 'var_call_UEhZhdP7Fe049y6chbtuhFpz': {'decade': None, 'avg_rating': None, 'distinct_books': 0}}

exec(code, env_args)
