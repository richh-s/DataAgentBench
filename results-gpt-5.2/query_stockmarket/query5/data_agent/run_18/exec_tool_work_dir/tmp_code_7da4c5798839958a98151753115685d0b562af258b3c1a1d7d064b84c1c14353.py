code = """import json, pandas as pd

# Load info
with open(var_call_COIkrGN9cWpnuc7Vnq57yeIM, 'r', encoding='utf-8') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)

# Load trade tables list
with open(var_call_I5zOU2gwHrCtH6ksASeIM4im, 'r', encoding='utf-8') as f:
    trade_tables = set(json.load(f))

# Filter symbols to those with price tables
symbols = [s for s in df_info['Symbol'].dropna().unique().tolist() if s in trade_tables]

# Build UNION ALL SQL to count qualifying days in 2019
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS days_cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2")

union_sql = "\nUNION ALL\n".join(parts)
full_sql = f"WITH counts AS (\n{union_sql}\n)\nSELECT Symbol, days_cnt FROM counts ORDER BY days_cnt DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'sql': full_sql, 'n_tables_used': len(symbols)}))"""

env_args = {'var_call_COIkrGN9cWpnuc7Vnq57yeIM': 'file_storage/call_COIkrGN9cWpnuc7Vnq57yeIM.json', 'var_call_CIdqd6spRth4VQvXVr16cRmW': {'n_symbols': 86}, 'var_call_I5zOU2gwHrCtH6ksASeIM4im': 'file_storage/call_I5zOU2gwHrCtH6ksASeIM4im.json'}

exec(code, env_args)
