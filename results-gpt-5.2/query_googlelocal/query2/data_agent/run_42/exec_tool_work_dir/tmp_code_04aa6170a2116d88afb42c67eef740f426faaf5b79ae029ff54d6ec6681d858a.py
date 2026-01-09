code = """import json, pandas as pd

# business list
biz = pd.DataFrame(var_call_OTdX6Vd94GVcQXu1sBt0ngre)

# reviews
path = var_call_g7tYGg5yVCi2ztjvF81CTDRd
with open(path, 'r', encoding='utf-8') as f:
    rev = json.load(f)
revdf = pd.DataFrame(rev)
revdf['rating'] = pd.to_numeric(revdf['rating'], errors='coerce')

# filter to biz gmap_ids
revdf = revdf[revdf['gmap_id'].isin(biz['gmap_id'])]

avg = revdf.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
res = biz.merge(avg, on='gmap_id', how='left')
res = res[res['avg_rating'].notna() & (res['avg_rating']>=4.0)]
res = res.sort_values(['avg_rating','name'], ascending=[False, True])
res['avg_rating'] = res['avg_rating'].round(2)

out = res[['name','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gi5LxVA0GA4kXjDWt85mfX1C': [], 'var_call_g7tYGg5yVCi2ztjvF81CTDRd': 'file_storage/call_g7tYGg5yVCi2ztjvF81CTDRd.json', 'var_call_Y0IoBY0quQSof5sOb7Vxk9Xc': [], 'var_call_OTdX6Vd94GVcQXu1sBt0ngre': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
