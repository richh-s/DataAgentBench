code = """import json, pandas as pd
from datetime import datetime
import math

# load trade data
path = var_call_D4jx5lOar7n08KLm39xQZzxO
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)

# parse dates robustly
fmts = ['%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p','%Y-%m-%d %H:%M:%S']

def parse_one(s):
    if pd.isna(s):
        return pd.NaT
    s = str(s)
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return pd.NaT

df['dt'] = df['Date'].map(parse_one)
df = df.dropna(subset=['dt'])

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# filter from 2000-01-01
start = datetime(2000,1,1)
df = df[df['dt']>=start]

# monthly series: pick last available trading day close in each month per index
# create month period
df['month'] = df['dt'].dt.to_period('M')
# sort and take last close per month
monthly = (df.sort_values(['Index','dt'])
             .groupby(['Index','month'], as_index=False)
             .tail(1))

# compute DCA growth assuming $1 invested at each month-end close
# shares added each month = 1/price
monthly['shares_add'] = 1.0 / monthly['CloseUSD']
shares = monthly.groupby('Index')['shares_add'].sum()

# final price per index = last month close in available data
last_price = monthly.sort_values(['Index','month']).groupby('Index').tail(1).set_index('Index')['CloseUSD']

# total invested = number of months (each $1)
months_count = monthly.groupby('Index').size().astype(float)

final_value = shares * last_price
multiple = final_value / months_count

res = pd.DataFrame({
    'Index': multiple.index,
    'months': months_count.reindex(multiple.index).values,
    'final_value_per_1monthly': final_value.values,
    'invested': months_count.values,
    'multiple': multiple.values
}).sort_values('multiple', ascending=False)

# keep top 5
top5 = res.head(5)

# map index to exchange and country
idx_to_exchange_country = {
    'NYA': ('New York Stock Exchange','United States'),
    'IXIC': ('NASDAQ','United States'),
    'HSI': ('Hong Kong Stock Exchange','Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange','China'),
    '399001.SZ': ('Shenzhen Stock Exchange','China'),
    'N225': ('Tokyo Stock Exchange','Japan'),
    'N100': ('Euronext','Europe'),
    'GSPTSE': ('Toronto Stock Exchange','Canada'),
    'GDAXI': ('Frankfurt Stock Exchange','Germany'),
    'SSMI': ('SIX Swiss Exchange','Switzerland'),
    'TWII': ('Taiwan Stock Exchange','Taiwan'),
    'J203.JO': ('Johannesburg Stock Exchange','South Africa'),
    'NSEI': ('National Stock Exchange of India','India'),
}

out = []
for _, r in top5.iterrows():
    exch, country = idx_to_exchange_country.get(r['Index'], (None,None))
    out.append({
        'Index': r['Index'],
        'Country': country,
        'Exchange': exch,
        'Months_invested': int(r['months']),
        'DCA_multiple_final_value_over_total_contrib': float(r['multiple']),
        'Final_value_if_1USD_each_month': float(r['final_value_per_1monthly']),
        'Total_contributed_USD': float(r['invested'])
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_x8ZlQlKtkiKIviA1zvcsJCmT': ['index_trade'], 'var_call_jlXzdU9exxWJvObbekxJTvX8': ['index_info'], 'var_call_kLILf0mqOBYUHEzoDz4WfJTT': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}], 'var_call_Yzx0XxzhUBwHtR1qFmvWrlE4': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'CloseUSD': '319.865'}], 'var_call_c8xINCnxeQUUn3XOkjEp8O00': {'status': 'need_full_data_query'}, 'var_call_D4jx5lOar7n08KLm39xQZzxO': 'file_storage/call_D4jx5lOar7n08KLm39xQZzxO.json', 'var_call_z424sxkD4wFzUJQDtrVOTYGh': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
