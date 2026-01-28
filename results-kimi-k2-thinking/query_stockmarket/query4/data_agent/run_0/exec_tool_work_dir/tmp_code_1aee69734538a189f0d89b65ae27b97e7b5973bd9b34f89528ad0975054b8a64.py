code = """import json

# Load all NYSE non-ETF symbols and descriptions
common_info = locals().get('var_functions.execute_python:10')
if isinstance(common_info, str) and common_info.endswith('.json'):
    with open(common_info, 'r') as f:
        data = json.load(f)
else:
    data = common_info

symbols = data['symbols']
desc_lookup = data['desc_lookup']

# Create batch queries for 2017 data
# Since we can't execute all 234 queries at once, let's create a plan
print(f"Analyzing {len(symbols)} NYSE non-ETF stocks for 2017 performance")

# We'll need to query each stock's 2017 data and count up/down days
# Let's create a structured plan
analysis_plan = {
    'total_stocks': len(symbols),
    'stocks_with_descriptions': desc_lookup
}

print('__RESULT__:')
print(json.dumps(analysis_plan))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_symbols_count': 234, 'common_symbols_count': 234, 'common_symbols_preview': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'Date': '1994-07-22', 'Open': '18.5', 'High': '18.625', 'Low': '18.5', 'Close': '18.5', 'Adj Close': '4.698645114898682', 'Volume': '1415500'}, {'Date': '1994-07-25', 'Open': '18.5', 'High': '18.625', 'Low': '18.5', 'Close': '18.625', 'Adj Close': '4.730391979217529', 'Volume': '138600'}, {'Date': '1994-07-26', 'Open': '18.5', 'High': '18.625', 'Low': '18.5', 'Close': '18.5', 'Adj Close': '4.698645114898682', 'Volume': '71500'}, {'Date': '1994-07-27', 'Open': '18.625', 'High': '18.625', 'Low': '18.5', 'Close': '18.5', 'Adj Close': '4.698645114898682', 'Volume': '37300'}, {'Date': '1994-07-28', 'Open': '18.5', 'High': '18.625', 'Low': '18.5', 'Close': '18.5', 'Adj Close': '4.698645114898682', 'Volume': '83500'}], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_functions.execute_python:34': 'file_storage/functions.execute_python:34.json'}

exec(code, env_args)
