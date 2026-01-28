code = """import json, pandas as pd

with open(var_call_lsWEadc109kwWv5jdXkUgWbB, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_VDn7pDm6A1YBRdsQaIjs0gEy, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

info_df = info_df[info_df['Symbol'].isin(tbls_set)].copy()
syms = info_df['Symbol'].tolist()

batch_size=200
batch1=syms[:batch_size]
batch2=syms[batch_size:]

# generate queries for each batch

def make_union(symbols):
    parts=[]
    for s in symbols:
        parts.append("SELECT '"+s+"' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \""+s+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")
    return "\nUNION ALL\n".join(parts)

q1 = make_union(batch1)
q2 = make_union(batch2)

print('__RESULT__:')
print(json.dumps({'batch1_len': len(batch1), 'batch2_len': len(batch2), 'q2_preview': q2[:400]}))"""

env_args = {'var_call_lsWEadc109kwWv5jdXkUgWbB': 'file_storage/call_lsWEadc109kwWv5jdXkUgWbB.json', 'var_call_VDn7pDm6A1YBRdsQaIjs0gEy': 'file_storage/call_VDn7pDm6A1YBRdsQaIjs0gEy.json', 'var_call_xSqbgAv8TtV5xeodQAmRI5Vl': {'n_symbols': 234, 'n_batches': 2}, 'var_call_se7wRvt0IxMH6ofL49wfG1Fd': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_NlakGaS25EgBGQvvIq3gMOH4': {'batch1_first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'batch2_first10': ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS']}}

exec(code, env_args)
