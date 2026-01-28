code = """import json
import pandas as pd

# Read the stockinfo results (NASDAQ Capital Market symbols)
stockinfo_path = locals()['var_functions.query_db:0']
if isinstance(stockinfo_path, str):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals()['var_functions.query_db:0']

# Extract symbols from stockinfo
nasdaq_cap_symbols = {item['Symbol'] for item in stockinfo_data}

# Read the available tables in stocktrade database
stocktrade_path = locals()['var_functions.list_db:2']
if isinstance(stocktrade_path, str):
    with open(stocktrade_path, 'r') as f:
        available_tables = json.load(f)
else:
    available_tables = locals()['var_functions.list_db:2']

# Find intersection of symbols (NASDAQ Capital Market stocks with trade data)
available_symbols = set(available_tables)
eligible_symbols = list(nasdaq_cap_symbols.intersection(available_symbols))

print('__RESULT__:')
print(json.dumps({
    'eligible_count': len(eligible_symbols),
    'sample_symbols': eligible_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
