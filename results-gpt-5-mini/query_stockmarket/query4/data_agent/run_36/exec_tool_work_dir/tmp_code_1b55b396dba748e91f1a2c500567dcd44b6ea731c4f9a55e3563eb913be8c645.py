code = """import json
with open(var_call_ncBu1Lzcg4m7AkwV5rMhxZUu, 'r') as f:
    updown = json.load(f)
with open(var_call_vmDsNwAUDEnAmcVZgN9s4pNQ, 'r') as f:
    info = json.load(f)

# Map symbol to company description (name)
desc = {r['Symbol']: r['Company Description'] for r in info}

# Build final ordered list of company names in the order from updown
result = []
for r in updown:
    sym = r['symbol']
    name = desc.get(sym, sym)
    result.append({"symbol": sym, "company_name": name, "up_count": float(r['up_count']), "down_count": float(r['down_count'])})

# We only need the names (not symbols) of the top 5
names = [r['company_name'] for r in result]

print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_HU07LgpwYKt6DI2bxvoKFoaW': 'file_storage/call_HU07LgpwYKt6DI2bxvoKFoaW.json', 'var_call_bp0oaTukSilXP0rpxGJ4KeOY': 'file_storage/call_bp0oaTukSilXP0rpxGJ4KeOY.json', 'var_call_36uZa34fIjQJ0zYclTxHC53x': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_ncBu1Lzcg4m7AkwV5rMhxZUu': [{'symbol': 'AIN', 'up_count': '143.0', 'down_count': '101.0'}, {'symbol': 'AMP', 'up_count': '141.0', 'down_count': '110.0'}, {'symbol': 'AMN', 'up_count': '134.0', 'down_count': '111.0'}, {'symbol': 'AVA', 'up_count': '134.0', 'down_count': '112.0'}, {'symbol': 'ARGD', 'up_count': '133.0', 'down_count': '82.0'}], 'var_call_vmDsNwAUDEnAmcVZgN9s4pNQ': [{'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'ARGD', 'Company Description': 'Argo Group International Holdings, Ltd. specializes in providing insurance and reinsurance solutions, helping businesses manage risks and safeguard their assets worldwide.'}, {'Symbol': 'AVA', 'Company Description': 'Avista Corporation is an energy company that provides electricity and natural gas services to customers across the Pacific Northwest, focusing on sustainable and reliable energy solutions.'}]}

exec(code, env_args)
