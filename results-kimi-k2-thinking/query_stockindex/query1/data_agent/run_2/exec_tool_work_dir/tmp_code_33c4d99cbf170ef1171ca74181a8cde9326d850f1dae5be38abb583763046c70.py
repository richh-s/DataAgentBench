code = """import json
import pandas as pd
import os

# Check available variables with var_ prefix
available_vars = [var for var in locals().keys() if var.startswith('var_')]
print('Available variables:', available_vars)

# The query result was stored in a file - the path should be in var_functions.query_db:10
# Let's access it using the proper storage key name
# Note: variable names with special characters need to be accessed via locals()
storage_key = 'var_functions.query_db:10'
if storage_key in locals():
    file_path = locals()[storage_key]
    print('File path found:', file_path)
    
    # Read the data from the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f'Total records loaded: {len(data)}')
    
    if len(data) > 0:
        print('First record sample:', data[0])
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        print('DataFrame shape:', df.shape)
        print('Indices in data:', df['Index'].unique() if 'Index' in df.columns else 'No Index column')
        
        # Check data types
        print('Data types:', df.dtypes.head() if not df.empty else 'Empty dataframe')
        
        # Convert numeric columns
        numeric_cols = ['Open', 'High', 'Low', 'Close']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Calculate intraday volatility
        df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']
        
        # Group by index and calculate average volatility
        avg_volatility = df.groupby('Index')['Intraday_Volatility'].mean().reset_index()
        avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)
        
        print('\nAll indices average volatility:')
        print(avg_volatility)
        
        # Filter for Asian indices
        asian_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']
        asian_volatility = avg_volatility[avg_volatility['Index'].isin(asian_indices)]
        
        print('\nAsian indices average volatility:')
        print(asian_volatility)
        
        # Get the highest
        if not asian_volatility.empty:
            highest = asian_volatility.iloc[0]
            result = {
                'index': highest['Index'],
                'avg_volatility': float(highest['Intraday_Volatility']),
                'all_asian': asian_volatility.to_dict('records')
            }
        else:
            result = {'error': 'No Asian indices found in data'}
    else:
        result = {'error': 'No data loaded'}
else:
    print('File path not found in storage')
    result = {'error': 'File not found'}

# Print in required format
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
