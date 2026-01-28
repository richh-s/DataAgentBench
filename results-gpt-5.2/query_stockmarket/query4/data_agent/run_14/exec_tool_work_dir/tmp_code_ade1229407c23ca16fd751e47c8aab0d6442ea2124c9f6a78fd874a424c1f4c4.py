code = """import json, pandas as pd

src = var_call_9KkYakqJdaS1o0ssxYdG90nb
if isinstance(src, str):
    with open(src, 'r') as f:
        recs = json.load(f)
else:
    recs = src
info = pd.DataFrame(recs)
info['Symbol'] = info['Symbol'].astype(str)

# trade tables
tbl_src = var_call_R5Fm9qBHEnIjJw8IdgrwecTb
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tbl_src
trade_tables = set(tables)

symbols = sorted(set(info['Symbol']).intersection(trade_tables))

parts = []
for sym in symbols:
    t = '"' + sym.replace('"','""') + '"'
    parts.append(
        "SELECT '" + sym + "' AS Symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM " + t + " WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    )

duck_query = "\nUNION ALL\n".join(parts)
name_map = dict(zip(info['Symbol'], info['company_name']))

out = {'duck_query': duck_query, 'name_map': name_map, 'symbol_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_R5Fm9qBHEnIjJw8IdgrwecTb': 'file_storage/call_R5Fm9qBHEnIjJw8IdgrwecTb.json', 'var_call_9KkYakqJdaS1o0ssxYdG90nb': 'file_storage/call_9KkYakqJdaS1o0ssxYdG90nb.json'}

exec(code, env_args)
