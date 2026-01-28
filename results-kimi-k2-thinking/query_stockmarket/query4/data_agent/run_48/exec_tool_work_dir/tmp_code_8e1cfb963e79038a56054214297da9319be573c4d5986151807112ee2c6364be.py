code = """import json

# Read the NYSE non-ETF symbols from previous query
nyse_symbols_result = locals()['var_functions.query_db:9']
nyse_symbols = [item['Symbol'] for item in nyse_symbols_result]

# Read all table names from stocktrade database
with open(locals()['var_functions.list_db:5'], 'r') as f:
    all_tables = json.load(f)

# Find intersection (tables that are also NYSE non-ETF stocks)
tradeable_symbols = set(nyse_symbols) & set(all_tables)
tradeable_symbols = list(tradeable_symbols)

print(f"Number of NYSE non-ETF symbols: {len(nyse_symbols)}")
print(f"Number of tradeable symbols with price data: {len(tradeable_symbols)}")
print(f"First 10 tradeable symbols: {tradeable_symbols[:10]}")

# Store results for next step
result = {
    'tradeable_symbols': tradeable_symbols,
    'count': len(tradeable_symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:9': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}, {'Symbol': 'ARGD'}, {'Symbol': 'ARLO'}, {'Symbol': 'ASG'}, {'Symbol': 'AVA'}, {'Symbol': 'BANC'}, {'Symbol': 'BBU'}, {'Symbol': 'BBVA'}, {'Symbol': 'BDXA'}, {'Symbol': 'BKH'}, {'Symbol': 'BKT'}, {'Symbol': 'BLD'}, {'Symbol': 'BNS'}, {'Symbol': 'BV'}, {'Symbol': 'BZH'}, {'Symbol': 'CADE'}, {'Symbol': 'CAE'}, {'Symbol': 'CAF'}, {'Symbol': 'CBT'}, {'Symbol': 'CCC'}, {'Symbol': 'CCZ'}, {'Symbol': 'CHAP'}, {'Symbol': 'CIA'}, {'Symbol': 'CMA'}, {'Symbol': 'CMI'}, {'Symbol': 'CMSA'}, {'Symbol': 'CNK'}, {'Symbol': 'COTY'}, {'Symbol': 'CRC'}, {'Symbol': 'CRM'}, {'Symbol': 'CRS'}, {'Symbol': 'CSL'}, {'Symbol': 'CTS'}, {'Symbol': 'CUBE'}, {'Symbol': 'CURO'}, {'Symbol': 'CVIA'}, {'Symbol': 'CVX'}, {'Symbol': 'CXH'}, {'Symbol': 'DAC'}, {'Symbol': 'DDS'}, {'Symbol': 'DDT'}, {'Symbol': 'DEO'}, {'Symbol': 'DGX'}, {'Symbol': 'DMB'}, {'Symbol': 'DTQ'}, {'Symbol': 'DXC'}, {'Symbol': 'EARN'}, {'Symbol': 'EBS'}, {'Symbol': 'EGO'}, {'Symbol': 'EGY'}, {'Symbol': 'EIG'}, {'Symbol': 'ELF'}, {'Symbol': 'EMP'}, {'Symbol': 'ENLC'}, {'Symbol': 'EPR'}, {'Symbol': 'EPRT'}, {'Symbol': 'ES'}, {'Symbol': 'ESRT'}, {'Symbol': 'ESS'}, {'Symbol': 'ETM'}, {'Symbol': 'EV'}, {'Symbol': 'EVT'}, {'Symbol': 'EXP'}, {'Symbol': 'FMN'}, {'Symbol': 'FPAC'}, {'Symbol': 'FSM'}, {'Symbol': 'GCO'}, {'Symbol': 'GD'}, {'Symbol': 'GDL'}, {'Symbol': 'GDV'}, {'Symbol': 'GEL'}, {'Symbol': 'GJP'}, {'Symbol': 'GLOB'}, {'Symbol': 'GLT'}, {'Symbol': 'GOL'}, {'Symbol': 'GSLD'}, {'Symbol': 'GTY'}, {'Symbol': 'GVA'}, {'Symbol': 'GWB'}, {'Symbol': 'H'}, {'Symbol': 'HBI'}, {'Symbol': 'HDB'}, {'Symbol': 'HEP'}, {'Symbol': 'HIL'}, {'Symbol': 'HIO'}, {'Symbol': 'HIX'}, {'Symbol': 'HLF'}, {'Symbol': 'HLT'}, {'Symbol': 'HNI'}, {'Symbol': 'HRB'}, {'Symbol': 'HTFA'}, {'Symbol': 'IBM'}, {'Symbol': 'IGR'}, {'Symbol': 'IHC'}, {'Symbol': 'IPG'}, {'Symbol': 'IRM'}, {'Symbol': 'IT'}, {'Symbol': 'JGH'}, {'Symbol': 'JHY'}, {'Symbol': 'JKS'}, {'Symbol': 'JMP'}, {'Symbol': 'JNPR'}, {'Symbol': 'KMB'}, {'Symbol': 'KNX'}, {'Symbol': 'KW'}, {'Symbol': 'KYN'}, {'Symbol': 'LB'}, {'Symbol': 'LDOS'}, {'Symbol': 'LHC'}, {'Symbol': 'LHX'}, {'Symbol': 'LOMA'}, {'Symbol': 'MANU'}, {'Symbol': 'MDLX'}, {'Symbol': 'MDLY'}, {'Symbol': 'MED'}, {'Symbol': 'MFO'}, {'Symbol': 'MGR'}, {'Symbol': 'MGU'}, {'Symbol': 'MHE'}, {'Symbol': 'MIY'}, {'Symbol': 'MKC'}, {'Symbol': 'MLI'}, {'Symbol': 'MNE'}, {'Symbol': 'MR'}, {'Symbol': 'MS'}, {'Symbol': 'MTD'}, {'Symbol': 'MYD'}, {'Symbol': 'NFH'}, {'Symbol': 'NGG'}, {'Symbol': 'NJV'}, {'Symbol': 'NNI'}, {'Symbol': 'NNY'}, {'Symbol': 'NRUC'}, {'Symbol': 'NUE'}, {'Symbol': 'NXN'}, {'Symbol': 'OCFT'}, {'Symbol': 'OEC'}, {'Symbol': 'ORA'}, {'Symbol': 'ORAN'}, {'Symbol': 'ORCL'}, {'Symbol': 'ORN'}, {'Symbol': 'PAG'}, {'Symbol': 'PBI'}, {'Symbol': 'PFE'}, {'Symbol': 'PFSI'}, {'Symbol': 'PGR'}, {'Symbol': 'PIM'}, {'Symbol': 'PKE'}, {'Symbol': 'PLAN'}, {'Symbol': 'PLNT'}, {'Symbol': 'PMT'}, {'Symbol': 'PNM'}, {'Symbol': 'PPG'}, {'Symbol': 'PRSP'}, {'Symbol': 'PRTY'}, {'Symbol': 'PSV'}, {'Symbol': 'PSXP'}, {'Symbol': 'QTS'}, {'Symbol': 'QUAD'}, {'Symbol': 'RBC'}, {'Symbol': 'RCB'}, {'Symbol': 'RCI'}, {'Symbol': 'RES'}, {'Symbol': 'REXR'}, {'Symbol': 'RH'}, {'Symbol': 'RMT'}, {'Symbol': 'ROG'}, {'Symbol': 'ROL'}, {'Symbol': 'RPAI'}, {'Symbol': 'RPM'}, {'Symbol': 'RQI'}, {'Symbol': 'RWT'}, {'Symbol': 'SAF'}, {'Symbol': 'SAIL'}, {'Symbol': 'SAM'}, {'Symbol': 'SBR'}, {'Symbol': 'SCU'}, {'Symbol': 'SFUN'}, {'Symbol': 'SHAK'}, {'Symbol': 'SI'}, {'Symbol': 'SITC'}, {'Symbol': 'SJM'}, {'Symbol': 'SJT'}, {'Symbol': 'SJW'}, {'Symbol': 'SLF'}, {'Symbol': 'SMP'}, {'Symbol': 'SOL'}, {'Symbol': 'SPOT'}, {'Symbol': 'SRC'}, {'Symbol': 'SRF'}, {'Symbol': 'SRT'}, {'Symbol': 'SSD'}, {'Symbol': 'STG'}, {'Symbol': 'STL'}, {'Symbol': 'STON'}, {'Symbol': 'SYX'}, {'Symbol': 'TBB'}, {'Symbol': 'TCP'}, {'Symbol': 'TDJ'}, {'Symbol': 'TGP'}, {'Symbol': 'TLYS'}, {'Symbol': 'TNC'}, {'Symbol': 'TPH'}, {'Symbol': 'TRV'}, {'Symbol': 'TTI'}, {'Symbol': 'TUFN'}, {'Symbol': 'TWTR'}, {'Symbol': 'UHT'}, {'Symbol': 'UIS'}, {'Symbol': 'USX'}, {'Symbol': 'UTL'}, {'Symbol': 'VET'}, {'Symbol': 'VGR'}, {'Symbol': 'VHI'}, {'Symbol': 'VIV'}, {'Symbol': 'VKQ'}, {'Symbol': 'VRT'}, {'Symbol': 'VVI'}, {'Symbol': 'WOR'}, {'Symbol': 'WPG'}, {'Symbol': 'WSM'}, {'Symbol': 'X'}, {'Symbol': 'YEXT'}, {'Symbol': 'ZNH'}, {'Symbol': 'ZTR'}]}

exec(code, env_args)
