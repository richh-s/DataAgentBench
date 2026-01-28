code = """import json
import os

# Load NYSE stock data
nyse_file = locals()['var_functions.query_db:12']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract clean company name
    company_name = desc
    for separator in [' specializes', ' is ', ' Inc.', ' Corporation', ' Company', ' LLC', ' LP', ' Ltd.', ' Co.', ' Plc']:
        if separator in company_name:
            company_name = company_name.split(separator)[0].strip()
            break
    symbol_to_company[symbol] = company_name

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'sample_companies': list(symbol_to_company.items())[:5]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'stock_count': 234, 'sample_stocks': [['AEFC', 'Aegon Funding'], ['AIN', 'Albany International'], ['AIV', 'Apartment Investment and Management'], ['AIZP', 'Assurant,'], ['AJRD', 'Aerojet Rocketdyne Holdings,'], ['AL', 'Air Lease'], ['AMN', 'AMN Healthcare Services'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.execute_python:20': {'total_nyse_stocks': 234, 'total_trade_symbols': 2753, 'available_nyse_symbols': 234, 'sample_symbols': ['CADE', 'CUBE', 'CHAP', 'EIG', 'USX', 'MNE', 'EV', 'ORCL', 'WOR', 'SAM']}, 'var_functions.execute_python:22': {'mapped_companies': 234, 'sample_mapping': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc.'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that'], ['ARD', 'Ardagh Group S.A.']]}}

exec(code, env_args)
