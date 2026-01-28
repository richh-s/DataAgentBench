code = """import pandas as pd
import json
# Data from previous query_db calls
df_business = pd.DataFrame(var_call_UrDaoO7crcvK4m8ysUuVXOJ6)
df_reviews = pd.DataFrame(var_call_UmkbC421aatz3ohrw5yD0ZoT)

# Convert numeric fields
if not df_reviews.empty:
    df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)
    df_reviews['review_count'] = df_reviews['review_count'].astype(int)

# Merge on gmap_id
df_merged = pd.merge(df_business, df_reviews, on='gmap_id', how='inner')

# Filter for avg_rating >= 4.0
df_result = df_merged[df_merged['avg_rating'] >= 4.0].copy()

# Prepare output list of dicts with rounded ratings
output = []
for _, row in df_result.iterrows():
    output.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'avg_rating': round(float(row['avg_rating']), 2),
        'review_count': int(row['review_count'])
    })

# Sort by avg_rating descending
output = sorted(output, key=lambda x: (-x['avg_rating'], x['name']))

# Print in required format as a JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_UrDaoO7crcvK4m8ysUuVXOJ6': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_UmkbC421aatz3ohrw5yD0ZoT': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)
