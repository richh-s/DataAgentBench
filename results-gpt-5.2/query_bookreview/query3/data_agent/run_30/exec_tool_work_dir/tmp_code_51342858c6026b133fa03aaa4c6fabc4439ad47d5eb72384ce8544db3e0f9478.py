code = """import json, pandas as pd

# Load books
books_src = var_call_lKw2GcBMhR3qbUZsT3sfVpTi
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src
books_df = pd.DataFrame(books)

# keep Children's Books
books_df['categories_str'] = books_df['categories'].fillna('')
child_books_df = books_df[books_df['categories_str'].str.contains("Children's Books", na=False, regex=False)][['book_id','title']].copy()

# Load reviews from 2020 onwards
rev_src = var_call_fwoAcDQKxD4BU1Jcsh1ioioH
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src
rev_df = pd.DataFrame(reviews)

# Coerce rating to numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Fuzzy join: purchase_id suffix number equals book_id suffix number (purchaseid_# vs bookid_#)
rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
child_books_df['id_num'] = child_books_df['book_id'].astype(str).str.extract(r'(\d+)$')[0]

merged = rev_df.merge(child_books_df, on='id_num', how='inner', suffixes=('_rev','_book'))

# Average rating per book for reviews from 2020+
agg = (merged.groupby(['book_id','title'], as_index=False)
       .agg(avg_rating=('rating','mean'), review_count=('rating','count')))

res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lKw2GcBMhR3qbUZsT3sfVpTi': 'file_storage/call_lKw2GcBMhR3qbUZsT3sfVpTi.json', 'var_call_1wKe2jQXtrETP6a7begFLr6h': ['review'], 'var_call_fwoAcDQKxD4BU1Jcsh1ioioH': 'file_storage/call_fwoAcDQKxD4BU1Jcsh1ioioH.json'}

exec(code, env_args)
