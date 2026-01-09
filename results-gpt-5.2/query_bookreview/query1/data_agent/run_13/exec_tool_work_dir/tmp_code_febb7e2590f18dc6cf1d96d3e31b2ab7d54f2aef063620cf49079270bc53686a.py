code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books_details = load_records(var_call_1hnd3BAjJRy1eLvCicF64SzO)
pat = re.compile(r'\b(17\d{2}|18\d{2}|19\d{2}|20\d{2})\b')

cnt=0
samples=[]
for r in books_details:
    det = r.get('details') or ''
    m = pat.search(det)
    if m:
        cnt += 1
        if len(samples) < 5:
            samples.append({'book_id': r.get('book_id'), 'match': m.group(1), 'details_snip': det[:120]})

print('__RESULT__:')
print(json.dumps({'n_with_year_match': cnt, 'sample_matches': samples, 'total_books': len(books_details)}))"""

env_args = {'var_call_1hnd3BAjJRy1eLvCicF64SzO': 'file_storage/call_1hnd3BAjJRy1eLvCicF64SzO.json', 'var_call_Ju0rflhBZZCI0gaSIDNbn0i9': 'file_storage/call_Ju0rflhBZZCI0gaSIDNbn0i9.json', 'var_call_7lsT6uyUTXIHzv7aZ4ejmCo0': [{'n_books': '200'}], 'var_call_NU4QC8lFewmA6eAgXwb8aZVC': ['review'], 'var_call_udp5uxHOeuJJMs5wpyX11aoG': 'file_storage/call_udp5uxHOeuJJMs5wpyX11aoG.json', 'var_call_UEhZhdP7Fe049y6chbtuhFpz': {'decade': None, 'avg_rating': None, 'distinct_books': 0}, 'var_call_gAWu3jeALer7NHqxJw3kAoZc': {'sample_book_record_keys': [{'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}, {'keys': ['book_id', 'details']}], 'first_record': {'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}}, 'var_call_H0Mi4cqJMgnZjocJ9oZR2Uds': {'rev_cols': ['purchase_id', 'rating'], 'first': {'purchase_id': 'purchaseid_186', 'rating': '4'}}, 'var_call_AvekNXxL6BVksYZAhePY2tPx': {'books_df_cols': [], 'books_df_len': 0, 'rev_df_cols': ['purchase_id', 'rating', 'book_id'], 'rev_df_len': 1833, 'books_df_head': [], 'rev_df_head': [{'purchase_id': 'purchaseid_186', 'rating': 4, 'book_id': 'bookid_186'}, {'purchase_id': 'purchaseid_191', 'rating': 4, 'book_id': 'bookid_191'}, {'purchase_id': 'purchaseid_190', 'rating': 4, 'book_id': 'bookid_190'}]}}

exec(code, env_args)
