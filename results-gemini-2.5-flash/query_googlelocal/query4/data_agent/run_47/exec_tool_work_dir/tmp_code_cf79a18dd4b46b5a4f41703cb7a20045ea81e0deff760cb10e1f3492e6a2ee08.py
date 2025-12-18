code = """import json
import re

# The entire tool output is stored in locals()['var_function-call-16734970030880208519']
full_output_str = locals()['var_function-call-16734970030880208519']['query_db_response']['results'][0]

# Use regex to extract the JSON array string
json_array_match = re.search(r'\[.*\]', full_output_str, re.DOTALL)

if json_array_match:
    json_array_str = json_array_match.group(0)
    review_data = json.loads(json_array_str)

    extracted_data = []
    gmap_ids = []
    for item in review_data:
        gmap_id = item['gmap_id']
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
