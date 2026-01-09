code = """import json, pandas as pd

# load reviews (may be in json file)
rev_src = var_call_lBCJfTsbKwTxWn8Y5GClSGc4
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz = var_call_lN3kvYZCnq7W3wA1qLGmlfh7

df_rev = pd.DataFrame(rev)
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

df_biz = pd.DataFrame(biz)

avg = df_rev.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
res = df_biz.merge(avg, on='gmap_id', how='inner')
res = res[res['avg_rating']>=4.0][['name','avg_rating']].sort_values(['avg_rating','name'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KRv9KoVW7doLkuJEbWSqiqIN': [], 'var_call_lBCJfTsbKwTxWn8Y5GClSGc4': 'file_storage/call_lBCJfTsbKwTxWn8Y5GClSGc4.json', 'var_call_U10NfgMnEJX4ZjO48xIrO0sN': [], 'var_call_lN3kvYZCnq7W3wA1qLGmlfh7': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}]}

exec(code, env_args)
