code = """import json

# Load all NYSE non-ETF stocks with company names
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping and symbol list
stock_names = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
stock_symbols = list(stock_names.keys())

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(stock_symbols),
    'sample_data': {sym: stock_names[sym] for sym in stock_symbols[:5]}
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 234, 'first_10': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'], ['AL', 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'], ['AMN', 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'], ['AMP', 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'], ['ARD', 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.']]}, 'var_functions.execute_python:12': {'total_count': 234}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:18': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:22': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'Close': '47.150001525878906'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'Close': '48.150001525878906'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'Close': '47.75'}, {'Date': '2017-01-06', 'Open': '47.75', 'Close': '46.59999847412109'}, {'Date': '2017-01-09', 'Open': '46.5', 'Close': '45.54999923706055'}]}

exec(code, env_args)
