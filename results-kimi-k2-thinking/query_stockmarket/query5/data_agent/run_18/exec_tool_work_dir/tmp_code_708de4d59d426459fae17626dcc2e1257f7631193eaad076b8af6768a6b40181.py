code = """# Access the NASDAQ Capital Market data
nasdaq_data = locals()['var_functions.query_db:0']
import json

# Read the JSON file
with open(nasdaq_data, 'r') as f:
    nasdaq_companies = json.load(f)

# Create dictionaries for symbol to company name mapping
symbol_to_company = {item['Symbol']: item['company_name'] for item in nasdaq_companies}
symbols = list(symbol_to_company.keys())

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'symbols_subset': symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'nasdaq_cap_count': 86, 'stocktrade_table_count': 2753, 'overlap_count': 86, 'first_20_overlap': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
