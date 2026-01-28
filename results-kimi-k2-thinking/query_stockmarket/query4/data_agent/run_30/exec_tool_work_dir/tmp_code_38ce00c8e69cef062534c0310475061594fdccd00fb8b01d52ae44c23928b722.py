code = """import json
import os

# Load data files
all_path = globals()['var_functions.list_db:0']
nyse_path = globals()['var_functions.query_db:2']

with open(all_path) as f:
    all_tickers = json.load(f)
with open(nyse_path) as f:
    nyse_records = json.load(f)

# Create mapping
ticker_to_name = {}
for r in nyse_records:
    ticker_to_name[r['Symbol']] = r.get('Company Description', r['Symbol'])

# Get valid tickers
valid = [t for t in all_tickers if t in ticker_to_name]

# Build queries
queries = []
for t in valid:
    table = '"' + t + '"' if not t.isalnum() else t
    q = "SELECT '" + t + "' as s, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as u, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as d FROM " + table + " WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

union_query = " UNION ALL ".join(queries)
final = "WITH stats AS (" + union_query + ") SELECT s, u, d, (u - d) as diff FROM stats WHERE u > d ORDER BY diff DESC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'tickers': len(valid), 'query_start': union_query[:200]}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.list_db:0.json', 'var_functions.execute_python:14': {'all_tickers_count': 2753, 'nyse_tickers_count': 234, 'valid_tickers_count': 234}, 'var_functions.execute_python:16': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'var_functions.query_db:22': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'Close': '25.450000762939453'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'Close': '25.670000076293945'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'Close': '25.59000015258789'}, {'Date': '2019-10-29', 'Open': '25.61000061035156', 'Close': '25.56999969482422'}, {'Date': '2019-10-30', 'Open': '25.530000686645508', 'Close': '25.65999984741211'}, {'Date': '2019-10-31', 'Open': '25.729999542236328', 'Close': '25.76000022888184'}, {'Date': '2019-11-01', 'Open': '25.739999771118164', 'Close': '25.700000762939453'}, {'Date': '2019-11-04', 'Open': '25.68000030517578', 'Close': '25.670000076293945'}, {'Date': '2019-11-05', 'Open': '25.549999237060547', 'Close': '25.520000457763672'}, {'Date': '2019-11-06', 'Open': '25.520000457763672', 'Close': '25.530000686645508'}], 'var_functions.execute_python:24': {'ticker_count': 234, 'tickers': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:26': [{'days_2017': '251'}], 'var_functions.execute_python:28': {'ticker_count': 234, 'sample': ['CXH', 'HTFA', 'CMA', 'PPG', 'YEXT']}, 'var_functions.execute_python:34': {'count': 234, 'query_preview': "SELECT 'AEFC' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM AEFC WHERE Date >= '2017-01-01' AND Date <= '2017-12-"}, 'var_functions.execute_python:36': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}

exec(code, env_args)
