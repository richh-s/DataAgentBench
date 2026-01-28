code = """import pandas as pd
import json

# The reviews data is available as var_functions.query_db:0
# The massage businesses data is available as var_functions.query_db:2

# Access the data from storage
reviews_data = locals()['var_functions.query_db:0']
businesses_data = locals()['var_functions.query_db:2']

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_reviews['rating'] = df_reviews['rating'].astype(float)

# Massage businesses
massage_gmap_ids = [biz['gmap_id'] for biz in businesses_data]
massage_names = {biz['gmap_id']: biz['name'] for biz in businesses_data}

# Filter reviews for massage businesses only
df_massage_reviews = df_reviews[df_reviews['gmap_id'].isin(massage_gmap_ids)]

# Calculate average rating for each massage business
avg_ratings = df_massage_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating']

# Filter businesses with average rating >= 4.0
high_rated = avg_ratings[avg_ratings['avg_rating'] >= 4.0]

# Add business names
high_rated['business_name'] = high_rated['gmap_id'].map(massage_names)

# Sort by rating (descending)
result = high_rated[['business_name', 'avg_rating']].sort_values('avg_rating', ascending=False)

# Convert to list of dictionaries for JSON serialization
result_list = result.to_dict('records')

# Print in the required format
print('__RESULT__:')
print(json.dumps(result_list, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}]}

exec(code, env_args)
