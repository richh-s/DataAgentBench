code = """import json, re, pandas as pd

with open(var_call_AcvS8AtzwsKpedNY4MtCjYEn, 'r') as f:
    books = json.load(f)
reviews = json.load(open(var_call_8ORH9hZKchN9U2if1jsad9Lk,'r'))

rows = []
for b in books:
    d = b.get('details') or ''
    m = re.search(r'(19|20)\d{2}', d)
    year = int(m.group(0)) if m else None
    decade = (year//10)*10 if year else None
    rows.append({'book_id': b.get('book_id'), 'year': year, 'decade': decade})

books_df = pd.DataFrame(rows)
reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = reviews_df['rating'].astype(float)
merged = pd.merge(reviews_df, books_df, left_on='purchase_id', right_on='book_id', how='inner')

book_avg = merged.groupby('book_id')['rating'].mean().reset_index()
book_avg = book_avg.merge(books_df[['book_id','decade']], on='book_id', how='left')

# Count distinct books per decade
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')

# Prepare debug info
debug = {
  'books_with_decade': int(books_df['decade'].notna().sum()),
  'merged_rows': int(len(merged)),
  'n_decades': int(decade_counts.shape[0]),
  'decade_counts': decade_counts.to_dict(orient='records')
}

import json as _json
res = _json.dumps(debug)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_AcvS8AtzwsKpedNY4MtCjYEn': 'file_storage/call_AcvS8AtzwsKpedNY4MtCjYEn.json', 'var_call_UO7J5bn8Ysnif7sfqlgKd0u7': [{'name': 'review'}], 'var_call_8ORH9hZKchN9U2if1jsad9Lk': 'file_storage/call_8ORH9hZKchN9U2if1jsad9Lk.json'}

exec(code, env_args)
