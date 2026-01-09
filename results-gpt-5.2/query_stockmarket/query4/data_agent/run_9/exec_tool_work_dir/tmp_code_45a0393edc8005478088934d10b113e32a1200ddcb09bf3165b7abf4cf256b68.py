code = """import json, pandas as pd

# load tables
with open(var_call_XVn8eaOQR3oF28TjAK0kSeBn,'r') as f:
    tables = json.load(f)
tables_set=set(tables)

# load info
with open(var_call_xuUBpv3sy51zl3phgaF7zb0y,'r') as f:
    info=json.load(f)
info_df=pd.DataFrame(info)

candidates=info_df[info_df['symbol'].isin(tables_set)].copy()

symbols=candidates['symbol'].tolist()
chunk_size=120
chunk2_syms=symbols[120:240]

# double-check membership (should all be in tables_set) and then remove known-missing encountered
missing=['FLGT','RACE','RDN']
chunk2_syms=[s for s in chunk2_syms if s in tables_set and s not in missing]

def dq_ident(s):
    return '"'+s.replace('"','""')+'"'

selects=[]
for sym in chunk2_syms:
    selects.append(
        f"SELECT '{sym}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM {dq_ident(sym)} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    )
q2=' UNION ALL '.join(selects)

print('__RESULT__:')
print(json.dumps({'chunk2_query': q2, 'chunk2_count': len(chunk2_syms), 'dropped': missing}))"""

env_args = {'var_call_xuUBpv3sy51zl3phgaF7zb0y': 'file_storage/call_xuUBpv3sy51zl3phgaF7zb0y.json', 'var_call_XVn8eaOQR3oF28TjAK0kSeBn': 'file_storage/call_XVn8eaOQR3oF28TjAK0kSeBn.json', 'var_call_dMw99Vz3STfDqoQKskcapZd3': 'file_storage/call_dMw99Vz3STfDqoQKskcapZd3.json', 'var_call_Y6a0MKx5RXrQmRRpZCasNMCn': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}], 'var_call_hq0IzLpe1RKlwNBtxFUHYy8B': 'file_storage/call_hq0IzLpe1RKlwNBtxFUHYy8B.json', 'var_call_umk7cB8JmqJTRNboAlpsyQpk': 'file_storage/call_umk7cB8JmqJTRNboAlpsyQpk.json'}

exec(code, env_args)
