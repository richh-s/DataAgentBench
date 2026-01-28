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

# intersection should ensure existence, but DuckDB says some don't exist; filter by strict identifier match
# Remove any symbols that would require quoting with special chars - not needed here.
# Ensure case-sensitive match
symbols = sorted([s for s in syms_info if s in tables_set])

# As a safeguard, build query in smaller chunks and include only those in tables_set at time of building

def esc_ident(sym):
    return '"' + sym.replace('"','""') + '"'

# verify again
symbols = [s for s in symbols if s in tables_set]

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'first10': symbols[:10], 'has_MRKR': 'MRKR' in symbols}))"""

env_args = {'var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X': 'file_storage/call_KkYc3f4Uo7DPaLEWKgf8Qy8X.json', 'var_call_rKHS1duJaB92sUCGFoGTg21g': 'file_storage/call_rKHS1duJaB92sUCGFoGTg21g.json', 'var_call_hLBEBSNaiF65beO5tPUloU2C': 'file_storage/call_hLBEBSNaiF65beO5tPUloU2C.json', 'var_call_Mk49FmuluC2X5BxSQDwQxBCT': 'file_storage/call_Mk49FmuluC2X5BxSQDwQxBCT.json', 'var_call_vtSwwwvTau8MPXHdAfFGwNkD': 'file_storage/call_vtSwwwvTau8MPXHdAfFGwNkD.json', 'var_call_gt1wOIQ8kS4o9zuGcnst3gWY': 'file_storage/call_gt1wOIQ8kS4o9zuGcnst3gWY.json'}

exec(code, env_args)
