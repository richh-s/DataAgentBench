code = """import pandas as pd
import json

# Load data
with open('var_function-call-7351229990786155510', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])
df = df.sort_values(['Index', 'Date'])

results = []

# Map Index to Country
# Based on the list:
# N225 -> Japan
# GSPTSE -> Canada
# NSEI -> India
# GDAXI -> Germany
# IXIC -> USA
# HSI -> Hong Kong
# J203.JO -> South Africa
# NYA -> USA
# 000001.SS -> China
# SSMI -> Switzerland
# TWII -> Taiwan
# N100 -> Europe (Euronext)
# 399001.SZ -> China

country_map = {
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "J203.JO": "South Africa",
    "NYA": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

for idx, group in df.groupby('Index'):
    # Resample to get first trading day of each month
    # We can group by Year-Month and take the first entry
    group = group.set_index('Date')
    monthly_investments = group.resample('MS').first() # This gives the first day of month, but we need the first *trading* day.
    
    # Correct way: Group by Year-Month, take nth(0)
    # create YM column
    group_reset = group.reset_index()
    group_reset['YM'] = group_reset['Date'].dt.to_period('M')
    invest_dates = group_reset.groupby('YM').first()
    
    # Filter for investments starting from 2000-01
    invest_dates = invest_dates[invest_dates['Date'] >= '2000-01-01']
    
    if invest_dates.empty:
        continue
    
    # Simulation
    monthly_amount = 1000 # arbitrary
    total_invested = 0
    total_units = 0
    
    for _, row in invest_dates.iterrows():
        price = row['Adj Close']
        units = monthly_amount / price
        total_units += units
        total_invested += monthly_amount
        
    # Final Value
    last_price = group_reset.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        "Index": idx,
        "Country": country_map.get(idx, "Unknown"),
        "Start Date": invest_dates['Date'].min().strftime('%Y-%m-%d'),
        "Total Invested": total_invested,
        "Final Value": final_value,
        "Overall Return": overall_return
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Overall Return', ascending=False)

print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-15152579714944318513': ['index_info'], 'var_function-call-15152579714944316350': ['index_trade'], 'var_function-call-639504378125954384': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8645442487183065632': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'J203.JO'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-7351229990786155510': 'file_storage/function-call-7351229990786155510.json'}

exec(code, env_args)
