code = """import json
import pandas as pd
import numpy as np

# Load the data
file_path = locals().get('var_functions.query_db:11')
if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = file_path or []

df_trade = pd.DataFrame(trade_data)

# Filter for the Shenzhen index (399001.SZ) which had highest volatility
df_shenzhen = df_trade[df_trade['Index'] == '399001.SZ'].copy()

# Convert data types
df_shenzhen['Open'] = pd.to_numeric(df_shenzhen['Open'], errors='coerce')
df_shenzhen['High'] = pd.to_numeric(df_shenzhen['High'], errors='coerce')
df_shenzhen['Low'] = pd.to_numeric(df_shenzhen['Low'], errors='coerce')

# Calculate intraday volatility for each day
df_shenzhen['intraday_volatility'] = (df_shenzhen['High'] - df_shenzhen['Low']) / df_shenzhen['Open']

# Get summary statistics
summary_stats = {
    'count': len(df_shenzhen),
    'avg_volatility': df_shenzhen['intraday_volatility'].mean(),
    'median_volatility': df_shenzhen['intraday_volatility'].median(),
    'max_volatility': df_shenzhen['intraday_volatility'].max(),
    'min_volatility': df_shenzhen['intraday_volatility'].min(),
    'std_volatility': df_shenzhen['intraday_volatility'].std()
}

# Check for outliers (volatility > 0.5 which would be 50% intraday swing)
outliers = df_shenzhen[df_shenzhen['intraday_volatility'] > 0.5]

print('__RESULT__:')
print(json.dumps({
    'summary_stats': summary_stats,
    'outliers_count': len(outliers),
    'outliers_sample': outliers.head().to_dict('records') if len(outliers) > 0 else []
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:5': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM', 'Open': '2553.300049', 'High': '2553.300049', 'Low': '2553.300049', 'Close': '2553.300049', 'Adj Close': '2553.300049', 'CloseUSD': '331.92900637'}, {'Index': 'HSI', 'Date': 'February 04, 1987 at 12:00 AM', 'Open': '2636.600098', 'High': '2636.600098', 'Low': '2636.600098', 'Close': '2636.600098', 'Adj Close': '2636.600098', 'CloseUSD': '342.75801274'}, {'Index': 'HSI', 'Date': 'February 05, 1987 at 12:00 AM', 'Open': '2672.399902', 'High': '2672.399902', 'Low': '2672.399902', 'Close': '2672.399902', 'Adj Close': '2672.399902', 'CloseUSD': '347.41198726000005'}, {'Index': 'HSI', 'Date': 'February 13, 1987 at 12:00 AM', 'Open': '2740.5', 'High': '2740.5', 'Low': '2740.5', 'Close': '2740.5', 'Adj Close': '2740.5', 'CloseUSD': '356.265'}, {'Index': 'HSI', 'Date': 'February 17, 1987 at 12:00 AM', 'Open': '2792.100098', 'High': '2792.100098', 'Low': '2792.100098', 'Close': '2792.100098', 'Adj Close': '2792.100098', 'CloseUSD': '362.97301274'}, {'Index': 'HSI', 'Date': 'February 18, 1987 at 12:00 AM', 'Open': '2801.5', 'High': '2801.5', 'Low': '2801.5', 'Close': '2801.5', 'Adj Close': '2801.5', 'CloseUSD': '364.195'}, {'Index': 'HSI', 'Date': 'February 23, 1987 at 12:00 AM', 'Open': '2879.0', 'High': '2879.0', 'Low': '2879.0', 'Close': '2879.0', 'Adj Close': '2879.0', 'CloseUSD': '374.27'}, {'Index': 'HSI', 'Date': '24 Feb 1987, 00:00', 'Open': '2848.199951', 'High': '2848.199951', 'Low': '2848.199951', 'Close': '2848.199951', 'Adj Close': '2848.199951', 'CloseUSD': '370.26599363'}, {'Index': 'HSI', 'Date': 'February 25, 1987 at 12:00 AM', 'Open': '2873.600098', 'High': '2873.600098', 'Low': '2873.600098', 'Close': '2873.600098', 'Adj Close': '2873.600098', 'CloseUSD': '373.56801274'}, {'Index': 'HSI', 'Date': '26 Feb 1987, 00:00', 'Open': '2843.600098', 'High': '2843.600098', 'Low': '2843.600098', 'Close': '2843.600098', 'Adj Close': '2843.600098', 'CloseUSD': '369.66801274'}], 'var_functions.query_db:10': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'info_rows': 14, 'trade_rows': 20187, 'info_columns': ['Exchange', 'Currency'], 'trade_columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'info_sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'trade_sample': [{'Index': '000001.SS', 'Date': '2020-01-08 00:00:00', 'Open': '3094.239014', 'High': '3094.239014', 'Low': '3059.131104', 'Close': '3066.893066'}, {'Index': '000001.SS', 'Date': '2020-01-10 00:00:00', 'Open': '3102.293945', 'High': '3105.225098', 'Low': '3081.395996', 'Close': '3092.291016'}, {'Index': '000001.SS', 'Date': '2020-01-15 00:00:00', 'Open': '3103.169922', 'High': '3107.939941', 'Low': '3082.040039', 'Close': '3090.040039'}, {'Index': '000001.SS', 'Date': '2020-02-03 00:00:00', 'Open': '2716.697998', 'High': '2766.576904', 'Low': '2716.697998', 'Close': '2746.605957'}, {'Index': '000001.SS', 'Date': '2020-02-05 00:00:00', 'Open': '2792.371094', 'High': '2842.74292', 'Low': '2778.864014', 'Close': '2818.087891'}], 'unique_indices': ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']}, 'var_functions.execute_python:14': [{'Index': '399001.SZ', 'intraday_volatility': 0.020202435308195838, 'trading_days': 2719}, {'Index': '000001.SS', 'intraday_volatility': 0.017311424071026715, 'trading_days': 2752}, {'Index': 'NSEI', 'intraday_volatility': 0.01585173971531031, 'trading_days': 1610}, {'Index': 'HSI', 'intraday_volatility': 0.013823046802453519, 'trading_days': 4006}, {'Index': 'TWII', 'intraday_volatility': 0.013488352260842065, 'trading_days': 2751}, {'Index': 'N225', 'intraday_volatility': 0.008720764073041308, 'trading_days': 6349}]}

exec(code, env_args)
