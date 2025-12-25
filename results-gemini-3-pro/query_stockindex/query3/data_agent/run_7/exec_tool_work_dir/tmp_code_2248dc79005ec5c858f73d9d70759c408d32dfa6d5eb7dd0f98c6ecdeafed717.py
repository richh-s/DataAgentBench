code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-5773205835372737063'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# explicit format to avoid ambiguity or warning
# The preview showed "2000-01-04 00:00:00"
# We can try to converting to string first just in case
df['Date'] = df['Date'].astype(str)
# We use errors='coerce' to handle potential bad data, though DuckDB usually returns valid dates.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Drop invalid dates
df = df.dropna(subset=['Date'])

df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Define mapping
index_country_map = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China',
    'NYA': 'United States'
}

results = []

for index_name, group in df.groupby('Index'):
    group = group.sort_values('Date')
    
    # Create Month column
    group['Month'] = group['Date'].dt.to_period('M')
    
    # Get first trading day of each month available in the data
    monthly_investment_dates = group.groupby('Month')['Date'].min()
    
    total_shares = 0
    total_invested = 0
    monthly_amount = 100.0
    
    for month, date in monthly_investment_dates.items():
        price_row = group[group['Date'] == date]
        if not price_row.empty:
            price = price_row.iloc[0]['Adj Close']
            if price > 0: # Avoid division by zero
                shares = monthly_amount / price
                total_shares += shares
                total_invested += monthly_amount
            
    if total_invested > 0:
        last_price = group.iloc[-1]['Adj Close']
        final_value = total_shares * last_price
        pct_return = (final_value - total_invested) / total_invested * 100
        
        results.append({
            'Index': index_name,
            'Country': index_country_map.get(index_name, 'Unknown'),
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'Return_Pct': pct_return
        })

results_df = pd.DataFrame(results).sort_values('Return_Pct', ascending=False)
top_5 = results_df.head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-10021783300953503103': ['index_info'], 'var_function-call-11595194589530822852': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6069480066467942252': ['index_trade'], 'var_function-call-3250475692665861912': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-14715549604581522807': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5773205835372737063': 'file_storage/function-call-5773205835372737063.json'}

exec(code, env_args)
