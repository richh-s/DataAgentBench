code = """import pandas as pd, json

path = var_call_esx15UuJfPK6N4gOqKiTsDnM

df = pd.read_json(path)

# parse dates robustly
s = df['dt'].astype(str)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# second pass for remaining NaT
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', dayfirst=True, infer_datetime_format=True)
    dt.loc[mask] = dt2

df['date'] = dt

# keep from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date']>=start].copy()

# numeric close
df['closeusd'] = pd.to_numeric(df['closeusd'], errors='coerce')
df = df[df['closeusd'].notna() & (df['closeusd']>0)]

# monthly contribution at last available trading day each month
# create month period
df['month'] = df['date'].dt.to_period('M')
# last date per idx,month
df = df.sort_values(['idx','date'])
last = df.groupby(['idx','month'], as_index=False).tail(1)

# compute DCA shares and value
last = last.sort_values(['idx','month'])
last['inv'] = 1.0
last['shares_bought'] = last['inv'] / last['closeusd']
summary = last.groupby('idx').agg(
    months=('month','nunique'),
    total_invested=('inv','sum'),
    total_shares=('shares_bought','sum'),
    last_close=('closeusd','last'),
    first_month=('month','min'),
    last_month=('month','max')
).reset_index()
summary['final_value'] = summary['total_shares'] * summary['last_close']
summary['multiple'] = summary['final_value'] / summary['total_invested']
summary = summary.sort_values('multiple', ascending=False)

top5 = summary.head(5).copy()

# map idx to country and exchange
idx_map = {
 'NYA': {'exchange':'New York Stock Exchange', 'country':'United States'},
 'IXIC': {'exchange':'NASDAQ', 'country':'United States'},
 'HSI': {'exchange':'Hong Kong Stock Exchange', 'country':'Hong Kong (China)'},
 '000001.SS': {'exchange':'Shanghai Stock Exchange', 'country':'China'},
 '399001.SZ': {'exchange':'Shenzhen Stock Exchange', 'country':'China'},
 'N225': {'exchange':'Tokyo Stock Exchange', 'country':'Japan'},
 'N100': {'exchange':'Euronext', 'country':'Europe (Euronext)'},
 'GSPTSE': {'exchange':'Toronto Stock Exchange', 'country':'Canada'},
 'NSEI': {'exchange':'National Stock Exchange of India', 'country':'India'},
 'GDAXI': {'exchange':'Frankfurt Stock Exchange', 'country':'Germany'},
 'SSMI': {'exchange':'SIX Swiss Exchange', 'country':'Switzerland'},
 'TWII': {'exchange':'Taiwan Stock Exchange', 'country':'Taiwan'},
 'J203.JO': {'exchange':'Johannesburg Stock Exchange', 'country':'South Africa'},
}

top5['country'] = top5['idx'].map(lambda x: idx_map.get(x,{}).get('country'))

res = top5[['idx','country','months','multiple','total_invested','final_value','first_month','last_month']].to_dict('records')
print('__RESULT__:')
print(json.dumps(res, default=str))"""

env_args = {'var_call_Vj1pRZVtgU4aThYZAJEzI9cf': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_L0QtvdtnmkRG1Y5tqH9aVKVw': [], 'var_call_kxPk2Hg81KWGTE301029i0DB': [{'sample_date': '31 Dec 1986, 00:00'}, {'sample_date': 'January 02, 1987 at 12:00 AM'}, {'sample_date': '1987-01-05 00:00:00'}, {'sample_date': '06 Jan 1987, 00:00'}, {'sample_date': '07 Jan 1987, 00:00'}, {'sample_date': '1987-01-08 00:00:00'}, {'sample_date': '1987-01-09 00:00:00'}, {'sample_date': '1987-01-12 00:00:00'}, {'sample_date': '1987-01-13 00:00:00'}, {'sample_date': '1987-01-14 00:00:00'}, {'sample_date': 'January 15, 1987 at 12:00 AM'}, {'sample_date': 'January 16, 1987 at 12:00 AM'}, {'sample_date': 'January 19, 1987 at 12:00 AM'}, {'sample_date': '20 Jan 1987, 00:00'}, {'sample_date': 'January 21, 1987 at 12:00 AM'}, {'sample_date': '22 Jan 1987, 00:00'}, {'sample_date': 'January 23, 1987 at 12:00 AM'}, {'sample_date': 'January 26, 1987 at 12:00 AM'}, {'sample_date': '27 Jan 1987, 00:00'}, {'sample_date': 'January 28, 1987 at 12:00 AM'}], 'var_call_2XBKrJPr8vyvXHnuclabti5d': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_call_nnQClJoB5FtcIss7D3qxs2zG': [{'idx': '000001.SS'}, {'idx': '399001.SZ'}, {'idx': 'GDAXI'}, {'idx': 'GSPTSE'}, {'idx': 'HSI'}, {'idx': 'IXIC'}, {'idx': 'J203.JO'}, {'idx': 'N100'}, {'idx': 'N225'}, {'idx': 'NSEI'}, {'idx': 'NYA'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_sZpkjVyAFiG9eRqSrEzB0BBM': [{'idx': 'J203.JO', 'n': '2346'}, {'idx': 'N225', 'n': '13874'}, {'idx': 'GSPTSE', 'n': '10526'}, {'idx': 'NSEI', 'n': '3346'}, {'idx': 'GDAXI', 'n': '8438'}, {'idx': 'IXIC', 'n': '12690'}, {'idx': 'HSI', 'n': '8492'}, {'idx': 'NYA', 'n': '13947'}, {'idx': '000001.SS', 'n': '5791'}, {'idx': 'SSMI', 'n': '7671'}, {'idx': 'TWII', 'n': '5869'}, {'idx': 'N100', 'n': '5474'}, {'idx': '399001.SZ', 'n': '5760'}], 'var_call_gQP3kjnfh57KC7zAysj1W2Vf': {'note': 'ready'}, 'var_call_esx15UuJfPK6N4gOqKiTsDnM': 'file_storage/call_esx15UuJfPK6N4gOqKiTsDnM.json'}

exec(code, env_args)
