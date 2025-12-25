code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-16922781104202852561']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# We try to convert to datetime. Since formats are mixed, we let pandas guess.
# Coerce errors to NaT to handle unparseable dates, then drop them.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD', 'Date'])

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Add YearMonth to identify months
df['YearMonth'] = df['Date'].dt.to_period('M')

# For monthly investment, we take the first available trading day of each month
monthly_data = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Simulation
results = []
indices = monthly_data['Index'].unique()

for idx in indices:
    idx_df = monthly_data[monthly_data['Index'] == idx].sort_values('Date')
    
    # Check if data exists
    if len(idx_df) == 0:
        continue
        
    # Assume investment of $100 per month
    monthly_investment = 100
    
    # Calculate units bought each month
    # units = investment / price
    idx_df['Units'] = monthly_investment / idx_df['CloseUSD']
    
    total_units = idx_df['Units'].sum()
    total_invested = len(idx_df) * monthly_investment
    
    # Final value = total units * last available price in the dataset (not necessarily last month)
    # We should use the last available price in the original daily dataframe to be accurate, 
    # but using the last monthly price is a good approximation. 
    # Let's use the last price from the filtered daily dataframe for that index.
    last_price = df[df['Index'] == idx].iloc[-1]['CloseUSD']
    
    final_value = total_units * last_price
    
    pct_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': pct_return,
        'TotalInvested': total_invested,
        'FinalValue': final_value
    })

# Sort by Return descending
results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

# Mapping
country_map = {
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe', 
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'J203.JO': 'South Africa'
}

results_df['Country'] = results_df['Index'].map(country_map)

# Get top 5
top_5 = results_df.head(5)

print("__RESULT__:")
print(top_5[['Index', 'Country', 'Return']].to_json(orient='records'))"""

env_args = {'var_function-call-4525215006901702855': ['index_info'], 'var_function-call-4525215006901702758': ['index_trade'], 'var_function-call-1383220658992783069': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-1383220658992780406': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-11667858090032048248': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-11667858090032047147': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8172338423216481950': [{'count_star()': '104224'}], 'var_function-call-16922781104202852561': 'file_storage/function-call-16922781104202852561.json'}

exec(code, env_args)
