code = """import pandas as pd
import json
import os

# Retrieve the query result variable; it may be a path string due to large size.
# The stored variable name likely uses underscore instead of colon.
var_names = [k for k in locals().keys() if 'query_db' in k]
# For safety, locate the variable containing the data or path.
# The result may be a list (if small) or a string path.
path_or_data = None
for vn in var_names:
    val = locals()[vn]
    if isinstance(val, str) and os.path.isfile(val):
        path_or_data = val
        break
    elif isinstance(val, list):
        path_or_data = val
        break

if path_or_data is None:
    result = {'error': 'No data found'}
else:
    if isinstance(path_or_data, str):
        with open(path_or_data, 'r') as f:
            records = json.load(f)
    else:
        records = path_or_data

    # Create DataFrame
    df = pd.DataFrame(records)
    # Convert numeric columns
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    # Parse dates using pandas to_datetime (flexible)
    df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
    # Filter from 2020 onward
    start_date = pd.Timestamp('2020-01-01')
    df_filtered = df[df['Date_parsed'] >= start_date].copy()
    # Compute intraday volatility: (High - Low) / Open
    df_filtered['Intraday_Vol'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']
    # Average per index
    avg_vol = df_filtered.groupby('Index')['Intraday_Vol'].mean().reset_index()
    # Find the index with highest average intraday volatility
    if avg_vol.empty:
        result = {'error': 'No data after 2020 filtering'}
    else:
        max_row = avg_vol.loc[avg_vol['Intraday_Vol'].idxmax()]
        result = {
            'Index': max_row['Index'],
            'AvgIntradayVolatility': max_row['Intraday_Vol']
        }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:10': [{'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_functions.query_db:12': [{'Index': 'N225', 'Date': '1965-01-05 00:00:00', 'Open': '1257.719971', 'High': '1257.719971', 'Low': '1257.719971'}, {'Index': 'N225', 'Date': 'January 06, 1965 at 12:00 AM', 'Open': '1263.98999', 'High': '1263.98999', 'Low': '1263.98999'}, {'Index': 'N225', 'Date': '07 Jan 1965, 00:00', 'Open': '1274.27002', 'High': '1274.27002', 'Low': '1274.27002'}, {'Index': 'N225', 'Date': '1965-01-08 00:00:00', 'Open': '1286.430054', 'High': '1286.430054', 'Low': '1286.430054'}, {'Index': 'N225', 'Date': '1965-01-12 00:00:00', 'Open': '1288.540039', 'High': '1288.540039', 'Low': '1288.540039'}], 'var_functions.query_db:14': [{'Index': '000001.SS', 'Date': '01 Apr 2020, 00:00', 'Open': '2743.541016', 'High': '2773.364014', 'Low': '2731.079102', 'Close': '2734.521973', 'Adj Close': '2734.521973', 'CloseUSD': '437.52351568'}, {'Index': '000001.SS', 'Date': '01 Apr 2021, 00:00', 'Open': '3444.810059', 'High': '3470.030029', 'Low': '3438.830078', 'Close': '3466.330078', 'Adj Close': '3466.330078', 'CloseUSD': '554.61281248'}, {'Index': '000001.SS', 'Date': '01 Jun 2020, 00:00', 'Open': '2871.964111', 'High': '2917.150879', 'Low': '2871.964111', 'Close': '2915.430908', 'Adj Close': '2915.430908', 'CloseUSD': '466.46894528'}, {'Index': '000001.SS', 'Date': '01 Sep 2020, 00:00', 'Open': '3389.741943', 'High': '3410.606934', 'Low': '3381.710938', 'Close': '3410.606934', 'Adj Close': '3410.606934', 'CloseUSD': '545.69710944'}, {'Index': '000001.SS', 'Date': '02 Mar 2021, 00:00', 'Open': '3566.852051', 'High': '3566.852051', 'Low': '3485.364014', 'Close': '3508.591064', 'Adj Close': '3508.591064', 'CloseUSD': '561.37457024'}, {'Index': '000001.SS', 'Date': '03 Dec 2020, 00:00', 'Open': '3448.540039', 'High': '3452.160889', 'Low': '3428.803955', 'Close': '3442.135986', 'Adj Close': '3442.135986', 'CloseUSD': '550.7417577599999'}, {'Index': '000001.SS', 'Date': '03 Jan 2020, 00:00', 'Open': '3089.021973', 'High': '3093.819092', 'Low': '3074.518066', 'Close': '3083.785889', 'Adj Close': '3083.785889', 'CloseUSD': '493.40574224000005'}, {'Index': '000001.SS', 'Date': '03 Jul 2020, 00:00', 'Open': '3103.995117', 'High': '3152.812988', 'Low': '3103.995117', 'Close': '3152.812988', 'Adj Close': '3152.812988', 'CloseUSD': '504.45007808'}, {'Index': '000001.SS', 'Date': '03 Nov 2020, 00:00', 'Open': '3239.805908', 'High': '3278.381104', 'Low': '3237.854004', 'Close': '3271.073975', 'Adj Close': '3271.073975', 'CloseUSD': '523.371836'}, {'Index': '000001.SS', 'Date': '04 Feb 2020, 00:00', 'Open': '2685.269043', 'High': '2786.164063', 'Low': '2685.269043', 'Close': '2783.288086', 'Adj Close': '2783.288086', 'CloseUSD': '445.32609376'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
