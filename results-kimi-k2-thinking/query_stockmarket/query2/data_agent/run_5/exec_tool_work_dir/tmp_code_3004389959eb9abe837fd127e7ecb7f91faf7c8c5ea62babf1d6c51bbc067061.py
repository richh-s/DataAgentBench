code = """import json
import os

# Get the result from the previous query
try:
    result_key = 'var_functions.query_db:0'
    result_value = locals().get(result_key)
    
    # Check if it's a file path or raw data
    tickers = []
    if isinstance(result_value, str) and os.path.exists(result_value):
        with open(result_value, 'r') as f:
            tickers_data = json.load(f)
            tickers = [item['Symbol'] for item in tickers_data]
    elif isinstance(result_value, list):
        tickers = [item['Symbol'] for item in result_value]
    else:
        # Try to parse as JSON string
        try:
            tickers_data = json.loads(str(result_value))
            tickers = [item['Symbol'] for item in tickers_data]
        except:
            tickers = []
    
    result_string = json.dumps({'tickers_count': len(tickers), 'first_10': tickers[:10]})
except Exception as e:
    result_string = json.dumps({'error': str(e)})

print('__RESULT__:')
print(result_string)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
