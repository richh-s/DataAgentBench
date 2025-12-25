code = """import pandas as pd
import json

# Load the full result from the trade data file
with open(locals()['var_function-call-7948131773756513851'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)
df_trade["Date"] = pd.to_datetime(df_trade["Date"], dayfirst=False) # Assuming YYYY-MM-DD format based on preview
df_trade["CloseUSD"] = pd.to_numeric(df_trade["CloseUSD"])

# Filter data from 2000 onwards
df_trade = df_trade[df_trade["Date"].dt.year >= 2000]

# Get the last available closing price for each index
last_close_prices = df_trade.groupby("Index")["CloseUSD"].max() # Use max date for last price, or just max CloseUSD

# Get the first trading day of each month for each index
df_trade['YearMonth'] = df_trade['Date'].dt.to_period('M')
df_monthly_investments = df_trade.sort_values('Date').groupby(['Index', 'YearMonth']).first().reset_index()

returns = {}
for index_symbol in df_monthly_investments["Index"].unique():
    index_monthly_df = df_monthly_investments[df_monthly_investments["Index"] == index_symbol]
    
    if not index_monthly_df.empty and index_symbol in last_close_prices:
        final_close_for_index = last_close_prices[index_symbol]
        
        cumulative_return_values = []
        for _, row in index_monthly_df.iterrows():
            investment_close = row["CloseUSD"]
            if investment_close != 0: # Avoid division by zero
                # Value of a $1 investment made at month 'i' at the end of the period
                value_at_end = final_close_for_index / investment_close
                cumulative_return_values.append(value_at_end)
        
        if cumulative_return_values:
            # The average of these values represents the overall return for each dollar invested, minus 1
            overall_return = (sum(cumulative_return_values) / len(cumulative_return_values)) - 1
            returns[index_symbol] = overall_return
        else:
            returns[index_symbol] = 0.0
    else:
        returns[index_symbol] = 0.0

# Sort indices by returns in descending order
sorted_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)

# Get the top 5 indices
top_5_indices = sorted_indices[:5]

# Define a mapping from index symbol to country (based on general knowledge and hint)
index_to_country = {
    "000001.SS": "China", # Shanghai Stock Exchange
    "HSI": "Hong Kong", # Hong Kong Stock Exchange
    "N225": "Japan", # Tokyo Stock Exchange
    "399001.SZ": "China", # Shenzhen Stock Exchange
    "GDAXI": "Germany", # Frankfurt Stock Exchange
    "IXIC": "United States", # NASDAQ
    "NSEI": "India", # National Stock Exchange of India
    "J203.JO": "South Africa", # Johannesburg Stock Exchange
    "TWII": "Taiwan", # Taiwan Stock Exchange
    "KS11": "South Korea", # Korea Exchange
    "SSMI": "Switzerland", # SIX Swiss Exchange
    "DJI": "United States", # New York Stock Exchange
    "SPX": "United States", # New York Stock Exchange
    "TSX": "Canada", # Toronto Stock Exchange
    "FCHI": "France", # Euronext
    "STOXX50E": "Europe" # Euronext
}

final_result = []
for index, return_val in top_5_indices:
    country = index_to_country.get(index, "Unknown")
    final_result.append({"Index": index, "Overall Return": return_val, "Country": country})

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-7948131773756513851': 'file_storage/function-call-7948131773756513851.json', 'var_function-call-13250496787799692278': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
