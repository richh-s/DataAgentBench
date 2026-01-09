code = """import json, pandas as pd

syms = var_call_qrqL4JMwUacaGBFf37S8zISP['first_chunk']
# Actually need all intersect syms. Recompute from stored lists
import json
nyse_path = var_call_Kl9WM852XoYXievB7ZKT9WmR
with open(nyse_path,'r') as f: nyse=json.load(f)
nyse_syms=set(r['Symbol'] for r in nyse)
trade_path = var_call_5uLgy0g3jtEOABnbcitc36CV
with open(trade_path,'r') as f: tables=json.load(f)
syms=sorted(list(nyse_syms.intersection(set(tables))))

# check data coverage quickly by symbol max/min date
sample=syms[:30]
print('__RESULT__:')
print(json.dumps(sample))"""

env_args = {'var_call_Kl9WM852XoYXievB7ZKT9WmR': 'file_storage/call_Kl9WM852XoYXievB7ZKT9WmR.json', 'var_call_5uLgy0g3jtEOABnbcitc36CV': 'file_storage/call_5uLgy0g3jtEOABnbcitc36CV.json', 'var_call_qrqL4JMwUacaGBFf37S8zISP': {'symbol_count': 234, 'chunks': 1, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_call_OliLBdcv4tHwcqi7e4nro5QH': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_R6lJnEs0dmj5tktXtH9VXyGv': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}], 'var_call_wdRqwdsFHKParLM0yKdoRsnd': [{'c': '0'}]}

exec(code, env_args)
