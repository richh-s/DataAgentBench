code = """import json
import pandas as pd

df = pd.DataFrame(var_call_ZpOnHwZLT6FCFeDNOZ3cjGHN)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)
# Infer Asia region indices present in dataset
asia = {
    'N225': 'Japan (Nikkei 225)',
    'HSI': 'Hong Kong (Hang Seng Index)',
    '000001.SS': 'China (Shanghai Composite)',
    '399001.SZ': 'China (Shenzhen Component)',
    'TWII': 'Taiwan (TAIEX)',
    'NSEI': 'India (NIFTY 50)'
}
df_asia = df[df['Index'].isin(asia.keys())].copy()
df_asia['name'] = df_asia['Index'].map(asia)
# pick highest
best = df_asia.sort_values('avg_intraday_vol', ascending=False).head(1)
answer = {
    'Index': best.iloc[0]['Index'],
    'Description': best.iloc[0]['name'],
    'AvgIntradayVolatility': best.iloc[0]['avg_intraday_vol']
}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_yBbEmFRmevxLmUdSx6BE15xr': ['index_info'], 'var_call_EEAIHRtp57Yi9h76GJy4SnTC': ['index_trade'], 'var_call_ZpOnHwZLT6FCFeDNOZ3cjGHN': [{'Index': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'Index': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'Index': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}]}

exec(code, env_args)
