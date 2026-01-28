code = """import json
import pandas as pd

df = pd.DataFrame(var_call_ZWq5ReTlHtbADjX3TD2XwBIa)
# cast numeric cols
for c in ['n_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# infer North American indices among available tickers
north_america = {'IXIC', 'NYA', 'GSPTSE'}  # Nasdaq Composite, NYSE Composite, S&P/TSX Composite
na = df[df['idx'].isin(north_america)].copy()
na['more_up_than_down'] = na['up_days'] > na['down_days']
res = na[na['more_up_than_down']].sort_values('idx')[['idx','up_days','down_days','n_days']]

# map to names
name_map = {
    'IXIC': 'NASDAQ Composite (IXIC)',
    'NYA': 'NYSE Composite (NYA)',
    'GSPTSE': 'S&P/TSX Composite (GSPTSE)'
}
res['index_name'] = res['idx'].map(name_map).fillna(res['idx'])

out = res[['index_name','up_days','down_days','n_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iRvW81qLulPf8p6FEdpxHo3f': ['index_info'], 'var_call_uE1HqqN9XCu3wR3ftJlKVdQK': ['index_trade'], 'var_call_ZWq5ReTlHtbADjX3TD2XwBIa': [{'idx': 'J203.JO', 'n_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'idx': 'N225', 'n_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'idx': 'GSPTSE', 'n_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'idx': 'NSEI', 'n_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'idx': 'GDAXI', 'n_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'idx': 'HSI', 'n_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'idx': 'IXIC', 'n_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'idx': 'NYA', 'n_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'idx': '000001.SS', 'n_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'idx': 'SSMI', 'n_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'idx': 'TWII', 'n_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'idx': 'N100', 'n_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'idx': '399001.SZ', 'n_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
