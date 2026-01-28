code = """import pandas as pd
import json
# Data from previous queries available as variables
# var_call_yNtyZDEsffqUpLzOeN8U5g1Z: business entries with name, gmap_id, description
# var_call_FaavrCTQ22pEo5JOpg41ph9T: review aggregates with gmap_id, avg_rating, review_count

biz = pd.DataFrame(var_call_yNtyZDEsffqUpLzOeN8U5g1Z)
rev = pd.DataFrame(var_call_FaavrCTQ22pEo5JOpg41ph9T)

# Convert avg_rating and review_count to numeric
rev['avg_rating'] = rev['avg_rating'].astype(float)
rev['review_count'] = rev['review_count'].astype(int)

# Merge on gmap_id
merged = pd.merge(biz, rev, on='gmap_id', how='inner')

# Filter average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Prepare output list
output = []
for _, row in filtered.iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'average_rating': round(float(row['avg_rating']), 3),
        'review_count': int(row['review_count'])
    })

# Sort by average_rating descending then by review_count descending
output = sorted(output, key=lambda x: (-x['average_rating'], -x['review_count']))

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_AkEJaajolbouqcB2o220OM8X': [], 'var_call_yNtyZDEsffqUpLzOeN8U5g1Z': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_FaavrCTQ22pEo5JOpg41ph9T': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)
