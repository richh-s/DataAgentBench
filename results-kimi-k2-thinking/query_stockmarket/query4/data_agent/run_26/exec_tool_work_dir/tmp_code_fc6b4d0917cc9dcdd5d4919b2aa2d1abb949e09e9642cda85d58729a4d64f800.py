code = """import json
import os

# Load NYSE symbols and company data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
all_symbols = list(symbol_to_company.keys())

print('Total symbols to process:', len(all_symbols))

# This script will track top 5 stocks with most up>down difference
top_stocks = []

# Load existing results we've gathered so far
existing_results = {
    'AIN': {'up': 143, 'down': 101, 'diff': 42},
    'AIV': {'up': 118, 'down': 128, 'diff': -10},
    'AJRD': {'up': 123, 'down': 123, 'diff': 0},
    'AL': {'up': 131, 'down': 117, 'diff': 14},
    'AMN': {'up': 134, 'down': 111, 'diff': 23},
    'AMP': {'up': 141, 'down': 110, 'diff': 31},
    'AMT': {'up': 128, 'down': 123, 'diff': 5},
    'ARD': {'up': 80, 'down': 119, 'diff': -39},
    'ARGD': {'up': 133, 'down': 82, 'diff': 51}
}

# Build initial top 5 from what we have
for symbol, data in existing_results.items():
    if data['diff'] > 0:
        top_stocks.append({
            'symbol': symbol,
            'up_days': data['up'],
            'down_days': data['down'],
            'diff': data['diff'],
            'company': symbol_to_company[symbol]
        })

# Sort by diff descending
top_stocks.sort(key=lambda x: x['diff'], reverse=True)
top_5 = top_stocks[:5]

print('Current top 5:')
for i, stock in enumerate(top_5, 1):
    print(f"{i}. {stock['symbol']}: {stock['up_days']} up, {stock['down_days']} down, diff={stock['diff']}")
    
print('Will process remaining', len(all_symbols) - len(existing_results), 'symbols')

result = {
    'top_5_current': top_5,
    'remaining': len(all_symbols) - len(existing_results)
}

print('__RESULT__:'))
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_nyse_symbols': 234, 'available_tables': 234, 'sample_symbols': ['MTD', 'PAG', 'SMP', 'ESS', 'MKC']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'symbol_to_company_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.execute_python:30': {'total_stocks': 234, 'batch_size': 20, 'symbols_to_test': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:34': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}], 'var_functions.query_db:36': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}], 'var_functions.query_db:38': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.query_db:40': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0', 'total_days': '251'}], 'var_functions.execute_python:42': {'total_stocks': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:44': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0', 'total_days': '251'}], 'var_functions.query_db:46': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.execute_python:48': {'status': 'setup_complete', 'symbols_count': 234, 'results_keys': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:50': {'total_symbols': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'approach': 'Will query each stock table for 2017 data, count days where Close > Open (up) and Close < Open (down), exclude days where Close = Open', 'tracking': 'Keep top 5 stocks where up_days > down_days, sorted by (up_days - down_days) descending'}, 'var_functions.execute_python:54': {'ready': True, 'count': 234}, 'var_functions.query_db:56': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0', 'total_days': '251'}], 'var_functions.query_db:58': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0', 'flat_days': '3.0', 'total_days': '251'}], 'var_functions.query_db:60': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0', 'total_days': '251'}], 'var_functions.query_db:62': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0', 'total_days': '251'}], 'var_functions.query_db:64': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0', 'total_days': '251'}], 'var_functions.query_db:66': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0', 'total_days': '204'}], 'var_functions.query_db:68': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0', 'total_days': '251'}]}

exec(code, env_args)
