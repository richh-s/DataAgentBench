code = """import json
import pandas as pd

# Access the stored results using the correct variable names
business_data = locals()['var_functions.query_db:6']
review_data = locals()['var_functions.query_db:8']

# Convert to DataFrames for easier processing
business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

# Convert rating to numeric
review_df['rating'] = pd.to_numeric(review_df['rating'])

# Group by gmap_id and calculate average rating
avg_ratings = review_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

# Filter businesses with average rating >= 4.0
high_rated = avg_ratings[avg_ratings['avg_rating'] >= 4.0]

# Merge with business data to get business names
result = pd.merge(high_rated, business_df[['gmap_id', 'name']], on='gmap_id', how='inner')

# Sort by avg_rating descending
result = result.sort_values('avg_rating', ascending=False)

# Calculate average ratings to 2 decimal places
result['avg_rating'] = result['avg_rating'].round(2)

# Create final output - just name and avg_rating
final_result = result[['name', 'avg_rating']].to_dict('records')

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '3'}, {'gmap_id': 'gmap_25', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '2'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '4'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '4'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}], 'var_functions.execute_python:18': {'available_variables': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', '__builtins__', 'json']}}

exec(code, env_args)
