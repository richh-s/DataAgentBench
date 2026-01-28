code = """import json

# Load the NASDAQ Capital Market stocks
with open('/tmp/tmp5d6q1f7r.json', 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Get first few symbols to understand structure
print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(nasdaq_cap_stocks),
    'sample_stocks': nasdaq_cap_stocks[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
