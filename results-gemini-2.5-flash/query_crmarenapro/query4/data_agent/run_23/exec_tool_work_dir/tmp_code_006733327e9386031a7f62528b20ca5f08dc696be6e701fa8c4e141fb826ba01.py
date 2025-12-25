code = """import json
import re

raw_output_string = locals()['var_function-call-9320036195922497951']['results'][0]

# Extract the JSON array string using regex
match = re.search(r'\[.*\]', raw_output_string, re.DOTALL)

if match:
    json_list_string = match.group(0)
    order_item_ids_list = json.loads(json_list_string)
    cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in order_item_ids_list]
    ids_string = ', '.join(cleaned_ids)
else:
    ids_string = '' # Handle case where JSON list is not found

print("__RESULT__:")
print(json.dumps(ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
