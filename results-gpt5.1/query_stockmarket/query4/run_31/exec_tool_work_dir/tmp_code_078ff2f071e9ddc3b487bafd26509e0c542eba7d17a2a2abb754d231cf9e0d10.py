code = """import json, pandas as pd
symbols_path = var_call_zU99Fxte1Bcp2x6apIWJa9lZ
with open(symbols_path) as f:
    all_symbols = json.load(f)
meta_path = var_call_aUdwq8xcMiHn7BUlVAl9daU3
with open(meta_path) as f:
    meta = json.load(f)
nyse_non_etf = {row['Symbol']: row['Company Description'] for row in meta}
nyse_symbols = [s for s in all_symbols if s in nyse_non_etf]
nyse_symbols = nyse_symbols[:200]
res = json.dumps({'symbols': nyse_symbols})
print('__RESULT__:')
print(res)"""

env_args = {'var_call_zU99Fxte1Bcp2x6apIWJa9lZ': 'file_storage/call_zU99Fxte1Bcp2x6apIWJa9lZ.json', 'var_call_aUdwq8xcMiHn7BUlVAl9daU3': 'file_storage/call_aUdwq8xcMiHn7BUlVAl9daU3.json', 'var_call_39whR5F4OITn5QCzy2rx0Md8': {'chunks': [['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], ['DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA'], ['IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN'], ['PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT'], ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']]}, 'var_call_NV7BcVqGbJlCAhO6OaYbQgM7': [], 'var_call_6qUKn6KxCfjzqeEjaZAvZven': 'file_storage/call_6qUKn6KxCfjzqeEjaZAvZven.json', 'var_call_ToKep71vrqlRfdLijscHZsCE': 'file_storage/call_ToKep71vrqlRfdLijscHZsCE.json', 'var_call_ia37ELgJpNtotuzwg2i3jXTT': [], 'var_call_8jmXI6yLrkO0rfnjBQwdfRSd': 'file_storage/call_8jmXI6yLrkO0rfnjBQwdfRSd.json', 'var_call_LrGMZZKg8slZEnRXqpxmS93G': {'AIN': {'up': 143, 'down': 101}, 'AIV': {'up': 118, 'down': 128}, 'AJRD': {'up': 123, 'down': 123}}}

exec(code, env_args)
