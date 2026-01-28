code = """import json
import pandas as pd
import re

# Load the review data from the file
file_path = var_functions.query_db_5
with open(file_path, 'r') as f:
    review_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(review_data)
print(f"Total records loaded: {len(df)}")
print("Sample records:")
print(df.head())
print("\nRating distribution:")
print(df['rating'].value_counts())

# Count reviews by gmap_id
gmap_counts = df['gmap_id'].value_counts()
print(f"\nTop 10 businesses by high-rating review count:")
print(gmap_counts.head(10))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'rating': '5', 'time': 'September 03, 2020 at 04:15 PM'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2021-04-12 17:07:52'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2018-04-23 16:24:26'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2017-07-10 22:12:19'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'June 12, 2021 at 06:15 PM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'January 06, 2021 at 12:12 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'February 09, 2021 at 12:47 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'March 07, 2019 at 12:56 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '2017-05-16 01:01:41'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '18 Jan 2019, 03:19'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
