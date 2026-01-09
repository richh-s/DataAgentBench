code = """import json, pandas as pd

# load reviews (may be in file)
rev_src = var_call_uRZObdXF7PnlPxIijAA63lGw
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

biz = var_call_ylQrvqfDUO6DK0YpXh3XZvOA

rev_df = pd.DataFrame(reviews)
# ensure numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

g = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

biz_df = pd.DataFrame(biz)
out = biz_df.merge(g, on='gmap_id', how='left')
out = out.dropna(subset=['avg_rating'])
out = out[out['avg_rating'] >= 4.0]
out = out.sort_values(['avg_rating','name'], ascending=[False, True])

out['avg_rating'] = out['avg_rating'].round(3)
result = out[['name','avg_rating']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aAfqShM7c9cGCgnRLxHa5lLa': [], 'var_call_uRZObdXF7PnlPxIijAA63lGw': 'file_storage/call_uRZObdXF7PnlPxIijAA63lGw.json', 'var_call_ylQrvqfDUO6DK0YpXh3XZvOA': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
