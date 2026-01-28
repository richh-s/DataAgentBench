code = """import json, pandas as pd

with open(var_call_COIkrGN9cWpnuc7Vnq57yeIM, 'r', encoding='utf-8') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)

with open(var_call_I5zOU2gwHrCtH6ksASeIM4im, 'r', encoding='utf-8') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in df_info['Symbol'].dropna().unique().tolist() if s in trade_tables]

parts = []
for s in symbols:
    q = (
        "SELECT '{sym}' AS Symbol, COUNT(*) AS days_cnt "
        "FROM \"{sym}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low > 0 "
        "AND (High - Low) / Low > 0.2"
    ).format(sym=s)
    parts.append(q)

union_sql = " UNION ALL ".join(parts)
full_sql = ("WITH counts AS ({u}) "
            "SELECT Symbol, days_cnt FROM counts "
            "ORDER BY days_cnt DESC, Symbol ASC LIMIT 5;").format(u=union_sql)

print('__RESULT__:')
print(json.dumps({'sql': full_sql, 'n_tables_used': len(symbols)}))"""

env_args = {'var_call_COIkrGN9cWpnuc7Vnq57yeIM': 'file_storage/call_COIkrGN9cWpnuc7Vnq57yeIM.json', 'var_call_CIdqd6spRth4VQvXVr16cRmW': {'n_symbols': 86}, 'var_call_I5zOU2gwHrCtH6ksASeIM4im': 'file_storage/call_I5zOU2gwHrCtH6ksASeIM4im.json'}

exec(code, env_args)
