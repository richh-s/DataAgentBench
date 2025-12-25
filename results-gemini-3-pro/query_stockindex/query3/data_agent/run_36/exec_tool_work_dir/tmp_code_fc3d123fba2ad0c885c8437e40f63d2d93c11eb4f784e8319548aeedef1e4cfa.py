code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-6795954848509195129']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter for data starting 2000
df = df[df['Date'] >= '2000-01-01']

# Group by Index
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    if sub.empty:
        continue
    
    # Check start date
    start_date = sub['Date'].min()
    end_date = sub['Date'].max()
    
    # Resample to get first trading day of each month
    # set index to Date
    sub_indexed = sub.set_index('Date')
    monthly = sub_indexed.resample('MS').first() # Get first day of month
    
    # If using 'first', it gets the value of the first available day in the bin? 
    # Actually resample().first() puts the value at the MS date. 
    # If there is no data in that month, it produces NaN.
    # We should drop NaNs to simulate investing only when market is open (or just skip months with no data)
    monthly = monthly.dropna(subset=['CloseUSD'])
    
    # If monthly data starts significantly later than 2000, it might disqualify "since 2000"
    # Let's verify start dates in the output.
    
    # Simulate Investment
    monthly_investment = 100
    monthly['Units'] = monthly_investment / monthly['CloseUSD']
    total_units = monthly['Units'].sum()
    total_invested = len(monthly) * monthly_investment
    
    # Final Value
    # use the last available price (which might be mid-month if data ends)
    # or better, the price at the last record of the full dataset for this index
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    if total_invested == 0:
        roi = 0
    else:
        roi = (final_value - total_invested) / total_invested
        
    results.append({
        'Index': idx,
        'Start Date': start_date.strftime('%Y-%m-%d'),
        'End Date': end_date.strftime('%Y-%m-%d'),
        'Total Invested': total_invested,
        'Final Value': final_value,
        'ROI': roi,
        'ROI %': roi * 100
    })

results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-14702660799195933244': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-14702660799195933693': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6795954848509195129': 'file_storage/function-call-6795954848509195129.json'}

exec(code, env_args)
