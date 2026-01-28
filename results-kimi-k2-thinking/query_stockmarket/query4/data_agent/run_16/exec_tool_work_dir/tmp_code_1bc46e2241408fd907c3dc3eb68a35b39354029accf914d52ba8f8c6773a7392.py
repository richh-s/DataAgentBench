code = """import json

# Load the full list of NYSE non-ETF symbols with company names
symbols_file = locals()['var_functions.query_db:0']

with open(symbols_file, 'r') as f:
    symbols_data = json.load(f)

company_map = {rec['Symbol']: rec['Company Description'] for rec in symbols_data}
symbols = list(company_map.keys())

# Track results
results = []

# Process a few stocks to start
sample_symbols = ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']

for symbol in sample_symbols:
    results.append({
        'symbol': symbol,
        'company': company_map[symbol]
    })

print('Total symbols to check:', len(symbols))
print('Sample symbols:', sample_symbols[:5])
print('__RESULT__:')
print(json.dumps(results, indent=2)[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_non_etf': 234, 'present_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:8': [{'Symbol': 'AEFC', 'Company': 'None'}, {'Symbol': 'AIN', 'Company': 'None'}, {'Symbol': 'AIV', 'Company': 'None'}, {'Symbol': 'AIZP', 'Company': 'None'}, {'Symbol': 'AJRD', 'Company': 'None'}], 'var_functions.query_db:10': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'High': '15.701873779296877', 'Low': '14.988152503967283', 'Close': '15.107105255126951', 'Adj Close': '8.918145179748535', 'Volume': '2292200'}, {'Date': '1987-10-01', 'Open': '15.107105255126951', 'High': '15.345012664794922', 'Low': '14.988152503967283', 'Close': '15.345012664794922', 'Adj Close': '9.05859375', 'Volume': '468200'}, {'Date': '1987-10-02', 'Open': '15.345012664794922', 'High': '15.701873779296877', 'Low': '15.107105255126951', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '371600'}, {'Date': '1987-10-05', 'Open': '15.701873779296877', 'High': '15.701873779296877', 'Low': '15.226058959960938', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '121300'}, {'Date': '1987-10-06', 'Open': '15.58292007446289', 'High': '15.58292007446289', 'Low': '15.226058959960938', 'Close': '15.463966369628906', 'Adj Close': '9.128814697265623', 'Volume': '159300'}], 'var_functions.execute_python:14': {'count': 234, 'example': ['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.']}, 'var_functions.query_db:16': [{'total_2017': '251', 'up_days': '143', 'down_days': '101'}], 'var_functions.query_db:20': [{'up_days': '0', 'down_days': '0'}], 'var_functions.execute_python:22': {'company_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}, 'var_functions.query_db:24': [{'total_days': '204', 'up_days': '80', 'down_days': '119'}], 'var_functions.query_db:26': [{'total_days': '251', 'up_days': '137', 'down_days': '113'}]}

exec(code, env_args)
