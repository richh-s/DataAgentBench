code = """import pandas as pd
import json

# Load the full data from the file for trade data
with open(locals()['var_function-call-7933476089365491817'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)
# Attempt to parse dates with format='mixed' and dayfirst=False
df_trade['Date'] = pd.to_datetime(df_trade['Date'], format='mixed', dayfirst=False)
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])

# Filter for data since 2000
df_trade = df_trade[df_trade['Date'] >= '2000-01-01']

# Get the first trading day of each month for each index
df_trade['YearMonth'] = df_trade['Date'].dt.to_period('M')
monthly_prices = df_trade.loc[df_trade.groupby(['Index', 'YearMonth'])['Date'].idxmin()]

# Calculate returns for each index
returns = {}
for index_name, group in monthly_prices.groupby('Index'):
    group = group.sort_values(by='Date')

    if len(group) < 2:
        continue

    total_invested = 0
    total_shares = 0

    for i in range(len(group)):
        investment = 1  # Assume $1 invested each month
        price = group.iloc[i]['CloseUSD']
        shares_bought = investment / price

        total_invested += investment
        total_shares += shares_bought

    final_value = total_shares * group.iloc[-1]['CloseUSD']

    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0

    returns[index_name] = overall_return

# Sort indices by overall return in descending order and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Load index_info data
index_info_data = locals()['var_function-call-7223997520362831221']
df_index_info = pd.DataFrame(index_info_data)

# Create a mapping from Exchange to Country
exchange_to_country = {
    "New York Stock Exchange": "United States",
    "NASDAQ": "United States",
    "Hong Kong Stock Exchange": "Hong Kong",
    "Shanghai Stock Exchange": "China",
    "Tokyo Stock Exchange": "Japan",
    "Euronext": "Europe (multiple countries)", # Euronext operates across several European countries
    "Shenzhen Stock Exchange": "China",
    "Toronto Stock Exchange": "Canada",
    "National Stock Exchange of India": "India",
    "Frankfurt Stock Exchange": "Germany",
    "Korea Exchange": "South Korea",
    "SIX Swiss Exchange": "Switzerland",
    "Taiwan Stock Exchange": "Taiwan",
    "Johannesburg Stock Exchange": "South Africa"
}

# Create a mapping from Index symbol to Exchange and then to Country
# This requires manual mapping based on common knowledge as it's not directly in the DB
index_to_exchange = {
    "000001.SS": "Shanghai Stock Exchange", # SSE Composite Index
    "399001.SZ": "Shenzhen Stock Exchange", # SZSE Component Index
    "DJI": "New York Stock Exchange", # Dow Jones Industrial Average
    "GSPTSE": "Toronto Stock Exchange", # S&P/TSX Composite Index
    "HSI": "Hong Kong Stock Exchange", # Hang Seng Index
    "IXIC": "NASDAQ", # NASDAQ Composite
    "N225": "Tokyo Stock Exchange", # Nikkei 225
    "NSEI": "National Stock Exchange of India", # NIFTY 50
    "SSMI": "SIX Swiss Exchange", # Swiss Market Index
    "TWII": "Taiwan Stock Exchange", # TAIEX
    "J203.JO": "Johannesburg Stock Exchange", # FTSE/JSE Top 40
    "STOXX50E": "Euronext", # EURO STOXX 50
    "DAX": "Frankfurt Stock Exchange", # DAX Performance-Index
    "KOSPI": "Korea Exchange" # KOSPI Composite Index
}

results_with_countries = []
for index_symbol, overall_return in top_5_indices:
    exchange = index_to_exchange.get(index_symbol, "Unknown Exchange")
    country = exchange_to_country.get(exchange, "Unknown Country")
    results_with_countries.append({"Index": index_symbol, "Overall Return": overall_return, "Country": country})

print("__RESULT__:")
print(json.dumps(results_with_countries))"""

env_args = {'var_function-call-7933476089365491817': 'file_storage/function-call-7933476089365491817.json', 'var_function-call-7223997520362831221': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
