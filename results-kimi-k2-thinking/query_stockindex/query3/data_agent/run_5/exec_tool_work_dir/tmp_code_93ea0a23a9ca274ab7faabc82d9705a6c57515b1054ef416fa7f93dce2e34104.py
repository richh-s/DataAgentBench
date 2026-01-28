code = """import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Get the file path from storage
file_path = locals()['var_functions.query_db:10']

# Load the data
with open(file_path, 'r') as f:
    all_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(all_data)

# Convert data types with error handling
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Parse dates with explicit format to avoid warnings
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for data from 2000 onwards
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Remove rows with missing data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Index to country mapping
index_to_country = {
    '000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany',
    'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'USA',
    'J203.JO': 'South Africa', 'N100': 'Belgium', 'N225': 'Japan',
    'NSEI': 'India', 'NYA': 'USA', 'SSMI': 'Switzerland', 'TWII': 'Taiwan'
}

# Calculate returns for monthly dollar-cost averaging
results = []

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy()
    idx_data = idx_data.sort_values('Date')
    
    if len(idx_data) < 12:  # Need at least a year of data
        continue
    
    start_date = idx_data['Date'].min()
    end_date = idx_data['Date'].max()
    
    # Generate monthly investment dates (first of each month)
    monthly_dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    
    total_invested = 0
    total_shares = 0
    
    # Simulate $100 monthly investment
    for invest_date in monthly_dates:
        # Find the first trading day on or after the investment date
        eligible_trades = idx_data[idx_data['Date'] >= invest_date]
        if not eligible_trades.empty:
            price = eligible_trades.iloc[0]['CloseUSD']
            if price > 0:
                shares = 100 / price
                total_invested += 100
                total_shares += shares
    
    if total_shares > 0 and total_invested > 0:
        final_price = idx_data.iloc[-1]['CloseUSD']
        final_value = total_shares * final_price
        total_return = final_value - total_invested
        return_pct = (total_return / total_invested) * 100
        
        results.append({
            'Index': index,
            'Country': index_to_country.get(index, 'Unknown'),
            'Total_Invested': round(total_invested, 2),
            'Final_Value': round(final_value, 2),
            'Return_Percentage': round(return_pct, 2),
            'Months': len(monthly_dates)
        })

# Sort by return percentage
results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values('Return_Percentage', ascending=False)
    
    # Get top 5
    top_5 = results_df.head(5)
    
    # Prepare output
    output = top_5[['Index', 'Country', 'Return_Percentage']].to_dict('records')
    
    print('__RESULT__:')
    print(json.dumps(output, indent=2))
else:
    print('__RESULT__:')
    print('[]')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min_date': '2000-01-14 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min_date': '2000-01-06 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min_date': '2012-02-08 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min_date': '2000-01-10 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min_date': '2007-09-25 00:00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min_date': '2000-01-03 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min_date': '2000-01-17 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
