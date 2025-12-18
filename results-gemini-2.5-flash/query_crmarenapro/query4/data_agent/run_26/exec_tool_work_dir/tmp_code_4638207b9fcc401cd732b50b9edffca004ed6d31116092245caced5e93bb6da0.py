code = """import json

# The result is a list where the first element is a string containing JSON data
raw_output_string = locals()['var_function-call-9684108676081928726']['results'][0]

# Find the start and end of the actual JSON array within the string
json_start = raw_output_string.find('[')
json_end = raw_output_string.rfind(']') + 1

# Extract the JSON array string
json_array_str = raw_output_string[json_start:json_end]

# Parse the JSON string into a Python list of dictionaries
parsed_order_item_ids = json.loads(json_array_str)

# Extract 'Id' values and clean them up (remove '#' and strip whitespace)
order_item_ids = [item['Id'].replace('#', '').strip() for item in parsed_order_item_ids]

# Format the IDs for the SQL IN clause, ensuring each is quoted
id_list_str = ', '.join([f"'{oid}'" for oid in order_item_ids])

# Construct the final SQL query for the 'support' database (PostgreSQL)
sql_query = f'SELECT createddate FROM "Case" WHERE orderitemid__c IN ({id_list_str});'

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-15518888999152830853': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-9684108676081928726': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
