code = """import json
import os

# Load NYSE stock data
nyse_file = locals()['var_functions.execute_python:28']
with open(nyse_file, 'r') as f:
    nyse_data = json.load(f)

nyse_symbols = nyse_data['symbols']
symbol_to_company = nyse_data['symbol_to_company']

print(f"Total NYSE non-ETF stocks to analyze: {len(nyse_symbols)}")
print(f"Sample symbols: {nyse_symbols[:5]}")

# Build queries for all stocks in batches to avoid overwhelming the system
# Let's create a comprehensive query that gets 2017 data for all NYSE stocks
# We'll use UNION ALL to combine data from all tables

# For performance, let's split into smaller batches
batch_size = 20
batches = []

for i in range(0, len(nyse_symbols), batch_size):
    batch = nyse_symbols[i:i+batch_size]
    query_parts = []
    for symbol in batch:
        # Ensure symbol is valid table name (alphanumeric/underscore)
        if symbol.replace('_', '').replace('-', '').isalnum():
            query_parts.append(
                f"SELECT '{symbol}' AS Symbol, Date, Open, Close FROM \"{symbol}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
            )
    
    if query_parts:
        union_query = " UNION ALL ".join(query_parts)
        batches.append(union_query)

print(f"Created {len(batches)} batches with {batch_size} stocks each")
print(f"First batch query preview: {batches[0][:200] if batches else 'No batches'}...")

# Save batches to file
output = {
    'batches': batches,
    'total_stocks': len(nyse_symbols),
    'symbol_to_company': symbol_to_company
}

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(nyse_symbols),
    'batch_count': len(batches),
    'first_batch_preview': batches[0][:200] if batches else ''
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'message': 'Ready to analyze 2017 trading data'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'query_preview': "SELECT 'AEFC' AS Symbol, Date, Open, Close FROM AEFC WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' AS Symbol, Date, Open, Close FROM AIN WHERE Date >= '2017-01-01' AND Dat...", 'symbols_count': 10}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json'}

exec(code, env_args)
