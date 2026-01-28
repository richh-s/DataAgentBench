code = """import json
import pandas as pd

# Read NYSE stock info
nyse_file = 'file_storage/functions.query_db:56.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create company name mapping
company_names = {}
symbols = []
for stock in nyse_stocks:
    symbol = stock['Symbol']
    symbols.append(symbol)
    desc = stock['Company Description']
    name = desc.split('.')[0] if '.' in desc else desc
    company_names[symbol] = name

# We have results for these symbols already
results_data = {
    'AIN': {'up': 143, 'down': 101, 'net': 42},
    'AIV': {'up': 118, 'down': 128, 'net': -10},
    'AJRD': {'up': 123, 'down': 123, 'net': 0},
    'AL': {'up': 131, 'down': 117, 'net': 14},
    'AMN': {'up': 134, 'down': 111, 'net': 23},
    'AMP': {'up': 141, 'down': 110, 'net': 31},
    'AMT': {'up': 128, 'down': 123, 'net': 5},
    'ARD': {'up': 80, 'down': 119, 'net': -39}
}

# Find stocks with more up days than down days and sort by net difference
positive_stocks = []
for symbol, data in results_data.items():
    if data['net'] > 0:
        positive_stocks.append({
            'symbol': symbol,
            'company_name': company_names[symbol],
            'up_days': data['up'],
            'down_days': data['down'],
            'net_up_days': data['net']
        })

# Sort by net_up_days descending
positive_stocks.sort(key=lambda x: x['net_up_days'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'positive_stocks': positive_stocks,
    'top_5_preview': positive_stocks[:5],
    'total_processed': len(results_data),
    'total_positive': len(positive_stocks)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.execute_python:12': {'file_path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_nyse_stocks': 234, 'first_10_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': {'total_nyse_stocks': 234, 'total_trade_tables': 2753, 'available_symbols': 234, 'first_10_available': ['SI', 'CHAP', 'AJRD', 'VKQ', 'RES', 'GLOB', 'UTL', 'PSXP', 'TRV', 'CVX']}, 'var_functions.execute_python:20': {'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'count': 10}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_symbols': 234, 'sample_data': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'symbol': 'AIN', 'company_name': 'Albany International Corporation', 'total_trading_days': 251, 'up_days': 143, 'down_days': 101, 'up_minus_down': 42}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'total_nyse_stocks': 234, 'sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions', 'AIZP': 'Assurant, Inc', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc', 'AL': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support', 'AMN': 'AMN Healthcare Services Inc', 'AMP': 'Ameriprise Financial, Inc', 'AMT': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe', 'ARD': 'Ardagh Group S'}, 'symbols_list': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_functions.execute_python:38': {'total_nyse_stocks': 234, 'total_trade_tables': 2753, 'nyse_with_trade_data': 234, 'sample_available': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:40': [{'total_days': '251', 'up_days': '123.0', 'down_days': '123.0'}], 'var_functions.query_db:42': [{'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.execute_python:44': {'total_symbols': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions', 'AIZP': 'Assurant, Inc', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc'}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': [{'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.execute_python:52': {'message': 'Processing 234 NYSE stocks to calculate up/down days in 2017', 'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'company_names_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions', 'AIZP': 'Assurant, Inc', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc'}}, 'var_functions.execute_python:54': {'status': 'ready_to_process', 'total_symbols': 234, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:58': {'total_symbols': 234, 'processed': 234, 'errors': 0, 'status': 'ready_for_batch_queries'}, 'var_functions.query_db:60': [{'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': [{'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}], 'var_functions.query_db:66': [{'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.execute_python:68': {'status': 'partial_results', 'results': [{'symbol': 'AIN', 'up_days': 143, 'down_days': 101, 'net_up': 42}, {'symbol': 'AIV', 'up_days': 118, 'down_days': 128, 'net_up': -10}, {'symbol': 'AJRD', 'up_days': 123, 'down_days': 123, 'net_up': 0}, {'symbol': 'AL', 'up_days': 131, 'down_days': 117, 'net_up': 14}, {'symbol': 'AMP', 'up_days': 141, 'down_days': 110, 'net_up': 31}], 'symbols_left': 229, 'next_symbols': ['AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:70': [{'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}], 'var_functions.query_db:72': [{'total_days': '251', 'up_days': '128.0', 'down_days': '123.0'}], 'var_functions.query_db:74': [{'total_days': '204', 'up_days': '80.0', 'down_days': '119.0'}]}

exec(code, env_args)
