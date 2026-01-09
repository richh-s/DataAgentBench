code = """import json
import pandas as pd

df = pd.DataFrame(var_call_NTTjQOgXwBZdeiwJLKh6DlsZ)
# cast numeric fields
for c in ['total_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices in this dataset: IXIC (NASDAQ Composite), NYA (NYSE Composite), GSPTSE (S&P/TSX Composite)
na = df[df['index_symbol'].isin(['IXIC','NYA','GSPTSE'])].copy()
res = na[na['up_days'] > na['down_days']].sort_values('index_symbol')[['index_symbol','up_days','down_days','total_days']]
out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NTTjQOgXwBZdeiwJLKh6DlsZ': [{'index_symbol': 'J203.JO', 'total_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'index_symbol': 'N225', 'total_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'index_symbol': 'GSPTSE', 'total_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'index_symbol': 'NSEI', 'total_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'index_symbol': 'GDAXI', 'total_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'index_symbol': 'IXIC', 'total_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'index_symbol': 'HSI', 'total_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'index_symbol': '000001.SS', 'total_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'index_symbol': 'SSMI', 'total_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'index_symbol': 'TWII', 'total_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'index_symbol': 'N100', 'total_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'index_symbol': '399001.SZ', 'total_days': '76', 'up_days': '33.0', 'down_days': '43.0'}, {'index_symbol': 'NYA', 'total_days': '79', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
