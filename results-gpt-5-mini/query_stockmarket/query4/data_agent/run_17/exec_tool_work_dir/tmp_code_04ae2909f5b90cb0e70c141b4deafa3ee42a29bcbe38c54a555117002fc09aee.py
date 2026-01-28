code = """import json, re
# Load sym_to_name mapping from earlier storage
with open(var_call_CS6mbDQaTBWaHXltXPXrtA1x, 'r') as f:
    data = json.load(f)
mapping = data.get('sym_to_name', {})
# Selected top-5 symbols based on earlier queries
selected = ['AIN', 'AMP', 'AVA', 'AMN', 'ARGD']
names = []
pattern = re.compile(r"^(.*?)(?:\s+(?:is|specializes|offers|provides|operates|serving|serves|offers|focuses|is an|is a|is an investment|is part of|is renowned|is a leading))", re.IGNORECASE)
for s in selected:
    desc = mapping.get(s, '')
    m = pattern.search(desc)
    if m:
        name = m.group(1).strip()
    else:
        # fallback: take first 4 words
        name = ' '.join(desc.split()[:4])
    names.append(name)
result = {'names': names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bYQyMqrBbLBPnHo5oOIwzCIP': ['stockinfo'], 'var_call_Js61eKeKPd8pJkBCv55jt5nu': 'file_storage/call_Js61eKeKPd8pJkBCv55jt5nu.json', 'var_call_LbZzmGVobT3Mgm9lwFj5SNHc': 'file_storage/call_LbZzmGVobT3Mgm9lwFj5SNHc.json', 'var_call_CS6mbDQaTBWaHXltXPXrtA1x': 'file_storage/call_CS6mbDQaTBWaHXltXPXrtA1x.json', 'var_call_kE4PCNKSQbPBMTRgCjDhjmbM': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_DVpfoBQ5ijct5e3CrI7C7XHt': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_yjyW3ADu0EG9GsuW3sLx0HQd': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_RLjmXQPBnHsvlc9SqGerQDs8': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_V2lzqikPdMiMoRfnw5HDAuXA': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_Dg0HTnJN6ejI1CsNXeTrP7Sv': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_LbUCGojhRzBzfWdivcZwRE9w': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_i4Lwc4RAOHnQC3n5r9TbJlJ2': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_JvFCYIehMerBdgx7tcUMmY9W': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_bGihKHbi77MgXQSOUbiQb24u': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_LQgfQ5SgCkVrNkJ9YEE1QYYx': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_nzfsMl5V1yos3NjbBt7kqMZk': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_gkNUZ1NDObe6rg2K4tGbmXo8': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_H49CWMqM4RGUXosgtKOpfE52': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_SOedsionjlJ6JNJBH5MztUfQ': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_jKEvoCEp6Oc84355dDy2hfyn': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}]}

exec(code, env_args)
