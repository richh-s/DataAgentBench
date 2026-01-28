code = """import json, pandas as pd

# reload intersection with trade tables using actual list
# info
r = var_call_8SQH7HGO9zXTat5DBZ5KCOLp
if isinstance(r, str):
    with open(r,'r') as f:
        r = json.load(f)
info = pd.DataFrame(r)

# trade tables
t = var_call_KtI05COHj2GeVxPnUriejCD4
if isinstance(t, str):
    with open(t,'r') as f:
        t = json.load(f)
trade_tables = set(t)

symbols = sorted(set(info['Symbol']).intersection(trade_tables))

# sanity check for EIX
present = 'EIX' in symbols

# build query
selects=[]
for sym in symbols:
    tn='"'+sym.replace('"','""')+'"'
    selects.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM {tn} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")
query = ' UNION ALL '.join(selects)

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'EIX_included': present, 'query_len': len(query), 'first20': symbols[:20], 'contains_EIX_substring': '"EIX"' in query}))"""

env_args = {'var_call_6eMnvquPseEJWBPYIuXkBczW': ['stockinfo'], 'var_call_8SQH7HGO9zXTat5DBZ5KCOLp': 'file_storage/call_8SQH7HGO9zXTat5DBZ5KCOLp.json', 'var_call_KtI05COHj2GeVxPnUriejCD4': 'file_storage/call_KtI05COHj2GeVxPnUriejCD4.json', 'var_call_b4DWohrCNtLwUeeUmUgHamqx': 'file_storage/call_b4DWohrCNtLwUeeUmUgHamqx.json'}

exec(code, env_args)
