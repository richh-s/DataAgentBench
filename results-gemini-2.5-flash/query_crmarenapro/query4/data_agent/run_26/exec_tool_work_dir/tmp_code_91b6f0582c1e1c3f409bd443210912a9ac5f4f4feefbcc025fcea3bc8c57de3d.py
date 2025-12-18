code = """import json

# The raw output from query_db is a dictionary with a 'query_db_response' key.
# The value associated with 'query_db_response' is another dictionary, which has a 'results' key.
# The 'results' key's value is a list, and the first element of this list is a string.
# This string contains the JSON representation of the list of dictionaries we are interested in.
raw_output_string_from_db = locals()['var_function-call-9684108676081928726']['query_db_response']['results'][0]

# The string looks like:\nThe tool query_db was executed successfully.\n\nThe result is stored under key:\nvar_function-call-9684108676081928726\n\nThe result is:\n[{{"Id": "#802Wt0000078yuGIAQ"}}, ...]
# We need to extract the actual JSON array string from this larger string.

# Find the index of the first '[' and last ']'
json_start_index = raw_output_string_from_db.find('[')
json_end_index = raw_output_string_from_db.rfind(']')

# Extract the substring that contains only the JSON array
json_array_str = raw_output_string_from_db[json_start_index : json_end_index + 1]

# Parse the JSON string into a Python list of dictionaries
parsed_order_item_ids = json.loads(json_array_str)

# Extract 'Id' values and clean them up (remove '#' and strip whitespace)
order_item_ids = [item['Id'].replace('#', '').strip() for item in parsed_order_item_ids]

# Format the IDs for the SQL IN clause, ensuring each is quoted
id_list_str = ', '.join([f"'{oid}'" for oid in order_item_ids])

# Construct the final SQL query for the 'support' database (PostgreSQL)
# The table name \"Case\" needs to be quoted because it might be a reserved keyword or mixed-case.
sql_query = f'SELECT createddate FROM "Case" WHERE orderitemid__c IN ({id_list_str});'

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-15518888999152830853': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-9684108676081928726': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
