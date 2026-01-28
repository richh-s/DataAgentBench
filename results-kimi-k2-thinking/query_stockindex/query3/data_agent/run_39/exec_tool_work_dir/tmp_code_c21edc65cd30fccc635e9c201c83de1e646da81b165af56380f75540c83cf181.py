code = """import json
import pandas as pd
from datetime import datetime

# Access the storage variable - it should be a file path string
file_path = var_functions.query_db_6

# Load the full data from file
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create mapping between index symbols and exchanges/countries
index_mapping = {
    "000001.SS": {"exchange": "Shanghai Stock Exchange", "country": "China", "currency": "CNY"},
    "399001.SZ": {"exchange": "Shenzhen Stock Exchange", "country": "China", "currency": "CNY"},
    "GDAXI": {"exchange": "Frankfurt Stock Exchange", "country": "Germany", "currency": "EUR"},
    "GSPTSE": {"exchange": "Toronto Stock Exchange", "country": "Canada", "currency": "CAD"},
    "HSI": {"exchange": "Hong Kong Stock Exchange", "country": "Hong Kong", "currency": "HKD"},
    "IXIC": {"exchange": "NASDAQ", "country": "USA", "currency": "USD"},
    "J203.JO": {"exchange": "Johannesburg Stock Exchange", "country": "South Africa", "currency": "ZAR"},
    "N100": {"exchange": "Euronext", "country": "EU", "currency": "EUR"},
    "N225": {"exchange": "Tokyo Stock Exchange", "country": "Japan", "currency": "JPY"},
    "NSEI": {"exchange": "National Stock Exchange of India", "country": "India", "currency": "INR"},
    "NYA": {"exchange": "New York Stock Exchange", "country": "USA", "currency": "USD"},
    "SSMI": {"exchange": "SIX Swiss Exchange", "country": "Switzerland", "currency": "CHF"},
    "TWII": {"exchange": "Taiwan Stock Exchange", "country": "Taiwan", "currency": "TWD"}
}

# Add country and index name info to dataframe
df['Country'] = df['Index'].map(lambda x: index_mapping.get(x, {}).get('country', 'Unknown'))

# Sort by Index and Date to ensure chronological order
df = df.sort_values(['Index', 'Date'])

# Group by index and calculate returns for regular monthly investments
results = []

for index_name in df['Index'].unique():
    index_data = df[df['Index'] == index_name].copy()
    
    # Get first and last available dates for this index
    first_date = index_data['Date'].min()
    last_date = index_data['Date'].max()
    
    # Skip if not enough data (less than a year)
    if (last_date - first_date).days < 365:
        continue
    
    # Generate monthly investment dates (first trading day of each month)
    monthly_dates = []
    current_date = first_date.replace(day=1)
    
    while current_date <= last_date:
        # Find the first trading day of the month
        month_start = current_date
        month_end = month_start + pd.DateOffset(months=1)
        
        month_data = index_data[
            (index_data['Date'] >= month_start) & 
            (index_data['Date'] < month_end)
        ]
        
        if not month_data.empty:
            # Use the first trading day of the month
            first_trading_day = month_data.iloc[0]
            monthly_dates.append({
                'Date': first_trading_day['Date'],
                'Price': float(first_trading_day['CloseUSD'])
            })
        
        current_date = month_end
    
    if len(monthly_dates) < 12:  # Need at least 12 months of data
        continue
    
    # Calculate returns for monthly dollar-cost averaging
    total_invested = 0
    total_shares = 0
    
    for investment in monthly_dates:
        total_invested += 100  # Assume $100 invested each month
        total_shares += 100 / investment['Price']
    
    # Calculate final value
    final_price = float(index_data.iloc[-1]['CloseUSD'])
    final_value = total_shares * final_price
    
    # Calculate total return
    total_return = (final_value - total_invested) / total_invested * 100
    
    # Calculate annualized return
    years = len(monthly_dates) / 12
    annualized_return = ((final_value / total_invested) ** (1 / years) - 1) * 100
    
    country = index_mapping.get(index_name, {}).get('country', 'Unknown')
    
    results.append({
        'Index': index_name,
        'Country': country,
        'Total_Return_Pct': round(total_return, 2),
        'Annualized_Return_Pct': round(annualized_return, 2),
        'Investment_Period_Years': round(years, 1),
        'Num_Investments': len(monthly_dates)
    })

# Sort by total return and get top 5
top_5_indices = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5_indices))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
