code = """import os
import json

# List all files in current directory
files = os.listdir('.')
print("Files in directory:")
for f in files:
    if f.startswith('var_functions'):
        print(f"  {f}")

# Try to find and read the NYSE data
nyse_file = None
trade_file = None

for f in files:
    if 'query_db' in f and 'stockinfo' in open(f).read()[:100]:
        nyse_file = f
    if 'list_db' in f and 'stocktrade' in open(f).read()[:100]:
        trade_file = f

print(f"NYSE file: {nyse_file}")
print(f"Trade file: {trade_file}")

# If we can't auto-detect, use known patterns
if not nyse_file:
    # Try common pattern
    candidates = [f for f in files if 'query_db' in f and 'stockinfo' in f]
    if candidates:
        nyse_file = candidates[0]

if not trade_file:
    candidates = [f for f in files if 'list_db' in f]
    if candidates:
        trade_file = candidates[0]

print(f"Using NYSE file: {nyse_file}")
print(f"Using Trade file: {trade_file}")

if nyse_file and trade_file:
    with open(nyse_file, 'r') as f:
        nyse_data = json.load(f)
    
    with open(trade_file, 'r') as f:
        trade_symbols = json.load(f)
    
    print(f"Loaded {len(nyse_data)} NYSE stocks")
    print(f"Loaded {len(trade_symbols)} trade symbols")
    
    # Create mappings
    symbol_to_company = {}
    for item in nyse_data:
        symbol_to_company[item['Symbol']] = item['Company Description']
    
    nyse_symbols = set(symbol_to_company.keys())
    available = nyse_symbols.intersection(set(trade_symbols))
    
    print(f"Available NYSE symbols: {len(available)}")
    
    # Save
    with open('symbol_to_company.json', 'w') as f:
        json.dump(symbol_to_company, f)
    
    with open('available_symbols.json', 'w') as f:
        json.dump(sorted(list(available)), f)
    
    result = {
        'nyse_count': len(nyse_symbols),
        'available_count': len(available)
    }
else:
    result = {'error': 'files not found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'ETF': 'N'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'ETF': 'N'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'ETF': 'N'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'ETF': 'N'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'ETF': 'N'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'ETF': 'N'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'ETF': 'N'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'ETF': 'N'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.', 'ETF': 'N'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.', 'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'count': '234'}], 'var_functions.query_db:32': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:36': [{'Date': '2017-01-03', 'Open': '45.68999862670898', 'High': '45.72999954223633', 'Low': '44.66999816894531', 'Close': '44.93999862670898', 'Adj Close': '40.33967971801758', 'Volume': '770100'}, {'Date': '2017-01-04', 'Open': '45.09999847412109', 'High': '45.52000045776367', 'Low': '44.79999923706055', 'Close': '45.36000061035156', 'Adj Close': '40.716678619384766', 'Volume': '1089400'}, {'Date': '2017-01-05', 'Open': '45.09999847412109', 'High': '45.650001525878906', 'Low': '44.650001525878906', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '833400'}, {'Date': '2017-01-06', 'Open': '45.29999923706055', 'High': '45.560001373291016', 'Low': '44.97999954223633', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '1299300'}, {'Date': '2017-01-09', 'Open': '45.540000915527344', 'High': '45.61000061035156', 'Low': '44.91999816894531', 'Close': '44.959999084472656', 'Adj Close': '40.35763168334961', 'Volume': '697700'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'up_days': 3, 'down_days': 2, 'symbol': 'AIV'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:48': {'nyse_count': 0, 'trade_count': 0, 'available_count': 0}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}, {'Symbol': 'ARGD'}, {'Symbol': 'ARLO'}, {'Symbol': 'ASG'}, {'Symbol': 'AVA'}, {'Symbol': 'BANC'}, {'Symbol': 'BBU'}, {'Symbol': 'BBVA'}, {'Symbol': 'BDXA'}, {'Symbol': 'BKH'}, {'Symbol': 'BKT'}, {'Symbol': 'BLD'}, {'Symbol': 'BNS'}, {'Symbol': 'BV'}, {'Symbol': 'BZH'}, {'Symbol': 'CADE'}, {'Symbol': 'CAE'}, {'Symbol': 'CAF'}, {'Symbol': 'CBT'}, {'Symbol': 'CCC'}, {'Symbol': 'CCZ'}, {'Symbol': 'CHAP'}, {'Symbol': 'CIA'}, {'Symbol': 'CMA'}, {'Symbol': 'CMI'}, {'Symbol': 'CMSA'}, {'Symbol': 'CNK'}, {'Symbol': 'COTY'}, {'Symbol': 'CRC'}, {'Symbol': 'CRM'}, {'Symbol': 'CRS'}, {'Symbol': 'CSL'}, {'Symbol': 'CTS'}, {'Symbol': 'CUBE'}, {'Symbol': 'CURO'}, {'Symbol': 'CVIA'}, {'Symbol': 'CVX'}, {'Symbol': 'CXH'}, {'Symbol': 'DAC'}, {'Symbol': 'DDS'}, {'Symbol': 'DDT'}, {'Symbol': 'DEO'}, {'Symbol': 'DGX'}, {'Symbol': 'DMB'}, {'Symbol': 'DTQ'}, {'Symbol': 'DXC'}, {'Symbol': 'EARN'}, {'Symbol': 'EBS'}, {'Symbol': 'EGO'}, {'Symbol': 'EGY'}, {'Symbol': 'EIG'}, {'Symbol': 'ELF'}, {'Symbol': 'EMP'}, {'Symbol': 'ENLC'}, {'Symbol': 'EPR'}, {'Symbol': 'EPRT'}, {'Symbol': 'ES'}, {'Symbol': 'ESRT'}, {'Symbol': 'ESS'}, {'Symbol': 'ETM'}, {'Symbol': 'EV'}, {'Symbol': 'EVT'}, {'Symbol': 'EXP'}, {'Symbol': 'FMN'}, {'Symbol': 'FPAC'}, {'Symbol': 'FSM'}, {'Symbol': 'GCO'}, {'Symbol': 'GD'}, {'Symbol': 'GDL'}, {'Symbol': 'GDV'}, {'Symbol': 'GEL'}, {'Symbol': 'GJP'}, {'Symbol': 'GLOB'}, {'Symbol': 'GLT'}, {'Symbol': 'GOL'}, {'Symbol': 'GSLD'}, {'Symbol': 'GTY'}, {'Symbol': 'GVA'}, {'Symbol': 'GWB'}, {'Symbol': 'H'}, {'Symbol': 'HBI'}, {'Symbol': 'HDB'}, {'Symbol': 'HEP'}, {'Symbol': 'HIL'}, {'Symbol': 'HIO'}, {'Symbol': 'HIX'}, {'Symbol': 'HLF'}, {'Symbol': 'HLT'}, {'Symbol': 'HNI'}, {'Symbol': 'HRB'}, {'Symbol': 'HTFA'}, {'Symbol': 'IBM'}, {'Symbol': 'IGR'}, {'Symbol': 'IHC'}, {'Symbol': 'IPG'}, {'Symbol': 'IRM'}, {'Symbol': 'IT'}, {'Symbol': 'JGH'}, {'Symbol': 'JHY'}, {'Symbol': 'JKS'}, {'Symbol': 'JMP'}, {'Symbol': 'JNPR'}, {'Symbol': 'KMB'}, {'Symbol': 'KNX'}, {'Symbol': 'KW'}, {'Symbol': 'KYN'}, {'Symbol': 'LB'}, {'Symbol': 'LDOS'}, {'Symbol': 'LHC'}, {'Symbol': 'LHX'}, {'Symbol': 'LOMA'}, {'Symbol': 'MANU'}, {'Symbol': 'MDLX'}, {'Symbol': 'MDLY'}, {'Symbol': 'MED'}, {'Symbol': 'MFO'}, {'Symbol': 'MGR'}, {'Symbol': 'MGU'}, {'Symbol': 'MHE'}, {'Symbol': 'MIY'}, {'Symbol': 'MKC'}, {'Symbol': 'MLI'}, {'Symbol': 'MNE'}, {'Symbol': 'MR'}, {'Symbol': 'MS'}, {'Symbol': 'MTD'}, {'Symbol': 'MYD'}, {'Symbol': 'NFH'}, {'Symbol': 'NGG'}, {'Symbol': 'NJV'}, {'Symbol': 'NNI'}, {'Symbol': 'NNY'}, {'Symbol': 'NRUC'}, {'Symbol': 'NUE'}, {'Symbol': 'NXN'}, {'Symbol': 'OCFT'}, {'Symbol': 'OEC'}, {'Symbol': 'ORA'}, {'Symbol': 'ORAN'}, {'Symbol': 'ORCL'}, {'Symbol': 'ORN'}, {'Symbol': 'PAG'}, {'Symbol': 'PBI'}, {'Symbol': 'PFE'}, {'Symbol': 'PFSI'}, {'Symbol': 'PGR'}, {'Symbol': 'PIM'}, {'Symbol': 'PKE'}, {'Symbol': 'PLAN'}, {'Symbol': 'PLNT'}, {'Symbol': 'PMT'}, {'Symbol': 'PNM'}, {'Symbol': 'PPG'}, {'Symbol': 'PRSP'}, {'Symbol': 'PRTY'}, {'Symbol': 'PSV'}, {'Symbol': 'PSXP'}, {'Symbol': 'QTS'}, {'Symbol': 'QUAD'}, {'Symbol': 'RBC'}, {'Symbol': 'RCB'}, {'Symbol': 'RCI'}, {'Symbol': 'RES'}, {'Symbol': 'REXR'}, {'Symbol': 'RH'}, {'Symbol': 'RMT'}, {'Symbol': 'ROG'}, {'Symbol': 'ROL'}, {'Symbol': 'RPAI'}, {'Symbol': 'RPM'}, {'Symbol': 'RQI'}, {'Symbol': 'RWT'}, {'Symbol': 'SAF'}, {'Symbol': 'SAIL'}, {'Symbol': 'SAM'}, {'Symbol': 'SBR'}, {'Symbol': 'SCU'}, {'Symbol': 'SFUN'}, {'Symbol': 'SHAK'}, {'Symbol': 'SI'}, {'Symbol': 'SITC'}, {'Symbol': 'SJM'}, {'Symbol': 'SJT'}, {'Symbol': 'SJW'}, {'Symbol': 'SLF'}, {'Symbol': 'SMP'}, {'Symbol': 'SOL'}, {'Symbol': 'SPOT'}, {'Symbol': 'SRC'}, {'Symbol': 'SRF'}, {'Symbol': 'SRT'}, {'Symbol': 'SSD'}, {'Symbol': 'STG'}, {'Symbol': 'STL'}, {'Symbol': 'STON'}, {'Symbol': 'SYX'}, {'Symbol': 'TBB'}, {'Symbol': 'TCP'}, {'Symbol': 'TDJ'}, {'Symbol': 'TGP'}, {'Symbol': 'TLYS'}, {'Symbol': 'TNC'}, {'Symbol': 'TPH'}, {'Symbol': 'TRV'}, {'Symbol': 'TTI'}, {'Symbol': 'TUFN'}, {'Symbol': 'TWTR'}, {'Symbol': 'UHT'}, {'Symbol': 'UIS'}, {'Symbol': 'USX'}, {'Symbol': 'UTL'}, {'Symbol': 'VET'}, {'Symbol': 'VGR'}, {'Symbol': 'VHI'}, {'Symbol': 'VIV'}, {'Symbol': 'VKQ'}, {'Symbol': 'VRT'}, {'Symbol': 'VVI'}, {'Symbol': 'WOR'}, {'Symbol': 'WPG'}, {'Symbol': 'WSM'}, {'Symbol': 'X'}, {'Symbol': 'YEXT'}, {'Symbol': 'ZNH'}, {'Symbol': 'ZTR'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:58': {'status': 'debug_complete'}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:74': [{'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.execute_python:92': {'status': 'done'}, 'var_functions.execute_python:94': {'status': 'variables_identified'}, 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.query_db:98': 'file_storage/functions.query_db:98.json', 'var_functions.execute_python:114': {'status': 'checked_variables'}, 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:118': [{'Date': '2017-01-03', 'Open': '69.29000091552734', 'High': '70.86000061035156', 'Low': '69.0', 'Close': '70.54000091552734', 'Adj Close': '70.54000091552734', 'Volume': '8112200'}, {'Date': '2017-01-04', 'Open': '71.08000183105469', 'High': '73.06999969482422', 'Low': '70.76000213623047', 'Close': '72.80000305175781', 'Adj Close': '72.80000305175781', 'Volume': '9289500'}, {'Date': '2017-01-05', 'Open': '72.80999755859375', 'High': '73.66000366210938', 'Low': '72.52999877929688', 'Close': '72.79000091552734', 'Adj Close': '72.79000091552734', 'Volume': '4695600'}, {'Date': '2017-01-06', 'Open': '72.88999938964844', 'High': '74.12999725341797', 'Low': '72.55000305175781', 'Close': '73.80000305175781', 'Adj Close': '73.80000305175781', 'Volume': '4466100'}, {'Date': '2017-01-09', 'Open': '74.05000305175781', 'High': '74.44000244140625', 'Low': '73.51000213623047', 'Close': '73.95999908447266', 'Adj Close': '73.95999908447266', 'Volume': '3933100'}, {'Date': '2017-01-10', 'Open': '74.12000274658203', 'High': '74.30000305175781', 'Low': '73.44000244140625', 'Close': '73.9800033569336', 'Adj Close': '73.9800033569336', 'Volume': '3994800'}, {'Date': '2017-01-11', 'Open': '74.2699966430664', 'High': '76.08000183105469', 'Low': '74.05999755859375', 'Close': '75.7699966430664', 'Adj Close': '75.7699966430664', 'Volume': '7591300'}, {'Date': '2017-01-12', 'Open': '75.16999816894531', 'High': '75.75', 'Low': '74.0', 'Close': '75.20999908447266', 'Adj Close': '75.20999908447266', 'Volume': '4681700'}, {'Date': '2017-01-13', 'Open': '74.83999633789062', 'High': '75.77999877929688', 'Low': '74.69999694824219', 'Close': '75.63999938964844', 'Adj Close': '75.63999938964844', 'Volume': '3690000'}, {'Date': '2017-01-17', 'Open': '75.30000305175781', 'High': '75.30000305175781', 'Low': '74.37000274658203', 'Close': '75.0199966430664', 'Adj Close': '75.0199966430664', 'Volume': '3152500'}], 'var_functions.execute_python:120': {'status': 'analysis_prepared'}, 'var_functions.query_db:126': [{'total_days': '251', 'up_days': '137.0', 'down_days': '113.0'}], 'var_functions.execute_python:132': {'error': 'Could not find data keys'}, 'var_functions.execute_python:138': {'status': 'ready_to_start'}, 'var_functions.query_db:140': 'file_storage/functions.query_db:140.json'}

exec(code, env_args)
