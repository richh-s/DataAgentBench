code = """import json

# Read NYSE non-ETF stocks data
nyse_file = 'var_functions.query_db:42'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

print('NYSE non-ETF stocks loaded:', len(nyse_stocks))

# Read available trade symbols from stocktrade database
trade_file = 'var_functions.list_db:0'
with open(trade_file, 'r') as f:
    trade_symbols = json.load(f)

# Create mapping of symbol to company description
symbol_to_desc = {item['Symbol']: item['Company Description'] for item in nyse_stocks}

# Find intersection
nyse_symbols = set(symbol_to_desc.keys())
available_symbols = nyse_symbols.intersection(set(trade_symbols))

print('Symbols with trade data:', len(available_symbols))
print('Sample symbols:', list(available_symbols)[:10])

# Save available symbols for next step
with open('available_nyse_symbols.json', 'w') as f:
    json.dump(list(available_symbols), f)

print('__RESULT__:')
print(json.dumps({
    'total_nyse': len(nyse_stocks),
    'with_trade_data': len(available_symbols),
    'symbol_to_desc_count': len(symbol_to_desc)
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'ETF': 'N'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'ETF': 'N'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'ETF': 'N'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'ETF': 'N'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'ETF': 'N'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'ETF': 'N'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'ETF': 'N'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'ETF': 'N'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.', 'ETF': 'N'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.', 'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'count': '234'}], 'var_functions.query_db:32': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:36': [{'Date': '2017-01-03', 'Open': '45.68999862670898', 'High': '45.72999954223633', 'Low': '44.66999816894531', 'Close': '44.93999862670898', 'Adj Close': '40.33967971801758', 'Volume': '770100'}, {'Date': '2017-01-04', 'Open': '45.09999847412109', 'High': '45.52000045776367', 'Low': '44.79999923706055', 'Close': '45.36000061035156', 'Adj Close': '40.716678619384766', 'Volume': '1089400'}, {'Date': '2017-01-05', 'Open': '45.09999847412109', 'High': '45.650001525878906', 'Low': '44.650001525878906', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '833400'}, {'Date': '2017-01-06', 'Open': '45.29999923706055', 'High': '45.560001373291016', 'Low': '44.97999954223633', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '1299300'}, {'Date': '2017-01-09', 'Open': '45.540000915527344', 'High': '45.61000061035156', 'Low': '44.91999816894531', 'Close': '44.959999084472656', 'Adj Close': '40.35763168334961', 'Volume': '697700'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'up_days': 3, 'down_days': 2, 'symbol': 'AIV'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
