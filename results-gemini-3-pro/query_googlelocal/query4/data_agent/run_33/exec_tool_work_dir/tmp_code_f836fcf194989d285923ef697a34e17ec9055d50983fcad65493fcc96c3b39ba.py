code = """import pandas as pd
import json
from dateutil import parser

# Get the file path from the previous variable
file_path = locals()['var_function-call-6489069949346524754']

# Load the reviews
with open(file_path, 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)

# Convert rating to float
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Filter by rating >= 4.5
df = df[df['rating'] >= 4.5]

# Function to extract year
def get_year(time_str):
    try:
        if not isinstance(time_str, str):
            return None
        dt = parser.parse(time_str)
        return dt.year
    except:
        return None

df['year'] = df['time'].apply(get_year)

# Filter for year 2019
df_2019 = df[df['year'] == 2019]

# Count reviews per gmap_id
counts = df_2019['gmap_id'].value_counts().reset_index()
counts.columns = ['gmap_id', 'review_count']

# Get top 3
top_3 = counts.head(3)

print("__RESULT__:")
print(top_3.to_json(orient='records'))"""

env_args = {'var_function-call-18107951898994660558': [{'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2021-04-12 17:07:52', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2018-04-23 16:24:26', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2017-07-10 22:12:19', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'gmap_id': 'gmap_44'}], 'var_function-call-1961291217156253887': [{'count(*)': '2000'}], 'var_function-call-6489069949346524754': 'file_storage/function-call-6489069949346524754.json'}

exec(code, env_args)
