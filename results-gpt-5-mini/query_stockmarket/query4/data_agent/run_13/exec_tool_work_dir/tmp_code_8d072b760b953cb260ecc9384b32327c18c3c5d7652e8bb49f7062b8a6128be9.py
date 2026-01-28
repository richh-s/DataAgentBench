code = """import json
# Read query results
rows = var_call_dldzx7cRDx7lqdaUQyw4x7OK
company_info = var_call_rs6SNP8LOpkZMgnxYnjmnwpe

# Build mapping from symbol to company name (extract name from Company Description: assume first phrase before 'is' or 'specializes' or 'specializes in')
import re
sym_to_name = {}
for rec in company_info:
    sym = rec['Symbol']
    desc = rec.get('Company Description','')
    # Try to extract company name as first token(s) before ' is ' or ' specializes '
    m = re.split(r'\s+(is|specializes|offers|provides|operates|specializing|offers|known)', desc, maxsplit=1)
    if m:
        name = m[0].strip()
    else:
        name = desc
    if not name:
        name = sym
    sym_to_name[sym] = name

# Prepare final list in order of up_days desc from rows
final = []
for r in rows:
    sym = r['Symbol']
    name = sym_to_name.get(sym, sym)
    final.append({'Symbol': sym, 'Name': name, 'up_days': float(r['up_days']), 'down_days': float(r['down_days'])})

# Output only the names of the top 5
names = [item['Name'] for item in final]
import json
print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_Zch6f3xWajnrHg8UxUqfGx5y': 'file_storage/call_Zch6f3xWajnrHg8UxUqfGx5y.json', 'var_call_YyTI2DqlV8KmfJTSLERIkxKH': 'file_storage/call_YyTI2DqlV8KmfJTSLERIkxKH.json', 'var_call_kMQAksDU5IEjDw6Pr6Bha4bg': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_dldzx7cRDx7lqdaUQyw4x7OK': [{'Symbol': 'HDB', 'up_days': '146.0', 'down_days': '102.0'}, {'Symbol': 'MTD', 'up_days': '143.0', 'down_days': '108.0'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'GTY', 'up_days': '143.0', 'down_days': '104.0'}, {'Symbol': 'PFE', 'up_days': '141.0', 'down_days': '105.0'}], 'var_call_rs6SNP8LOpkZMgnxYnjmnwpe': [{'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'GTY', 'Company Description': 'Getty Realty Corporation specializes in owning, leasing, and financing properties for the convenience store and gas station sectors across the United States.'}, {'Symbol': 'HDB', 'Company Description': 'HDFC Bank Limited is a leading financial institution in India, offering a wide range of banking services including personal and corporate banking, loans, and wealth management solutions.'}, {'Symbol': 'MTD', 'Company Description': 'Mettler-Toledo International, Inc. specializes in precision instruments and services for a wide range of laboratory, industrial, and food retailing applications, helping businesses ensure accuracy and efficiency in their operations.'}, {'Symbol': 'PFE', 'Company Description': 'Pfizer, Inc. is a leading pharmaceutical giant known for developing life-saving medications and vaccines, including the widely recognized COVID-19 vaccine.'}]}

exec(code, env_args)
