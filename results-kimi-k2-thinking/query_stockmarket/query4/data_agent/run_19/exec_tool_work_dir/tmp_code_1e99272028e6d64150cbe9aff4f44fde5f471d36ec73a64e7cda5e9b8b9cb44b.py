code = """import json
import os

# Get NYSE non-ETF stocks
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Get available tables from stocktrade_database
full_tables_file = locals()['var_functions.query_db:14']
with open(full_tables_file, 'r') as f:
    tables_data = json.load(f)

available_symbols = set([table['name'] for table in tables_data])

# Find NYSE stocks that have trading data
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
nyse_names = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

common_symbols = []
for symbol in nyse_symbols:
    if symbol in available_symbols:
        common_symbols.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'available_in_trade_db': len(common_symbols),
    'sample_symbols': common_symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 234, 'first_10': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'], ['AL', 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'], ['AMN', 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'], ['AMP', 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'], ['ARD', 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.']]}, 'var_functions.execute_python:12': {'total_count': 234}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
