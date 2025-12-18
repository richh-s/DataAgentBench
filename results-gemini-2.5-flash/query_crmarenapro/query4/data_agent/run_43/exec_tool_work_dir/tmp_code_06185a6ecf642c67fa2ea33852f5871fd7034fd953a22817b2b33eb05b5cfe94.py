code = """import json
from datetime import datetime

# Access the raw output string from the previous tool call
raw_output_string = locals()['var_function-call-14427941967854933840']['results'][0]

# The actual JSON array is embedded within a larger string. We need to find and extract it.
# The JSON array starts with '[' and ends with ']'.
json_start_index = raw_output_string.find('[')
json_end_index = raw_output_string.rfind(']') + 1

# Extract the JSON string part
json_data_string = raw_output_string[json_start_index:json_end_index]

# Parse the JSON string to get the list of dictionaries
order_item_ids_raw = json.loads(json_data_string)

# Clean and extract the item IDs. Remove '#' and strip whitespace.
order_item_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_raw]

# Prepare the IDs for the SQL IN clause by single-quoting each ID
quoted_ids_for_sql = [f"'{id_val}'" for id_val in order_item_ids]

# Construct the full SQL query string for PostgreSQL.
# "Case" and "orderitemid__c" must be double-quoted as per PostgreSQL conventions for mixed-case names.
# "createddate" needs to be double-quoted as well.
sql_query = f'SELECT "createddate" FROM "Case" WHERE "orderitemid__c" IN ({', '.join(quoted_ids_for_sql)});'

# Print the resulting SQL query string as a JSON-serializable string
print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-14427941967854933840': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
