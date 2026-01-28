code = """import json

# Filter NASDAQ Capital Market symbols that have price data tables
stockinfo_path = locals()['var_functions.query_db:0']
stocktrade_path = locals()['var_functions.list_db:2']

with open(stockinfo_path, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

with open(stocktrade_path, 'r') as f:
    all_tables = set(json.load(f))

# Get symbols and company descriptions
nasdaq_symbols = set(stock['Symbol'] for stock in nasdaq_capital_stocks)
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_capital_stocks}

# Find intersection
available_symbols = nasdaq_symbols.intersection(all_tables)
print('__RESULT__:')
print(json.dumps({
    'nasdaq_capital_count': len(nasdaq_symbols),
    'available_in_stocktrade': len(available_symbols),
    'sample_symbols': list(available_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:10': {'total_tables': 2753, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}}

exec(code, env_args)
