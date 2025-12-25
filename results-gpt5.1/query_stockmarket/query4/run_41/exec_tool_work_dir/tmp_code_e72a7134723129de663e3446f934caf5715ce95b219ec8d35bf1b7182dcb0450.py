code = """import json, pandas as pd
# collect stats from stored vars manually
rows = [
 var_call_lQk4615aPdX4CndFf4dUo8Dx[0],
 var_call_JVbRUNSRSqXjztfML43guyC4[0],
 var_call_Pd5wM2qxZyEVK8wUNukFAA0A[0],
 var_call_KuCUfcOOiM6SzcQUDdy9Df3w[0],
 var_call_2C0jee4eYxqtPzT3GSjUsxP0[0],
 var_call_p2yqLF3gjCAnFYcYRLNomEZH[0]
]
for r in rows:
 r['up_days'] = float(r['up_days'])
 r['down_days'] = float(r['down_days'])
df = pd.DataFrame(rows)
# filter up>down
fdf = df[df['up_days']>df['down_days']].copy()
fdf['diff'] = fdf['up_days']-fdf['down_days']
res = fdf.sort_values('diff', ascending=False)
result = res.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_afVObeOWlcs3f36o03J000HK': 'file_storage/call_afVObeOWlcs3f36o03J000HK.json', 'var_call_Iy21V2aMsG5xHrmDbqxcaKeg': 'file_storage/call_Iy21V2aMsG5xHrmDbqxcaKeg.json', 'var_call_LDDcDJxEYDt8tbl7TnxZWsp0': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_Wh2BLrffuBEMoOwkqok1xuxp': [{'up_days': '0'}], 'var_call_A9UcVdNoTFAGYGI8fC4XMcvH': [{'down_days': '0'}], 'var_call_NXwbMOnJTZCtyu0vEjotoAEB': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'var_call_Ctf7R34iLcWUGBVC1lOUoOEy': 'file_storage/call_Ctf7R34iLcWUGBVC1lOUoOEy.json', 'var_call_TGVSJ52jMElTbphA2OAuwQWM': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_lQk4615aPdX4CndFf4dUo8Dx': [{'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_JVbRUNSRSqXjztfML43guyC4': [{'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_fqugEv8mA7X4S2cx3qryhcDD': [{'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_JAVKJ9MhaQGRMdTsTugn7JJq': [{'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_Pd5wM2qxZyEVK8wUNukFAA0A': [{'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_KuCUfcOOiM6SzcQUDdy9Df3w': [{'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_2C0jee4eYxqtPzT3GSjUsxP0': [{'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_p2yqLF3gjCAnFYcYRLNomEZH': [{'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_0HDy95y94xYdJHb64JFM7qNG': [{'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}]}

exec(code, env_args)
