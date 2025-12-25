code = """import json, pandas as pd, os

batches = json.loads(var_call_3tquU8dAxELzZh965Urhornb)["batches"]

up_down_counts = []

for batch in batches:
    for sym in batch:
        q = f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31';"
        res = query_db(db_name='stocktrade_database', query=q)
        if isinstance(res, str):
            continue
        if not res:
            continue
        df = pd.DataFrame(res)
        df['Open'] = df['Open'].astype(float)
        df['Close'] = df['Close'].astype(float)
        up_days = (df['Close'] > df['Open']).sum()
        down_days = (df['Close'] < df['Open']).sum()
        if up_days > down_days:
            up_down_counts.append({'Symbol': sym, 'UpDays': int(up_days), 'DownDays': int(down_days)})

up_down_counts_sorted = sorted(up_down_counts, key=lambda x: x['UpDays']-x['DownDays'], reverse=True)[:5]

nyse_records_path = var_call_9qYsRCRBG6lqGuefPsqjksr5
with open(nyse_records_path, 'r') as f:
    nyse_records = json.load(f)
name_map = {r['Symbol']: r['CompanyDescription'] for r in nyse_records}

final = []
for rec in up_down_counts_sorted:
    sym = rec['Symbol']
    name = name_map.get(sym, '')
    final.append({'Symbol': sym, 'Name': name, 'UpDays': rec['UpDays'], 'DownDays': rec['DownDays']})

result = json.dumps(final)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_R5hudPl6aQNRDhoIcMWWjp6K': 'file_storage/call_R5hudPl6aQNRDhoIcMWWjp6K.json', 'var_call_9qYsRCRBG6lqGuefPsqjksr5': 'file_storage/call_9qYsRCRBG6lqGuefPsqjksr5.json', 'var_call_3tquU8dAxELzZh965Urhornb': {'batches': [['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT'], ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']]}, 'var_call_qdC9CwlzkJu1GoiaSRfAxzEf': 'file_storage/call_qdC9CwlzkJu1GoiaSRfAxzEf.json'}

exec(code, env_args)
