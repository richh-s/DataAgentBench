code = """import json

var_key = 'var_functions.query_db:10'

result = locals().get(var_key)
if result:
    print('Variable found, type:', type(result))
    if isinstance(result, str) and result.endswith('.json'):
        with open(result, 'r') as f:
            nyse_stocks = json.load(f)
    else:
        nyse_stocks = result
        
    print('Number of NYSE non-ETF stocks:', len(nyse_stocks))
    
    symbols = [stock['Symbol'] for stock in nyse_stocks]
    print('Total symbols:', len(symbols))
    
    unique_symbols = list(set(symbols))
    print('Unique symbols:', len(unique_symbols))
    
    output = json.dumps({
        'total_stocks': len(nyse_stocks),
        'symbols': symbols[:10]
    })
    print('__RESULT__:')
    print(output)
else:
    print('Variable not found:', var_key)
    print('Available keys:', [k for k in locals().keys() if 'functions' in k])"""

env_args = {'var_functions.query_db:0': [{'Listing Exchange': 'A', 'count': '28'}, {'Listing Exchange': 'N', 'count': '234'}, {'Listing Exchange': 'P', 'count': '1444'}, {'Listing Exchange': 'Q', 'count': '710'}, {'Listing Exchange': 'Z', 'count': '336'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
