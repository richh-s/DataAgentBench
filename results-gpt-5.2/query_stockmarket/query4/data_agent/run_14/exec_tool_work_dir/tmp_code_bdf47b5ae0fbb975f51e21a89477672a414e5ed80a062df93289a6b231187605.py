code = """import json, pandas as pd

# load info
src = var_call_9KkYakqJdaS1o0ssxYdG90nb
if isinstance(src, str):
    with open(src,'r') as f:
        recs = json.load(f)
else:
    recs = src
info = pd.DataFrame(recs)
info['Symbol'] = info['Symbol'].astype(str)

# load trade tables
src2 = var_call_R5Fm9qBHEnIjJw8IdgrwecTb
if isinstance(src2, str):
    with open(src2,'r') as f:
        tables = json.load(f)
else:
    tables = src2
trade_tables = set(tables)

symbols = sorted(set(info['Symbol']).intersection(trade_tables))

parts = []
for sym in symbols:
    t = '"' + sym.replace('"','""') + '"'
    q = "SELECT '{}' AS Symbol, ".format(sym) + \
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, " + \
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days " + \
        "FROM {} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(t)
    parts.append(q)

duck_query = " UNION ALL ".join(parts)
final_query = "SELECT Symbol FROM (" + duck_query + ") t WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC, Symbol ASC LIMIT 5"
name_map = dict(zip(info['Symbol'], info['company_name']))
print('__RESULT__:')
print(json.dumps({'final_query': final_query, 'name_map': name_map, 'symbol_count': len(symbols)}))"""

env_args = {'var_call_R5Fm9qBHEnIjJw8IdgrwecTb': 'file_storage/call_R5Fm9qBHEnIjJw8IdgrwecTb.json', 'var_call_9KkYakqJdaS1o0ssxYdG90nb': 'file_storage/call_9KkYakqJdaS1o0ssxYdG90nb.json', 'var_call_pSlDq3Iya59P4L94vtKPK8Li': 'file_storage/call_pSlDq3Iya59P4L94vtKPK8Li.json', 'var_call_33fgjpjrXsOxarmSqxpiXVXf': 'file_storage/call_33fgjpjrXsOxarmSqxpiXVXf.json'}

exec(code, env_args)
