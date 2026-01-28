code = """import json, pandas as pd

# load reviews
path = var_call_WGBVW04PtP3bE64aBqA5A5O1
with open(path, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# massage businesses from name
biz = pd.DataFrame(var_call_TUqQVPMvLrLfxVWSUtAqVpeK)

# compute avg rating per gmap_id
avg = df_r.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

out = biz.merge(avg, on='gmap_id', how='left')
out = out[out['avg_rating'] >= 4.0].copy()
out['avg_rating'] = out['avg_rating'].round(3)
out = out.sort_values(['avg_rating','name'], ascending=[False, True])
result = out[['name','avg_rating']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NoZNxuRuELCbBCBOjAt3r9rY': [], 'var_call_WGBVW04PtP3bE64aBqA5A5O1': 'file_storage/call_WGBVW04PtP3bE64aBqA5A5O1.json', 'var_call_VZC61pmB4HSSRBmd7KgcHgYN': [], 'var_call_TUqQVPMvLrLfxVWSUtAqVpeK': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
