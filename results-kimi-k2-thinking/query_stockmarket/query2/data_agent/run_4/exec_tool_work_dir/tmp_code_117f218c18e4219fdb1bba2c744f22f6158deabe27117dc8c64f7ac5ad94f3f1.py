code = """import json
import os

# Read the ETF list from the stored result
etf_list_file = locals()['var_functions.query_db:0']
etf_list = []

if isinstance(etf_list_file, str) and etf_list_file.endswith('.json'):
    with open(etf_list_file, 'r') as f:
        etf_list = json.load(f)
else:
    etf_list = locals()['var_functions.query_db:0']

print(f"Total NYSE Arca ETFs found: {len(etf_list)}")
print(f"First few ETFs: {[etf['Symbol'] for etf in etf_list[:5]]}")

# We'll store ETFs that meet the criteria
high_price_etfs = []

# For demonstration, let's process a few first to test
test_etfs = etf_list[:10]  # Test with first 10 ETFs

print(f"Testing with first {len(test_etfs)} ETFs...")

# Store the list for next steps
result = {
    'total_nyse_arc_etfs': len(etf_list),
    'test_etf_samples': [etf['Symbol'] for etf in test_etfs],
    'high_price_etfs': high_price_etfs
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
