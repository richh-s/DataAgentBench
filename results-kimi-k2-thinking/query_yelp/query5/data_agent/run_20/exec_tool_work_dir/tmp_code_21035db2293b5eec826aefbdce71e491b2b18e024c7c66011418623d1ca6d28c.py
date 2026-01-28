code = """import json
import pandas as pd

# Read the review data for PA businesses
review_file_path = locals()['var_functions.query_db:18']
with open(review_file_path, 'r') as f:
    review_data = json.load(f)

# Create DataFrame
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating
average_rating = df_reviews['rating'].mean()
count_reviews = len(df_reviews)

print('__RESULT__:')
print(json.dumps({
    'state': 'PA',
    'average_rating': round(average_rating, 2),
    'total_reviews': count_reviews,
    'total_wifi_businesses': 8
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'top_state': 'PA', 'top_state_count': 8, 'total_wifi_businesses': 21, 'state_counts': {'PA': 8, 'FL': 5, 'IN': 2, 'MO': 2, 'IL': 1, 'LA': 1, 'NV': 1, 'ID': 1}}, 'var_functions.execute_python:14': {'pa_wifi_business_ids': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82'], 'count': 8}, 'var_functions.execute_python:16': {'pa_business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
