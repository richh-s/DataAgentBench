code = """import pandas as pd
business_data = locals()['var_function-call-4650304912099587042']
review_data = locals()['var_function-call-5396663482894386193']

business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

# Convert 'rating' column to numeric
review_df['rating'] = pd.to_numeric(review_df['rating'])

# Merge the two dataframes
merged_df = pd.merge(business_df, review_df, on='gmap_id')

# Calculate average rating for each business
average_ratings = merged_df.groupby('name')['rating'].mean().reset_index()
average_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Filter businesses with average rating of at least 4.0
high_rated_businesses = average_ratings[average_ratings['average_rating'] >= 4.0]

# Convert to dictionary for output
result = high_rated_businesses.to_dict(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7290790458096822378': [], 'var_function-call-7428057111914331084': [], 'var_function-call-5222262404099714901': [], 'var_function-call-16446528833611637129': [], 'var_function-call-4650304912099587042': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-5396663482894386193': [{'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '3'}, {'gmap_id': 'gmap_25', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '2'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '4'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '4'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}]}

exec(code, env_args)
