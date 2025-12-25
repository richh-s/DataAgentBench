code = """import json
import pandas as pd

# Correctly access the JSON string from the tool output
full_output_string = locals()['var_function-call-5084043016580269099']['query_db_response']['results'][0]

# Find the start and end of the actual JSON array
start_index = full_output_string.find('[')
end_index = full_output_string.rfind(']') + 1

# Extract the JSON array string
review_data_string = full_output_string[start_index:end_index]

# Parse the JSON string into a Python list of dictionaries
review_data = json.loads(review_data_string)

df_review = pd.DataFrame(review_data)

# Extract gmap_ids to a list
gmap_ids = df_review['gmap_id'].tolist()

# Convert gmap_ids to a comma-separated string for the SQL IN clause
gmap_ids_str = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])

print('__RESULT__:')
print(json.dumps(gmap_ids_str))"""

env_args = {'var_function-call-5084043016580269099': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
