code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-13029525185552882347'], 'r') as f:
    reviews_data = json.load(f)

df_reviews = pd.DataFrame(reviews_data)

# Convert 'time' column to datetime objects
df_reviews['time'] = pd.to_datetime(df_reviews['time'], errors='coerce')

# Filter for reviews in 2019
df_2019_reviews = df_reviews[df_reviews['time'].dt.year == 2019]

# Count high-rating reviews per gmap_id
high_rating_counts = df_2019_reviews['gmap_id'].value_counts().reset_index()
high_rating_counts.columns = ['gmap_id', 'high_rating_review_count']

print("__RESULT__:")
print(high_rating_counts.to_json(orient='records'))"""

env_args = {'var_function-call-13029525185552882347': 'file_storage/function-call-13029525185552882347.json'}

exec(code, env_args)
