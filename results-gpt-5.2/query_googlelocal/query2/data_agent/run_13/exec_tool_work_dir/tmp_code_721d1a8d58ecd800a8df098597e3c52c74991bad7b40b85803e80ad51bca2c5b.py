code = """import json, pandas as pd

# load reviews (may be file path)
rv = var_call_ZD2GdwRhtJoRP1Syl6sUxxO6
if isinstance(rv, str):
    with open(rv, 'r') as f:
        rv = json.load(f)

df_r = pd.DataFrame(rv)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

biz = pd.DataFrame(var_call_DFtNxTFUwVci4faWrQ9vRGR7)

# compute avg ratings
avg = df_r.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

out = biz.merge(avg, on='gmap_id', how='left')
out = out[out['avg_rating'] >= 4.0].copy()
out = out.sort_values(['avg_rating','name'], ascending=[False, True])
out['avg_rating'] = out['avg_rating'].round(3)
res = out[['name','avg_rating']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_tGclEyX2nDmhFdv70BNRiPBx': [], 'var_call_ZD2GdwRhtJoRP1Syl6sUxxO6': 'file_storage/call_ZD2GdwRhtJoRP1Syl6sUxxO6.json', 'var_call_DFtNxTFUwVci4faWrQ9vRGR7': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}]}

exec(code, env_args)
