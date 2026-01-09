code = """import json, pandas as pd

# Load first chunk results
r1 = pd.DataFrame(var_call_Y6a0MKx5RXrQmRRpZCasNMCn)
# Convert nan strings to NaN and numeric
for c in ['up_days','down_days']:
    r1[c] = pd.to_numeric(r1[c], errors='coerce')

# Rebuild second chunk query excluding missing table FLGT that caused failure
path_info = var_call_xuUBpv3sy51zl3phgaF7zb0y
with open(path_info,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

path_tables = var_call_XVn8eaOQR3oF28TjAK0kSeBn
with open(path_tables,'r') as f:
    tables = json.load(f)
tables_set = set(tables)

candidates = info_df[info_df['symbol'].isin(tables_set)].copy()

# Determine the symbols included in chunk2 from earlier plan: it started at CVY ... XOM as seen in error message
# We'll reconstruct all candidate symbols and chunking with same size and then take chunk2 list.
symbols = candidates['symbol'].tolist()
chunk_size = 120
chunk2_syms = symbols[120:240]

# remove FLGT if present
chunk2_syms = [s for s in chunk2_syms if s != 'FLGT']

def dq_ident(s: str) -> str:
    return '"' + s.replace('"','""') + '"'

selects=[]
for sym in chunk2_syms:
    selects.append(
        f"SELECT '{sym}' AS symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM {dq_ident(sym)} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    )
q2 = ' UNION ALL '.join(selects)

print('__RESULT__:')
print(json.dumps({'chunk2_query': q2, 'chunk2_count': len(chunk2_syms)}))"""

env_args = {'var_call_xuUBpv3sy51zl3phgaF7zb0y': 'file_storage/call_xuUBpv3sy51zl3phgaF7zb0y.json', 'var_call_XVn8eaOQR3oF28TjAK0kSeBn': 'file_storage/call_XVn8eaOQR3oF28TjAK0kSeBn.json', 'var_call_dMw99Vz3STfDqoQKskcapZd3': 'file_storage/call_dMw99Vz3STfDqoQKskcapZd3.json', 'var_call_Y6a0MKx5RXrQmRRpZCasNMCn': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}]}

exec(code, env_args)
