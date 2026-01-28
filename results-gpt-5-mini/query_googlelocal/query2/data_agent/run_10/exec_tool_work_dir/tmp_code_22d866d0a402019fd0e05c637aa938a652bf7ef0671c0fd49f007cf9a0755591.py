code = """import json
import pandas as pd

# Load data from previous tool calls
biz = pd.DataFrame(var_call_bKgiZdp839YEC8XzGpX9uGez)
avgs = pd.DataFrame(var_call_0vCbciBB3vrW53koFJsUh28l)

# Ensure correct types
if not avgs.empty:
    avgs['avg_rating'] = avgs['avg_rating'].astype(float)

# Merge on gmap_id
merged = pd.merge(biz, avgs, on='gmap_id', how='inner')

# Filter for average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Prepare results: list of dicts with name and avg_rating (rounded to 3 decimals)
results = []
for _, row in filtered.iterrows():
    results.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 3),
        'num_reviews_in_reviews_table': int(row['cnt']) if 'cnt' in row and pd.notna(row['cnt']) else None
    })

# Sort results by avg_rating descending
results = sorted(results, key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_N2qbLxXG7W2vzzVseWhM1qIS': [], 'var_call_bKgiZdp839YEC8XzGpX9uGez': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_0vCbciBB3vrW53koFJsUh28l': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}]}

exec(code, env_args)
