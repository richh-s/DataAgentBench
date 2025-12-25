code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-16511267577190411835'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

def parse_date(date_str):
    date_str = str(date_str)
    date_str = re.sub(r' at \d{1,2}:\d{2} [AP]M', '', date_str)
    date_str = re.sub(r', \d{2}:\d{2}', '', date_str)
    date_str = date_str.split(' ')[0] if '-' in date_str and ':' in date_str else date_str
    return date_str

df['clean_date'] = df['Date'].apply(parse_date)
df['dt'] = pd.to_datetime(df['clean_date'], errors='coerce')

df_filtered = df[df['dt'] >= '2000-01-01'].copy()
df_filtered['Adj Close'] = pd.to_numeric(df_filtered['Adj Close'], errors='coerce')
df_filtered = df_filtered.dropna(subset=['Adj Close', 'dt'])
df_filtered = df_filtered.sort_values(by=['Index', 'dt'])

min_dates = df_filtered.groupby('Index')['dt'].min()
valid_indices = min_dates[min_dates < '2001-01-01'].index.tolist()

results = []
monthly_investment = 100.0

for idx in valid_indices:
    sub = df_filtered[df_filtered['Index'] == idx].copy()
    sub['Year'] = sub['dt'].dt.year
    sub['Month'] = sub['dt'].dt.month
    invest_days = sub.groupby(['Year', 'Month']).first().reset_index()
    invest_days['Units'] = monthly_investment / invest_days['Adj Close']
    total_units = invest_days['Units'].sum()
    total_invested = len(invest_days) * monthly_investment
    last_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0
    results.append({'Index': idx, 'Return': overall_return})

results_df = pd.DataFrame(results).sort_values(by='Return', ascending=False)
print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-7580508971202642257': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-7580508971202644492': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-11595469588490585805': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-12650114581479672954': [{'count_star()': '104224'}], 'var_function-call-16511267577190411835': 'file_storage/function-call-16511267577190411835.json', 'var_function-call-16511267577190409320': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-3615847063653708433': [{'Index': 'IXIC', 'Return': 3.6752650452550393, 'Country': 'United States'}, {'Index': '399001.SZ', 'Return': 1.3677777543840082, 'Country': 'China'}, {'Index': 'GDAXI', 'Return': 1.3479710594327972, 'Country': 'Germany'}, {'Index': 'NSEI', 'Return': 1.3410985429882916, 'Country': 'India'}, {'Index': 'TWII', 'Return': 1.2962878757605316, 'Country': 'Taiwan'}], 'var_function-call-16335683327486084847': {'000001.SS': '2000-01-06', '399001.SZ': '2000-01-04', 'GDAXI': '2000-01-03', 'GSPTSE': '2000-01-07', 'HSI': '2000-01-03', 'IXIC': '2000-01-04', 'J203.JO': '2012-02-09', 'N100': '2000-01-05', 'N225': '2000-01-06', 'NSEI': '2007-09-17', 'NYA': '2000-01-04', 'SSMI': '2000-01-10', 'TWII': '2000-01-04'}, 'var_function-call-4278032284777641644': [{'Index': 'IXIC', 'Return': 3.6752650452550393, 'Country': 'United States'}, {'Index': '399001.SZ', 'Return': 1.3677777543840082, 'Country': 'China'}, {'Index': 'GDAXI', 'Return': 1.3479710594327972, 'Country': 'Germany'}, {'Index': 'TWII', 'Return': 1.2962878757605316, 'Country': 'Taiwan'}, {'Index': 'N225', 'Return': 1.120160995801853, 'Country': 'Japan'}]}

exec(code, env_args)
