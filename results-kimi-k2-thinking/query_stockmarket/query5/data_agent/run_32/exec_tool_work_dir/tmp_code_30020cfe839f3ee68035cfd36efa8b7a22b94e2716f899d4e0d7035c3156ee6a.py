code = """import json

# Load the previously fetched data
nasdaq_file = locals()['var_functions.query_db:0']
with open(nasdaq_file, 'r') as f:
    nasdaq_stocks = json.load(f)

# Load the list of tables from stocktrade_database
tables_file = locals()['var_functions.list_db:6']
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Extract symbols from NASDAQ Capital Market stocks
nasdaq_symbols = [stock['Symbol'] for stock in nasdaq_stocks]

# Find intersection with available tables
available_symbols = list(set(nasdaq_symbols) & set(all_tables))

print("__RESULT__:")
print(json.dumps({
    "total_nasdaq_capital_stocks": len(nasdaq_stocks),
    "total_tables_in_db": len(all_tables),
    "available_symbols": len(available_symbols),
    "sample_symbols": available_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:4': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
