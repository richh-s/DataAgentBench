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
    if bid and m:
        rows.append({'book_id': bid, 'year': int(m.group(1))})
books_df = pd.DataFrame(rows)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

merged = pd.merge(rev_df, books_df, on='book_id', how='inner')
merged = merged.dropna(subset=['rating','year'])

merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

stats = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique')).reset_index()
stats10 = stats[stats['distinct_books']>=10].sort_values('avg_rating', ascending=False)

out = {
    'joined_books': int(merged['book_id'].nunique()),
    'joined_reviews': int(len(merged)),
    'decades_with_10_plus': int(len(stats10)),
    'top5': stats10.head(5).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1hnd3BAjJRy1eLvCicF64SzO': 'file_storage/call_1hnd3BAjJRy1eLvCicF64SzO.json', 'var_call_Ju0rflhBZZCI0gaSIDNbn0i9': 'file_storage/call_Ju0rflhBZZCI0gaSIDNbn0i9.json', 'var_call_7lsT6uyUTXIHzv7aZ4ejmCo0': [{'n_books': '200'}], 'var_call_NU4QC8lFewmA6eAgXwb8aZVC': ['review'], 'var_call_udp5uxHOeuJJMs5wpyX11aoG': 'file_storage/call_udp5uxHOeuJJMs5wpyX11aoG.json', 'var_call_UEhZhdP7Fe049y6chbtuhFpz': {'decade': None, 'avg_rating': None, 'distinct_books': 0}, 'var_call_gAWu3jeALer7NHqxJw3kAoZc': {'sample_book_record_keys': [{'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}], 'first_record': {'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}}, 'var_call_H0Mi4cqJMgnZjocJ9oZR2Uds': {'rev_cols': ['purchase_id', 'rating'], 'first': {'purchase_id': 'purchaseid_186', 'rating': '4'}}}

exec(code, env_args)
