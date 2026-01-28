code = """import json
import pandas as pd

data = var_call_NvFNr9FkYIgA7KbLA7ilhUtv

df = pd.DataFrame(data)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Map index symbols to region (Asia vs others)
asia = {
    'N225': 'Japan (Tokyo Stock Exchange) — Nikkei 225',
    'NSEI': 'India (NSE) — NIFTY 50',
    'HSI': 'Hong Kong — Hang Seng Index',
    '000001.SS': 'China (Shanghai) — SSE Composite',
    '399001.SZ': 'China (Shenzhen) — SZSE Component',
    'TWII': 'Taiwan — TAIEX'
}

asia_df = df[df['idx'].isin(asia.keys())].copy()
asia_df['description'] = asia_df['idx'].map(asia)

best = asia_df.sort_values('avg_intraday_vol', ascending=False).head(1)
result = {
    'index': best.iloc[0]['idx'],
    'description': best.iloc[0]['description'],
    'avg_intraday_volatility': float(best.iloc[0]['avg_intraday_vol'])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EXHVWTWLUB5NQgV2bgP0WKop': ['index_info'], 'var_call_NvFNr9FkYIgA7KbLA7ilhUtv': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'idx': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'idx': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'idx': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}]}

exec(code, env_args)
