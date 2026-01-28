code = """import json

# Load the complete symbol list from earlier
complete_file = locals()['var_functions.execute_python:54']
if isinstance(complete_file, str):
    with open(complete_file, 'r') as f:
        complete_data = json.load(f)
else:
    complete_data = complete_file

all_symbols = complete_data['symbols']
company_names = complete_data['names']

print('Starting analysis of ' + str(len(all_symbols)) + ' NYSE symbols')

# We'll collect stocks with more up days than down days
positive_stocks = []

# To save time, let's check a reasonable subset first
# We'll process in batches and track our progress
test_mode = True  # Set to False to process all

if test_mode:
    symbols_to_check = all_symbols[:20]  # Check first 20
else:
    symbols_to_check = all_symbols

print('Will check ' + str(len(symbols_to_check)) + ' symbols')

result = {
    'total_symbols': len(all_symbols),
    'checking': len(symbols_to_check),
    'symbols_list': symbols_to_check
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA'], 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}], 'var_functions.execute_python:18': {'up_days': 2, 'down_days': 3}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_stocks': 234, 'sample_name': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, 'var_functions.execute_python:26': {'count': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.list_db:28': 'file_storage/functions.list_db:28.json', 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'symbol': 'AEFC', 'name': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, 'var_functions.execute_python:34': {'count': 234, 'first_batch': ['AEFC', 'AIN', 'AIV']}, 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:46': 'file_storage/functions.execute_python:46.json', 'var_functions.execute_python:48': {'total_symbols': 234, 'batches': 24, 'first_batch_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': 'file_storage/functions.execute_python:54.json', 'var_functions.execute_python:56': 'file_storage/functions.execute_python:56.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': 'file_storage/functions.execute_python:60.json', 'var_functions.execute_python:62': {'to_check': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:64': [], 'var_functions.query_db:66': [{'Date': '2017-01-03', 'Open': '18.26000022888184', 'High': '18.489999771118164', 'Low': '17.920000076293945', 'Close': '18.40999984741211', 'Adj Close': '18.40999984741211', 'Volume': '427400'}, {'Date': '2017-01-04', 'Open': '18.5', 'High': '18.61000061035156', 'Low': '18.3799991607666', 'Close': '18.489999771118164', 'Adj Close': '18.489999771118164', 'Volume': '450000'}, {'Date': '2017-01-05', 'Open': '18.520000457763672', 'High': '18.729999542236328', 'Low': '18.299999237060547', 'Close': '18.440000534057617', 'Adj Close': '18.440000534057617', 'Volume': '318100'}, {'Date': '2017-01-06', 'Open': '18.450000762939453', 'High': '18.450000762939453', 'Low': '18.06999969482422', 'Close': '18.06999969482422', 'Adj Close': '18.06999969482422', 'Volume': '275400'}, {'Date': '2017-01-09', 'Open': '18.09000015258789', 'High': '18.09000015258789', 'Low': '17.780000686645508', 'Close': '17.780000686645508', 'Adj Close': '17.780000686645508', 'Volume': '205800'}]}

exec(code, env_args)
