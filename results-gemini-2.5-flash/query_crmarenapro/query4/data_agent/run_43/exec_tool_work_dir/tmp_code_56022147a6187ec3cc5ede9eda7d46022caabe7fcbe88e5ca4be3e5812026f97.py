code = """import json
from datetime import datetime

# Access the raw output from the previous tool call
query_result = locals()['var_function-call-14427941967854933840']

# The actual result is nested under 'query_db_response' and then 'results'
raw_output_list = query_result['query_db_response']['results']

# The first element of the list contains the string with the JSON data
raw_output_string = raw_output_list[0]

# Extract the JSON array part from the raw_output_string
# It starts after "The result is:\n" and ends before the last '\n'
json_start_tag = "The result is:\n"
json_start_index = raw_output_string.find(json_start_tag) + len(json_start_tag)
json_end_index = raw_output_string.rfind('\n')

json_data_string = raw_output_string[json_start_index:json_end_index].strip()

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
