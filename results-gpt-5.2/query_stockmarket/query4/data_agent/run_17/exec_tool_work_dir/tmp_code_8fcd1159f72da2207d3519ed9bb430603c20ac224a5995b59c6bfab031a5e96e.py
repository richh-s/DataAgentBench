code = """import json, pandas as pd

src = var_call_gYJbskZiMLDqMqhJmUIqMw5P
if isinstance(src, str):
    with open(src, 'r') as f:
        nyse_rows = json.load(f)
else:
    nyse_rows = src
nyse_df = pd.DataFrame(nyse_rows)
nyse_syms = set(nyse_df['Symbol'].dropna().astype(str))

src2 = var_call_yC5xzU04KLrHiVtr69INvnjw
if isinstance(src2, str):
    with open(src2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = src2
trade_syms = set(trade_tables)

cands = sorted(nyse_syms.intersection(trade_syms))

# Build a few sample parts to validate string construction
parts = []
for s in cands[:3]:
    tbl = '"' + s.replace('"','""') + '"'
    q = (
        "SELECT '{sym}' AS Symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM {tbl} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    ).format(sym=s, tbl=tbl)
    parts.append(q)

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'sample_query': query}))"""

env_args = {'var_call_gYJbskZiMLDqMqhJmUIqMw5P': 'file_storage/call_gYJbskZiMLDqMqhJmUIqMw5P.json', 'var_call_yC5xzU04KLrHiVtr69INvnjw': 'file_storage/call_yC5xzU04KLrHiVtr69INvnjw.json'}

exec(code, env_args)
