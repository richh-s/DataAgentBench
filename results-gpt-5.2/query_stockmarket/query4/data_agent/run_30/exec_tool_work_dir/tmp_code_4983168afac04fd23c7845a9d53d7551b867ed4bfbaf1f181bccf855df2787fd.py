code = """import json, pandas as pd
symbols = var_call_lWjd5bU7yLBRjBeoDVOnWwKZ['symbols']
# Keep only plausible older tickers: length<=4 and no special chars (already)
syms = symbols
chunks = [syms[i:i+40] for i in range(0, len(syms), 40)]
queries=[]
for chunk in chunks:
    sub=[]
    for sym in chunk:
        sub.append(f"SELECT '{sym}' AS Symbol, MIN(Date) AS min_date, MAX(Date) AS max_date FROM \"{sym}\"")
    queries.append(" UNION ALL ".join(sub))
print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'first_query': queries[0]}))"""

env_args = {'var_call_4yJxBgN7c7oIup6a2mx3hC8o': 'file_storage/call_4yJxBgN7c7oIup6a2mx3hC8o.json', 'var_call_6kpaJecmr7U1o7D0tLDOguVk': 'file_storage/call_6kpaJecmr7U1o7D0tLDOguVk.json', 'var_call_lWjd5bU7yLBRjBeoDVOnWwKZ': {'n_symbols': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_izY7kplSnUtImSQlgme4oEyX': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_8fdBCqUcaD9QEiNsyzGXc9KO': [], 'var_call_vPrqf7PjQg9O676HUX99btEN': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}], 'var_call_mBuuCgELNqWrQ0KVIcCm7k8n': [{'min_date': '1962-01-02', 'max_date': '2020-04-01', 'n': '14663'}]}

exec(code, env_args)
