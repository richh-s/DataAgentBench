code = """import json
import pandas as pd

# Read the review data from the file
with open('/mnt/data/records_6d3x9g9.json', 'r') as f:
    review_data = json.load(f)

# Massage business gmap_ids from previous query
massage_business_ids = ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28']

# Filter for massage business reviews only
massage_reviews = [r for r in review_data if r['gmap_id'] in massage_business_ids]

# Convert to DataFrame for easier analysis
df = pd.DataFrame(massage_reviews)

# Convert rating to numeric
df['rating'] = pd.to_numeric(df['rating'])

# Compute average rating per business
avg_ratings = df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'num_reviews']

# Round avg_rating to 2 decimal places
avg_ratings['avg_rating'] = avg_ratings['avg_rating'].round(2)

# Filter for average rating >= 4.0
high_rated = avg_ratings[avg_ratings['avg_rating'] >= 4.0]

# Get business names and sort by avg_rating descending
business_info = {
    'gmap_22': 'Angel-A Massage',
    'gmap_25': 'Elite Massage', 
    'gmap_33': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)',
    'gmap_24': 'SUSY massage',
    'gmap_20': 'Aurora Massage',
    'gmap_21': 'Orient Massage',
    'gmap_28': 'Good Massage'
}

high_rated['business_name'] = high_rated['gmap_id'].map(business_info)
high_rated = high_rated.sort_values('avg_rating', ascending=False)

# Format result
result = high_rated[['business_name', 'avg_rating', 'num_reviews']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
