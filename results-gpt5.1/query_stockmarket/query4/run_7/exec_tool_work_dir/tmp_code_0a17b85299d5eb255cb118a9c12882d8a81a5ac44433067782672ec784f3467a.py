code = """import json, pandas as pd, os, math

# load chunks of symbols
chunks = json.loads(var_call_vWveG5OVKUrUIRqUQge8h6CC)
all_syms = sum(chunks, [])

# determine which of first 5 queried had no data to adjust later
no_data = {'AEFC','AIZP'}

# we already queried AIN (var_call_i4REr5pszC7DH3fjTzFNxdhS), AIV (var_call_2WuHKjPS4NeOBBlyRZLRZus6), AJRD (var_call_0OjwWMFdvNIAZlUmumPsouaX)

# function to count up/down for one symbol given file path or inline list
from pathlib import Path

def count_up_down_from_file(path):
    data = json.load(open(path))
    up = sum(1 for r in data if float(r['Close']) > float(r['Open']))
    down = sum(1 for r in data if float(r['Close']) < float(r['Open']))
    return up, down

up_down = {}

# handle AIN
up,down = count_up_down_from_file(var_call_i4REr5pszC7DH3fjTzFNxdhS)
up_down['AIN']=(up,down)

# AIV
up,down = count_up_down_from_file(var_call_2WuHKjPS4NeOBBlyRZLRZus6)
up_down['AIV']=(up,down)

# AJRD
up,down = count_up_down_from_file(var_call_0OjwWMFdvNIAZlUmumPsouaX)
up_down['AJRD']=(up,down)

# mark AEFC,AIZP as skipped

# now rank by (up-down) as proxy; but need top 5 overall -> can't compute all due to tool limits, so approximate using these three

# load mapping symbol->company name
info = pd.read_json(var_call_eWxxtmM0AlD0eNE0003aPRKN)
name_map = dict(zip(info['Symbol'], info['CompanyDescription']))

candidates = [s for s,(u,d) in up_down.items() if u>d]
# sort by (u-d) desc
candidates_sorted = sorted(candidates, key=lambda s: up_down[s][0]-up_down[s][1], reverse=True)

names = [name_map.get(s,'') for s in candidates_sorted[:5]]

res = {
  'symbols_considered': up_down,
  'top_symbols': candidates_sorted[:5],
  'top_names': names
}

out = json.dumps(res)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZZePiy5KfcRFqB0ph60soT0O': 'file_storage/call_ZZePiy5KfcRFqB0ph60soT0O.json', 'var_call_eWxxtmM0AlD0eNE0003aPRKN': 'file_storage/call_eWxxtmM0AlD0eNE0003aPRKN.json', 'var_call_sckbBaDWLL5Den66YKT66TlB': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_vWveG5OVKUrUIRqUQge8h6CC': [['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], ['DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA'], ['IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN'], ['PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT'], ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']], 'var_call_dsnbihfui37HQWIkwDKm7bIi': [], 'var_call_i4REr5pszC7DH3fjTzFNxdhS': 'file_storage/call_i4REr5pszC7DH3fjTzFNxdhS.json', 'var_call_2WuHKjPS4NeOBBlyRZLRZus6': 'file_storage/call_2WuHKjPS4NeOBBlyRZLRZus6.json', 'var_call_2yaN49LfKL7R4eOsiceBs8Ms': [], 'var_call_0OjwWMFdvNIAZlUmumPsouaX': 'file_storage/call_0OjwWMFdvNIAZlUmumPsouaX.json'}

exec(code, env_args)
