code = """import json
import re

# The result from the first query_db call is stored in var_function-call-9320036195922497951.
# This variable contains a dictionary with the structure: 
# {"query_db_response": {"results": ["<string containing JSON data>"]}}

# Step 1: Access the string that contains the actual JSON list of order item IDs.
# This string is the first (and likely only) element of the 'results' list.
raw_result_string = locals()['var_function-call-9320036195922497951']['query_db_response']['results'][0]

# Step 2: Use a regular expression to extract the JSON array string from the raw result string.
# The regex r'\[.*\]' matches any string starting with '[' and ending with ']', 
# including newlines (due to re.DOTALL), which is suitable for extracting the JSON array.
json_array_match = re.search(r'\[.*\]', raw_result_string, re.DOTALL)

cleaned_ids_for_sql = ''

if json_array_match:
    # Step 3: Extract the matched JSON array string.
    json_list_str = json_array_match.group(0)
    
    # Step 4: Parse the JSON string into a Python list of dictionaries.
    # Each dictionary in this list represents an order item ID (e.g., {"Id": "#802Wt..."}).
    order_item_dicts = json.loads(json_list_str)
    
    # Step 5: Process each dictionary to extract, clean, and format the 'Id' values.
    # Cleaning involves removing the leading '#' character and stripping any whitespace.
    # The IDs are then wrapped in single quotes for use in a SQL IN clause.
    cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in order_item_dicts]
    
    # Step 6: Join the cleaned and formatted IDs into a comma-separated string.
    cleaned_ids_for_sql = ', '.join(cleaned_ids)

# Step 7: Print the final comma-separated string of IDs as a JSON string.
print("__RESULT__:")
print(json.dumps(cleaned_ids_for_sql))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
