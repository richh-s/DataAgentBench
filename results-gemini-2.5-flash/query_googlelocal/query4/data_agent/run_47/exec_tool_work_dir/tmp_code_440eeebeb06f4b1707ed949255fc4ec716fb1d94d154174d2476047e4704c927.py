code = """import json
import re

# Access the raw string result from the previous query_db call
# The variable 'var_function-call-16734970030880208519' is the entire dictionary output from the tool.
db_response_dict = locals()['var_function-call-16734970030880208519']
raw_db_result_str = db_response_dict['query_db_response']['results'][0]

# Use regex to extract the JSON array string from the potentially verbose output
json_array_match = re.search(r'\[.*\]', raw_db_result_str, re.DOTALL)

if json_array_match:
    json_array_str = json_array_match.group(0)
    review_data = json.loads(json_array_str)

    extracted_data = []
    gmap_ids = []
    for item in review_data:
        gmap_id = item['gmap_id']
        # Ensure 'high_rating_review_count' is converted to an integer
        high_rating_review_count = int(item['high_rating_review_count'])
        extracted_data.append({'gmap_id': gmap_id, 'high_rating_review_count': high_rating_review_count})
        gmap_ids.append(gmap_id)

    print('__RESULT__:')
    print(json.dumps({'extracted_data': extracted_data, 'gmap_ids': gmap_ids}))
else:
    print('__RESULT__:')
    print(json.dumps({'extracted_data': [], 'gmap_ids': []}))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
