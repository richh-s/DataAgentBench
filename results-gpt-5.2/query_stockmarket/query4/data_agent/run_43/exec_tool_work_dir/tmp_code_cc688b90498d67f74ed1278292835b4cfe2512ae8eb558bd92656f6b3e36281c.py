code = """import json, pandas as pd

a = var_call_8SQH7HGO9zXTat5DBZ5KCOLp
if isinstance(a,str):
    with open(a,'r') as f:
        a=json.load(f)
info=pd.DataFrame(a)

t = var_call_KtI05COHj2GeVxPnUriejCD4
if isinstance(t,str):
    with open(t,'r') as f:
        t=json.load(f)
trade=set(t)

symbols = sorted(set(info['Symbol']).intersection(trade))

# build full union query
parts=[]
for s in symbols:
    part = "SELECT '" + s + "' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"" + s + "\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    parts.append(part)
query = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'query_len': len(query), 'query_preview': query[:500]}))"""

env_args = {'var_call_6eMnvquPseEJWBPYIuXkBczW': ['stockinfo'], 'var_call_8SQH7HGO9zXTat5DBZ5KCOLp': 'file_storage/call_8SQH7HGO9zXTat5DBZ5KCOLp.json', 'var_call_KtI05COHj2GeVxPnUriejCD4': 'file_storage/call_KtI05COHj2GeVxPnUriejCD4.json', 'var_call_b4DWohrCNtLwUeeUmUgHamqx': 'file_storage/call_b4DWohrCNtLwUeeUmUgHamqx.json', 'var_call_dHD5rxh9vR2TTbVC3xXFAsqa': {'n_symbols': 234, 'EIX_included': False, 'query_len': 49903, 'first20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'contains_EIX_substring': False}, 'var_call_L4q9xkZVw50qF6avt7Tk89YC': {'n_info': 234, 'n_trade': 2753, 'n_missing': 0, 'missing_sample': []}, 'var_call_z8xed14PSfHWo0Q111DUdc7e': {'IVZ_in_info': False, 'IVZ_in_trade': False}, 'var_call_LOkh8YoVXUx7oprA4QWHAw9H': {'n_symbols': 234, 'EIX_included': False, 'query_len': 49903, 'first20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'contains_EIX_substring': False}, 'var_call_4PWuSxTt3Y1Z5z0y9eua27eD': {'I_symbols_sample': ['IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT'], 'count_I_symbols': 6}, 'var_call_e9XiVEOQZcvsYWJLPT1cztbj': [{'Symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}, {'Symbol': 'IGR', 'up_days': '126.0', 'down_days': '101.0'}, {'Symbol': 'IHC', 'up_days': '98.0', 'down_days': '134.0'}, {'Symbol': 'IPG', 'up_days': '129.0', 'down_days': '116.0'}, {'Symbol': 'IRM', 'up_days': '131.0', 'down_days': '116.0'}, {'Symbol': 'IT', 'up_days': '125.0', 'down_days': '125.0'}], 'var_call_9VdpkkKq3LFRBX2FJIioI1CZ': {'ok': True}, 'var_call_BVv7Uy9ukpo0EKeJW1GX6jTm': {'sym': 'AEFC', 'q': 'SELECT \'{}\' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM "AEFC" WHERE Date >= \'2017-01-01\' AND Date < \'2018-01-01\''}}

exec(code, env_args)
