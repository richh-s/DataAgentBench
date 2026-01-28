code = """import json, pandas as pd

# load books
books_src = var_call_qBa6TfeiDAWZ5S6GyI1pppWf
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

# load reviews
rev_src = var_call_Q641KOjusIu9UAKSunDpoS5e
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# filter children's books
bdf['is_childrens'] = bdf['categories'].fillna('').str.contains("Children's Books", regex=False)
cb = bdf[bdf['is_childrens']].copy()

# join on numeric suffix as fuzzy key (bookid_123 <-> purchaseid_123)
cb['join_key'] = cb['book_id'].astype(str).str.extract(r'(\d+)$')[0]
rdf['join_key'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]

rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

j = rdf.merge(cb[['book_id','title','join_key']], on='join_key', how='inner')

agg = j.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qBa6TfeiDAWZ5S6GyI1pppWf': 'file_storage/call_qBa6TfeiDAWZ5S6GyI1pppWf.json', 'var_call_VNvQ7ojRsP1fLfrnSnmsy4CM': ['review'], 'var_call_Q641KOjusIu9UAKSunDpoS5e': 'file_storage/call_Q641KOjusIu9UAKSunDpoS5e.json'}

exec(code, env_args)
