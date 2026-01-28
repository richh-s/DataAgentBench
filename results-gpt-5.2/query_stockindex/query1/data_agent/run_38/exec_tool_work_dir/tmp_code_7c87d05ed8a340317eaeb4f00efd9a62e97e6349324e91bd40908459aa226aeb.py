code = """import json, pandas as pd

df = pd.DataFrame(var_call_5L77RaZgzrsHQA0M8eDZKzMG)
# cast numeric
for c in ['avg_intraday_vol','n_days']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

asia = {
    'N225':'Japan (Asia)',
    'HSI':'Hong Kong (Asia)',
    '000001.SS':'China (Asia)',
    '399001.SZ':'China (Asia)',
    'TWII':'Taiwan (Asia)',
    'NSEI':'India (Asia)'
}

asia_df = df[df['idx'].isin(asia.keys())].copy()
asia_df['market'] = asia_df['idx'].map(asia)

# pick highest average
best = asia_df.sort_values('avg_intraday_vol', ascending=False).head(1)
res = {
    'index': best.iloc[0]['idx'] if len(best) else None,
    'avg_intraday_volatility': float(best.iloc[0]['avg_intraday_vol']) if len(best) else None,
    'n_days': int(best.iloc[0]['n_days']) if len(best) else None,
    'note': '(High-Low)/Open averaged over trading days since 2020-01-01'
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_AYLsPtgsRmpMPFhzDmyq25TW': ['index_trade'], 'var_call_DmZxkzDw7Iv23uXW8ivIzJKC': ['index_info'], 'var_call_5L77RaZgzrsHQA0M8eDZKzMG': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.017949408823972023', 'n_days': '234'}, {'idx': 'N225', 'avg_intraday_vol': '0.013052566337351822', 'n_days': '244'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.011917473847069163', 'n_days': '229'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017339709656220562', 'n_days': '233'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.01670059829168851', 'n_days': '233'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018352634174080888', 'n_days': '229'}, {'idx': 'HSI', 'avg_intraday_vol': '0.015096167383143023', 'n_days': '240'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014235196916380324', 'n_days': '233'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013797724957835671', 'n_days': '232'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.013976293824740756', 'n_days': '228'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013549346375859089', 'n_days': '219'}, {'idx': 'N100', 'avg_intraday_vol': '0.01445236872292471', 'n_days': '227'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.018367121551882994', 'n_days': '220'}]}

exec(code, env_args)
