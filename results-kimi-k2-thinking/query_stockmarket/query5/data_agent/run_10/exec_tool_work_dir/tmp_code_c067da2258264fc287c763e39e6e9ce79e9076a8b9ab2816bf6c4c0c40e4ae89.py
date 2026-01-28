code = """import json

# Get the result from the variable
companies = locals()['var_functions.query_db:0']

# Count the companies
num_companies = len(companies) if isinstance(companies, list) else 0

# Show first few entries
first_few = []
if isinstance(companies, list) and companies:
    first_few = companies[:3]

result_data = {
    "num_companies": num_companies,
    "sample": first_few
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
