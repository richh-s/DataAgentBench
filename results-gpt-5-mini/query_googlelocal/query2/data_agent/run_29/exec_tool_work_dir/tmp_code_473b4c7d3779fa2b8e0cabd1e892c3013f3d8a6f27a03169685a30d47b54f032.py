code = """import pandas as pd
import json
# Access previous query results
biz = pd.DataFrame(var_call_OkfQrBS0mjmXbiy7xyXbcY2I)
rev = pd.DataFrame(var_call_lSRE1B5UTtU3GwRrrBflS31Y)

# Convert avg_rating to float and review_count to int
rev['avg_rating'] = rev['avg_rating'].astype(float)
rev['review_count'] = rev['review_count'].astype(int)

# Merge on gmap_id
merged = pd.merge(biz, rev, on='gmap_id', how='inner')

# Filter for average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Round avg_rating to 3 decimals for readability
filtered['avg_rating'] = filtered['avg_rating'].round(3)

# Prepare result list of dicts
result = filtered[['gmap_id', 'name', 'avg_rating']].sort_values(by='avg_rating', ascending=False).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TDU5eESpKcii1brAJgx4mtlC': [], 'var_call_OkfQrBS0mjmXbiy7xyXbcY2I': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_lSRE1B5UTtU3GwRrrBflS31Y': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)
