code = """import json
import pandas as pd
from datetime import datetime
import numpy as np

# Get the data from storage
storage_key = 'var_functions.query_db:18'
file_path = locals()[storage_key]

# Read the full result from the file if it's a file path
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = file_path

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates and prices
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter data from 2000 onwards and drop any null values
df = df[df['Date'] >= '2000-01-01'].dropna()

# Create mapping of indices to their countries
index_mapping = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China', 'name': 'Shanghai Composite'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China', 'name': 'Shenzhen Component'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany', 'name': 'DAX'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada', 'name': 'S&P/TSX Composite'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong', 'name': 'Hang Seng Index'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA', 'name': 'NASDAQ Composite'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa', 'name': 'FTSE/JSE All Share'},
    'N100': {'exchange': 'Euronext', 'country': 'Europe', 'name': 'Euronext 100'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan', 'name': 'Nikkei 225'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India', 'name': 'NIFTY 50'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA', 'name': 'NYSE Composite'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland', 'name': 'Swiss Market Index'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan', 'name': 'TAIEX'}
}

# Function to simulate dollar cost averaging (DCA)
def simulate_dca(group, monthly_investment=100):
    """
    Simulate monthly dollar cost averaging
    """
    if group.empty:
        return 0, 0, 0, []
    
    # Sort by date
    group = group.sort_values('Date')
    
    # Generate monthly dates from start to end
    start_date = group['Date'].min()
    end_date = group['Date'].max()
    
    # Create monthly investment schedule (first trading day of each month)
    current_date = start_date
    investment_dates = []
    
    while current_date <= end_date:
        # Find the closest trading day to the first of the month
        month_end = current_date + pd.offsets.MonthEnd(1)
        month_data = group[(group['Date'] >= current_date) & (group['Date'] <= month_end)]
        
        if not month_data.empty:
            investment_dates.append(month_data.iloc[0]['Date'])
        
        current_date = current_date + pd.offsets.MonthBegin(1)
    
    if not investment_dates:
        return 0, 0, 0, []
    
    # Simulate DCA
    total_invested = 0
    units_held = 0
    portfolio_values = []
    
    for invest_date in investment_dates:
        # Find the closing price on investment date
        price_data = group[group['Date'] == invest_date]
        if price_data.empty:
            continue
            
        price = price_data.iloc[0]['CloseUSD']
        
        # Invest fixed amount
        total_invested += monthly_investment
        units_bought = monthly_investment / price
        units_held += units_bought
        
        # Calculate current portfolio value
        current_price = group[group['Date'] <= invest_date]['CloseUSD'].iloc[-1]
        portfolio_value = units_held * current_price
        portfolio_values.append({
            'date': invest_date,
            'invested': total_invested,
            'value': portfolio_value
        })
    
    # Final portfolio value
    final_price = group.iloc[-1]['CloseUSD']
    final_value = units_held * final_price
    
    # Calculate total return
    total_return = final_value - total_invested
    total_return_percentage = (total_return / total_invested * 100) if total_invested > 0 else 0
    
    return total_invested, total_return_percentage, final_value, portfolio_values

# Run DCA simulation for each index
results = []

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy()
    
    # Skip if there's insufficient data (less than 1 year)
    if index_data['Date'].max() - index_data['Date'].min() < pd.Timedelta(days=365):
        continue
    
    invested, return_pct, final_value, _ = simulate_dca(index_data)
    
    if invested > 0:
        mapping = index_mapping.get(index, {})
        results.append({
            'index_symbol': index,
            'index_name': mapping.get('name', index),
            'country': mapping.get('country', 'Unknown'),
            'total_invested': invested,
            'final_portfolio_value': final_value,
            'total_return_percentage': return_pct
        })

# Sort by total return percentage
top_indices = sorted(results, key=lambda x: x['total_return_percentage'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_indices, default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_records': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5869'}], 'var_functions.execute_python:12': {'status': 'mapping_created'}, 'var_functions.query_db:14': [{'Index': 'GDAXI', 'Date': '01 Apr 1992, 00:00', 'CloseUSD': '2082.1617280200003'}, {'Index': 'GDAXI', 'Date': '01 Apr 1993, 00:00', 'CloseUSD': '2037.44884758'}, {'Index': 'GDAXI', 'Date': '01 Apr 1997, 00:00', 'CloseUSD': '4003.38115242'}, {'Index': 'GDAXI', 'Date': '01 Apr 2005, 00:00', 'CloseUSD': '5335.7063377'}, {'Index': 'GDAXI', 'Date': '01 Apr 2008, 00:00', 'CloseUSD': '8198.80269516'}, {'Index': 'GDAXI', 'Date': '01 Apr 2011, 00:00', 'CloseUSD': '8759.36827198'}, {'Index': 'GDAXI', 'Date': '01 Apr 2015, 00:00', 'CloseUSD': '14641.6834536'}, {'Index': 'GDAXI', 'Date': '01 Apr 2019, 00:00', 'CloseUSD': '14252.0280806'}, {'Index': 'GDAXI', 'Date': '01 Apr 2020, 00:00', 'CloseUSD': '11644.595'}, {'Index': 'GDAXI', 'Date': '01 Aug 1988, 00:00', 'CloseUSD': '1452.61745368'}, {'Index': 'GDAXI', 'Date': '01 Aug 1995, 00:00', 'CloseUSD': '2697.7372122'}, {'Index': 'GDAXI', 'Date': '01 Aug 2001, 00:00', 'CloseUSD': '7118.9805756'}, {'Index': 'GDAXI', 'Date': '01 Aug 2006, 00:00', 'CloseUSD': '6828.023085479999'}, {'Index': 'GDAXI', 'Date': '01 Aug 2008, 00:00', 'CloseUSD': '7803.681152419999'}, {'Index': 'GDAXI', 'Date': '01 Aug 2013, 00:00', 'CloseUSD': '10261.09117218'}, {'Index': 'GDAXI', 'Date': '01 Aug 2016, 00:00', 'CloseUSD': '12603.2338266'}, {'Index': 'GDAXI', 'Date': '01 Dec 1992, 00:00', 'CloseUSD': '1887.12033412'}, {'Index': 'GDAXI', 'Date': '01 Dec 1997, 00:00', 'CloseUSD': '5033.62230484'}, {'Index': 'GDAXI', 'Date': '01 Dec 2003, 00:00', 'CloseUSD': '4661.86394022'}, {'Index': 'GDAXI', 'Date': '01 Dec 2004, 00:00', 'CloseUSD': '5106.9563377'}], 'var_functions.query_db:16': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'records_loaded': 21342, 'indices': 13}}

exec(code, env_args)
