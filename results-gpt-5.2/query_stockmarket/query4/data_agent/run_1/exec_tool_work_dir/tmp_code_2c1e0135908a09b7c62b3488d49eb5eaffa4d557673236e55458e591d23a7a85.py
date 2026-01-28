code = """import json, pandas as pd

counts = var_call_oN4ufVAbCxnFqdgcy4NJ1v6t
if isinstance(counts, str):
    with open(counts,'r') as f:
        counts = json.load(f)
counts_df = pd.DataFrame(counts)

# numeric
for c in ['up_days','down_days']:
    counts_df[c] = pd.to_numeric(counts_df[c], errors='coerce')
counts_df = counts_df.dropna(subset=['up_days','down_days'])
counts_df = counts_df[counts_df['up_days'] > counts_df['down_days']].copy()
counts_df['diff'] = counts_df['up_days'] - counts_df['down_days']

# join company names
info = var_call_pMsh5yuKRacB6eyqcaS4pm30
if isinstance(info, str):
    with open(info,'r') as f:
        info = json.load(f)
info_df = pd.DataFrame(info)
merged = counts_df.merge(info_df, on='Symbol', how='left')

# top 5 by diff, tie-breaker by up_days desc then Symbol
merged = merged.sort_values(['diff','up_days','Symbol'], ascending=[False, False, True]).head(5)

out = merged[['Symbol','company_name','up_days','down_days','diff']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pMsh5yuKRacB6eyqcaS4pm30': 'file_storage/call_pMsh5yuKRacB6eyqcaS4pm30.json', 'var_call_LRg6M8X1BFvDc4y8td0zwKSz': 'file_storage/call_LRg6M8X1BFvDc4y8td0zwKSz.json', 'var_call_7hgfO4yiK2vTkX1NafddHUZH': {'n_candidates': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_LhgMFVhL5wXiEfgBtdiWMcuR': 'file_storage/call_LhgMFVhL5wXiEfgBtdiWMcuR.json', 'var_call_zV7r9fAXlHjDoNsnQKaBBIpK': 'file_storage/call_zV7r9fAXlHjDoNsnQKaBBIpK.json', 'var_call_oN4ufVAbCxnFqdgcy4NJ1v6t': 'file_storage/call_oN4ufVAbCxnFqdgcy4NJ1v6t.json'}

exec(code, env_args)
