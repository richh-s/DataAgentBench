code = """import json
import re

result_string_with_extra = locals()['var_function-call-15883378990604638904']['query_db_response']['results'][0]

# Extract the JSON array string from the overall string
json_match = re.search(r'\[.*\]', result_string_with_extra)
if json_match:
    json_array_string = json_match.group(0)
    parsed_list = json.loads(json_array_string)
    business_ref = parsed_list[0]['business_ref']
    business_id = 'businessid_' + business_ref.split('_')[1]
    print('__RESULT__:')
    print(json.dumps(business_id))
else:
    print('__RESULT__:')
    print(json.dumps('Error: Could not find JSON array in the result string.'))"""

env_args = {'var_function-call-15883378990604638904': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}]}

exec(code, env_args)
