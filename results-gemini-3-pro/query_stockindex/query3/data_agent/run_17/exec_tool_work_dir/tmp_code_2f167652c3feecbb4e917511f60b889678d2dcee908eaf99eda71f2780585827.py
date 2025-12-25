code = """import pandas as pd
import json

# Load data
trade_data_path = locals()['var_function-call-15961951031335421892']
with open(trade_data_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert CloseUSD to float
# Some might be None or empty?
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows where CloseUSD is NaN
df = df.dropna(subset=['CloseUSD'])

# Parse Date
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True, errors='coerce')

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']
df = df.sort_values(['Index', 'Date'])

# Check unique indices
indices = df['Index'].unique()
results = []

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    if sub.empty:
        continue
    
    # Resample to monthly. We want to invest once a month.
    # We'll take the first record of each month.
    # Create a YearMonth column
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    
    # Group by YearMonth and take the first entry
    monthly_invest = sub.groupby('YearMonth').first().reset_index()
    
    # Investment calculation
    # Invest $1 each month
    monthly_invest['Units'] = 1.0 / monthly_invest['CloseUSD']
    total_units = monthly_invest['Units'].sum()
    total_invested = len(monthly_invest)
    
    # Final value
    # Get the very last available price for this index
    final_price = sub.iloc[-1]['CloseUSD']
    final_value = total_units * final_price
    
    roi = (final_value - total_invested) / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'FinalValue': final_value,
        'TotalInvested': total_invested
    })

results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)
top_5 = results_df.head(5)

print("__RESULT__:")
print(json.dumps(top_5.to_dict(orient='records')))"""

env_args = {'var_function-call-10802789048753933568': ['index_info'], 'var_function-call-10802789048753933413': ['index_trade'], 'var_function-call-10717884044383904817': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-10717884044383906968': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-1263844451791534859': [{'count_star()': '104224'}], 'var_function-call-15961951031335421892': 'file_storage/function-call-15961951031335421892.json', 'var_function-call-15961951031335422909': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
