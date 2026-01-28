code = """import json, pandas as pd

# load stockinfo symbols
with open(var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
syms_info = set(info_df['Symbol'].astype(str))

# load trade tables
with open(var_call_rKHS1duJaB92sUCGFoGTg21g,'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# intersection
symbols = sorted(syms_info.intersection(tables_set))

# Build query

def esc_ident(sym):
    return '"' + sym.replace('"','""') + '"'

parts = []
for sym in symbols:
    t = esc_ident(sym)
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_exceed FROM {t} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL AND ((High - Low)/Low) > 0.2"
    )

union_query = " UNION ALL ".join(parts)
final_query = f"WITH counts AS ({union_query}) SELECT Symbol, days_exceed FROM counts ORDER BY days_exceed DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'query': final_query}))"""

env_args = {'var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X': 'file_storage/call_KkYc3f4Uo7DPaLEWKgf8Qy8X.json', 'var_call_rKHS1duJaB92sUCGFoGTg21g': 'file_storage/call_rKHS1duJaB92sUCGFoGTg21g.json', 'var_call_hLBEBSNaiF65beO5tPUloU2C': 'file_storage/call_hLBEBSNaiF65beO5tPUloU2C.json', 'var_call_Mk49FmuluC2X5BxSQDwQxBCT': 'file_storage/call_Mk49FmuluC2X5BxSQDwQxBCT.json'}

exec(code, env_args)
