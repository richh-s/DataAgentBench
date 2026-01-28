code = """import json
import pandas as pd

df_b = pd.DataFrame(var_call_AEu5UQTCwTEfHdsbErIbMCGz)
df_r = pd.DataFrame(var_call_Pq9zr5AF3TlXZ7foglZIwdEV)

df_r['avg_rating'] = pd.to_numeric(df_r['avg_rating'], errors='coerce')
df_r['cnt'] = pd.to_numeric(df_r['cnt'], errors='coerce').fillna(0).astype(int)

df = pd.merge(df_b, df_r, on='gmap_id', how='inner')

df['avg_rating'] = df['avg_rating'].astype(float)

res = df[df['avg_rating'] >= 4.0][['name', 'gmap_id', 'avg_rating', 'cnt']]

out = []
for _, row in res.iterrows():
    out.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 2),
        'num_reviews': int(row['cnt'])
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_pVbiIUKZcC6NTiuj4c6FBHUv': [], 'var_call_AEu5UQTCwTEfHdsbErIbMCGz': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_Pq9zr5AF3TlXZ7foglZIwdEV': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}]}

exec(code, env_args)
