code = """import json
import pandas as pd
import re

# Load data from storage using the variable names provided
business_result = var_functions.query_db:18
review_result = var_functions.query_db:20

# Read the JSON files from the stored paths
with open(business_result, 'r') as f:
    business_data = json.load(f)

with open(review_result, 'r') as f:
    review_data = json.load(f)

# Print sample data to debug
print('Business data sample:', business_data[:2])
print('Review data sample:', review_data[:2])

# Create DataFrames
df_business = pd.DataFrame(business_data)
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'average_rating']

# Merge business with average ratings
df_merged = df_business.merge(avg_ratings, on='gmap_id', how='inner')

print('Merged data shape:', df_merged.shape)
print('Sample merged data:', df_merged.head())

result = df_merged.head(5).to_dict('records')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_19', 'name': 'PODS Sacramento Hub'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_48', 'name': 'State Street/7th Street'}, {'gmap_id': 'gmap_50', 'name': 'HDR'}, {'gmap_id': 'gmap_18', 'name': 'Porvene Doors'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
