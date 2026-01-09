code = """import json
import pandas as pd

df = pd.DataFrame(var_call_IspGA9mStCnoEJJfEf66PPAK)
df['avg_intraday_vol'] = df['avg_intraday_vol'].astype(float)

asia = {
    'N225': 'Japan (Tokyo Stock Exchange)',
    'HSI': 'Hong Kong (Hong Kong Stock Exchange)',
    '000001.SS': 'China (Shanghai Stock Exchange)',
    '399001.SZ': 'China (Shenzhen Stock Exchange)',
    'NSEI': 'India (National Stock Exchange of India)',
    'TWII': 'Taiwan (Taiwan Stock Exchange)',
}

df_asia = df[df['Index'].isin(asia.keys())].copy()
df_asia['Exchange/Country'] = df_asia['Index'].map(asia)

top = df_asia.sort_values('avg_intraday_vol', ascending=False).iloc[0]
result = {
    'index': top['Index'],
    'exchange_country': top['Exchange/Country'],
    'avg_intraday_volatility': float(top['avg_intraday_vol'])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VuyDcVbiy3zRqDDPOcD3fc62': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_ohn7hIcSOPszD9zdlRJU9oGH': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_AjeXxbW6DWiHFet7ZgdsV4gE': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '05 Aug 2020, 00:00', 'n': '9'}, {'Date': 'April 23, 2013 at 12:00 AM', 'n': '9'}, {'Date': 'January 15, 2021 at 12:00 AM', 'n': '9'}, {'Date': 'May 15, 2015 at 12:00 AM', 'n': '9'}, {'Date': '01 Jun 2016, 00:00', 'n': '9'}, {'Date': 'January 02, 2018 at 12:00 AM', 'n': '9'}, {'Date': '09 Jun 2015, 00:00', 'n': '9'}, {'Date': 'April 28, 2014 at 12:00 AM', 'n': '9'}, {'Date': 'April 09, 2018 at 12:00 AM', 'n': '9'}, {'Date': 'November 05, 2013 at 12:00 AM', 'n': '9'}, {'Date': '26 Apr 2013, 00:00', 'n': '9'}], 'var_call_IspGA9mStCnoEJJfEf66PPAK': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.018293021165089372'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.01826128391465914'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.0176915716830824'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01653278149621257'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.016433893332157116'}, {'Index': 'NYA', 'avg_intraday_vol': '0.015450175155161689'}, {'Index': 'HSI', 'avg_intraday_vol': '0.014566131296198794'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.01441505190039977'}, {'Index': 'N225', 'avg_intraday_vol': '0.014339806107587037'}, {'Index': 'N100', 'avg_intraday_vol': '0.014333060651167389'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.013745402784616082'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.013654973139045913'}, {'Index': 'TWII', 'avg_intraday_vol': '0.012634393668700278'}]}

exec(code, env_args)
