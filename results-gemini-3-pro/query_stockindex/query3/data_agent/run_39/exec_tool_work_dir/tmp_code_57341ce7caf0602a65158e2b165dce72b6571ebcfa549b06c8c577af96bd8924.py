code = """import pandas as pd
import json

with open(locals()['var_function-call-2156361878744612089'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Fix date
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df[df['Date'] >= '2000-01-01']
df['Price'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Price', 'Date'])

results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    if sub.empty:
        continue
    
    sub['YM'] = sub['Date'].dt.to_period('M')
    investments = sub.groupby('YM').first()
    
    monthly_investment = 100
    total_invested = len(investments) * monthly_investment
    
    units = (monthly_investment / investments['Price']).sum()
    last_price = sub.iloc[-1]['Price']
    final_value = units * last_price
    
    if total_invested > 0:
        roi = (final_value - total_invested) / total_invested * 100
        results.append({'Index': idx, 'Return': roi})

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-244087051243510578': ['index_info'], 'var_function-call-244087051243508825': ['index_trade'], 'var_function-call-700512233624923906': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-700512233624920769': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-17115233311631203296': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-9855506612224461883': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-2156361878744612089': 'file_storage/function-call-2156361878744612089.json', 'var_function-call-14090485196445933031': [{'Index': 'IXIC', 'Return': 382.6943154204}, {'Index': 'NSEI', 'Return': 135.842734458}, {'Index': '399001.SZ', 'Return': 134.7487523496}, {'Index': 'GDAXI', 'Return': 134.7028715908}, {'Index': 'TWII', 'Return': 129.8207618672}]}

exec(code, env_args)
