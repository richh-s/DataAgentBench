code = """import json
import pandas as pd

# Load results from previous query_db calls
biz = pd.DataFrame(var_call_U27vsu4tj9xfDCtEjKrldptP)
ratings = pd.DataFrame(var_call_mciNqAt96oQN0OlgobVab39Q)

# Convert types
ratings['avg_rating'] = ratings['avg_rating'].astype(float)
ratings['review_count'] = ratings['review_count'].astype(int)

# Merge on gmap_id
merged = pd.merge(biz, ratings, on='gmap_id', how='inner')

# Filter businesses with avg_rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Prepare result list
result_list = []
for _, row in filtered.sort_values('avg_rating', ascending=False).iterrows():
    result_list.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 3)
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_wYIOvOBpT0DYkcCO237XRTdk': [], 'var_call_U27vsu4tj9xfDCtEjKrldptP': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_mciNqAt96oQN0OlgobVab39Q': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)
