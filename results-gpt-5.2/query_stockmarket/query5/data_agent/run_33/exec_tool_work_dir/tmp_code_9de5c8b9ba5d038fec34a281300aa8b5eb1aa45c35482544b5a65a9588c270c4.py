code = """import json, pandas as pd

# load stockinfo (Capital Market, non-ETF)
path = var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X
with open(path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
info_df['Symbol'] = info_df['Symbol'].astype(str)

# load available trade tables
path2 = var_call_rKHS1duJaB92sUCGFoGTg21g
with open(path2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

symbols = [s for s in info_df['Symbol'].tolist() if s in tables_set]

# limit to those with plausible daily data (skip warrants/units preferred etc. but keep as is)
# Build a DuckDB query that unions all symbols and counts days with (High-Low)/Low > 0.2 in 2019

def esc_ident(sym):
    return '"' + sym.replace('"','""') + '"'

parts = []
for sym in symbols:
    t = esc_ident(sym)
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_exceed FROM {t} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL AND ((High - Low)/Low) > 0.2"
    )

# If no symbols, return empty
union_query = " UNION ALL ".join(parts) if parts else "SELECT NULL AS Symbol, 0 AS days_exceed WHERE FALSE"

result = {
    'duckdb_query': union_query,
    'n_symbols': len(symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X': 'file_storage/call_KkYc3f4Uo7DPaLEWKgf8Qy8X.json', 'var_call_rKHS1duJaB92sUCGFoGTg21g': 'file_storage/call_rKHS1duJaB92sUCGFoGTg21g.json'}

exec(code, env_args)
