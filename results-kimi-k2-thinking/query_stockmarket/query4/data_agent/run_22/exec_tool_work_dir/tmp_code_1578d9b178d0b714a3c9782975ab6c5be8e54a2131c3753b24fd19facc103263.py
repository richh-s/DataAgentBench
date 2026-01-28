code = """import json

# Load the stock symbols from the previous query
result_key = 'functions.query_db:0'
result_file = locals()[result_key]

with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

symbols = [stock['Symbol'] for stock in nyse_stocks]
print('__RESULT__:')
print(json.dumps({"count": len(symbols), "first_10": symbols[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
