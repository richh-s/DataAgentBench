code = """import json

# Load the NASDAQ Capital Market companies
companies = locals()['var_functions.query_db:0']
if isinstance(companies, str):
    with open(companies, 'r') as f:
        companies = json.load(f)

# Filter out ETFs
stocks = [c for c in companies if c['ETF'] == 'N']
print('__RESULT__:')
print(json.dumps('NASDAQ Capital Market stocks (non-ETF): ' + str(len(stocks))))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
