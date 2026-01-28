code = """import json
p = var_call_iOvFCGkDaV3qO2tUthxmFcC2
if isinstance(p, str):
    with open(p, 'r') as f:
        etfs = json.load(f)
else:
    etfs = p
p2 = var_call_PJXWtX99zzhlp0cs6kTsGt48
if isinstance(p2, str):
    with open(p2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = p2
trade_set = set(trade_tables)
syms = sorted([r['Symbol'] for r in etfs if r['Symbol'] in trade_set])

parts = []
for s in syms:
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

max_len = 200000
chunks = []
cur = []
cur_len = 0
sep_len = len(' UNION ALL ')
for q in parts:
    add = len(q) + (sep_len if cur else 0)
    if cur and cur_len + add > max_len:
        chunks.append(' UNION ALL '.join(cur))
        cur = [q]
        cur_len = len(q)
    else:
        if cur:
            cur_len += sep_len + len(q)
        else:
            cur_len = len(q)
        cur.append(q)
if cur:
    chunks.append(' UNION ALL '.join(cur))

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'union_chunks': chunks}))"""

env_args = {'var_call_iOvFCGkDaV3qO2tUthxmFcC2': 'file_storage/call_iOvFCGkDaV3qO2tUthxmFcC2.json', 'var_call_PJXWtX99zzhlp0cs6kTsGt48': 'file_storage/call_PJXWtX99zzhlp0cs6kTsGt48.json'}

exec(code, env_args)
