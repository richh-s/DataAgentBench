code = """import pandas as pd
import json

# Load data from previous query results
biz = pd.DataFrame(var_call_6veq69YB3p6lkWr9pQlfuudL)
rev = pd.DataFrame(var_call_hf2cUSKVyBjXgYguWpHiDRr5)

# Convert avg_rating to float
rev['avg_rating'] = rev['avg_rating'].astype(float)

# Merge on gmap_id
merged = pd.merge(biz, rev, on='gmap_id', how='inner')

# Filter businesses with average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()
filtered = filtered.sort_values(by='avg_rating', ascending=False)

# Prepare result list
result = []
for _, row in filtered.iterrows():
    result.append({
        'name': row['name'],
        'avg_rating': round(float(row['avg_rating']), 3)
    })

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bWXwWm0MtphkBFHzMB1J0Rb1': [], 'var_call_6veq69YB3p6lkWr9pQlfuudL': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_hf2cUSKVyBjXgYguWpHiDRr5': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
