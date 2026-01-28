code = """import json, os, pandas as pd

# Get the file path for capital market stocks
capital_market_file = locals()['var_functions.query_db:0']

# Load the capital market stocks data
with open(capital_market_file, 'r') as f:
    capital_market_data = json.load(f)

# Create a dictionary mapping symbol to company name
symbol_to_company = {}
for item in capital_market_data:
    symbol = item['Symbol']
    company_desc = item['Company Description']
    # Extract company name (before the first period)
    company_name = company_desc.split('.')[0]
    symbol_to_company[symbol] = company_name

# Get the list of all available tables in stocktrade_database
tables_file = locals()['var_functions.list_db:10']

# Load the tables data
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Create a set for faster lookup
available_symbols = set(all_tables)

# Count how many capital market stocks have price data
capital_symbols_with_data = []
for symbol in symbol_to_company.keys():
    if symbol in available_symbols:
        capital_symbols_with_data.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'total_capital_market_stocks': len(symbol_to_company),
    'stocks_with_price_data': len(capital_symbols_with_data),
    'sample_stocks': capital_symbols_with_data[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'file_', 'var_functions.execute_python:8': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}], 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
