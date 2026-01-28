code = """import pandas as pd
import json
# Load previous query results from storage variables
df_bus = pd.DataFrame(var_call_jD7fUKbCAT3lzKajFDPIeSDI)
df_r = pd.DataFrame(var_call_tZSx2ROHhhkEyw4HdZanqWhz)
# Convert avg_rating to float
if not df_r.empty:
    df_r['avg_rating'] = df_r['avg_rating'].astype(float)
# Merge on gmap_id
merged = pd.merge(df_r, df_bus, on='gmap_id', how='left')
# Prepare output list
out = []
for _, row in merged.iterrows():
    out.append({
        'name': None if pd.isna(row.get('name')) else row.get('name'),
        'gmap_id': row.get('gmap_id'),
        'avg_rating': None if pd.isna(row.get('avg_rating')) else round(float(row.get('avg_rating')), 3)
    })
# Sort by avg_rating descending
out = sorted(out, key=lambda x: (x['avg_rating'] is not None, x['avg_rating']), reverse=True)
result_json = json.dumps(out)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_gnjjaoW13w2Sd7RjA33l76KN': [], 'var_call_jD7fUKbCAT3lzKajFDPIeSDI': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_tZSx2ROHhhkEyw4HdZanqWhz': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
