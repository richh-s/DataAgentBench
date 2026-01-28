code = """import json, pandas as pd

def load(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load(var_call_Ru4EXMK2ylLxISWG1gkgc4uA)
books = load(var_call_0yD0Zoi09kbmmoFsUswYfnDI)

dfr = pd.DataFrame(reviews)
dfb = pd.DataFrame(books)

# normalize ids (fuzzy-ish: purchaseid_123 -> bookid_123)
dfr['book_id'] = dfr['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

# children books filter
child = dfb[dfb['categories'].fillna('').str.contains("Children's Books", regex=False)].copy()

# join and compute avg rating for reviews >=2020
m = dfr.merge(child[['book_id','title']], on='book_id', how='inner')
agg = (m.groupby(['book_id','title'], as_index=False)
         .agg(avg_rating=('rating','mean'), review_count=('rating','size')))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0yD0Zoi09kbmmoFsUswYfnDI': 'file_storage/call_0yD0Zoi09kbmmoFsUswYfnDI.json', 'var_call_SLEHAMmJL76ayk4rmW8eaZHM': ['review'], 'var_call_Ru4EXMK2ylLxISWG1gkgc4uA': 'file_storage/call_Ru4EXMK2ylLxISWG1gkgc4uA.json'}

exec(code, env_args)
