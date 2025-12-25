code = """import json, pandas as pd
from datetime import datetime

path = var_call_AvJtTJDLqH9d90j9OvJ7GJgg
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates: format like '01 Apr 2003, 00:00'
df['dt'] = pd.to_datetime(df['Date'], format='%d %b %Y, %H:%M', errors='coerce')

# filter from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['dt'] >= start]

# ensure CloseUSD numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# pick first trading day each month per index
df['ym'] = df['dt'].dt.to_period('M')
first_per_month = df.sort_values('dt').groupby(['Index','ym']).first().reset_index()

# assume $1 invested each month
first_per_month['units'] = 1.0 / first_per_month['CloseUSD']

agg = first_per_month.groupby('Index').agg(total_units=('units','sum'), n_months=('units','size')).reset_index()

# get final price per index (latest date in dataset)
latest = df.sort_values('dt').groupby('Index').tail(1)[['Index','CloseUSD']].rename(columns={'CloseUSD':'final_price'})

res = agg.merge(latest, on='Index')
res['final_value'] = res['total_units'] * res['final_price']

# sort descending and take top 5
Top = res.sort_values('final_value', ascending=False).head(5)

result = Top.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_scjxYddpI03qBknsVQeGdAGY': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Gso5o43OU7St4uREWsOfINSS': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_qrTzbLS5Cs8Mk9uCkvm0jDJ3': [{'year': ' 01,'}, {'year': ' 02,'}, {'year': ' 03,'}, {'year': ' 04,'}, {'year': ' 05,'}, {'year': ' 06,'}, {'year': ' 07,'}, {'year': ' 08,'}, {'year': ' 09,'}, {'year': ' 10,'}, {'year': ' 11,'}, {'year': ' 12,'}, {'year': ' 13,'}, {'year': ' 14,'}, {'year': ' 15,'}, {'year': ' 16,'}, {'year': ' 17,'}, {'year': ' 18,'}, {'year': ' 19,'}, {'year': ' 196'}, {'year': ' 197'}, {'year': ' 198'}, {'year': ' 199'}, {'year': ' 20,'}, {'year': ' 200'}, {'year': ' 201'}, {'year': ' 202'}, {'year': ' 21,'}, {'year': ' 22,'}, {'year': ' 23,'}, {'year': ' 24,'}, {'year': ' 25,'}, {'year': ' 26,'}, {'year': ' 27,'}, {'year': ' 28,'}, {'year': ' 29,'}, {'year': ' 30,'}, {'year': ' 31,'}, {'year': ', 19'}, {'year': ', 20'}, {'year': '-01 '}, {'year': '-02 '}, {'year': '-03 '}, {'year': '-04 '}, {'year': '-05 '}, {'year': '-06 '}, {'year': '-07 '}, {'year': '-08 '}, {'year': '-09 '}, {'year': '-10 '}, {'year': '-11 '}, {'year': '-12 '}, {'year': '-13 '}, {'year': '-14 '}, {'year': '-15 '}, {'year': '-16 '}, {'year': '-17 '}, {'year': '-18 '}, {'year': '-19 '}, {'year': '-20 '}, {'year': '-21 '}, {'year': '-22 '}, {'year': '-23 '}, {'year': '-24 '}, {'year': '-25 '}, {'year': '-26 '}, {'year': '-27 '}, {'year': '-28 '}, {'year': '-29 '}, {'year': '-30 '}, {'year': '-31 '}, {'year': '0, 1'}, {'year': '0, 2'}, {'year': '01, '}, {'year': '02, '}, {'year': '03, '}, {'year': '04, '}, {'year': '05, '}, {'year': '06, '}, {'year': '07, '}, {'year': '08, '}, {'year': '09, '}, {'year': '1, 1'}, {'year': '1, 2'}, {'year': '10, '}, {'year': '11, '}, {'year': '12, '}, {'year': '13, '}, {'year': '14, '}, {'year': '15, '}, {'year': '16, '}, {'year': '17, '}, {'year': '18, '}, {'year': '19, '}, {'year': '1965'}, {'year': '1966'}, {'year': '1967'}, {'year': '1968'}, {'year': '1969'}, {'year': '1970'}, {'year': '1971'}, {'year': '1972'}, {'year': '1973'}, {'year': '1974'}, {'year': '1975'}, {'year': '1976'}, {'year': '1977'}, {'year': '1978'}, {'year': '1979'}, {'year': '1980'}, {'year': '1981'}, {'year': '1982'}, {'year': '1983'}, {'year': '1984'}, {'year': '1985'}, {'year': '1986'}, {'year': '1987'}, {'year': '1988'}, {'year': '1989'}, {'year': '1990'}, {'year': '1991'}, {'year': '1992'}, {'year': '1993'}, {'year': '1994'}, {'year': '1995'}, {'year': '1996'}, {'year': '1997'}, {'year': '1998'}, {'year': '1999'}, {'year': '2, 1'}, {'year': '2, 2'}, {'year': '20, '}, {'year': '2000'}, {'year': '2001'}, {'year': '2002'}, {'year': '2003'}, {'year': '2004'}, {'year': '2005'}, {'year': '2006'}, {'year': '2007'}, {'year': '2008'}, {'year': '2009'}, {'year': '2010'}, {'year': '2011'}, {'year': '2012'}, {'year': '2013'}, {'year': '2014'}, {'year': '2015'}, {'year': '2016'}, {'year': '2017'}, {'year': '2018'}, {'year': '2019'}, {'year': '2020'}, {'year': '2021'}, {'year': '21, '}, {'year': '22, '}, {'year': '23, '}, {'year': '24, '}, {'year': '25, '}, {'year': '26, '}, {'year': '27, '}, {'year': '28, '}, {'year': '29, '}, {'year': '3, 1'}, {'year': '3, 2'}, {'year': '30, '}, {'year': '31, '}, {'year': '4, 1'}, {'year': '4, 2'}, {'year': '5, 1'}, {'year': '5, 2'}, {'year': '6, 1'}, {'year': '6, 2'}, {'year': '7, 1'}, {'year': '7, 2'}, {'year': '8, 1'}, {'year': '8, 2'}, {'year': '9, 1'}, {'year': '9, 2'}, {'year': 'er 0'}, {'year': 'er 1'}, {'year': 'er 2'}, {'year': 'er 3'}, {'year': 'r 01'}, {'year': 'r 02'}, {'year': 'r 03'}, {'year': 'r 04'}, {'year': 'r 05'}, {'year': 'r 06'}, {'year': 'r 07'}, {'year': 'r 08'}, {'year': 'r 09'}, {'year': 'r 10'}, {'year': 'r 11'}, {'year': 'r 12'}, {'year': 'r 13'}, {'year': 'r 14'}, {'year': 'r 15'}, {'year': 'r 16'}, {'year': 'r 17'}, {'year': 'r 18'}, {'year': 'r 19'}, {'year': 'r 20'}, {'year': 'r 21'}, {'year': 'r 22'}, {'year': 'r 23'}, {'year': 'r 24'}, {'year': 'r 25'}, {'year': 'r 26'}, {'year': 'r 27'}, {'year': 'r 28'}, {'year': 'r 29'}, {'year': 'r 30'}, {'year': 'r 31'}, {'year': 'y 01'}, {'year': 'y 02'}, {'year': 'y 03'}, {'year': 'y 04'}, {'year': 'y 05'}, {'year': 'y 06'}, {'year': 'y 07'}, {'year': 'y 08'}, {'year': 'y 09'}, {'year': 'y 10'}, {'year': 'y 11'}, {'year': 'y 12'}, {'year': 'y 13'}, {'year': 'y 14'}, {'year': 'y 15'}, {'year': 'y 16'}, {'year': 'y 17'}, {'year': 'y 18'}, {'year': 'y 19'}, {'year': 'y 20'}, {'year': 'y 21'}, {'year': 'y 22'}, {'year': 'y 23'}, {'year': 'y 24'}, {'year': 'y 25'}, {'year': 'y 26'}, {'year': 'y 27'}, {'year': 'y 28'}, {'year': 'y 29'}], 'var_call_AvJtTJDLqH9d90j9OvJ7GJgg': 'file_storage/call_AvJtTJDLqH9d90j9OvJ7GJgg.json'}

exec(code, env_args)
