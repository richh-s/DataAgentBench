code = """import json, pandas as pd
from pathlib import Path

# Load full books data
books_path = var_call_ZIee5IbCkaEgt89Xd9wqBHEw
with open(books_path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books
child_mask = books_df['categories'].astype(str).str.contains("Children's Books", regex=False)
child_books = books_df[child_mask].copy()

# Load full review data
reviews_path = var_call_rn7QJlZHNpxPWCBpg1xqmtOb
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Fuzzy join: purchase_id <-> book_id
merged = rev_df.merge(child_books[['book_id','title']], left_on='purchase_id', right_on='book_id', how='inner')

# Compute average rating per book from 2020 onwards (already filtered in SQL)
agg = merged.groupby(['book_id','title'], as_index=False)['rating'].mean()
res = agg[agg['rating'] >= 4.5].sort_values('rating', ascending=False)

out = res.to_dict(orient='records')

s = json.dumps(out)
print('__RESULT__:')
print(s)"""

env_args = {'var_call_ZIee5IbCkaEgt89Xd9wqBHEw': 'file_storage/call_ZIee5IbCkaEgt89Xd9wqBHEw.json', 'var_call_BgpDQc2ZEOXNkoY92SGiBfqZ': ['review'], 'var_call_rn7QJlZHNpxPWCBpg1xqmtOb': 'file_storage/call_rn7QJlZHNpxPWCBpg1xqmtOb.json'}

exec(code, env_args)
