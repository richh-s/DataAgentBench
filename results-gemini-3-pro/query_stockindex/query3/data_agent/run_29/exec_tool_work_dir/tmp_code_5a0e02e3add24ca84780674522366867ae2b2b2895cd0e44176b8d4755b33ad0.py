code = """import pandas as pd
import json

# Reload data
with open(locals()['var_function-call-17767560524898677932'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Process
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

df = df[df['Date'] >= '2000-01-01']
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

indices = df['Index'].unique()
results = []

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date').copy()
    if sub.empty: continue
    
    sub.set_index('Date', inplace=True)
    monthly_investments = sub.resample('MS').first().dropna()
    
    if monthly_investments.empty: continue
    
    monthly_investments['Units'] = 100.0 / monthly_investments['CloseUSD']
    total_units = monthly_investments['Units'].sum()
    total_invested = len(monthly_investments) * 100.0
    last_price = sub['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'Profit': final_value - total_invested,
        'Total_Invested': total_invested,
        'Final_Value': final_value
    })

res_df = pd.DataFrame(results)

# Sort by ROI
print("Sorted by ROI:")
print(res_df.sort_values('ROI', ascending=False)[['Index', 'ROI', 'Profit', 'Final_Value']].to_json(orient='records'))

# Sort by Profit
print("Sorted by Profit:")
print(res_df.sort_values('Profit', ascending=False)[['Index', 'ROI', 'Profit', 'Final_Value']].to_json(orient='records'))"""

env_args = {'var_function-call-9373037933998248330': ['index_info'], 'var_function-call-9373037933998250959': ['index_trade'], 'var_function-call-12400334992328815541': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-12400334992328817304': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-12400334992328814971': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5973883566672673142': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13230771878049426078': [{'count_star()': '104224'}], 'var_function-call-17767560524898677932': 'file_storage/function-call-17767560524898677932.json', 'var_function-call-3745416912847956730': [{'Index': 'IXIC', 'Total_Invested': 25700.0, 'Final_Value': 124052.4390630478, 'Return_ROI': 3.8269431542, 'Return_Multiple': 4.8269431542}, {'Index': 'NSEI', 'Total_Invested': 16500.0, 'Final_Value': 38914.0511855678, 'Return_ROI': 1.3584273446, 'Return_Multiple': 2.3584273446}, {'Index': '399001.SZ', 'Total_Invested': 25800.0, 'Final_Value': 60564.5627346235, 'Return_ROI': 1.3474636719, 'Return_Multiple': 2.3474636719}, {'Index': 'GDAXI', 'Total_Invested': 25700.0, 'Final_Value': 60318.6379988427, 'Return_ROI': 1.3470287159, 'Return_Multiple': 2.3470287159}, {'Index': 'TWII', 'Total_Invested': 25700.0, 'Final_Value': 59063.7481172075, 'Return_ROI': 1.2982003158, 'Return_Multiple': 2.2982003158}]}

exec(code, env_args)
