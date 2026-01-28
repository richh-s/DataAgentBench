code = """import json, pandas as pd

# load books
books_src = var_call_bmOEUG1SlKraxP0O2A5DNgtx
if isinstance(books_src, str):
    with open(books_src, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_src

# load reviews
rev_src = var_call_4dvapX4TV6zZcuyw7NFCkMjg
if isinstance(rev_src, str):
    with open(rev_src, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

books_df = pd.DataFrame(books)
rev_df = pd.DataFrame(reviews)

# normalize ids: purchaseid_123 -> bookid_123
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# children's books filter
books_df['is_childrens'] = books_df['categories'].astype(str).str.contains("Children's Books", regex=False, na=False)
child_df = books_df[books_df['is_childrens']].copy()

# ratings to float
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

merged = rev_df.merge(child_df[['book_id','title']], on='book_id', how='inner')
agg = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False,False,True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bmOEUG1SlKraxP0O2A5DNgtx': 'file_storage/call_bmOEUG1SlKraxP0O2A5DNgtx.json', 'var_call_tGE5v9ebZt6BUrhcA3OYNo1g': ['review'], 'var_call_4dvapX4TV6zZcuyw7NFCkMjg': 'file_storage/call_4dvapX4TV6zZcuyw7NFCkMjg.json'}

exec(code, env_args)
