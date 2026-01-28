code = """import json
path_stocktrade_tables = var_call_9EqcyJTTNqzbni5nT5m8eM89
path_stockinfo = var_call_w0BWMEldosjQXfLC7QjaVZWn

with open(path_stocktrade_tables, 'r') as f:
    tables = json.load(f)
with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)

symbols_info = [rec['Symbol'] for rec in stockinfo]
available_symbols = set(tables)
symbols = [s for s in symbols_info if s in available_symbols]

if not symbols:
    sql = ''
else:
    dq = '"'
    parts = []
    for s in symbols:
        q = f"SELECT {repr(s)} AS symbol, COALESCE(SUM(CASE WHEN {dq}Close{dq} > {dq}Open{dq} THEN 1 ELSE 0 END),0) AS up, COALESCE(SUM(CASE WHEN {dq}Close{dq} < {dq}Open{dq} THEN 1 ELSE 0 END),0) AS down FROM {dq}{s}{dq} WHERE {dq}Date{dq} >= '2017-01-01' AND {dq}Date{dq} <= '2017-12-31'"
        parts.append(q)
    union_sql = "\nUNION ALL\n".join(parts)
    sql = f"SELECT symbol, up, down FROM (\n{union_sql}\n) AS t ORDER BY up DESC;"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_ILvcekgasuDAplGbc9NsdFXR': ['stockinfo'], 'var_call_9EqcyJTTNqzbni5nT5m8eM89': 'file_storage/call_9EqcyJTTNqzbni5nT5m8eM89.json', 'var_call_w0BWMEldosjQXfLC7QjaVZWn': 'file_storage/call_w0BWMEldosjQXfLC7QjaVZWn.json'}

exec(code, env_args)
