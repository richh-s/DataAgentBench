code = """import json

# Access the variable from locals since it contains a colon in the name
storage_key = 'var_functions.query_db:0'
capital_market_stocks = locals()[storage_key]

# Show the first few records to verify the data
print('__RESULT__:')
print(json.dumps(capital_market_stocks[:5]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
