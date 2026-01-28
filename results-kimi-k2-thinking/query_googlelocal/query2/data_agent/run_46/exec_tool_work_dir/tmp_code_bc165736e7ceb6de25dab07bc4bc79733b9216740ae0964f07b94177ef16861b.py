code = """import json
import pandas as pd

# Get the review data from storage
review_data = locals()['var_functions.query_db:5']

# If the result is a file path, read it
if isinstance(review_data, str) and review_data.endswith('.json'):
    with open(review_data, 'r') as f:
        review_data = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating for each business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()

# Filter businesses with average rating >= 4.0
high_rated = avg_ratings[avg_ratings['rating'] >= 4.0]

# Get business names from the business data
business_data = locals()['var_functions.query_db:2']
df_business = pd.DataFrame(business_data)

# Merge to get business names
result = pd.merge(high_rated, df_business, on='gmap_id', how='left')
result = result[['name', 'rating']].sort_values('rating', ascending=False)

# Convert to JSON serializable format
result_json = result.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1', 'hours': 'None', 'MISC': 'None', 'state': 'None'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'MISC': '{"Health & safety": ["Mask required", "Staff wear masks"], "Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.', 'num_of_reviews': '56', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.', 'num_of_reviews': '15', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 8PM'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}], 'var_functions.query_db:2': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
