code = """import json
import pandas as pd

df = pd.DataFrame(var_call_1sif1avRPuvCIBK6wCyhmPpZ)
# numeric
df['avg_intraday_vol'] = pd.to_numeric(df['avg_intraday_vol'], errors='coerce')

asia = {
  'N225': 'Japan (Tokyo Stock Exchange)',
  'HSI': 'Hong Kong (Hong Kong Stock Exchange)',
  '000001.SS': 'China (Shanghai Stock Exchange)',
  '399001.SZ': 'China (Shenzhen Stock Exchange)',
  'TWII': 'Taiwan (Taiwan Stock Exchange)',
  'NSEI': 'India (NSE)'
}

df_asia = df[df['idx'].isin(asia.keys())].copy()
df_asia['market'] = df_asia['idx'].map(asia)

winner = df_asia.sort_values('avg_intraday_vol', ascending=False).head(1)
res = {
    'winner_index': winner.iloc[0]['idx'],
    'winner_market': winner.iloc[0]['market'],
    'avg_intraday_volatility': float(winner.iloc[0]['avg_intraday_vol']),
    'ranking_asia': df_asia.sort_values('avg_intraday_vol', ascending=False).assign(avg_intraday_vol=lambda x: x['avg_intraday_vol'].astype(float)).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_1sif1avRPuvCIBK6wCyhmPpZ': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'idx': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'idx': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'idx': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}]}

exec(code, env_args)
