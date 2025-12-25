code = """import json

# Safely parse the JSON string from the results list
# The result is a list containing a string representation of a list of dictionaries
# So, first parse the outer list, then the inner string, then iterate.
parsed_results = json.loads(locals()['var_function-call-9684108676081928726']['results'][0])
order_item_ids_raw = [item['Id'] for item in parsed_results]

# Clean up IDs by removing '#' character
order_item_ids = [id_str.replace('#', '') for id_str in order_item_ids_raw]

# Construct the IN clause with properly quoted IDs for the SQL query
id_list_str = ', '.join([f"'{oid}'" for oid in order_item_ids])

# Construct the SQL query string using f-string and proper escaping for the table name
sql_query = f"SELECT createddate FROM \"Case\" WHERE orderitemid__c IN ({id_list_str});"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-15518888999152830853': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-9684108676081928726': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
