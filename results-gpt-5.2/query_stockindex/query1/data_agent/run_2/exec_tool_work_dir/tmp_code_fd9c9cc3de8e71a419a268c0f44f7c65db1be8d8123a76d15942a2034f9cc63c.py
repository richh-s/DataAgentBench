code = """import json, pandas as pd

df = pd.DataFrame(var_call_Yeujv1hbCCpOzIc65hWKJ1OK)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Infer Asia-region indices from known symbols in dataset
asia = {'399001.SZ','000001.SS','N225','HSI','TWII','NSEI'}
df_asia = df[df['idx'].isin(asia)].copy().sort_values('avg_intraday_vol', ascending=False)

winner = df_asia.iloc[0].to_dict()
res = {
  'winner_index': winner['idx'],
  'avg_intraday_volatility': winner['avg_intraday_vol'],
  'asia_ranking': df_asia.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_gyWqSLUANzjxmsB24z5xNtKD': [{'idx': 'J203.JO'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'IXIC'}, {'idx': 'HSI'}, {'idx': 'NYA'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}, {'idx': 'N100'}, {'idx': '399001.SZ'}], 'var_call_gvGmJuxc1jFufQcKeoK4DqNS': ['index_info'], 'var_call_Yeujv1hbCCpOzIc65hWKJ1OK': [{'idx': '399001.SZ', 'avg_intraday_vol': '0.018293021165089372'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01826128391465914'}, {'idx': 'J203.JO', 'avg_intraday_vol': '0.0176915716830824'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.01653278149621257'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.016433893332157116'}, {'idx': 'NYA', 'avg_intraday_vol': '0.015450175155161689'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014566131296198794'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.01441505190039977'}, {'idx': 'N225', 'avg_intraday_vol': '0.014339806107587037'}, {'idx': 'N100', 'avg_intraday_vol': '0.014333060651167389'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013745402784616082'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.013654973139045913'}, {'idx': 'TWII', 'avg_intraday_vol': '0.012634393668700278'}]}

exec(code, env_args)
