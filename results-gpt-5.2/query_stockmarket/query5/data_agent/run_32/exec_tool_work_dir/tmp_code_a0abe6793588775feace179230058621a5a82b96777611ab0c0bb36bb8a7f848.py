code = """import json, pandas as pd

# load stockinfo result (may be file path)
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
# only tickers that exist as price tables
symbols = sorted(set(info_df['Symbol']).intersection(set(tables)))

# build a single UNION ALL query across all relevant tickers for 2019
parts = []
for sym in symbols:
    # table names are tickers; quote with double quotes for DuckDB if needed
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_over_20pct "
        f"FROM \"{sym}\" "
        f"WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        f"  AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        f"  AND (High - Low) / Low > 0.2"
    )

query = "\nUNION ALL\n".join(parts)
print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'union_query': query}))"""

env_args = {'var_call_Km4pD3Vt20x9IJsbZQuKm7E6': 'file_storage/call_Km4pD3Vt20x9IJsbZQuKm7E6.json', 'var_call_e3WXalL5luM4t2iSV4nYQGQX': 'file_storage/call_e3WXalL5luM4t2iSV4nYQGQX.json'}

exec(code, env_args)
