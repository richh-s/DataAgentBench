code = """import json, pandas as pd
from pathlib import Path

stats_part = var_call_CawEzLqDTkYPm8FH4aTYiMEE

symbols_path = Path(var_call_ztbaJgeCz9oZX2eUsKrA5Vda)
with symbols_path.open() as f:
    symbols_data = json.load(f)

info_df = pd.DataFrame(symbols_data)

stats_df = pd.DataFrame(stats_part)

merged = stats_df.merge(info_df, on='Symbol', how='left')

filtered = merged[merged['more_up_than_down']]

result = filtered[['Symbol','Company Description','up_days','down_days']].to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_IAIAXD5wrlL3zcJ2yOOOF8NI': 'file_storage/call_IAIAXD5wrlL3zcJ2yOOOF8NI.json', 'var_call_ztbaJgeCz9oZX2eUsKrA5Vda': 'file_storage/call_ztbaJgeCz9oZX2eUsKrA5Vda.json', 'var_call_2ZSaEOLuLWHWk9atPkig6MiM': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT'], 'var_call_qbbPx9zZ6DBxVdZPuSsyCLQV': 'file_storage/call_qbbPx9zZ6DBxVdZPuSsyCLQV.json', 'var_call_CawEzLqDTkYPm8FH4aTYiMEE': [{'Symbol': 'AIN', 'up_days': 143, 'down_days': 101, 'more_up_than_down': True}, {'Symbol': 'AIV', 'up_days': 118, 'down_days': 128, 'more_up_than_down': False}, {'Symbol': 'AJRD', 'up_days': 123, 'down_days': 123, 'more_up_than_down': False}, {'Symbol': 'AL', 'up_days': 131, 'down_days': 117, 'more_up_than_down': True}, {'Symbol': 'AMN', 'up_days': 134, 'down_days': 111, 'more_up_than_down': True}, {'Symbol': 'AMP', 'up_days': 141, 'down_days': 110, 'more_up_than_down': True}, {'Symbol': 'AMT', 'up_days': 128, 'down_days': 123, 'more_up_than_down': True}, {'Symbol': 'ARD', 'up_days': 80, 'down_days': 119, 'more_up_than_down': False}]}

exec(code, env_args)
