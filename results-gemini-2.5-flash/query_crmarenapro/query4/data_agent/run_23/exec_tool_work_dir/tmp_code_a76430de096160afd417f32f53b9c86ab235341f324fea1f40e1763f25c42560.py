code = """import json
import re

# Access the raw output string correctly.
# var_function-call-9320036195922497951 contains the full dictionary from query_db_response.
raw_output_message_string = locals()['var_function-call-9320036195922497951']['query_db_response']['results'][0]

# Use a regular expression to extract the JSON array string from the raw output message.
match = re.search(r'\[.*?\]', raw_output_message_string, re.DOTALL)

cleaned_ids_string = ''
if match:
    json_list_str = match.group(0)
    order_item_ids_list = json.loads(json_list_str)
    cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in order_item_ids_list]
    cleaned_ids_string = ', '.join(cleaned_ids)

print("__RESULT__:")
print(json.dumps(cleaned_ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
