code = """import json

# Get the result from the previous query
companies_result = locals()['var_functions.query_db:16']
print(f"Type of result: {type(companies_result)}")

# If it's a string path or JSON string, parse it
if isinstance(companies_result, str):
    if companies_result.endswith('.json'):
        with open(companies_result, 'r') as f:
            companies_data = json.load(f)
    else:
        companies_data = json.loads(companies_result)
else:
    companies_data = companies_result

print(f"Number of NASDAQ Capital Market companies: {len(companies_data)}")
print(f"First 5 companies: {[c['Symbol'] for c in companies_data[:5]]}")

# Return the data for next steps
print('__RESULT__:')
print(json.dumps(companies_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'num_companies': 0, 'sample': []}, 'var_functions.query_db:12': [{'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Market Category': 'G'}, {'Market Category': 'Q'}, {'Market Category': 'S'}], 'var_functions.query_db:14': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json'}

exec(code, env_args)
