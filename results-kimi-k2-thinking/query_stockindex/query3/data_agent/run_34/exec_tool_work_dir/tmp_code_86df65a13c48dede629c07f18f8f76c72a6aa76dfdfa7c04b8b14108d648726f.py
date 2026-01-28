code = """import json
import pandas as pd
from datetime import datetime
import numpy as np

# Read the file path from storage
file_path_key = 'var_functions.query_db:10'
file_path = locals()[file_path_key]

# Read the full result from the file
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Parse dates - handle different date formats
def parse_date(date_str):
    try:
        # Try ISO format first
        return pd.to_datetime(date_str)
    except:
        try:
            # Try common formats
            return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
        except:
            return pd.to_datetime(date_str, infer_datetime_format=True, errors='coerce')

df['Date'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date'])
df['Date'] = df['Date'].dt.date
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Group by index and sort by date
df = df.sort_values(['Index', 'Date'])

# Create mapping for exchanges to indices based on the hint and common knowledge
exchange_to_index = {
    'New York Stock Exchange': 'NYA',
    'NASDAQ': 'IXIC',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Tokyo Stock Exchange': 'N225',
    'Euronext': 'N100',
    'Shenzhen Stock Exchange': '399001.SZ',
    'Toronto Stock Exchange': 'GSPTSE',
    'National Stock Exchange of India': 'NSEI',
    'Frankfurt Stock Exchange': 'GDAXI',
    'SIX Swiss Exchange': 'SSMI',
    'Taiwan Stock Exchange': 'TWII',
    'Johannesburg Stock Exchange': 'J203.JO'
}

# Get available indices in our data
available_indices = df['Index'].unique()

# Filter mapping to only include available data
valid_exchange_mapping = {}
index_to_exchange = {}
for exchange, index_symbol in exchange_to_index.items():
    if index_symbol in available_indices:
        valid_exchange_mapping[exchange] = index_symbol
        index_to_exchange[index_symbol] = exchange

# Calculate returns from regular monthly investments (dollar cost averaging)
# Starting from January 2000, invest $100 at the beginning of each month
results = {}

for index_symbol in index_to_exchange.keys():
    # Get data for this index
    idx_data = df[df['Index'] == index_symbol].copy()
    
    if idx_data.empty:
        continue
    
    # Set date as index for easier resampling
    idx_data['Date'] = pd.to_datetime(idx_data['Date'])
    idx_data = idx_data.set_index('Date')
    
    # Get monthly prices (first trading day of each month)
    monthly_prices = idx_data['CloseUSD'].resample('MS').first()
    
    # Filter from January 2000 onwards
    start_date = pd.Timestamp('2000-01-01')
    monthly_prices = monthly_prices[monthly_prices.index >= start_date]
    
    if monthly_prices.empty:
        continue
    
    # Calculate DCA returns
    monthly_investment = 100  # $100 per month
    total_invested = 0
    total_shares = 0
    
    for date, price in monthly_prices.items():
        if not np.isnan(price):
            total_invested += monthly_investment
            total_shares += monthly_investment / price
    
    # Calculate final value
    if len(idx_data) > 0:
        final_price = idx_data['CloseUSD'].iloc[-1]
        final_value = total_shares * final_price
        total_return = (final_value - total_invested) / total_invested * 100
        
        results[index_symbol] = {
            'total_return_pct': total_return,
            'total_invested': total_invested,
            'final_value': final_value,
            'gain': final_value - total_invested
        }

# Sort results by total return
sorted_results = sorted(results.items(), key=lambda x: x[1]['total_return_pct'], reverse=True)

# Store top 5 for final answer
top_5 = sorted_results[:5]

# Map indices to countries
exchange_to_country = {
    'New York Stock Exchange': 'United States',
    'NASDAQ': 'United States',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Shanghai Stock Exchange': 'China',
    'Tokyo Stock Exchange': 'Japan',
    'Euronext': 'Europe (Netherlands)',
    'Shenzhen Stock Exchange': 'China',
    'Toronto Stock Exchange': 'Canada',
    'National Stock Exchange of India': 'India',
    'Frankfurt Stock Exchange': 'Germany',
    'SIX Swiss Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan',
    'Johannesburg Stock Exchange': 'South Africa'
}

final_data = []
for index_symbol, data in top_5:
    exchange_name = index_to_exchange.get(index_symbol, 'Unknown')
    country = exchange_to_country.get(exchange_name, 'Unknown')
    final_data.append({
        'index': index_symbol,
        'exchange': exchange_name,
        'country': country,
        'total_return_pct': float(data['total_return_pct'])
    })

result_json = json.dumps(final_data, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': '20 Jan 1987, 00:00', 'Open': '2449.899902', 'High': '2449.899902', 'Low': '2449.899902', 'Close': '2449.899902', 'Adj Close': '2449.899902', 'CloseUSD': '318.48698726000003'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM', 'Open': '2553.300049', 'High': '2553.300049', 'Low': '2553.300049', 'Close': '2553.300049', 'Adj Close': '2553.300049', 'CloseUSD': '331.92900637'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
