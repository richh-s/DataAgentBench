code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-8190422837704511171'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse dates. explicit format is not possible due to variation. Let pandas guess.
# It might take a moment.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']
df = df.dropna(subset=['Date', 'CloseUSD'])

# Sort by Date
df = df.sort_values('Date')

# Define a function to calculate return
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    if sub.empty:
        continue
    
    # Check start date
    start_date = sub['Date'].iloc[0]
    # If start date is too far from 2000 (e.g. > 2000-02-01), maybe exclude?
    # The prompt says "investments ... since 2000". If index started in 2005, it doesn't fit the "since 2000" description well?
    # However, let's just calculate for whatever data is available in the 2000+ range.
    # But for fair comparison, usually we want the same duration.
    # Let's check start dates in the output to be sure.
    
    # Identify monthly investment dates (first available day of each month)
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    monthly_invest = sub.drop_duplicates('YearMonth', keep='first')
    
    # Invest $1 each month
    # Shares = $1 / Price
    monthly_invest['Shares'] = 1 / monthly_invest['CloseUSD']
    
    total_shares = monthly_invest['Shares'].sum()
    total_invested = len(monthly_invest)
    
    # Current Value
    last_price = sub['CloseUSD'].iloc[-1]
    final_value = total_shares * last_price
    
    # Return
    ret = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Start Date': start_date.strftime('%Y-%m-%d'),
        'End Date': sub['Date'].iloc[-1].strftime('%Y-%m-%d'),
        'Total Invested': total_invested,
        'Final Value': final_value,
        'Return': ret
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(json.dumps(results_df.to_dict(orient='records')))"""

env_args = {'var_function-call-11201131661863914384': ['index_info'], 'var_function-call-11201131661863913437': ['index_trade'], 'var_function-call-1313105551519661517': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-1313105551519660470': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-16619267845454007713': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16619267845454004500': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-7503413296308662144': [{'count_star()': '104224'}], 'var_function-call-8190422837704511171': 'file_storage/function-call-8190422837704511171.json'}

exec(code, env_args)
