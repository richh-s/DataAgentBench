code = """import json
import pandas as pd

review_data_str = locals()['var_function-call-5084043016580269099']['query_db_response']['results'][0]
review_data = json.loads(review_data_str)
df_review = pd.DataFrame(review_data)

gmap_ids = df_review['gmap_id'].tolist()
print('__RESULT__:')
print(json.dumps(gmap_ids))"""

env_args = {'var_function-call-5084043016580269099': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
