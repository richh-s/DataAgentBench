code = """import json
import pandas as pd

df_b = pd.DataFrame(var_call_iumdgemvZWPQdmBsSwEu4YVe)
df_r = pd.DataFrame(var_call_P6G3KNBZ5VCnowpBvdgCH0Ry)

# Convert types
if not df_r.empty:
    df_r['avg_rating'] = df_r['avg_rating'].astype(float)
    df_r['num_reviews'] = df_r['num_reviews'].astype(int)

# Merge on gmap_id
df = pd.merge(df_r, df_b, on='gmap_id', how='left')

result = []
for _, row in df.iterrows():
    result.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'avg_rating': round(row['avg_rating'], 2),
        'num_reviews': int(row['num_reviews'])
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rfZLZRmAMtlvMgBlhSAYecSS': [], 'var_call_iumdgemvZWPQdmBsSwEu4YVe': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_P6G3KNBZ5VCnowpBvdgCH0Ry': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}]}

exec(code, env_args)
