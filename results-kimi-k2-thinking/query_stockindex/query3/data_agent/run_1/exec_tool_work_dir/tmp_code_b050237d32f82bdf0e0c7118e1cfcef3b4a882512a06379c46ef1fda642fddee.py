code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Get the data using locals() to access the variable with colon in name
data_key = 'var_functions.query_db:10'
price_data_file = locals()[data_key]

# Read the price data from the file
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
if not price_data:
    result = {'error': 'No price data available'}
else:
    df = pd.DataFrame(price_data)
    
    # Parse dates using pandas
    df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Remove rows with failed date parsing
    df_clean = df.dropna(subset=['Date_parsed']).copy()
    
    if len(df_clean) == 0:
        result = {'error': 'No valid dates parsed'}
    else:
        # Convert CloseUSD to numeric
        df_clean['CloseUSD'] = pd.to_numeric(df_clean['CloseUSD'], errors='coerce')
        
        # Filter for data from 2000 onwards
        df_clean = df_clean[df_clean['Date_parsed'] >= pd.Timestamp('2000-01-01')]
        
        # Create year-month period for grouping
        df_clean['YearMonth'] = df_clean['Date_parsed'].dt.to_period('M')
        
        # Get the last trading day of each month for each index
        monthly_prices = []
        for (idx, ym), group in df_clean.groupby(['Index', 'YearMonth']):
            # Get the row with the latest date in the group
            latest_idx = group['Date_parsed'].idxmax()
            latest_row = group.loc[latest_idx]
            monthly_prices.append({
                'Index': str(idx),
                'YearMonth': str(ym),
                'Date': latest_row['Date_parsed'].strftime('%Y-%m-%d'),
                'CloseUSD': float(latest_row['CloseUSD']) if pd.notna(latest_row['CloseUSD']) else None
            })
        
        df_monthly = pd.DataFrame(monthly_prices)
        
        # Calculate statistics
        num_indices = df_monthly['Index'].nunique()
        total_records = len(df_monthly)
        
        if total_records > 0:
            all_dates = pd.to_datetime(df_monthly['Date'])
            date_range = f"{all_dates.min().strftime('%Y-%m-%d')} to {all_dates.max().strftime('%Y-%m-%d')}"
        else:
            date_range = "No data"
        
        indices_list = sorted([str(x) for x in df_monthly['Index'].dropna().unique().tolist()])
        
        result = {
            'num_indices': int(num_indices),
            'total_months': int(total_records),
            'date_range': date_range,
            'indices': indices_list
        }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
