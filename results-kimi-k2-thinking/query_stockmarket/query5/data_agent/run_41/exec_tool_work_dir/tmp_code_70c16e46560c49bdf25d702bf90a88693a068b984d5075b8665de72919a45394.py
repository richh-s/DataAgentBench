code = """import json

# Load NASDAQ Capital Market stocks
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    nasdaq_stocks = json.load(f)

# Create mapping of symbol to company description
symbol_to_company = {}
for stock in nasdaq_stocks:
    symbol_to_company[stock['Symbol']] = stock['Company Description']

symbols = list(symbol_to_company.keys())

# Build queries properly
query_parts = []
for symbol in symbols:
    # Properly quote the table name
    quoted_symbol = f'"{symbol}"' if not symbol.startswith('"') else symbol
    part = f"SELECT '{symbol}' as Symbol, COUNT(*) as high_volatility_days FROM {quoted_symbol} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (Low * 0.20)"
    query_parts.append(part)

# Combine with UNION ALL
union_query = ' UNION ALL '.join(query_parts) + ' ORDER BY high_volatility_days DESC LIMIT 5'

print('__RESULT__:')
print(json.dumps({'query': union_query}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:10': {'total_tables': 2753, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}, 'var_functions.execute_python:12': {'nasdaq_capital_count': 86, 'available_in_stocktrade': 86, 'sample_symbols': ['BWEN', 'SSNT', 'HQI', 'FSBW', 'CCCL', 'CUBA', 'WHLM', 'IGIC', 'CPAH', 'FTFT']}, 'var_functions.query_db:14': [{'high_volatility_days': '13'}], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
