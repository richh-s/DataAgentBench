code = """import json, pandas as pd

# load reviews (may be file path)
rev = var_call_VrWwbrFhlc01hqFNCCqWphaO
if isinstance(rev, str):
    with open(rev, 'r') as f:
        rev = json.load(f)

biz = var_call_8EUFHFYG7C6RIRV8AuEA5Xty

df_rev = pd.DataFrame(rev)
df_biz = pd.DataFrame(biz)

# ratings may be strings
if not df_rev.empty:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

avg = df_rev.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

df = df_biz[['gmap_id','name']].merge(avg, on='gmap_id', how='left')
df = df[df['avg_rating'] >= 4.0].sort_values(['avg_rating','name'], ascending=[False, True])

out = df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ec0vZCPgkWFxxNWNP3w6jGuR': [], 'var_call_VrWwbrFhlc01hqFNCCqWphaO': 'file_storage/call_VrWwbrFhlc01hqFNCCqWphaO.json', 'var_call_nulxKSbt5KOnrnuVUyXxiY4G': [], 'var_call_8EUFHFYG7C6RIRV8AuEA5Xty': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}]}

exec(code, env_args)
