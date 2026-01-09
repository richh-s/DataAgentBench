code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_oV3AvJT2jJ7j30MIO2Tv6lHF)
books = load_records(var_call_WDMgUqeAWLISMS5Z7iWoeLz9)

rdf = pd.DataFrame(reviews)
bdf = pd.DataFrame(books)

# normalize ids: extract trailing digits and map purchaseid_<n> -> bookid_<n>
# keep only well-formed ids
rdf['id_num'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
bdf['id_num'] = bdf['book_id'].astype(str).str.extract(r'(\d+)$')[0]

rdf = rdf.dropna(subset=['id_num'])
bdf = bdf.dropna(subset=['id_num'])

# ratings numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['rating'])

# children books filter
bdf['is_children'] = bdf['categories'].astype(str).str.contains("Children's Books", regex=False, na=False)
cb = bdf[bdf['is_children']][['id_num','title']].drop_duplicates()

# join and aggregate
j = rdf.merge(cb, on='id_num', how='inner')
agg = j.groupby('title', as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WDMgUqeAWLISMS5Z7iWoeLz9': 'file_storage/call_WDMgUqeAWLISMS5Z7iWoeLz9.json', 'var_call_Jf6N4K9ryO7GgBNeI1jGiSR3': ['review'], 'var_call_oV3AvJT2jJ7j30MIO2Tv6lHF': 'file_storage/call_oV3AvJT2jJ7j30MIO2Tv6lHF.json'}

exec(code, env_args)
