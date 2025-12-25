code = """import json, pandas as pd

with open(var_call_EpFrSahH8JFsrOEmiOAlKz2k, 'r') as f:
    data = json.load(f)

prices = pd.DataFrame(data)

# no datetime conversion, just compute per-index return using first and last Adj Close after 2000-01-01 as approximation
prices = prices[prices['Date'] >= '2000-01-01 00:00:00']
prices['Adj Close'] = prices['Adj Close'].astype(float)

first = prices.groupby('Index').head(1)[['Index','Adj Close']].rename(columns={'Adj Close':'first_price'})
last = prices.groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'last_price'})

result = first.merge(last, on='Index')
result['return_multiple'] = result['last_price'] / result['first_price']

first_dates = pd.DataFrame(var_call_tb7m01uCIwPKq5lxg5NNihcQ)

eligible = first_dates[first_dates['first_date'] <= '01 Jan 2001, 00:00']['Index']
result = result[result['Index'].isin(eligible)]

result = result.dropna(subset=['return_multiple'])

top5 = result.sort_values('return_multiple', ascending=False).head(5)

index_country = {
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
}

top5['Country'] = top5['Index'].map(index_country)

answer = top5[['Index','Country','return_multiple']].to_dict(orient='records')

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tb7m01uCIwPKq5lxg5NNihcQ': [{'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_EpFrSahH8JFsrOEmiOAlKz2k': 'file_storage/call_EpFrSahH8JFsrOEmiOAlKz2k.json', 'var_call_e8YdBazaaa1XBIx2cFE56qG8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_3T1Um4Zaf6jEVAielBLhIPWn': [{'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_r5q2GW4FT2OAqghADND3g0qI': {'cols': ['Index', 'Date', 'Adj Close'], 'sample_dates': ['2000-01-04 00:00:00', '2000-01-05 00:00:00', '2000-01-10 00:00:00', '2000-01-12 00:00:00', '2000-01-14 00:00:00']}}

exec(code, env_args)
