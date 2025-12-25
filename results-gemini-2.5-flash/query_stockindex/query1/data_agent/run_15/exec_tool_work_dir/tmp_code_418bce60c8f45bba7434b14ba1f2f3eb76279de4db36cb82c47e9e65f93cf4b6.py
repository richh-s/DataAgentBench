code = """import pandas as pd
import json

# Load the index_info data
index_info_data = json.loads(locals()['var_function-call-3003213005305761994']['results'])
index_info_df = pd.DataFrame(index_info_data)

# Define Asian exchanges and their corresponding index symbols based on the hint and previous observation.
# The query for index_trade already filtered these indices, so we just need to confirm the region logic for index_info.
asian_indices_map = {
    "Hong Kong Stock Exchange": "HSI",
    "Shanghai Stock Exchange": "000001.SS",
    "Tokyo Stock Exchange": "N225",
    "Shenzhen Stock Exchange": "399001.SZ",
    "National Stock Exchange of India": "NSEI",
    "Korea Exchange": "KOSPI",
    "Taiwan Stock Exchange": "TWII"
}

asian_exchanges_df = index_info_df[index_info_df['Exchange'].isin(asian_indices_map.keys())]
asian_exchanges_df['Index'] = asian_exchanges_df['Exchange'].map({v: k for k, v in asian_indices_map.items()})

# Load the index_trade data
with open(locals()['var_function-call-16393888339412451216'], 'r') as f:
    index_trade_data = json.load(f)
index_trade_df = pd.DataFrame(index_trade_data)

# Convert relevant columns to numeric
index_trade_df['Open'] = pd.to_numeric(index_trade_df['Open'])
index_trade_df['High'] = pd.to_numeric(index_trade_df['High'])
index_trade_df['Low'] = pd.to_numeric(index_trade_df['Low'])

# Calculate intraday volatility
index_trade_df['Intraday_Volatility'] = (index_trade_df['High'] - index_trade_df['Low']) / index_trade_df['Open']

# Calculate average intraday volatility for each index
avg_intraday_volatility = index_trade_df.groupby('Index')['Intraday_Volatility'].mean().reset_index()

# Find the index with the highest average intraday volatility
highest_volatility_index = avg_intraday_volatility.loc[avg_intraday_volatility['Intraday_Volatility'].idxmax()]

result = highest_volatility_index.to_json()

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-3003213005305761994': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-16393888339412451216': 'file_storage/function-call-16393888339412451216.json'}

exec(code, env_args)
