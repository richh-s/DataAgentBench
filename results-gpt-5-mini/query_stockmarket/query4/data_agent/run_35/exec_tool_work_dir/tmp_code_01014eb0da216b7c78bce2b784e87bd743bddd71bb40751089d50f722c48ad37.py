code = """import json
# Load variables from storage
with open(var_call_qYdfCqtOdxawG4fqVCTDZmg1, 'r') as f:
    stockinfo = json.load(f)
# var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6 is small (query result)
# It may be a Python list already or a filepath; check
import os
if isinstance(var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6, str) and os.path.exists(var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6):
    with open(var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6, 'r') as f:
        top5 = json.load(f)
else:
    top5 = var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6

symbols = [rec['symbol'] for rec in top5]

# Build mapping from symbol to Company Description
info_map = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}

separators = [' is an ', ' is a ', ' is the ', ' is ', ' specializes', ' offers', ' operates', ' provides', ' generates', ' focuses', ' produces', ' excels', ' offers', ' is headquartered', ' trades', ' manufactures']

names = []
for s in symbols:
    desc = info_map.get(s, '')
    if not desc:
        name = s
    else:
        low = desc.lower()
        idxs = [low.find(sep) for sep in separators if low.find(sep) != -1]
        if idxs:
            idx = min(idxs)
            name = desc[:idx].strip()
        else:
            # fallback: split by comma and take first part
            name = desc.split(',')[0].strip()
    # Remove trailing punctuation
    name = name.rstrip(' ,.')
    names.append(name)

print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_qYdfCqtOdxawG4fqVCTDZmg1': 'file_storage/call_qYdfCqtOdxawG4fqVCTDZmg1.json', 'var_call_UmK4HAX9PImijvhVJFGZOOKX': 'file_storage/call_UmK4HAX9PImijvhVJFGZOOKX.json', 'var_call_2Qbazqjt6QyQnkufaWtCTI7g': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_ZEQ1KxwtpXwxTS2F3N8dFGe6': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}]}

exec(code, env_args)
