code = """import json
with open(var_call_GMzb8liIAFgyaYUJnZrUCUPM, 'r') as f:
    stockinfo_rows = json.load(f)
# Create dict symbol->company description
sym2desc = {r['Symbol']: r['company'] for r in stockinfo_rows}
# Choose symbols based on prior analysis
chosen = ['ARGD','AIN','AMP','AMN','AVA']
# Function to extract company name from description
import re
seps = [' is part of', ' is an ', ' is a ', ' is ', ' specializes in', ' specializes', ' offers', ' provides', ' operates', ' offers investors', ' provides investors', ' is renowned', ' is known']

names = []
for s in chosen:
    desc = sym2desc.get(s, '')
    name = desc
    # find earliest separator
    idx = None
    for sep in seps:
        i = desc.find(sep)
        if i != -1:
            if idx is None or i < idx:
                idx = i
    if idx is not None:
        name = desc[:idx]
    name = name.strip()
    names.append(name)

print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_GMzb8liIAFgyaYUJnZrUCUPM': 'file_storage/call_GMzb8liIAFgyaYUJnZrUCUPM.json', 'var_call_YZ5Xgzpbizwx61KMort8zyjY': 'file_storage/call_YZ5Xgzpbizwx61KMort8zyjY.json', 'var_call_5oQ3ExKCTmPFFVfC9fHSnacj': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_hTgHzxqh58kJJ4eskKXlLgoh': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_jLSL8XZPQPP2O6SSyNVqRKyW': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_GcnypWuT5OwNeXpnrqsBJwQz': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}]}

exec(code, env_args)
