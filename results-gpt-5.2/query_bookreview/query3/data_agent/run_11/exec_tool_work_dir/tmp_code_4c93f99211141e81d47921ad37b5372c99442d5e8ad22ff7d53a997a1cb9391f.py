code = """import json, pandas as pd

books_src = var_call_qKvIbYZ77VsYYZS1d9Pdcuq8
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

rev_src = var_call_JvCr1TMQp2FPd7knjBEjPnPH
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

bdf['categories_str'] = bdf['categories'].fillna('')
child = bdf[bdf['categories_str'].str.contains("Children's Books", na=False)]

rdf['book_id'] = rdf['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

j = rdf.merge(child[['book_id','title']], on='book_id', how='inner')
agg = j.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating']>=4.5].sort_values(['avg_rating','review_count','title'], ascending=[False,False,True])

lines = []
for _, r in res.iterrows():
    lines.append(f"{r['title']} (avg_rating={r['avg_rating']:.2f}, reviews_since_2020={int(r['review_count'])})")

answer = "\n".join(lines) if lines else "No Children's Books found with average rating >= 4.5 from 2020 onwards."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_qKvIbYZ77VsYYZS1d9Pdcuq8': 'file_storage/call_qKvIbYZ77VsYYZS1d9Pdcuq8.json', 'var_call_KPXv25LkCRJQEaJr6oiyAUtg': ['review'], 'var_call_JvCr1TMQp2FPd7knjBEjPnPH': 'file_storage/call_JvCr1TMQp2FPd7knjBEjPnPH.json'}

exec(code, env_args)
