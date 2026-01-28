code = """import json
import pandas as pd

file_path = var_functions.query_db_5

with open(file_path, 'r') as f:
    review_data = json.load(f)

print(f"Loaded {len(review_data)} reviews")

# Create DataFrame
df = pd.DataFrame(review_data)

# Group by gmap_id and count reviews
gmap_counts = df['gmap_id'].value_counts().reset_index()
gmap_counts.columns = ['gmap_id', 'review_count']

print("Top 10 businesses by 4.5+ rating reviews in 2019:")
print(gmap_counts.head(10))

# Get top 3
top_3 = gmap_counts.head(3)

print("__RESULT__:")
print(top_3.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'rating': '5', 'time': 'September 03, 2020 at 04:15 PM'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2021-04-12 17:07:52'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2018-04-23 16:24:26'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2017-07-10 22:12:19'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'June 12, 2021 at 06:15 PM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'January 06, 2021 at 12:12 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'February 09, 2021 at 12:47 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'March 07, 2019 at 12:56 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '2017-05-16 01:01:41'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '18 Jan 2019, 03:19'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
