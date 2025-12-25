code = """import json
import pandas as pd

# Load data
file_path = locals()['var_function-call-6375617379289947384']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Date using a flexible approach
# The sample showed "2000-01-04 00:00:00", which is ISO-like.
try:
    df['Date'] = pd.to_datetime(df['Date'])
except:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

results = []

for index_name, group in df.groupby('Index'):
    group = group.sort_values('Date')
    
    # Identify first trading day of each month
    # Create a YearMonth column
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # Drop duplicates on YearMonth, keeping the first occurrence
    investment_days = group.drop_duplicates(subset=['YearMonth'], keep='first')
    
    total_invested = 0
    total_units = 0
    investment_amount = 100 
    
    # Vectorized calculation for speed and simplicity
    prices = investment_days['CloseUSD'].values
    units = investment_amount / prices
    total_units = units.sum()
    total_invested = len(units) * investment_amount
            
    # Final value
    last_price = group.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': index_name,
        'Return': overall_return
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-110759798618603580': ['index_info'], 'var_function-call-110759798618606141': ['index_trade'], 'var_function-call-1888189874408097317': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3993405376474384505': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-8702784125424971527': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-4714428077862934541': [{'count_star()': '67948'}], 'var_function-call-6375617379289947384': 'file_storage/function-call-6375617379289947384.json'}

exec(code, env_args)
