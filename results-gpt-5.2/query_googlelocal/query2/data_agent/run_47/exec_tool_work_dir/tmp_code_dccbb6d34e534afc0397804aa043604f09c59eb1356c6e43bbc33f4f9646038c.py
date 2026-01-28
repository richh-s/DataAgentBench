code = """import json, pandas as pd

# load reviews (large)
path = var_call_36DpPMVRP63hyIAa8ULKBQi1
with open(path, 'r') as f:
    reviews = json.load(f)

biz = pd.DataFrame(var_call_KVAy5dZSu9jED613nMmrrckL)
rev = pd.DataFrame(reviews)
rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')

avg = rev.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
res = biz.merge(avg, on='gmap_id', how='left')
res = res[res['avg_rating'] >= 4.0].sort_values(['avg_rating','name'], ascending=[False, True])
res['avg_rating'] = res['avg_rating'].round(3)
out = res[['name','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Tw8eFO3K2yRShCxfAWDnDGxn': [], 'var_call_36DpPMVRP63hyIAa8ULKBQi1': 'file_storage/call_36DpPMVRP63hyIAa8ULKBQi1.json', 'var_call_btpvxRx3TzNPHzQGlGY5AdT4': [], 'var_call_KVAy5dZSu9jED613nMmrrckL': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
