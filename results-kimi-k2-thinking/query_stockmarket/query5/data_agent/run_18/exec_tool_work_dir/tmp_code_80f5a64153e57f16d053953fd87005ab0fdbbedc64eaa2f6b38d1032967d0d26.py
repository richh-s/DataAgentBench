code = """import json
import pandas as pd

# Access the stored results directly from the variable names
nasdaq_capital_result_key = 'var_functions.query_db:0'
stocktrade_tables_result_key = 'var_functions.list_db:2'

# Try to read the files directly using the keys
nasdaq_capital_file = locals()[nasdaq_capital_result_key]
stocktrade_tables_file = locals()[stocktrade_tables_result_key]

with open(nasdaq_capital_file, 'r') as f:
    nasdaq_capital_list = json.load(f)

with open(stocktrade_tables_file, 'r') as f:
    stocktrade_tables = json.load(f)

num_nasdaq_tickers = len(nasdaq_capital_list)
num_stocktrade_tables = len(stocktrade_tables)

nasdaq_symbols = [item['Symbol'] for item in nasdaq_capital_list]
company_names = {item['Symbol']: item['company_name'] for item in nasdaq_capital_list}

overlap = set(nasdaq_symbols) & set(stocktrade_tables)
overlap_count = len(overlap)

print('__RESULT__:')
print(json.dumps({
    'nasdaq_cap_count': num_nasdaq_tickers,
    'stocktrade_table_count': num_stocktrade_tables,
    'overlap_count': overlap_count,
    'first_20_overlap': sorted(list(overlap))[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
