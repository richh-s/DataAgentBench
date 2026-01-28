code = """import json, re
# var_call_WGtNdnmvbVbn2kAfzsgFDDO4 is available as a Python variable (list of dicts)
info = var_call_WGtNdnmvbVbn2kAfzsgFDDO4
# create mapping symbol -> company description
mapping = {r['Symbol']: r['Company Description'] for r in info}
order = ['MFO','ARGD','HDB','AIN','DTQ']
names = []
for sym in order:
    desc = mapping.get(sym, '')
    if not desc:
        names.append('')
        continue
    # split at common verbs that start the description
    parts = re.split(r'\s+is\b|\s+is an\b|\s+is a\b|\s+specializes\b|\s+provides\b|\s+offers\b|\s+focuses\b', desc, flags=re.IGNORECASE)
    name_part = parts[0].strip().strip(',')
    names.append(name_part)
# final output as list of names
print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_vjXSw3GgFSZmNZ3yUiZxY25q': 'file_storage/call_vjXSw3GgFSZmNZ3yUiZxY25q.json', 'var_call_HYFoZC2x6p6sNxHwwLnio59Y': 'file_storage/call_HYFoZC2x6p6sNxHwwLnio59Y.json', 'var_call_1UthaBMyMoepZHSkrqD3KjAD': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_PCC3A4uLbd67H6sNsaIj1Nwr': {'count': 234}, 'var_call_bvNaAiQzfyPjbbvG5q1mc9Io': [{'symbol': 'MFO', 'up_days': '139.0', 'down_days': '67.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'HDB', 'up_days': '146.0', 'down_days': '102.0'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'DTQ', 'up_days': '139.0', 'down_days': '98.0'}], 'var_call_WGtNdnmvbVbn2kAfzsgFDDO4': [{'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'ARGD', 'Company Description': 'Argo Group International Holdings, Ltd. specializes in providing insurance and reinsurance solutions, helping businesses manage risks and safeguard their assets worldwide.'}, {'Symbol': 'DTQ', 'Company Description': 'DTE Energy Company provides essential energy services, specializing in electricity and natural gas distribution to support and power homes and businesses across the Midwest.'}, {'Symbol': 'HDB', 'Company Description': 'HDFC Bank Limited is a leading financial institution in India, offering a wide range of banking services including personal and corporate banking, loans, and wealth management solutions.'}, {'Symbol': 'MFO', 'Company Description': 'MFA Financial, Inc. is a company that specializes in investing in residential mortgage assets, focusing on generating steady income through a diversified portfolio of real estate-related investments.'}]}

exec(code, env_args)
