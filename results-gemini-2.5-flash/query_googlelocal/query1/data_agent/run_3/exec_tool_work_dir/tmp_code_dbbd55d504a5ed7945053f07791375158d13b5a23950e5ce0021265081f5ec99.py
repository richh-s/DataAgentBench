code = """import pandas as pd
import json

business_data = locals()['var_function-call-2659360206557064791']
review_data = locals()['var_function-call-13763239324144717517']

business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

review_df['rating'] = review_df['rating'].astype(int)
average_ratings = review_df.groupby('gmap_id')['rating'].mean().reset_index()
average_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

merged_df = pd.merge(business_df, average_ratings, on='gmap_id')

sorted_businesses = merged_df.sort_values(by='average_rating', ascending=False)
top_5_businesses = sorted_businesses.head(5)

result = []
for index, row in top_5_businesses.iterrows():
    result.append({'name': row['name'], 'average_rating': round(row['average_rating'], 2)})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9852848788310143683': [], 'var_function-call-2659360206557064791': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-13763239324144717517': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '3'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}]}

exec(code, env_args)
