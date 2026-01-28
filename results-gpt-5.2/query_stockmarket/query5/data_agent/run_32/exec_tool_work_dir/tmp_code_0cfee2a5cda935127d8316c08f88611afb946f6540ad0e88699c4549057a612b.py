code = """import json, pandas as pd

info_src = var_call_Km4pD3Vt20x9IJsbZQuKm7E6
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

tables_src = var_call_e3WXalL5luM4t2iSV4nYQGQX
if isinstance(tables_src, str):
    with open(tables_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tables_src

info_df = pd.DataFrame(info)
symbols = sorted(set(info_df['Symbol']).intersection(set(tables)))

parts = []
for sym in symbols:
    part = (
        "SELECT '{sym}' AS Symbol, COUNT(*) AS days_over_20pct "
        "FROM \"{sym}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "  AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        "  AND (High - Low) / Low > 0.2"
    ).format(sym=sym)
    parts.append(part)

query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps({'symbols_count': len(symbols), 'union_query': query[:5000]}))"""

env_args = {'var_call_Km4pD3Vt20x9IJsbZQuKm7E6': 'file_storage/call_Km4pD3Vt20x9IJsbZQuKm7E6.json', 'var_call_e3WXalL5luM4t2iSV4nYQGQX': 'file_storage/call_e3WXalL5luM4t2iSV4nYQGQX.json'}

exec(code, env_args)
