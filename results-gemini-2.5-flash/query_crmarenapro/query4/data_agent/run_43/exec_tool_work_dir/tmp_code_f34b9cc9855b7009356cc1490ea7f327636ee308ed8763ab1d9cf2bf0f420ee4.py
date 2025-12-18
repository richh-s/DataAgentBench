code = """import json
from datetime import datetime

# Access the raw output from the previous tool call
query_result = locals()['var_function-call-14427941967854933840']

# The actual result is nested under 'query_db_response' and then 'results'
raw_output_string = query_result['query_db_response']['results'][0]

# The raw_output_string itself contains the JSON array that needs to be parsed.
# It looks like: "\nThe tool query_db was executed successfully.\n\nThe result is stored under key:\nvar_function-call-14427941967854933840\n\nThe result is:\n[{\"Id\": \"#802Wt0000078yuGIAQ\"}, ...]\n"

# Find the start of the actual JSON array
json_start_index = raw_output_string.find('[{')
json_end_index = raw_output_string.rfind('}]})') + 1 # Adjust for potential trailing '}'

# If json_start_index is -1, it means the structure is different, or it wasn't found
# Let's assume a simpler case first for finding '[' and ']'
json_start_index = raw_output_string.find('[')
json_end_index = raw_output_string.rfind(']') + 1

# Extract the JSON string
json_data_string = raw_output_string[json_start_index:json_end_index]

# Parse the JSON string to get the list of dictionaries
order_item_ids_raw = json.loads(json_data_string)

# Clean and extract the item IDs: remove '#' and strip whitespace
order_item_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_raw]

# Prepare the IDs for the SQL IN clause by single-quoting each ID
quoted_ids_for_sql = [f"'{id_val}'" for id_val in order_item_ids]

# Construct the full SQL query string for PostgreSQL.
# "Case", "orderitemid__c", and "createddate" must be double-quoted for PostgreSQL due to mixed-case names.
sql_query = f'SELECT "createddate" FROM "Case" WHERE "orderitemid__c" IN ({', '.join(quoted_ids_for_sql)});'

# Print the resulting SQL query string as a JSON-serializable string
print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-14427941967854933840': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
