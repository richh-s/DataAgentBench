code = """import json
import re

# The result from the query_db tool call is a dictionary with a specific structure.
# It contains a 'query_db_response' key, which itself holds a 'results' key.
# The 'results' key's value is a list, and the actual data (a JSON string)
# is the first element of that list.
raw_output_message_string = locals()['var_function-call-9320036195922497951']['query_db_response']['results'][0]

# Use a regular expression to extract the JSON array string from the raw output message.
# The pattern r'\[.*\]' matches a string that starts with '[' and ends with ']',
# capturing everything in between. re.DOTALL is crucial here as it allows '.' to match
# newline characters, in case the JSON string spans multiple lines.
match = re.search(r'\[.*\]', raw_output_message_string, re.DOTALL)

cleaned_ids_string = ''

if match:
    # If a match is found, extract the JSON array string.
    json_list_str = match.group(0)
    
    # Parse the extracted JSON string into a Python list of dictionaries.
    # Each dictionary in this list will have an 'Id' key.
    order_item_ids_list = json.loads(json_list_str)
    
    # Iterate through the list, cleaning each 'Id' by removing leading '#'
    # and stripping any whitespace, then format it for a SQL IN clause (e.g., 'ID_VALUE').
    cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in order_item_ids_list]
    
    # Join the cleaned and formatted IDs into a single comma-separated string.
    cleaned_ids_string = ', '.join(cleaned_ids)

# Print the final string of cleaned IDs, wrapped in a JSON string for tool output.
print("__RESULT__:")
print(json.dumps(cleaned_ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
