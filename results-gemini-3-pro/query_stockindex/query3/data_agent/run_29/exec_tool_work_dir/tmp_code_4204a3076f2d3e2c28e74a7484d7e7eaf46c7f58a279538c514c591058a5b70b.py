code = """import pandas as pd
import json
import numpy as np

# Load data
with open(locals()['var_function-call-17767560524898677932'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates. Using mixed format since we saw different formats.
# Note: pd.to_datetime with format='mixed' is available in pandas >= 2.0.
# If older, we might need to try different formats or let it infer.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback for older pandas or if mixed fails
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Indices list
indices = df['Index'].unique()
results = []

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date').copy()
    
    if sub.empty:
        continue
        
    # Resample to get the first trading day of each month
    # We set Date as index
    sub.set_index('Date', inplace=True)
    
    # We want to buy on the first available day of each month.
    # We can group by Year-Month and take the first entry.
    monthly_investments = sub.resample('ME').first() # 'ME' is Month End, but .first() takes the first record in the bin?
    # Wait, resample('MS') (Month Start) creates bins. If we take .first(), we get the first data point in that month.
    # If a month has no data, it creates a row with NaNs (which we should drop).
    monthly_investments = sub.resample('MS').first().dropna()
    
    if monthly_investments.empty:
        continue
        
    # Investment strategy: Invest $100 each month
    monthly_investments['Units'] = 100.0 / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units'].sum()
    total_invested = len(monthly_investments) * 100.0
    
    # Final value
    last_price = sub['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    
    # Return (Ratio of Final Value to Total Invested)
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Return_ROI': roi,
        'Return_Multiple': final_value / total_invested
    })

# Convert to DataFrame
res_df = pd.DataFrame(results)
res_df = res_df.sort_values('Return_ROI', ascending=False)

# Top 5
top_5 = res_df.head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-9373037933998248330': ['index_info'], 'var_function-call-9373037933998250959': ['index_trade'], 'var_function-call-12400334992328815541': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-12400334992328817304': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-12400334992328814971': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5973883566672673142': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13230771878049426078': [{'count_star()': '104224'}], 'var_function-call-17767560524898677932': 'file_storage/function-call-17767560524898677932.json'}

exec(code, env_args)
