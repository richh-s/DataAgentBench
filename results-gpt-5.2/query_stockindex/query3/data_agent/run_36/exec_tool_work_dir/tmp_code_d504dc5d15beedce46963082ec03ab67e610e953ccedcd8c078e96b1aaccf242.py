code = """import json, pandas as pd
from datetime import datetime

path = var_call_mIrUwii8KIRqxsZCAKqMyz2A
with open(path,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse dates robustly
s = df['Date'].astype(str)
# unify known formats
s2 = s.str.replace(' at 12:00 AM','', regex=False)
# try parse with pandas
parsed = pd.to_datetime(s2, errors='coerce', infer_datetime_format=True)
# for remaining NaT, try specific format like '01 Apr 2003, 00:00'
mask = parsed.isna()
if mask.any():
    parsed2 = pd.to_datetime(s2[mask], errors='coerce', format='%d %b %Y, %H:%M')
    parsed.loc[mask] = parsed2
mask = parsed.isna()
if mask.any():
    parsed3 = pd.to_datetime(s2[mask], errors='coerce', format='%B %d, %Y')
    parsed.loc[mask] = parsed3

df['DateParsed'] = parsed
# keep from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['DateParsed']>=start].copy()
# closeusd numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD','DateParsed','Index'])

# monthly last close
df['Month'] = df['DateParsed'].dt.to_period('M').dt.to_timestamp('M')
monthly = (df.sort_values('DateParsed').groupby(['Index','Month'])['CloseUSD'].last().reset_index())

# DCA: invest $1 at end of each month -> shares += 1/price. final value = shares_total * last_price
last_price = monthly.sort_values('Month').groupby('Index').tail(1).set_index('Index')['CloseUSD']
shares = (monthly.assign(inv=1.0).assign(sh=lambda x: x['inv']/x['CloseUSD']).groupby('Index')['sh'].sum())
final_value = shares * last_price
n_months = monthly.groupby('Index')['Month'].nunique()
total_invested = n_months * 1.0
return_mult = final_value / total_invested
res = pd.DataFrame({'Index':return_mult.index, 'ReturnMultiple':return_mult.values, 'Months':n_months.loc[return_mult.index].values,
                    'FinalValuePer$1Monthly':final_value.values, 'TotalInvested':total_invested.loc[return_mult.index].values})
res = res.sort_values('ReturnMultiple', ascending=False).head(5)

# map index to country (manual knowledge)
country_map = {
    'IXIC':'United States',
    'NYA':'United States',
    'GDAXI':'Germany',
    'GSPTSE':'Canada',
    'N225':'Japan',
    'HSI':'Hong Kong',
    'N100':'Europe (Eurozone)',
    'SSMI':'Switzerland',
    'TWII':'Taiwan',
    '000001.SS':'China',
    '399001.SZ':'China',
    'J203.JO':'South Africa',
    'NSEI':'India'
}
res['Country'] = res['Index'].map(country_map)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3By6Fb81yj2CDZOutM8uDo37': ['index_info'], 'var_call_bcCg3VNfcvuABVzU5bkzh5Q6': ['index_trade'], 'var_call_18X0gK6QWSI17lX9N2BBTuRw': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}], 'var_call_clXxmt3ljm5zI5zXS8Awm8sU': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'CloseUSD': '319.865'}], 'var_call_7yFCHexzgiBg23GntvLsUrLI': [{'Index': 'HSI', 'Date': '03 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 04, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '05 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 06, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 07, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '10 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 11, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 12, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '13 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '2000-01-14 00:00:00'}, {'Index': 'HSI', 'Date': 'January 17, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '18 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '19 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '20 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '2000-01-21 00:00:00'}, {'Index': 'HSI', 'Date': '2000-01-24 00:00:00'}, {'Index': 'HSI', 'Date': '25 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '2000-01-26 00:00:00'}, {'Index': 'HSI', 'Date': 'January 27, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '28 Jan 2000, 00:00'}], 'var_call_mIrUwii8KIRqxsZCAKqMyz2A': 'file_storage/call_mIrUwii8KIRqxsZCAKqMyz2A.json'}

exec(code, env_args)
