code = """import pandas as pd
import json
# Load results from previous queries
business = pd.DataFrame(var_call_9EIEh4OM8FStjTl4cB9wMstM)
reviews = pd.DataFrame(var_call_SvSiQVZtljwsHC46yiV7NvKj)
# Ensure numeric avg_rating
if not reviews.empty:
    reviews['avg_rating'] = pd.to_numeric(reviews['avg_rating'])
# Merge on gmap_id
merged = pd.merge(business, reviews, on='gmap_id', how='inner')
# Filter average rating >= 4.0
result_df = merged[merged['avg_rating'] >= 4.0].copy()
# Prepare output list
output = []
for _, row in result_df.sort_values('avg_rating', ascending=False).iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 2)
    })
# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_6Fy7EndUBP0QhmsYTLIqYiH5': [], 'var_call_9EIEh4OM8FStjTl4cB9wMstM': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_SvSiQVZtljwsHC46yiV7NvKj': [{'gmap_id': 'gmap_20', 'avg_rating': '4.18', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.93', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.33', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.88', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.88', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.13', 'review_count': '8'}]}

exec(code, env_args)
