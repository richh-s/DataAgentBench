code = """import json
import os

# Load NYSE non-ETF stocks
nyse_file = locals()['var_functions.query_db:30']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    company_name = desc.split(' specializes')[0].split(' is ')[0].split(' Inc.')[0].split(' Corporation')[0].split(' Company')[0].split(' LLC')[0].split(' LP')[0].strip()
    if company_name.endswith('.'):
        company_name = company_name[:-1]
    symbol_to_company[symbol] = company_name

# Get all NYSE symbols (these have corresponding tables in stocktrade_database)
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(nyse_symbols),
    'first_symbols': nyse_symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'stock_count': 234, 'sample_stocks': [['AEFC', 'Aegon Funding'], ['AIN', 'Albany International'], ['AIV', 'Apartment Investment and Management'], ['AIZP', 'Assurant,'], ['AJRD', 'Aerojet Rocketdyne Holdings,'], ['AL', 'Air Lease'], ['AMN', 'AMN Healthcare Services'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.execute_python:20': {'total_nyse_stocks': 234, 'total_trade_symbols': 2753, 'available_nyse_symbols': 234, 'sample_symbols': ['CADE', 'CUBE', 'CHAP', 'EIG', 'USX', 'MNE', 'EV', 'ORCL', 'WOR', 'SAM']}, 'var_functions.execute_python:22': {'mapped_companies': 234, 'sample_mapping': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc.'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.execute_python:24': {'total_nyse_stocks': 234, 'sample_companies': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.']]}, 'var_functions.execute_python:26': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding', 'AIN': 'Albany International', 'AIV': 'Apartment Investment and Management', 'AIZP': 'Assurant,', 'AJRD': 'Aerojet Rocketdyne Holdings,'}}, 'var_functions.execute_python:34': {'total_symbols': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}}

exec(code, env_args)
