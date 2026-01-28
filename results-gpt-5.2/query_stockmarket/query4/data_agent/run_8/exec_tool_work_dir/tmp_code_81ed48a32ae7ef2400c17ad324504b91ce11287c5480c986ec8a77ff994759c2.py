code = """import json
import pandas as pd
import re

syms = var_call_ApHCkFqXdwxXgKxo8v7lKnd3['symbols_alpha']

# build multi-statement SQL: create temp table of counts for each symbol with data in 2017
stmts = ["CREATE OR REPLACE TEMP TABLE updown(symbol VARCHAR, up_days BIGINT, down_days BIGINT);", "DELETE FROM updown;"]
for s in syms:
    stmts.append(
        "INSERT INTO updown "
        "SELECT '{sym}' AS symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM \"{sym}\" "
        "WHERE Date >= '2017-01-01' AND Date < '2018-01-01' "
        "HAVING COUNT(*) > 0;".format(sym=s)
    )
stmts.append("SELECT * FROM updown WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC LIMIT 5;")

sql = "\n".join(stmts)
print('__RESULT__:')
print(json.dumps({'sql': sql, 'n_syms': len(syms)}))"""

env_args = {'var_call_ShAWqPqxsj4pHI1S9zIIoOt3': 'file_storage/call_ShAWqPqxsj4pHI1S9zIIoOt3.json', 'var_call_vI8ekiN5VeJk6XqELl5IDD41': 'file_storage/call_vI8ekiN5VeJk6XqELl5IDD41.json', 'var_call_ApHCkFqXdwxXgKxo8v7lKnd3': {'n_nyse_nonetf': 234, 'n_alpha': 234, 'symbols_alpha': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_ZL5UbN2jhcD93INGkBf5lGqs': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_haHZkTg3x32NtWDVUOM5q2Km': [{'n': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_nu7Hj8ejF6AqTDuIdyVIFxzo': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}]}

exec(code, env_args)
