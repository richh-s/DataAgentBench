code = """import json, pandas as pd

# load books
books_src = var_call_VTsDkoKihsLggax5gtNNy1na
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

# load reviews
rev_src = var_call_nTXEtJ6XWIjun6drMBZA77n9
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# filter children books by categories containing "Children's Books"
bdf['is_children'] = bdf['categories'].fillna('').str.contains("Children's Books", regex=False)
cb = bdf[bdf['is_children']].copy()

# join reviews on exact id match after normalizing prefixes purchaseid_ vs bookid_
rdf['book_id'] = rdf['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
# ratings are strings
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

j = rdf.merge(cb[['book_id','title']], on='book_id', how='inner')

agg = j.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating']>=4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VTsDkoKihsLggax5gtNNy1na': 'file_storage/call_VTsDkoKihsLggax5gtNNy1na.json', 'var_call_0URJZ4khk6gHV3rPYhgbfRsD': ['review'], 'var_call_nTXEtJ6XWIjun6drMBZA77n9': 'file_storage/call_nTXEtJ6XWIjun6drMBZA77n9.json'}

exec(code, env_args)
