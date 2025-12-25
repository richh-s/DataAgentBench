code = """import json
import pandas as pd

review_counts_data = json.loads(locals()['var_function-call-717367244536023637'][0])
gmap_ids = [item["gmap_id"] for item in review_counts_data]
gmap_ids_str = "', '".join(gmap_ids)
print("__RESULT__:")
print(json.dumps(gmap_ids_str))"""

env_args = {'var_function-call-717367244536023637': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
