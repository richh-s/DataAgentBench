code = """import json, pandas as pd

df = pd.DataFrame(var_call_w3q7tiU4MooqcMaz1Cpp5jqy)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

# Define Asia-region indices present in dataset
asia = {
    'N225': 'Japan (Tokyo) - Nikkei 225',
    'HSI': 'Hong Kong - Hang Seng',
    '000001.SS': 'China (Shanghai) - SSE Composite',
    '399001.SZ': 'China (Shenzhen) - SZSE Component',
    'TWII': 'Taiwan - TAIEX',
    'NSEI': 'India - NIFTY 50'
}

df_asia = df[df['Index'].isin(list(asia.keys()))].copy()
df_asia['name'] = df_asia['Index'].map(asia)

best = df_asia.sort_values('avg_intraday_vol', ascending=False).iloc[0]
result = {
    'Index': best['Index'],
    'Description': best['name'],
    'AvgIntradayVolatility': best['avg_intraday_vol'],
    'Period': 'since 2020-01-01',
    'Formula': '(High-Low)/Open averaged over days'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3Ex9Tx8rnoYOAsONKl5qRZUt': ['index_info'], 'var_call_cx7MCiQX2jokPBIH2VEU2P9b': ['index_trade'], 'var_call_WWfDP7EmARqzS7iiifuywO5j': [{'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}], 'var_call_w3q7tiU4MooqcMaz1Cpp5jqy': [{'Index': 'J203.JO', 'avg_intraday_vol': '0.017341240029622774'}, {'Index': 'N225', 'avg_intraday_vol': '0.013420362105889214'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.01190372004768639'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01754961385149785'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.015735863769325373'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014688234063144042'}, {'Index': 'NYA', 'avg_intraday_vol': '0.014161525969530046'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.014082512769161384'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.014043436205293046'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01267113951326394'}, {'Index': 'N100', 'avg_intraday_vol': '0.013102109556857611'}, {'Index': '399001.SZ', 'avg_intraday_vol': '0.017785300962291015'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.018396922846873384'}]}

exec(code, env_args)
