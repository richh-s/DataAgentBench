code = """import json
import pandas as pd
from datetime import datetime

# Load the query result from file
file_path = locals()['var_functions.query_db:24']

if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = file_path

# Create DataFrame
df = pd.DataFrame(data)

# Convert string values to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Handle date conversion - the format varies, so let's try different approaches
def parse_date(date_str):
    if isinstance(date_str, datetime):
        return date_str
    
    if isinstance(date_str, str):
        # Remove "at" if present
        date_str = date_str.replace(' at ', ' ')
        
        # Try various formats
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%d %b %Y, %H:%M',
            '%d %B %Y at %I:%M %p',
            '%d %b %Y',  # e.g., "01 Apr 2003"
            '%B %d, %Y at %I:%M %p'  # e.g., "September 30, 2015 at 12:00 AM"
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue
    
    return None

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for dates from 2020 onwards
df_2020 = df[df['Date_parsed'] >= datetime(2020, 1, 1)].copy()

# Calculate intraday volatility for each day
df_2020['intraday_volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average intraday volatility per index
volatility_stats = df_2020.groupby('Index')['intraday_volatility'].agg([
    'mean', 'count', 'std', 'min', 'max'
]).round(4)

# Sort by mean volatility descending
volatility_stats_sorted = volatility_stats.sort_values('mean', ascending=False)

print("__RESULT__:")
print(volatility_stats_sorted.to_json())"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:5': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:10': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:11': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.execute_python:14': {'Tokyo Stock Exchange': 'N225', 'Hong Kong Stock Exchange': 'HSI', 'Shanghai Stock Exchange': '000001.SS', 'Shenzhen Stock Exchange': '399001.SZ', 'National Stock Exchange of India': 'NSEI', 'Taiwan Stock Exchange': 'TWII'}, 'var_functions.query_db:16': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:20': [{'Index': 'HSI', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049'}, {'Index': 'HSI', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098'}, {'Index': 'HSI', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098'}, {'Index': 'HSI', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098'}, {'Index': 'HSI', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5'}, {'Index': 'HSI', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902'}, {'Index': 'HSI', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902'}, {'Index': 'HSI', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902'}, {'Index': 'HSI', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902'}, {'Index': 'HSI', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0'}, {'Index': 'HSI', 'Open': '2553.300049', 'High': '2553.300049', 'Low': '2553.300049'}, {'Index': 'HSI', 'Open': '2636.600098', 'High': '2636.600098', 'Low': '2636.600098'}, {'Index': 'HSI', 'Open': '2672.399902', 'High': '2672.399902', 'Low': '2672.399902'}, {'Index': 'HSI', 'Open': '2740.5', 'High': '2740.5', 'Low': '2740.5'}, {'Index': 'HSI', 'Open': '2792.100098', 'High': '2792.100098', 'Low': '2792.100098'}, {'Index': 'HSI', 'Open': '2801.5', 'High': '2801.5', 'Low': '2801.5'}, {'Index': 'HSI', 'Open': '2879.0', 'High': '2879.0', 'Low': '2879.0'}, {'Index': 'HSI', 'Open': '2848.199951', 'High': '2848.199951', 'Low': '2848.199951'}, {'Index': 'HSI', 'Open': '2873.600098', 'High': '2873.600098', 'Low': '2873.600098'}, {'Index': 'HSI', 'Open': '2843.600098', 'High': '2843.600098', 'Low': '2843.600098'}], 'var_functions.query_db:22': [{'Index': 'N225', 'Date': '2020-01-07 00:00:00', 'Open': '23320.11914', 'High': '23577.43945', 'Low': '23299.91992'}, {'Index': 'N225', 'Date': '2020-01-22 00:00:00', 'Open': '23835.49023', 'High': '24040.86914', 'Low': '23831.09961'}, {'Index': 'N225', 'Date': '2020-01-28 00:00:00', 'Open': '23126.92969', 'High': '23243.35938', 'Low': '23115.15039'}, {'Index': 'N225', 'Date': '2020-01-29 00:00:00', 'Open': '23309.32031', 'High': '23392.60938', 'Low': '23214.2793'}, {'Index': 'N225', 'Date': '2020-01-30 00:00:00', 'Open': '23284.58008', 'High': '23318.57031', 'Low': '22892.94922'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_records': 20187, 'index_symbols': ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII'], 'columns': ['Index', 'Date', 'Open', 'High', 'Low']}}

exec(code, env_args)
