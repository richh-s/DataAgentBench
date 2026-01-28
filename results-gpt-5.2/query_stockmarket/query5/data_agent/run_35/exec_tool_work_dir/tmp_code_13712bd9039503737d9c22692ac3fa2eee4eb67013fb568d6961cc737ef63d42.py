code = """import json, pandas as pd

info_src = var_call_W5TuiiyrfPi6o1EtMXMSQu1H
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

trade_src = var_call_OYmEXJVMf4LWCZSkuzjovqPJ
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_src

info_df = pd.DataFrame(info)
trade_set = set(trade_tables)
symbols = [s for s in info_df['Symbol'].tolist() if s in trade_set]

parts = []
for sym in symbols:
    q = "SELECT '{}' AS Symbol, COUNT(*) AS days_cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2".format(sym, sym)
    parts.append(q)

union_query = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'symbols_n': len(symbols), 'union_query_len': len(union_query)}))"""

env_args = {'var_call_W5TuiiyrfPi6o1EtMXMSQu1H': 'file_storage/call_W5TuiiyrfPi6o1EtMXMSQu1H.json', 'var_call_OYmEXJVMf4LWCZSkuzjovqPJ': 'file_storage/call_OYmEXJVMf4LWCZSkuzjovqPJ.json'}

exec(code, env_args)
