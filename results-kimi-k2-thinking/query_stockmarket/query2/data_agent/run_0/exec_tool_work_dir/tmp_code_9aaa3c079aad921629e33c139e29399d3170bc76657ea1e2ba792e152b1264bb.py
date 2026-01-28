code = """import json

# Read the file containing NYSE Arca ETFs
result_file = locals()['var_functions.query_db:0']

with open(result_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Count total number of ETFs
num_etfs = len(nyse_arca_etfs)
print('__RESULT__:')
print(str(num_etfs))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
