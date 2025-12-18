code = """import json
import pandas as pd

# Directly use the result of the previous query, which is a list of dicts
review_data = locals()['var_function-call-5084043016580269099']
df_review = pd.DataFrame(review_data)

# Extract gmap_ids to a list
gmap_ids = df_review['gmap_id'].tolist()

# Convert gmap_ids to a comma-separated string for the SQL IN clause
# Each gmap_id needs to be quoted, e.g., 'gmap_20', 'gmap_53'
gmap_ids_str = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])

print('__RESULT__:')
print(json.dumps(gmap_ids_str))"""

env_args = {'var_function-call-5084043016580269099': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
