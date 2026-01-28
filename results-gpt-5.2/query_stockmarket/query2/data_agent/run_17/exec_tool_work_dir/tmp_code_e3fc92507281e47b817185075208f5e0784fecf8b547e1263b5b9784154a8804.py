code = """import json, pandas as pd

# Load NYSE Arca ETFs list
p = var_call_iOvFCGkDaV3qO2tUthxmFcC2
if isinstance(p, str):
    with open(p, 'r') as f:
        etfs = json.load(f)
else:
    etfs = p

etf_syms = [r['Symbol'] for r in etfs]

# Load available trade tables
p2 = var_call_PJXWtX99zzhlp0cs6kTsGt48
if isinstance(p2, str):
    with open(p2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = p2

trade_set = set(trade_tables)
syms = sorted([s for s in etf_syms if s in trade_set])

# build a union query to find max adj close in 2015 per symbol > 200
parts = []
for s in syms:
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

# chunk to avoid overly long query
chunks = []
chunk = []
max_len = 200000
cur = 0
for q in parts:
    if cur + len(q) + 11 > max_len and chunk:
        chunks.append(chunk)
        chunk = [q]
        cur = len(q)
    else:
        chunk.append(q)
        cur += len(q) + 11
if chunk:
    chunks.append(chunk)

out = {
    'symbols': syms,
    'union_chunks': [" UNION ALL ".join(c) for c in chunks]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iOvFCGkDaV3qO2tUthxmFcC2': 'file_storage/call_iOvFCGkDaV3qO2tUthxmFcC2.json', 'var_call_PJXWtX99zzhlp0cs6kTsGt48': 'file_storage/call_PJXWtX99zzhlp0cs6kTsGt48.json'}

exec(code, env_args)
