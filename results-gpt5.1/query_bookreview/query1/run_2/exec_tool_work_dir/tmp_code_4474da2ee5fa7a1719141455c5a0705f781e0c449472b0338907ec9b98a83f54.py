code = """import json, re, pandas as pd

# Load full books details
with open(var_call_AcvS8AtzwsKpedNY4MtCjYEn, 'r') as f:
    books = json.load(f)

reviews = json.load(open(var_call_8ORH9hZKchN9U2if1jsad9Lk,'r'))

# Extract year from details text
rows = []
for b in books:
    d = b.get('details') or ''
    # Look for patterns like 'on January 1, 2004' or 'on May 20, 1996' or 'on March 20, 1995' or 'January 1, 1945'
    m = re.search(r'(19|20)\d{2}', d)
    year = int(m.group(0)) if m else None
    if year:
        decade = (year//10)*10
    else:
        decade = None
    rows.append({'book_id': b.get('book_id'), 'year': year, 'decade': decade})

books_df = pd.DataFrame(rows)

reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = reviews_df['rating'].astype(float)

# purchase_id matches book_id exactly in this synthetic data
merged = pd.merge(reviews_df, books_df, left_on='purchase_id', right_on='book_id', how='inner')

# Compute per-book average rating
book_avg = merged.groupby('book_id')['rating'].mean().reset_index()
book_avg = book_avg.merge(books_df[['book_id','decade']], on='book_id', how='left')

# Filter decades with at least 10 distinct books
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = decade_counts[decade_counts['n_books']>=10]['decade']

filtered = book_avg[book_avg['decade'].isin(valid_decades)]

decade_avg = filtered.groupby('decade')['rating'].mean().reset_index()

best_row = decade_avg.sort_values('rating', ascending=False).iloc[0]

answer = f"{int(best_row['decade'])}s"

import json as _json
res = _json.dumps(answer)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_AcvS8AtzwsKpedNY4MtCjYEn': 'file_storage/call_AcvS8AtzwsKpedNY4MtCjYEn.json', 'var_call_UO7J5bn8Ysnif7sfqlgKd0u7': [{'name': 'review'}], 'var_call_8ORH9hZKchN9U2if1jsad9Lk': 'file_storage/call_8ORH9hZKchN9U2if1jsad9Lk.json'}

exec(code, env_args)
