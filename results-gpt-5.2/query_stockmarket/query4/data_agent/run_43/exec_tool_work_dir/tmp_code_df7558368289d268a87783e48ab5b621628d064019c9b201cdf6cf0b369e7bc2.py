code = """import json, pandas as pd

# load symbols+names from sqlite query
r = var_call_8SQH7HGO9zXTat5DBZ5KCOLp
if isinstance(r, str):
    with open(r, 'r') as f:
        r = json.load(f)
info = pd.DataFrame(r)

# load available trade tables list
t = var_call_KtI05COHj2GeVxPnUriejCD4
if isinstance(t, str):
    with open(t, 'r') as f:
        t = json.load(f)
trade_tables = set(t)

# intersection: only tickers we can compute
symbols = sorted(set(info['Symbol']).intersection(trade_tables))

# build a single UNION ALL query for 2017 up/down counts
selects = []
for sym in symbols:
    # duckdb table names may need quoting if special chars; keep safe with double quotes
    tn = '"' + sym.replace('"','""') + '"'
    selects.append(
        f"SELECT '{sym}' AS Symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM {tn} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )

# chunk query to avoid overly long strings
chunks = []
chunk = []
max_len = 900000
cur_len = 0
for s in selects:
    if cur_len + len(s) + 12 > max_len and chunk:
        chunks.append(' UNION ALL '.join(chunk))
        chunk = [s]
        cur_len = len(s)
    else:
        chunk.append(s)
        cur_len += len(s)
if chunk:
    chunks.append(' UNION ALL '.join(chunk))

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'n_chunks': len(chunks), 'chunks': chunks[:3]}))"""

env_args = {'var_call_6eMnvquPseEJWBPYIuXkBczW': ['stockinfo'], 'var_call_8SQH7HGO9zXTat5DBZ5KCOLp': 'file_storage/call_8SQH7HGO9zXTat5DBZ5KCOLp.json', 'var_call_KtI05COHj2GeVxPnUriejCD4': 'file_storage/call_KtI05COHj2GeVxPnUriejCD4.json'}

exec(code, env_args)
