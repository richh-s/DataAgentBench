code = """import json
import pandas as pd
from datetime import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:10']

# Read the data from the file
data = []
with open(file_path, 'r') as f:
    for line in f:
        if line.strip():
            try:
                records = json.loads(line.strip())
                if isinstance(records, list):
                    data.extend(records)
                else:
                    data.append(records)
            except:
                continue

print(f"Loaded {len(data)} records")

# Create DataFrame
df = pd.DataFrame(data)
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Sample data:")
print(df.head(3))

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000 onwards
df_2000 = df[(df['Date'] >= '2000-01-01') & (df['Date'].notna())].copy()
print(f"Records from 2000 onwards: {len(df_2000)}")

# Create year-month for monthly grouping
df_2000['YearMonth'] = df_2000['Date'].dt.to_period('M')

# Get monthly closing prices (last trading day of each month)
monthly_prices = df_2000.groupby(['Index', 'YearMonth']).agg({
    'CloseUSD': 'last',
    'Date': 'last'
}).reset_index()

print(f"Monthly price records: {len(monthly_prices)}")
print(f"Indices found: {monthly_prices['Index'].unique()}")

# Map indices to countries (based on common index symbols)
index_to_country = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'USA',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'USA',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Calculate Dollar Cost Averaging (DCA) returns for each index
results = []

for index in monthly_prices['Index'].unique():
    index_data = monthly_prices[monthly_prices['Index'] == index].sort_values('Date')
    
    if len(index_data) < 24:  # Need at least 2 years of data
        print(f"Skipping {index}: only {len(index_data)} months of data")
        continue
    
    # DCA simulation: $100 invested at the end of each month
    monthly_investment = 100.0
    total_invested = 0.0
    total_shares = 0.0
    
    valid_months = 0
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
            valid_months += 1
    
    if valid_months < 24:  # Need at least 2 years of valid data
        print(f"Skipping {index}: only {valid_months} valid months")
        continue
    
    # Calculate final value
    final_price = index_data.iloc[-1]['CloseUSD']
    if pd.notna(final_price) and final_price > 0:
        final_value = total_shares * final_price
        
        # Calculate returns
        total_return_pct = ((final_value - total_invested) / total_invested) * 100
        
        # Calculate time period in years
        start_date = index_data['Date'].min()
        end_date = index_data['Date'].max()
        years = (end_date - start_date).days / 365.25
        
        # Annualized return
        if years > 0 and total_invested > 0:
            annualized_return = ((final_value / total_invested) ** (1.0 / years) - 1.0) * 100
        else:
            annualized_return = 0
        
        # Get country
        country = index_to_country.get(index, 'Unknown')
        
        results.append({
            'Index': index,
            'Country': country,
            'Total_Return_Percent': round(total_return_pct, 2),
            'Annualized_Return_Percent': round(annualized_return, 2),
            'Years': round(years, 1),
            'Months_Invested': valid_months,
            'Final_Value': round(final_value, 2),
            'Total_Invested': round(total_invested, 2)
        })
        
        print(f"{index}: {total_return_pct:.2f}% return over {years:.1f} years")

# Sort by total return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Percent', ascending=False)

print(f"\nSuccessfully calculated returns for {len(results_df)} indices")
print("\nTop 10 indices by total return:")
print(results_df.head(10).to_string(index=False))

# Get top 5
top_5 = results_df.head(5).copy()

print('\n=== TOP 5 INDICES FOR DCA SINCE 2000 ===')
for _, row in top_5.iterrows():
    print(f"{row['Index']}: {row['Total_Return_Percent']}% total return ({row['Country']})")

# Prepare final result
final_result = results_df.to_dict('records')
result_json = json.dumps(final_result, indent=2)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
