code = """import json, pandas as pd

# load info list
r = var_call_8SQH7HGO9zXTat5DBZ5KCOLp
if isinstance(r,str):
    with open(r,'r') as f:
        r=json.load(f)
info=pd.DataFrame(r)

# load trade tables
t = var_call_KtI05COHj2GeVxPnUriejCD4
if isinstance(t,str):
    with open(t,'r') as f:
        t=json.load(f)
trade=set(t)

# compute symbols in info but not in trade
missing = sorted(set(info['Symbol']) - trade)

print('__RESULT__:')
print(json.dumps({'n_info': len(info), 'n_trade': len(trade), 'n_missing': len(missing), 'missing_sample': missing[:30]}))"""

env_args = {'var_call_6eMnvquPseEJWBPYIuXkBczW': ['stockinfo'], 'var_call_8SQH7HGO9zXTat5DBZ5KCOLp': 'file_storage/call_8SQH7HGO9zXTat5DBZ5KCOLp.json', 'var_call_KtI05COHj2GeVxPnUriejCD4': 'file_storage/call_KtI05COHj2GeVxPnUriejCD4.json', 'var_call_b4DWohrCNtLwUeeUmUgHamqx': 'file_storage/call_b4DWohrCNtLwUeeUmUgHamqx.json', 'var_call_dHD5rxh9vR2TTbVC3xXFAsqa': {'n_symbols': 234, 'EIX_included': False, 'query_len': 49903, 'first20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'contains_EIX_substring': False}}

exec(code, env_args)
