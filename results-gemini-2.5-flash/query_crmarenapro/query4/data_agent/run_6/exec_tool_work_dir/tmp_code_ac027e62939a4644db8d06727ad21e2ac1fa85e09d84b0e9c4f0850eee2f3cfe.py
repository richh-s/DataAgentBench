code = """import json

raw_result = locals()['var_function-call-8876751307380815954']
# The actual list of dictionaries is inside 'results' key, and is a stringified JSON within a list.
# The output format has an outer 'query_db_response' key, so we need to access that first.
string_with_json_and_info = raw_result['query_db_response']['results'][0]

# Extract the JSON array part from the string
start_index = string_with_json_and_info.find('[')
end_index = string_with_json_and_info.rfind(']')
json_array_str = string_with_json_and_info[start_index : end_index + 1]

order_item_ids = json.loads(json_array_str)
cleaned_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids]

ids_str = ', '.join([f"'{_id}'" for _id in cleaned_ids])

print("__RESULT__:")
print(json.dumps(ids_str))"""

env_args = {'var_function-call-8876751307380815954': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
