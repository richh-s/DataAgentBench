code = """import json
import os

# Read NYSE stock data
result_file = locals()['var_functions.execute_python:10']
with open(result_file, 'r') as f:
    nyse_data = json.load(f)

nyse_symbols = nyse_data['symbols']
print(f"Processing {len(nyse_symbols)} NYSE stocks for 2017...")

# Create company name mapping
symbol_to_company = nyse_data['symbol_to_company']

# Function to extract company name from description
def extract_company_name(description):
    return description.split(' specializes in')[0].split(' is ')[0].strip()

company_names = {}
for symbol, desc in symbol_to_company.items():
    company_names[symbol] = extract_company_name(desc)

print(f"Sample company names: {dict(list(company_names.items())[:5])}")

# Save data for next step
output = {
    'symbols': nyse_symbols,
    'company_names': company_names
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
