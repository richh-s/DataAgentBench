code = """import json
import re

# Access the raw string result from the previous query_db call
raw_db_result = locals()['var_function-call-16734970030880208519']['query_db_response']['results'][0]

# Use a regex to extract only the JSON array part from the string
json_array_str_match = re.search(r'\[.*\]', raw_db_result, re.DOTALL)

if json_array_str_match:
    json_array_str = json_array_str_match.group(0)
    review_data = json.loads(json_array_str)
    gmap_ids = [item['gmap_id'] for item in review_data]
    print('__RESULT__:')
    print(json.dumps(gmap_ids))
else:
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
