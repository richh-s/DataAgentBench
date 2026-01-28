code = """# Check which tables exist for the NASDAQ Capital Market symbols
table_list_file = locals()['var_functions.list_db:6']

import json
with open(table_list_file, 'r') as f:
    all_tables = json.load(f)

# Get the NASDAQ Capital Market symbols from previous query
stockinfo_file = locals()['var_functions.query_db:0']
with open(stockinfo_file, 'r') as f:
    nasdaq_capital_data = json.load(f)

nasdaq_symbols = [row['Symbol'] for row in nasdaq_capital_data]

# Check which of these symbols have tables in the database
available_tables = set(all_tables)
nasdaq_symbols_with_data = [sym for sym in nasdaq_symbols if sym in available_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_capital_symbols': len(nasdaq_symbols),
    'symbols_with_tables': len(nasdaq_symbols_with_data),
    'first_few_with_tables': nasdaq_symbols_with_data[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'symbol_count': 86, 'first_few_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'company_names_sample': {'AGMH': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'ALACU': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'AMHC': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
