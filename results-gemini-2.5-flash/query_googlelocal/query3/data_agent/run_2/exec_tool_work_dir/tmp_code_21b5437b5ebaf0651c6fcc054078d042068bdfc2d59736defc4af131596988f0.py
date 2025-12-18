code = """import json
import pandas as pd

filtered_businesses_path = locals()['var_function-call-17887064346993606697']
reviews_data_path = locals()['var_function-call-7572177186537588015']

with open(filtered_businesses_path, 'r') as f:
    filtered_businesses = json.load(f)

with open(reviews_data_path, 'r') as f:
    reviews_data = json.load(f)

df_filtered_businesses = pd.DataFrame(filtered_businesses)
df_reviews = pd.DataFrame(reviews_data)

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

average_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
average_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

merged_df = pd.merge(df_filtered_businesses, average_ratings, on='gmap_id', how='inner')

sorted_businesses = merged_df.sort_values(by='average_rating', ascending=False)
top_5_businesses = sorted_businesses.head(5)[['name', 'hours', 'average_rating']]

print("__RESULT__:")
print(top_5_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-17531646216573112097': 'file_storage/function-call-17531646216573112097.json', 'var_function-call-17887064346993606697': 'file_storage/function-call-17887064346993606697.json', 'var_function-call-7572177186537588015': 'file_storage/function-call-7572177186537588015.json'}

exec(code, env_args)
