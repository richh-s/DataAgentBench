code = """import json, re
p = var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e
with open(p, 'r') as f:
    data = json.load(f)
# build mapping
sym2desc = {rec['Symbol']: rec.get('Company Description','') for rec in data}
# top symbols determined from prior queries
top_symbols = ['AIN','AMP','AMN','AVA','BKH']
names = []
pattern = re.compile(r"\b(is an|is a|is the|is|specializes in|specializes|offers|provides|operates|generates|focuses|serves)\b", flags=re.IGNORECASE)
for s in top_symbols:
    desc = sym2desc.get(s, '')
    if not desc:
        names.append('')
        continue
    m = pattern.search(desc)
    if m:
        name = desc[:m.start()].strip()
    else:
        # fallback: take up to first sentence terminator
        name = desc.split('.')[0].strip()
    names.append(name)

result = json.dumps(names)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_NOrOeolxry3KNh5kwmiCZwYH': 'file_storage/call_NOrOeolxry3KNh5kwmiCZwYH.json', 'var_call_mt89zRyxGP2HAtEkz4Dmna3z': 'file_storage/call_mt89zRyxGP2HAtEkz4Dmna3z.json', 'var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e': 'file_storage/call_qO5UOjJhgUd3ljUq9Cpo6Q7e.json', 'var_call_pzgIXutuSg5PSbl8pUosa5yX': {'count': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_bawAbP4LtISyMNzlK6JvnWep': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_aWAFHWEDlv5wER8TG7OjPTmh': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_call_DdKh1SWSk6wGBHg9hskwJkBR': [{'up_days': '143.0', 'down_days': '101.0'}], 'var_call_M5BfOlfcxU16nATtEqxbgAJn': [{'up_days': '118.0', 'down_days': '128.0'}], 'var_call_Zp37MDJc43Ryibdb27KIFO4j': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_call_iV0Rhw0DyF68GbP7oJCweCHo': [{'up_days': '123.0', 'down_days': '123.0'}], 'var_call_23we0BJNFY9dBLi9wsjh5cou': [{'up_days': '131.0', 'down_days': '117.0'}], 'var_call_oB1mbSbgN9y0qsMHHmMQVEAt': [{'up_days': '134.0', 'down_days': '111.0'}], 'var_call_ZLUOowd3kLW12Bl802sQzR5e': [{'up_days': '141.0', 'down_days': '110.0'}], 'var_call_HGlrpzQq8vVQLYEwTrrpBYc0': [{'up_days': '128.0', 'down_days': '123.0'}], 'var_call_j1Q0gNcAp5iWNxO6NcvKtKrY': [{'up_days': '80.0', 'down_days': '119.0'}], 'var_call_QlQ6A2ey989gBkDeEeGwkyxS': [{'up_days': '133.0', 'down_days': '82.0'}], 'var_call_tm5I0sLdCip7gN7sE9UC4c8r': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_call_62dFSKh6Ez4czJxdR1PJiisn': [{'up_days': '110.0', 'down_days': '110.0'}], 'var_call_LvkJLJkBbUBh6krotPyxk5CI': [{'up_days': '134.0', 'down_days': '112.0'}], 'var_call_k9ejcssRMhsLIkDuaoHJ6Owu': [{'up_days': '108.0', 'down_days': '119.0'}], 'var_call_FZwcSmG54BVWV9qyB09eH6g1': [{'up_days': '129.0', 'down_days': '120.0'}], 'var_call_2jvYLIH3LXxvLkWnBx9nT6p3': [{'up_days': '126.0', 'down_days': '104.0'}], 'var_call_QxhOCMMcC12ss1eDWkCsGJTs': [{'up_days': '83.0', 'down_days': '77.0'}], 'var_call_rbZT5WCjzRAWQIqJxAxfFEZg': [{'up_days': '134.0', 'down_days': '115.0'}]}

exec(code, env_args)
