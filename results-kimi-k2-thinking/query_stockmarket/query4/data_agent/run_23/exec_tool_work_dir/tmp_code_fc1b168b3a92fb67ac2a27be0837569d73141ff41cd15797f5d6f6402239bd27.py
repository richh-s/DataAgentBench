code = """import json
import os

# Load NYSE stock data
nyse_file = locals()['var_functions.query_db:26']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create mapping of symbol to company name
def extract_company_name(description):
    # Take the first part before common separators
    parts = description.split(' specializes in')
    if len(parts) > 1:
        return parts[0].strip()
    
    parts = description.split(' is ')
    if len(parts) > 1:
        return parts[0].strip()
    
    parts = description.split(' operates ')
    if len(parts) > 1:
        return parts[0].strip()
        
    return description.split('.')[0].strip()

symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    symbol_to_company[symbol] = extract_company_name(stock['Company Description'])

nyse_symbols = list(symbol_to_company.keys())
print(f"Total NYSE non-ETF stocks: {len(nyse_symbols)}")

# Save data
output_data = {
    'symbols': nyse_symbols,
    'symbol_to_company': symbol_to_company
}

print('__RESULT__:')
print(json.dumps(output_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'message': 'Ready to analyze 2017 trading data'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'query_preview': "SELECT 'AEFC' AS Symbol, Date, Open, Close FROM AEFC WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' AS Symbol, Date, Open, Close FROM AIN WHERE Date >= '2017-01-01' AND Dat...", 'symbols_count': 10}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
