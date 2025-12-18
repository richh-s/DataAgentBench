code = """import json
import re

# Access the raw string result from the previous query_db call
db_response_dict = locals()['var_function-call-16734970030880208519']
raw_db_result_str = db_response_dict['query_db_response']['results'][0]

# Split the string by lines and find the line containing the JSON array
json_array_str = ""
for line in raw_db_result_str.splitlines():
    stripped_line = line.strip()
    if stripped_line.startswith('[') and stripped_line.endswith(']'):
        json_array_str = stripped_line
        break

if json_array_str:
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
