code = """import json, pandas as pd

# Load trade data
path = var_call_pAyxzPSMOc8Edq3VLYcv4Y5n
trade = pd.read_json(path)
trade['dt'] = pd.to_datetime(trade['dt']).dt.date
trade['closeusd'] = pd.to_numeric(trade['closeusd'], errors='coerce')
trade = trade.dropna(subset=['dt','closeusd'])

# Monthly contribution simulation: invest $1 at each month's first trading day, value at end using last trading day price
trade['month'] = pd.to_datetime(trade['dt']).astype('datetime64[ns]').dt.to_period('M')

# first and last close in each month per index
first = trade.sort_values(['Index','dt']).groupby(['Index','month'], as_index=False).first()[['Index','month','closeusd']].rename(columns={'closeusd':'first_close'})
last = trade.sort_values(['Index','dt']).groupby(['Index','month'], as_index=False).last()[['Index','month','closeusd']].rename(columns={'closeusd':'last_close'})
ml = first.merge(last, on=['Index','month'], how='inner')

# Shares bought each month with $1 at first_close, valued at end at last_close => contribution value = 1/first_close * last_close
ml['contrib_value'] = (1.0/ml['first_close']) * ml['last_close']
res = ml.groupby('Index').agg(months=('month','nunique'), final_value=('contrib_value','sum')).reset_index()
res['total_contributed'] = res['months'] * 1.0
res['multiple'] = res['final_value'] / res['total_contributed']
res = res.sort_values(['multiple','final_value'], ascending=False)

# Map index to exchange/country
idx_to_exchange = {
    'NYA':'New York Stock Exchange',
    'IXIC':'NASDAQ',
    'HSI':'Hong Kong Stock Exchange',
    '000001.SS':'Shanghai Stock Exchange',
    'N225':'Tokyo Stock Exchange',
    'N100':'Euronext',
    '399001.SZ':'Shenzhen Stock Exchange',
    'GSPTSE':'Toronto Stock Exchange',
    'NSEI':'National Stock Exchange of India',
    'GDAXI':'Frankfurt Stock Exchange',
    'SSMI':'SIX Swiss Exchange',
    'TWII':'Taiwan Stock Exchange',
    'J203.JO':'Johannesburg Stock Exchange',
}
exchange_to_country = {
    'New York Stock Exchange':'United States',
    'NASDAQ':'United States',
    'Hong Kong Stock Exchange':'Hong Kong',
    'Shanghai Stock Exchange':'China',
    'Shenzhen Stock Exchange':'China',
    'Tokyo Stock Exchange':'Japan',
    'Euronext':'Netherlands/France/Belgium (pan-European)',
    'Toronto Stock Exchange':'Canada',
    'National Stock Exchange of India':'India',
    'Frankfurt Stock Exchange':'Germany',
    'SIX Swiss Exchange':'Switzerland',
    'Taiwan Stock Exchange':'Taiwan',
    'Johannesburg Stock Exchange':'South Africa',
}

res['Exchange'] = res['Index'].map(idx_to_exchange)
res['Country'] = res['Exchange'].map(exchange_to_country)

top5 = res.head(5)
out = top5[['Index','Exchange','Country','months','multiple','final_value','total_contributed']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UQNKGW67dSqn2nd1Mho4VPxt': ['index_info'], 'var_call_PVuChzZX3CspOa7HKxa95Eeg': ['index_trade'], 'var_call_zAQmgj6aeYMp2ef4zfMBIwF8': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_UGk8U6XpFKCriQcAq41gNckN': {'samples': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', '1987-01-05 00:00:00', '06 Jan 1987, 00:00', '07 Jan 1987, 00:00'], 'parsed': ['1986-12-31', '1987-01-02', '1987-01-05', '1987-01-06', '1987-01-07']}, 'var_call_LhPtf4qvNBGvdzlxcsepRVG7': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'CloseUSD': '338.92301274'}], 'var_call_Sq7PKHHvVgeIfU6oV1xKfNTO': [{'n': '104224', 'non_numeric_closeusd': '0.0'}], 'var_call_UmXQdqjiMCQ4CS3L8ahVbGlZ': [{'Index': 'J203.JO', 'min_dt': '2012-02-08 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '2346'}, {'Index': 'IXIC', 'min_dt': '1971-02-05 00:00:00', 'max_dt': '2021-05-28 00:00:00', 'n': '12690'}, {'Index': 'HSI', 'min_dt': '1986-12-31 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '8492'}, {'Index': 'N225', 'min_dt': '1965-01-05 00:00:00', 'max_dt': '2021-06-03 00:00:00', 'n': '13874'}, {'Index': 'GSPTSE', 'min_dt': '1979-06-29 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '10526'}, {'Index': 'NSEI', 'min_dt': '2007-09-17 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '3346'}, {'Index': 'GDAXI', 'min_dt': '1987-12-30 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '8438'}, {'Index': 'NYA', 'min_dt': '1965-12-31 00:00:00', 'max_dt': '2021-05-28 00:00:00', 'n': '13947'}, {'Index': '000001.SS', 'min_dt': '1997-07-02 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '5791'}, {'Index': 'SSMI', 'min_dt': '1990-11-09 00:00:00', 'max_dt': '2021-05-28 00:00:00', 'n': '7671'}, {'Index': 'TWII', 'min_dt': '1997-07-02 00:00:00', 'max_dt': '2021-05-31 00:00:00', 'n': '5869'}, {'Index': 'N100', 'min_dt': '1999-12-31 00:00:00', 'max_dt': '2021-06-02 00:00:00', 'n': '5474'}, {'Index': '399001.SZ', 'min_dt': '1997-08-22 00:00:00', 'max_dt': '2021-06-02 00:00:00', 'n': '5760'}], 'var_call_pAyxzPSMOc8Edq3VLYcv4Y5n': 'file_storage/call_pAyxzPSMOc8Edq3VLYcv4Y5n.json', 'var_call_HMppnigSSeBC26ItYYmadk8R': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
