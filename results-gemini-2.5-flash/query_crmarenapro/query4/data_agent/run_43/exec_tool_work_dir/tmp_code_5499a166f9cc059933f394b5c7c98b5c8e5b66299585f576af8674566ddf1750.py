code = """import json
from datetime import datetime

# Access the raw output from the previous tool call
query_result_dict = locals()['var_function-call-14427941967854933840']

# The actual query result is nested under 'query_db_response' and then 'results'.
# 'results' is a list, and the actual string containing the JSON is the first element of this list.
raw_output_string = query_result_dict['query_db_response']['results'][0]

# Extract the JSON array string by finding the relevant substring.
# The JSON data is embedded after "The result is:\n" and has a trailing newline which we strip.
json_start_tag = "The result is:\n"
json_start_index = raw_output_string.find(json_start_tag) + len(json_start_tag)
json_data_string = raw_output_string[json_start_index:].strip()

# Parse the JSON string to get the list of dictionaries
order_item_ids_raw = json.loads(json_data_string)

# Clean and extract the item IDs: remove '#' and strip whitespace
order_item_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_raw]

# Prepare the IDs for the SQL IN clause by single-quoting each ID
quoted_ids_for_sql = [f"'{id_val}'" for id_val in order_item_ids]

# Join the quoted IDs to form the IN clause content
in_clause_values = ', '.join(quoted_ids_for_sql)

# Construct the full SQL query string for PostgreSQL.
# "Case", "orderitemid__c", and "createddate" must be double-quoted for PostgreSQL due to mixed-case names.
# Use a raw string literal (r prefix) for the SQL query string to handle backslashes correctly if any, though not strictly needed here.
# Ensure the Python string itself does not interfere with the SQL string structure.
sql_query = f'SELECT "createddate" FROM "Case" WHERE "orderitemid__c" IN ({in_clause_values});'

# Print the resulting SQL query string as a JSON-serializable string
print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-14427941967854933840': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
