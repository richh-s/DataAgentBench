code = """import pandas as pd, json, math

path = var_call_mxAJnuy20AlHKK0gw4MjW5Ol
with open(path,'r') as f:
    data=json.load(f)

df=pd.DataFrame(data)
# parse date
df['Date_parsed']=pd.to_datetime(df['Date'].str.replace(' at 12:00 AM','', regex=False), errors='coerce', infer_datetime_format=True)
# try additional parse for remaining
mask=df['Date_parsed'].isna()
if mask.any():
    df.loc[mask,'Date_parsed']=pd.to_datetime(df.loc[mask,'Date'], errors='coerce')

df=df.dropna(subset=['Date_parsed','CloseUSD'])
df['CloseUSD']=pd.to_numeric(df['CloseUSD'], errors='coerce')
df=df.dropna(subset=['CloseUSD'])
df=df[df['Date_parsed']>=pd.Timestamp('2000-01-01')]
# monthly returns
df['month']=df['Date_parsed'].dt.to_period('M').dt.to_timestamp()
# first and last within month
first=df.sort_values('Date_parsed').groupby(['Index','month'], as_index=False).first()[['Index','month','CloseUSD']].rename(columns={'CloseUSD':'first'})
last=df.sort_values('Date_parsed').groupby(['Index','month'], as_index=False).last()[['Index','month','CloseUSD']].rename(columns={'CloseUSD':'last'})
m=pd.merge(first,last,on=['Index','month'])
m=m[(m['first']>0) & (m['last']>0)]
m['ret']=m['last']/m['first']-1
# aggregate cumulative via log
m=m[m['ret']>-0.999999]
agg=m.groupby('Index').agg(n_months=('ret','size'), cum_log=('ret', lambda x: float((pd.Series(1+x)).apply(math.log).sum())))
agg['cumulative_return']=agg['cum_log'].apply(math.exp)-1
agg=agg.reset_index().sort_values('cumulative_return', ascending=False)
# top 5
out=agg.head(5)[['Index','n_months','cumulative_return']]
print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_573u2hpe6FOd5xoZgzFGwUqh': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_oYCG8MlFBCwuPR7xHlWkVQRF': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2016-12-29 00:00:00', 'n': '9'}, {'Date': 'January 15, 2021 at 12:00 AM', 'n': '9'}, {'Date': '2002-01-11 00:00:00', 'n': '9'}, {'Date': '01 Jun 2016, 00:00', 'n': '9'}, {'Date': '26 Apr 2013, 00:00', 'n': '9'}], 'var_call_0Wpoj5FzHWXSMuFfwdwboZFW': [['January 27, 2015 at 12:00 AM', '2015-01-27 00:00:00'], ['2017-10-12 00:00:00', '2017-10-12 00:00:00'], ['2015-01-16 00:00:00', '2015-01-16 00:00:00'], ['27 Sep 2013, 00:00', '2013-09-27 00:00:00'], ['2013-05-21 00:00:00', '2013-05-21 00:00:00'], ['July 12, 2010 at 12:00 AM', '2010-07-12 00:00:00'], ['2012-05-25 00:00:00', '2012-05-25 00:00:00'], ['June 19, 2019 at 12:00 AM', '2019-06-19 00:00:00'], ['07 Apr 2011, 00:00', '2011-04-07 00:00:00'], ['April 15, 2005 at 12:00 AM', '2005-04-15 00:00:00'], ['16 Jan 2014, 00:00', '2014-01-16 00:00:00'], ['2017-06-14 00:00:00', '2017-06-14 00:00:00'], ['12 Nov 2010, 00:00', '2010-11-12 00:00:00'], ['15 May 2019, 00:00', '2019-05-15 00:00:00'], ['2012-06-18 00:00:00', '2012-06-18 00:00:00'], ['2016-12-29 00:00:00', '2016-12-29 00:00:00'], ['January 15, 2021 at 12:00 AM', '2021-01-15 00:00:00'], ['2002-01-11 00:00:00', '2002-01-11 00:00:00'], ['01 Jun 2016, 00:00', '2016-06-01 00:00:00'], ['26 Apr 2013, 00:00', '2013-04-26 00:00:00']], 'var_call_mxAJnuy20AlHKK0gw4MjW5Ol': 'file_storage/call_mxAJnuy20AlHKK0gw4MjW5Ol.json'}

exec(code, env_args)
