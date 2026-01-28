code = """import json

# Get NYSE stock data from the previous query result
nyse_result = var_functions.query_db:0

# Read the data
with open(nyse_result, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to name mapping
symbol_to_name = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
symbols = list(symbol_to_name.keys())

print(f"Loaded {len(symbols)} NYSE stocks")
print("Sample symbols: ", symbols[:5])

# Return the symbols and mapping
output = {
    "symbols": symbols,
    "symbol_to_name": symbol_to_name,
    "count": len(symbols)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Loaded 234 NYSE stocks', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:13': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'all_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_functions.query_db:12': [{'Date': '2017-01-03', 'Open': '45.68999862670898', 'High': '45.72999954223633', 'Low': '44.66999816894531', 'Close': '44.93999862670898', 'Adj Close': '40.33967971801758', 'Volume': '770100'}, {'Date': '2017-01-04', 'Open': '45.09999847412109', 'High': '45.52000045776367', 'Low': '44.79999923706055', 'Close': '45.36000061035156', 'Adj Close': '40.716678619384766', 'Volume': '1089400'}, {'Date': '2017-01-05', 'Open': '45.09999847412109', 'High': '45.650001525878906', 'Low': '44.650001525878906', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '833400'}, {'Date': '2017-01-06', 'Open': '45.29999923706055', 'High': '45.560001373291016', 'Low': '44.97999954223633', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '1299300'}, {'Date': '2017-01-09', 'Open': '45.540000915527344', 'High': '45.61000061035156', 'Low': '44.91999816894531', 'Close': '44.959999084472656', 'Adj Close': '40.35763168334961', 'Volume': '697700'}]}

exec(code, env_args)
