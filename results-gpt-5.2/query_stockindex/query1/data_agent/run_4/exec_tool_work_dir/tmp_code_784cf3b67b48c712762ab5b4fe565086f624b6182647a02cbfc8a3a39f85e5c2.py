code = """import json, pandas as pd

df = pd.DataFrame(var_call_uh9DXAEPMgyddkXJW2oKifQ6)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

asia = {
  'N225': 'Japan (Tokyo Stock Exchange)',
  'HSI': 'Hong Kong (Hong Kong Stock Exchange)',
  '000001.SS': 'China (Shanghai Stock Exchange)',
  '399001.SZ': 'China (Shenzhen Stock Exchange)',
  'NSEI': 'India (National Stock Exchange of India)',
  'TWII': 'Taiwan (Taiwan Stock Exchange)',
}

df_asia = df[df['idx'].isin(list(asia.keys()))].copy()
df_asia['exchange_region'] = df_asia['idx'].map(asia)

top = df_asia.sort_values('avg_intraday_vol', ascending=False).head(1)
ans = {
  'index': top.iloc[0]['idx'],
  'exchange_region': top.iloc[0]['exchange_region'],
  'avg_intraday_volatility': float(top.iloc[0]['avg_intraday_vol'])
}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_TW7PDJYQJb2zPlXhNOWTqkFz': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_741UEJ7yEQODeFRxJqd7bQxB': [{'sample_date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'sample_date': '2015-01-16 00:00:00', 'n': '11'}, {'sample_date': '2017-10-12 00:00:00', 'n': '11'}, {'sample_date': '2017-06-14 00:00:00', 'n': '10'}, {'sample_date': '2013-05-21 00:00:00', 'n': '10'}], 'var_call_uh9DXAEPMgyddkXJW2oKifQ6': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066'}]}

exec(code, env_args)
