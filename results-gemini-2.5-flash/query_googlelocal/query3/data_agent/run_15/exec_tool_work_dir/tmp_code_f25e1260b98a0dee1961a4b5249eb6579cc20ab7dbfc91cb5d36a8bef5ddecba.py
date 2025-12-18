code = """import pandas as pd
import json

filtered_businesses_path = locals()['var_function-call-9986999021756992693']
reviews_path = locals()['var_function-call-4657041441758768857']

with open(filtered_businesses_path, 'r') as f:
    filtered_businesses = json.load(f)

with open(reviews_path, 'r') as f:
    reviews = json.load(f)

df_filtered_businesses = pd.DataFrame(filtered_businesses)
df_reviews = pd.DataFrame(reviews)

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
average_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
average_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

merged_df = pd.merge(df_filtered_businesses, average_ratings, on='gmap_id', how='inner')

sorted_businesses = merged_df.sort_values(by='average_rating', ascending=False)
top_5_businesses = sorted_businesses.head(5)

result = top_5_businesses[['name', 'hours', 'average_rating']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10971755212049758279': 'file_storage/function-call-10971755212049758279.json', 'var_function-call-9986999021756992693': 'file_storage/function-call-9986999021756992693.json', 'var_function-call-4657041441758768857': 'file_storage/function-call-4657041441758768857.json'}

exec(code, env_args)
