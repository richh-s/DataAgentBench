code = """import json, pandas as pd

df = pd.DataFrame(var_call_GjDptcXEHyI8a9ujXgl5quAv)
# cast
for c in ['avg_intraday_vol','n_days']:
    df[c]=pd.to_numeric(df[c])

asia = {
    'N225': 'Japan (Tokyo)',
    'HSI': 'Hong Kong',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'TWII': 'Taiwan',
    'NSEI': 'India'
}

adf = df[df['idx'].isin(asia.keys())].copy()
adf['market'] = adf['idx'].map(asia)
# highest
row = adf.sort_values('avg_intraday_vol', ascending=False).iloc[0]
result = {
    'index': row['idx'],
    'market': row['market'],
    'avg_intraday_volatility': float(row['avg_intraday_vol']),
    'period_start': '2020-01-01',
    'n_days': int(row['n_days']),
    'asia_ranking': adf.sort_values('avg_intraday_vol', ascending=False)[['idx','avg_intraday_vol']].to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Zm69hUe7aqFJWkJ8b91bZUtN': [], 'var_call_xiuvU9lziffkf65WkLO7d9uf': [{'Date': 'January 27, 2015 at 12:00 AM', 'cnt': '11'}, {'Date': '2017-10-12 00:00:00', 'cnt': '11'}, {'Date': '2015-01-16 00:00:00', 'cnt': '11'}, {'Date': '2012-06-18 00:00:00', 'cnt': '10'}, {'Date': '2017-06-14 00:00:00', 'cnt': '10'}, {'Date': '15 May 2019, 00:00', 'cnt': '10'}, {'Date': '2012-05-25 00:00:00', 'cnt': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'cnt': '10'}, {'Date': '12 Nov 2010, 00:00', 'cnt': '10'}, {'Date': '16 Jan 2014, 00:00', 'cnt': '10'}], 'var_call_GjDptcXEHyI8a9ujXgl5quAv': [{'idx': 'J203.JO', 'avg_intraday_vol': '0.01786200640333148', 'n_days': '354'}, {'idx': 'N225', 'avg_intraday_vol': '0.013426763944978347', 'n_days': '344'}, {'idx': 'GSPTSE', 'avg_intraday_vol': '0.012534163736615827', 'n_days': '355'}, {'idx': 'NSEI', 'avg_intraday_vol': '0.017071504307908447', 'n_days': '349'}, {'idx': 'GDAXI', 'avg_intraday_vol': '0.0166079612749325', 'n_days': '357'}, {'idx': 'HSI', 'avg_intraday_vol': '0.014931673425125858', 'n_days': '348'}, {'idx': 'NYA', 'avg_intraday_vol': '0.014652738733651685', 'n_days': '355'}, {'idx': 'IXIC', 'avg_intraday_vol': '0.01832021126510304', 'n_days': '355'}, {'idx': '000001.SS', 'avg_intraday_vol': '0.013781104973401202', 'n_days': '340'}, {'idx': 'SSMI', 'avg_intraday_vol': '0.014125090041703366', 'n_days': '345'}, {'idx': 'TWII', 'avg_intraday_vol': '0.013225469311378092', 'n_days': '339'}, {'idx': 'N100', 'avg_intraday_vol': '0.014407669280062476', 'n_days': '363'}, {'idx': '399001.SZ', 'avg_intraday_vol': '0.01834068808057066', 'n_days': '342'}]}

exec(code, env_args)
