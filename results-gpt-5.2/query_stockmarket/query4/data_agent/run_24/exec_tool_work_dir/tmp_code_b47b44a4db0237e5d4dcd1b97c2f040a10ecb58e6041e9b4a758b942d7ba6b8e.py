code = """import json, pandas as pd

path_counts = var_call_bgHgJeDBVBe7icHIlHKIsuUV
with open(path_counts,'r') as f:
    counts = json.load(f)
df = pd.DataFrame(counts)
# convert to numeric
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# filter more up than down
df = df[df['up_days'] > df['down_days']].copy()

# rank by up_days desc, tie-break by (up_days-down_days) desc, then symbol
df['diff'] = df['up_days'] - df['down_days']
df = df.sort_values(['up_days','diff','Symbol'], ascending=[False, False, True]).head(5)

syms = df['Symbol'].tolist()

# load stock info mapping symbol->company_name
path_info = var_call_1azq8avYekP4AJfnP0YbucJf
with open(path_info,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
name_map = dict(zip(info_df['Symbol'], info_df['company_name']))

names = [name_map.get(s, s) for s in syms]

out = json.dumps({'top5': [{'Symbol': s, 'Name': name_map.get(s), 'up_days': float(df.loc[df.Symbol==s,'up_days'].iloc[0]), 'down_days': float(df.loc[df.Symbol==s,'down_days'].iloc[0])} for s in syms]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_1azq8avYekP4AJfnP0YbucJf': 'file_storage/call_1azq8avYekP4AJfnP0YbucJf.json', 'var_call_1WDp8YTpSz1oSWbHEA5yX3HS': 'file_storage/call_1WDp8YTpSz1oSWbHEA5yX3HS.json', 'var_call_SbusLbdCXWDlbeb0YTBEXw5l': {'n_symbols': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_bgHgJeDBVBe7icHIlHKIsuUV': 'file_storage/call_bgHgJeDBVBe7icHIlHKIsuUV.json'}

exec(code, env_args)
