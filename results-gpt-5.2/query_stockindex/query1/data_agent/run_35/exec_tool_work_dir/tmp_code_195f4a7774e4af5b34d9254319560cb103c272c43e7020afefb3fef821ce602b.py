code = """import json, pandas as pd
rows = var_call_NWR5PCKtXsp3lTQCQC1uACcv

df = pd.DataFrame(rows)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Define Asia indices in this dataset
asia = {
    'N225': 'Nikkei 225 (Japan)',
    'HSI': 'Hang Seng Index (Hong Kong)',
    '000001.SS': 'Shanghai Composite (China)',
    '399001.SZ': 'Shenzhen Component (China)',
    'TWII': 'Taiwan Weighted (Taiwan)',
    'NSEI': 'NIFTY 50 (India)'
}

adf = df[df['Index'].isin(asia.keys())].copy()
adf['name'] = adf['Index'].map(asia)

best = adf.sort_values('avg_intraday_vol', ascending=False).iloc[0]
result = {
    'Index': best['Index'],
    'Name': best['name'],
    'avg_intraday_volatility_since_2020': best['avg_intraday_vol']
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_i04fAT3TqoCpBSRg6PpzNteB': ['index_trade'], 'var_call_xRp7xyUUOErnOsP20JU1b2yP': [{'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_NWR5PCKtXsp3lTQCQC1uACcv': [{'Index': 'J203.JO', 'avg_intraday_vol': '0.019699639505813247'}, {'Index': 'N225', 'avg_intraday_vol': '0.013887900570961271'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.014215163196948618'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.018080828608150572'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.018866577311000395'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014724878842912044'}, {'Index': 'NYA', 'avg_intraday_vol': '0.016009381830756668'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013856771330441555'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.016119645088528697'}, {'Index': 'TWII', 'avg_intraday_vol': '0.012301428585896706'}, {'Index': 'N100', 'avg_intraday_vol': '0.016562308113245508'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017627698638378268'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.019533255659865505'}]}

exec(code, env_args)
