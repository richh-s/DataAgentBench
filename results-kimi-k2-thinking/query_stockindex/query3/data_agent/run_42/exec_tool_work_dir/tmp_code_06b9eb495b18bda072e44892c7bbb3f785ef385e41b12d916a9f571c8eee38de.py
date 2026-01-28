code = """import json
import pandas as pd
from datetime import datetime

# Load the full data from the file
file_path = eval(locals()['var_functions.query_db:10'])
data = []
with open(file_path, 'r') as f:
    for line in f:
        if line.strip():
            data.extend(json.loads(line))

# Create DataFrame
df = pd.DataFrame(data)
print(f"Total records: {len(df)}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices: {df['Index'].unique()}")

# Convert Date to datetime and CloseUSD to float
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000 onwards
df_2000 = df[(df['Date'] >= '2000-01-01')].copy()
print(f"Records from 2000: {len(df_2000)}")

# Group by month and get last trading day of each month for each index
df_2000['YearMonth'] = df_2000['Date'].dt.to_period('M')

# Get end of month prices
monthly_prices = df_2000.groupby(['Index', 'YearMonth']).agg({
    'CloseUSD': 'last',
    'Date': 'last'
}).reset_index()

print(f"Monthly records: {len(monthly_prices)}")
print(monthly_prices.head(10))

# Create index to exchange/country mapping
index_mapping = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa'},
    'N100': {'exchange': 'Euronext', 'country': 'Netherlands'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA'},
    'SSMI': {'exchange': 'Swiss Exchange', 'country': 'Switzerland'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan'}
}

print("\nIndex mapping created successfully")

result_data = []

# Calculate DCA returns for each index
for index in monthly_prices['Index'].unique():
    index_data = monthly_prices[monthly_prices['Index'] == index].sort_values('Date')
    
    if len(index_data) < 12:  # Need at least 12 months of data
        continue
        
    # Calculate DCA performance
    monthly_investment = 100  # Invest $100 each month
    total_invested = 0
    total_shares = 0
    
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Final value
    final_price = index_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    
    # Total return
    total_return = (final_value - total_invested) / total_invested * 100
    
    # Years of data
    years = (index_data['Date'].max() - index_data['Date'].min()).days / 365.25
    
    # Annualized return (approximation)
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    # Get country info
    country = index_mapping.get(index, {}).get('country', 'Unknown')
    
    result_data.append({
        'Index': index,
        'Country': country,
        'Total_Return_Percent': round(total_return, 2),
        'Annualized_Return_Percent': round(annualized_return, 2),
        'Years_of_Data': round(years, 1),
        'Final_Value': round(final_value, 2),
        'Total_Invested': total_invested
    })

# Create results DataFrame and sort by total return
results_df = pd.DataFrame(result_data)
results_df = results_df.sort_values('Total_Return_Percent', ascending=False)

print(f"\nCalculated returns for {len(results_df)} indices")
print("\nTop 10 indices by total return:")
print(results_df.head(10).to_string(index=False))

# Get top 5
top_5 = results_df.head(5)

print('\n=== TOP 5 INDICES ===')
for _, row in top_5.iterrows():
    print(f"{row['Index']}: {row['Total_Return_Percent']}% ({row['Country']})")

# Save detailed results
results_json = results_df.to_json(orient='records', indent=2)

print('__RESULT__:')
print(results_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
