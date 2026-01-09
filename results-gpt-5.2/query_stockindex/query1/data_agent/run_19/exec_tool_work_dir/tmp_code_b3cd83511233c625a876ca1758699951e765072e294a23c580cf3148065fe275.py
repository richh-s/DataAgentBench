code = """import json, pandas as pd
records = var_call_27AodA4e5DbHqXh7vPG9TrHk

df = pd.DataFrame(records)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Define Asia indices present in this dataset
asia = {
  'N225': 'Japan (Tokyo Stock Exchange) – Nikkei 225',
  'NSEI': 'India (NSE) – Nifty 50',
  'HSI': 'Hong Kong – Hang Seng Index',
  '000001.SS': 'China (Shanghai) – SSE Composite',
  '399001.SZ': 'China (Shenzhen) – SZSE Component',
  'TWII': 'Taiwan – TAIEX'
}

df_asia = df[df['idx'].isin(asia.keys())].copy()
df_asia['name'] = df_asia['idx'].map(asia)

best = df_asia.sort_values('avg_intraday_vol', ascending=False).head(1)
answer = {
    'index_symbol': best.iloc[0]['idx'],
    'index_name': best.iloc[0]['name'],
    'avg_intraday_volatility': best.iloc[0]['avg_intraday_vol']
}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_35SpQ78eoRCGJG1cgNnvKAE3': ['index_info'], 'var_call_w79KH2NajKsvGepaD5cg2vN7': ['index_trade'], 'var_call_ifp0YXlQDuNwdzii2cxiMTad': [], 'var_call_SZM9gloGNRKRmOR5tQSqkUYW': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_27AodA4e5DbHqXh7vPG9TrHk': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}]}

exec(code, env_args)
