code = """import json
import pandas as pd
from datetime import datetime

# Load the trade data from file
result_data = var_functions.query_db:12

if isinstance(result_data, str):
    # It's a file path
    with open(result_data, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = result_data

# Create DataFrame
df = pd.DataFrame(trade_data)

# Try to parse dates - handle various formats
def parse_date(date_str):
    if isinstance(date_str, str):
        # Try multiple formats
        try:
            # Format: "31 Dec 1986, 00:00"
            return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
        except:
            try:
                # Format: "January 02, 1987 at 12:00 AM"
                return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
            except:
                try:
                    # Format: "22 Jan 1987, 00:00"
                    return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
                except:
                    try:
                        # Format: "22 Apr 1987, 00:00"
                        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
                    except:
                        # Try pandas auto parser as fallback
                        return pd.to_datetime(date_str, errors='coerce')
    return pd.NaT

# Parse dates
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for 2020 onwards
df_2020 = df[df['Date_parsed'] >= '2020-01-01'].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'].astype(float) - df_2020['Low'].astype(float)) / df_2020['Open'].astype(float)

# Group by Index and calculate average intraday volatility
volatility_by_index = df_2020.groupby('Index')['Intraday_Volatility'].mean().sort_values(ascending=False)

print('__RESULT__:')
print(volatility_by_index.to_json())"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
