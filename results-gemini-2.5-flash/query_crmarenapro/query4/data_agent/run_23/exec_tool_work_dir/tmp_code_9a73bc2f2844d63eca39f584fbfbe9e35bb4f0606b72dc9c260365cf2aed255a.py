code = """import json
import re

# The raw output from the query_db tool call is a dictionary. The actual result is a list of strings
# under the 'results' key. In this case, the first element of this list is a string
# that contains the JSON array of IDs along with other descriptive text.
raw_output_message_string = locals()['var_function-call-9320036195922497951']['results'][0]

# Use a regular expression to extract the JSON array string from the raw output message.
# The pattern r'\[.*\]' will find the outermost square brackets and everything inside.
# re.DOTALL is used to ensure that '.' matches newline characters as well.
match = re.search(r'\[.*\]', raw_output_message_string, re.DOTALL)

cleaned_ids_string = ''
if match:
    # Extract the matched JSON array string (e.g., '[{"Id": "..."}, ...]')
    json_list_str = match.group(0)
    
    # Parse the JSON string into a Python list of dictionaries
    order_item_ids_list = json.loads(json_list_str)
    
    # Iterate through the list of dictionaries, clean each 'Id', and format for SQL IN clause
    cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in order_item_ids_list]
    cleaned_ids_string = ', '.join(cleaned_ids)

print("__RESULT__:")
print(json.dumps(cleaned_ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
