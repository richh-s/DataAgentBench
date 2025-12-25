code = """import pandas as pd
import json

businesses = locals()['var_function-call-13576076299731638132']
ratings = locals()['var_function-call-3929087916353853908']

df_bus = pd.DataFrame(businesses)
df_rat = pd.DataFrame(ratings)

# Ensure rating is numeric
df_rat['rating'] = pd.to_numeric(df_rat['rating'])

# Calculate average rating
avg_ratings = df_rat.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Merge with business info
result = pd.merge(df_bus, avg_ratings, on='gmap_id')

# Sort by avg_rating descending
result = result.sort_values(by='avg_rating', ascending=False)

# Get top 5
top_5 = result.head(5)

# Format the output
output = top_5[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-15894347930259090757': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-13576076299731638132': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-3929087916353853908': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '3'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}]}

exec(code, env_args)
