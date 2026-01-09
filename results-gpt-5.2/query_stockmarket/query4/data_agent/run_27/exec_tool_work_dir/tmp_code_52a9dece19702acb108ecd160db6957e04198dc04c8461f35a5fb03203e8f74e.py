code = """import json, pandas as pd

syms_path = var_call_WVoSx04qn4Zmhus3YGKtwMJW
with open(syms_path,'r') as f:
    syms = pd.DataFrame(json.load(f))

tables_path = var_call_SXxuCg2PazNuuuXO4t5ddkAl
with open(tables_path,'r') as f:
    tables = set(json.load(f))

candidates = syms[syms['Symbol'].isin(tables)].copy()
all_symbols = candidates['Symbol'].tolist()

union_parts = []
for sym in all_symbols:
    qsym = '"' + sym.replace('"','""') + '"'
    part = (
        "SELECT '" + sym + "' AS Symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM " + qsym + " WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )
    union_parts.append(part)

query = "\nUNION ALL\n".join(union_parts)
print('__RESULT__:')
print(json.dumps({'n_symbols': len(all_symbols), 'query': query}))"""

env_args = {'var_call_WVoSx04qn4Zmhus3YGKtwMJW': 'file_storage/call_WVoSx04qn4Zmhus3YGKtwMJW.json', 'var_call_SXxuCg2PazNuuuXO4t5ddkAl': 'file_storage/call_SXxuCg2PazNuuuXO4t5ddkAl.json', 'var_call_70IfAWIkFH4YbUlx1VeBihF4': {'n_candidates': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT']}}

exec(code, env_args)
