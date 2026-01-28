code = """import json

# Get the NYSE non-ETF stocks data
if 'var_functions.query_db:0' in locals():
    nyse_stocks = locals()['var_functions.query_db:0']
    # Extract symbols
    symbols = [stock['Symbol'] for stock in nyse_stocks]
    print(f"Total NYSE non-ETF stocks: {len(symbols)}")
    print(f"First 20 symbols: {symbols[:20]}")
    
    result = {"symbols": symbols, "count": len(symbols)}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({"error": "var_functions.query_db:0 not found"}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
