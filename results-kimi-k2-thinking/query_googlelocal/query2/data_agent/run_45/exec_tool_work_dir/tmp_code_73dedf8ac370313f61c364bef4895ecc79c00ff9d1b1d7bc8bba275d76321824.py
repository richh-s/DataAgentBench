code = """import json
import pandas as pd

# Load the full review data from the file
reviews_file = locals()['var_functions.query_db:14']
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Load the business data
businesses = locals()['var_functions.query_db:6']

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_businesses = pd.DataFrame(businesses)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'average_rating']

# Filter businesses with average rating >= 4.0
high_rated = avg_ratings[avg_ratings['average_rating'] >= 4.0]

# Merge with business names
result = pd.merge(high_rated, df_businesses[['gmap_id', 'name']], on='gmap_id')

# Sort by average rating descending
result = result.sort_values('average_rating', ascending=False)

# Create a list of business names with their ratings
results_list = []
for _, row in result.iterrows():
    business_name = row['name']
    avg_rating = row['average_rating']
    results_list.append([business_name, round(avg_rating, 2)])

print('__RESULT__:')
print(json.dumps(results_list))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.list_db:1': ['review'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_functions.execute_python:12': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
