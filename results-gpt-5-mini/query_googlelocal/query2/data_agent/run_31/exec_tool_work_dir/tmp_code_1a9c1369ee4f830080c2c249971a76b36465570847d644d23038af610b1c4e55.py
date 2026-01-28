code = """import pandas as pd
import json

# Load results from previous queries
biz = pd.DataFrame(var_call_EGyT3nI60tNMBn1onA7scVDj)
rev = pd.DataFrame(var_call_t8GeCN0aJjrncIrio9PMDrPG)

# Ensure numeric types
rev['avg_rating'] = rev['avg_rating'].astype(float)
rev['num_reviews'] = rev['num_reviews'].astype(int)

# Merge on gmap_id
merged = pd.merge(biz, rev, on='gmap_id', how='inner')

# Filter businesses with average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Prepare output list
output = []
for _, row in filtered.iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 3),
        'num_reviews': int(row['num_reviews'])
    })

result_json = json.dumps(output)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_XXTcSQ1QqI1GYcTSpaBtvunh': [], 'var_call_EGyT3nI60tNMBn1onA7scVDj': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_t8GeCN0aJjrncIrio9PMDrPG': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}]}

exec(code, env_args)
