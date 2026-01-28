code = """import json, os, sys

# Debug file paths
nyse_path = 'var_functions.query_db:64'
tickers_path = 'var_functions.list_db:58'

print(f'File sizes: NYSE={os.path.getsize(nyse_path)}, Tickers={os.path.getsize(tickers_path)}')

# Load data with error handling
nyse_stocks = []
available_tickers = []

try:
    with open(nyse_path, 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            nyse_stocks = json.loads(content)
        else:
            for line in content.split('\n'):
                if line.strip():
                    nyse_stocks.append(json.loads(line))
    print(f'Loaded {len(nyse_stocks)} NYSE stocks')
except Exception as e:
    print(f'Error loading NYSE: {e}')

try:
    with open(tickers_path, 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            available_tickers = json.loads(content)
        else:
            for line in content.split('\n'):
                if line.strip():
                    available_tickers.append(line.strip('"'))
    print(f'Loaded {len(available_tickers)} tickers')
except Exception as e:
    print(f'Error loading tickers: {e}')

# Process if loaded successfully
if nyse_stocks and available_tickers:
    symbol_to_desc = {}
    for stock in nyse_stocks:
        if isinstance(stock, dict) and 'Symbol' in stock:
            symbol_to_desc[stock['Symbol']] = stock['Company Description']
    
    nyse_set = set(symbol_to_desc.keys())
    available_set = set(available_tickers)
    common = nyse_set.intersection(available_set)
    
    print(f'Common symbols: {len(common)}')
    print(f'Sample common: {list(common)[:10]}')
    
    result = {'common_count': len(common), 'common_symbols': list(common), 'symbol_desc': symbol_to_desc}
else:
    result = {'error': 'Failed to load data'}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Date': '2017-01-03', 'Open': '34.66999816894531', 'High': '35.220001220703125', 'Low': '34.52000045776367', 'Close': '35.15999984741211', 'Adj Close': '33.58498001098633', 'Volume': '631900'}, {'Date': '2017-01-04', 'Open': '35.06999969482422', 'High': '35.9900016784668', 'Low': '34.970001220703125', 'Close': '35.93000030517578', 'Adj Close': '34.320491790771484', 'Volume': '840900'}, {'Date': '2017-01-05', 'Open': '35.81999969482422', 'High': '36.29999923706055', 'Low': '35.43000030517578', 'Close': '36.02999877929688', 'Adj Close': '34.4160041809082', 'Volume': '918000'}, {'Date': '2017-01-06', 'Open': '36.18000030517578', 'High': '36.27999877929688', 'Low': '35.529998779296875', 'Close': '35.540000915527344', 'Adj Close': '33.94796371459961', 'Volume': '663000'}, {'Date': '2017-01-09', 'Open': '35.459999084472656', 'High': '35.459999084472656', 'Low': '34.70000076293945', 'Close': '34.72999954223633', 'Adj Close': '33.17424011230469', 'Volume': '659700'}], 'var_functions.execute_python:30': {'status': 'analysis_started', 'message': 'Need to query 2017 data for NYSE stocks'}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}, {'Symbol': 'ARGD'}, {'Symbol': 'ARLO'}, {'Symbol': 'ASG'}, {'Symbol': 'AVA'}, {'Symbol': 'BANC'}, {'Symbol': 'BBU'}, {'Symbol': 'BBVA'}, {'Symbol': 'BDXA'}, {'Symbol': 'BKH'}, {'Symbol': 'BKT'}, {'Symbol': 'BLD'}, {'Symbol': 'BNS'}, {'Symbol': 'BV'}, {'Symbol': 'BZH'}, {'Symbol': 'CADE'}, {'Symbol': 'CAE'}, {'Symbol': 'CAF'}, {'Symbol': 'CBT'}, {'Symbol': 'CCC'}, {'Symbol': 'CCZ'}, {'Symbol': 'CHAP'}, {'Symbol': 'CIA'}, {'Symbol': 'CMA'}, {'Symbol': 'CMI'}, {'Symbol': 'CMSA'}, {'Symbol': 'CNK'}, {'Symbol': 'COTY'}, {'Symbol': 'CRC'}, {'Symbol': 'CRM'}, {'Symbol': 'CRS'}, {'Symbol': 'CSL'}, {'Symbol': 'CTS'}, {'Symbol': 'CUBE'}, {'Symbol': 'CURO'}, {'Symbol': 'CVIA'}, {'Symbol': 'CVX'}, {'Symbol': 'CXH'}, {'Symbol': 'DAC'}, {'Symbol': 'DDS'}, {'Symbol': 'DDT'}, {'Symbol': 'DEO'}, {'Symbol': 'DGX'}, {'Symbol': 'DMB'}, {'Symbol': 'DTQ'}, {'Symbol': 'DXC'}, {'Symbol': 'EARN'}, {'Symbol': 'EBS'}, {'Symbol': 'EGO'}, {'Symbol': 'EGY'}, {'Symbol': 'EIG'}, {'Symbol': 'ELF'}, {'Symbol': 'EMP'}, {'Symbol': 'ENLC'}, {'Symbol': 'EPR'}, {'Symbol': 'EPRT'}, {'Symbol': 'ES'}, {'Symbol': 'ESRT'}, {'Symbol': 'ESS'}, {'Symbol': 'ETM'}, {'Symbol': 'EV'}, {'Symbol': 'EVT'}, {'Symbol': 'EXP'}, {'Symbol': 'FMN'}, {'Symbol': 'FPAC'}, {'Symbol': 'FSM'}, {'Symbol': 'GCO'}, {'Symbol': 'GD'}, {'Symbol': 'GDL'}, {'Symbol': 'GDV'}, {'Symbol': 'GEL'}, {'Symbol': 'GJP'}, {'Symbol': 'GLOB'}, {'Symbol': 'GLT'}, {'Symbol': 'GOL'}, {'Symbol': 'GSLD'}, {'Symbol': 'GTY'}, {'Symbol': 'GVA'}, {'Symbol': 'GWB'}, {'Symbol': 'H'}, {'Symbol': 'HBI'}, {'Symbol': 'HDB'}, {'Symbol': 'HEP'}, {'Symbol': 'HIL'}, {'Symbol': 'HIO'}, {'Symbol': 'HIX'}, {'Symbol': 'HLF'}, {'Symbol': 'HLT'}, {'Symbol': 'HNI'}, {'Symbol': 'HRB'}, {'Symbol': 'HTFA'}, {'Symbol': 'IBM'}, {'Symbol': 'IGR'}, {'Symbol': 'IHC'}, {'Symbol': 'IPG'}, {'Symbol': 'IRM'}, {'Symbol': 'IT'}, {'Symbol': 'JGH'}, {'Symbol': 'JHY'}, {'Symbol': 'JKS'}, {'Symbol': 'JMP'}, {'Symbol': 'JNPR'}, {'Symbol': 'KMB'}, {'Symbol': 'KNX'}, {'Symbol': 'KW'}, {'Symbol': 'KYN'}, {'Symbol': 'LB'}, {'Symbol': 'LDOS'}, {'Symbol': 'LHC'}, {'Symbol': 'LHX'}, {'Symbol': 'LOMA'}, {'Symbol': 'MANU'}, {'Symbol': 'MDLX'}, {'Symbol': 'MDLY'}, {'Symbol': 'MED'}, {'Symbol': 'MFO'}, {'Symbol': 'MGR'}, {'Symbol': 'MGU'}, {'Symbol': 'MHE'}, {'Symbol': 'MIY'}, {'Symbol': 'MKC'}, {'Symbol': 'MLI'}, {'Symbol': 'MNE'}, {'Symbol': 'MR'}, {'Symbol': 'MS'}, {'Symbol': 'MTD'}, {'Symbol': 'MYD'}, {'Symbol': 'NFH'}, {'Symbol': 'NGG'}, {'Symbol': 'NJV'}, {'Symbol': 'NNI'}, {'Symbol': 'NNY'}, {'Symbol': 'NRUC'}, {'Symbol': 'NUE'}, {'Symbol': 'NXN'}, {'Symbol': 'OCFT'}, {'Symbol': 'OEC'}, {'Symbol': 'ORA'}, {'Symbol': 'ORAN'}, {'Symbol': 'ORCL'}, {'Symbol': 'ORN'}, {'Symbol': 'PAG'}, {'Symbol': 'PBI'}, {'Symbol': 'PFE'}, {'Symbol': 'PFSI'}, {'Symbol': 'PGR'}, {'Symbol': 'PIM'}, {'Symbol': 'PKE'}, {'Symbol': 'PLAN'}, {'Symbol': 'PLNT'}, {'Symbol': 'PMT'}, {'Symbol': 'PNM'}, {'Symbol': 'PPG'}, {'Symbol': 'PRSP'}, {'Symbol': 'PRTY'}, {'Symbol': 'PSV'}, {'Symbol': 'PSXP'}, {'Symbol': 'QTS'}, {'Symbol': 'QUAD'}, {'Symbol': 'RBC'}, {'Symbol': 'RCB'}, {'Symbol': 'RCI'}, {'Symbol': 'RES'}, {'Symbol': 'REXR'}, {'Symbol': 'RH'}, {'Symbol': 'RMT'}, {'Symbol': 'ROG'}, {'Symbol': 'ROL'}, {'Symbol': 'RPAI'}, {'Symbol': 'RPM'}, {'Symbol': 'RQI'}, {'Symbol': 'RWT'}, {'Symbol': 'SAF'}, {'Symbol': 'SAIL'}, {'Symbol': 'SAM'}, {'Symbol': 'SBR'}, {'Symbol': 'SCU'}, {'Symbol': 'SFUN'}, {'Symbol': 'SHAK'}, {'Symbol': 'SI'}, {'Symbol': 'SITC'}, {'Symbol': 'SJM'}, {'Symbol': 'SJT'}, {'Symbol': 'SJW'}, {'Symbol': 'SLF'}, {'Symbol': 'SMP'}, {'Symbol': 'SOL'}, {'Symbol': 'SPOT'}, {'Symbol': 'SRC'}, {'Symbol': 'SRF'}, {'Symbol': 'SRT'}, {'Symbol': 'SSD'}, {'Symbol': 'STG'}, {'Symbol': 'STL'}, {'Symbol': 'STON'}, {'Symbol': 'SYX'}, {'Symbol': 'TBB'}, {'Symbol': 'TCP'}, {'Symbol': 'TDJ'}, {'Symbol': 'TGP'}, {'Symbol': 'TLYS'}, {'Symbol': 'TNC'}, {'Symbol': 'TPH'}, {'Symbol': 'TRV'}, {'Symbol': 'TTI'}, {'Symbol': 'TUFN'}, {'Symbol': 'TWTR'}, {'Symbol': 'UHT'}, {'Symbol': 'UIS'}, {'Symbol': 'USX'}, {'Symbol': 'UTL'}, {'Symbol': 'VET'}, {'Symbol': 'VGR'}, {'Symbol': 'VHI'}, {'Symbol': 'VIV'}, {'Symbol': 'VKQ'}, {'Symbol': 'VRT'}, {'Symbol': 'VVI'}, {'Symbol': 'WOR'}, {'Symbol': 'WPG'}, {'Symbol': 'WSM'}, {'Symbol': 'X'}, {'Symbol': 'YEXT'}, {'Symbol': 'ZNH'}, {'Symbol': 'ZTR'}], 'var_functions.list_db:58': 'file_storage/functions.list_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': [{'Symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}], 'var_functions.query_db:68': [{'Symbol': 'AIN', 'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
