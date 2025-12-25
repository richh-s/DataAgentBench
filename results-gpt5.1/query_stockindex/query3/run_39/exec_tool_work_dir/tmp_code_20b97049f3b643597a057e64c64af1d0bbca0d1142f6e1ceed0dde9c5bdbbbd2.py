code = """import pandas as pd, json, os

path = var_call_vU3RCpyvJArSKMcJyQsk9MqL
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# simulate monthly investment of 1 unit USD at first trading day of each month per index
results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    # first trading day per month
    firsts = g.groupby([g['Date'].dt.year, g['Date'].dt.month]).first().reset_index(drop=True)
    if firsts.empty:
        continue
    shares = (1.0 / firsts['CloseUSD']).sum()
    total_invested = len(firsts) * 1.0
    final_price = g.iloc[-1]['CloseUSD']
    final_value = shares * final_price
    results.append({'Index': idx, 'total_invested': total_invested, 'final_value': final_value, 'multiple': final_value/total_invested})

res_df = pd.DataFrame(results).sort_values('multiple', ascending=False).head(5)

# map indices to countries manually
country_map = {
 'IXIC': 'United States',
 'NYA': 'United States',
 'GSPTSE': 'Canada',
 'GDAXI': 'Germany',
 'N225': 'Japan',
 'HSI': 'Hong Kong, China',
 '000001.SS': 'China',
 '399001.SZ': 'China',
 'SSMI': 'Switzerland',
 'TWII': 'Taiwan',
 'N100': 'Eurozone',
 'NSEI': 'India',
 'J203.JO': 'South Africa'
}

res_df['Country'] = res_df['Index'].map(country_map)

answer = res_df[['Index','Country','multiple']].to_dict(orient='records')
answer_json = json.dumps(answer)
print('__RESULT__:')
print(answer_json)"""

env_args = {'var_call_4SaNHMEwo9EefyZ1eSpDf6FP': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_vU3RCpyvJArSKMcJyQsk9MqL': 'file_storage/call_vU3RCpyvJArSKMcJyQsk9MqL.json', 'var_call_pKkgmanhpLBUVpFGvXcub6N4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
