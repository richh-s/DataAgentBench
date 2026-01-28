code = """import json

# Load the stock symbols from the previous query
result_file = 'functions.query_db:10.json'
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Get stock symbols and company names
stock_info = {stock['Symbol']: stock['CompanyName'] for stock in nyse_stocks}
symbols = list(stock_info.keys())

print('__RESULT__:')
print(json.dumps({"count": len(symbols), "first_10": symbols[:10], "sample_data": nyse_stocks[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
