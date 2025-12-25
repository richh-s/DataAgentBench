code = """import pandas as pd
import json
import os

# Read the file
file_path = locals()['var_function-call-4108580030395729040']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date
# Using coerce to handle errors, but hoping most are fine.
# We will use dateutil parser logic via pandas inference
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter for data >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Drop rows with invalid CloseUSD or Date
df = df.dropna(subset=['Date', 'CloseUSD'])

# Monthly Resampling (first trading day of each month)
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_investments = df.sort_values('Date').groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate Returns
results = []
for idx, group in monthly_investments.groupby('Index'):
    # Check if we have enough data (at least starts near 2000)
    # The query asks "investments since 2000". If an index started in 2010, the return might be skewed or not comparable.
    # However, usually we just calculate based on available data in that period or punish late starts.
    # The query implies "in all indices since 2000". This might imply only indices that existed in 2000.
    # Let's check the start date for each index in the filtered data.
    # If the first date is far from 2000-01, maybe we should note it.
    # But DCA return is typically calculated over the period the investment was made.
    # If I invest from 2010 to 2024, the return is for that period.
    # But to compare "highest overall returns" since 2000, usually we require the index to be present since 2000.
    # Let's check start dates.
    
    start_date = group['Date'].min()
    # Let's proceed with calculation and I'll inspect the start dates in the output or intermediate step if needed.
    # But typically, if an index didn't exist, one couldn't invest "since 2000".
    # I will calculate for all and perhaps filtering those that start too late might be a refinement.
    # For now, I'll calculate normally.
    
    # Strategy: Invest $1 every month.
    group = group.sort_values('Date')
    
    # Units purchased
    prices = group['CloseUSD'].values
    units = 1.0 / prices
    total_units = units.sum()
    
    # Final Value
    final_price = prices[-1]
    portfolio_value = total_units * final_price
    
    total_invested = len(prices) # $1 * number of months
    
    # Return percentage
    if total_invested > 0:
        total_return = (portfolio_value - total_invested) / total_invested
    else:
        total_return = 0
        
    results.append({
        'Index': idx,
        'Return': total_return,
        'Start Date': str(start_date.date()),
        'End Date': str(group['Date'].max().date()),
        'Months': int(total_invested)
    })

results_df = pd.DataFrame(results)

# Sort by Return
top_indices = results_df.sort_values('Return', ascending=False)

# Mapping to Countries
mapping = {
    "NYA": "United States",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "000001.SS": "China",
    "N225": "Japan",
    "N100": "Europe", 
    "399001.SZ": "China",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "J203.JO": "South Africa"
}

top_indices['Country'] = top_indices['Index'].map(mapping)

print("__RESULT__:")
print(top_indices.to_json(orient='records'))"""

env_args = {'var_function-call-18032259852556152909': ['index_info'], 'var_function-call-18032259852556153692': ['index_trade'], 'var_function-call-15765637751705706839': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-15765637751705708758': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-18275306101637283611': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Close': '2460.5', 'CloseUSD': '319.865'}], 'var_function-call-4108580030395729040': 'file_storage/function-call-4108580030395729040.json'}

exec(code, env_args)
