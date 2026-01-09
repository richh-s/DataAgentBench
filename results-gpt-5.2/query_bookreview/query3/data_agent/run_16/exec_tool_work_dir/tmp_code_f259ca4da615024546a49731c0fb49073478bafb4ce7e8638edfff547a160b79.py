code = """import json, pandas as pd

# load reviews (may be file path)
rev_src = var_call_kjFAmqn0X9UlwJavxoqDqTiu
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

books_src = var_call_2vVNKsdqU5vD0sFBiK6CQjDS
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# normalize ids: purchaseid_123 -> bookid_123
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# compute avg rating and count since 2020
agg = rev_df.groupby('book_id', as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))

# filter children's books
books_df['is_children'] = books_df['categories'].astype(str).str.contains("Children's Books", na=False)
children = books_df[books_df['is_children']][['book_id','title']]

merged = pd.merge(children, agg, on='book_id', how='inner')
res = merged[merged['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False,False,True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2vVNKsdqU5vD0sFBiK6CQjDS': 'file_storage/call_2vVNKsdqU5vD0sFBiK6CQjDS.json', 'var_call_Q9IXtFlxmfQIg9OYh9IbnVhd': ['review'], 'var_call_kjFAmqn0X9UlwJavxoqDqTiu': 'file_storage/call_kjFAmqn0X9UlwJavxoqDqTiu.json'}

exec(code, env_args)
