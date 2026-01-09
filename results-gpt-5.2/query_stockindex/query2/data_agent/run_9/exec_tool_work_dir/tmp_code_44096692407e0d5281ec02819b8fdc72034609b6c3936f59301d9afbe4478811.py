code = """import json
import pandas as pd

df = pd.DataFrame(var_call_em79jlLnj04BbYzyOucarECn)
# cast
for c in ['total_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices in dataset: IXIC (NASDAQ Composite), NYA (NYSE Composite), GSPTSE (S&P/TSX Composite)
na = df[df['Index'].isin(['IXIC','NYA','GSPTSE'])].copy()
na['more_up_than_down'] = na['up_days'] > na['down_days']
res = na[na['more_up_than_down']].sort_values('Index')[['Index','up_days','down_days','total_days']]
result = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MdFoow4EAELcpCdo1gpE40DW': ['index_info'], 'var_call_em79jlLnj04BbYzyOucarECn': [{'Index': 'J203.JO', 'total_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'total_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'total_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'total_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'total_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'total_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'total_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'NYA', 'total_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'total_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'total_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'total_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'total_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'total_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
