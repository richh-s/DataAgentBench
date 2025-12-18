code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-7948131773756513851'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)
df_trade["Date"] = pd.to_datetime(df_trade["Date"])
df_trade["CloseUSD"] = pd.to_numeric(df_trade["CloseUSD"])

# Get the last available closing price for each index
last_close_prices = df_trade.groupby("Index")["CloseUSD"].last()

# Filter to get only the data from the first trading day of each month
# Create a column for year and month
df_trade['YearMonth'] = df_trade['Date'].dt.to_period('M')

# Get the first date for each YearMonth and Index
df_monthly_investments = df_trade.sort_values('Date').groupby(['Index', 'YearMonth']).first().reset_index()

returns = {}
for index_symbol in df_monthly_investments["Index"].unique():
    index_monthly_df = df_monthly_investments[df_monthly_investments["Index"] == index_symbol]
    
    if not index_monthly_df.empty and index_symbol in last_close_prices:
        final_close = last_close_prices[index_symbol]
        
        cumulative_return_values = []
        for _, row in index_monthly_df.iterrows():
            investment_close = row["CloseUSD"]
            if investment_close != 0: # Avoid division by zero
                value_at_end = final_close / investment_close
                cumulative_return_values.append(value_at_end)
        
        if cumulative_return_values:
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

# Define a mapping from index symbol to country
index_to_country = {
    "000001.SS": "China",
    "HSI": "Hong Kong",
    "N225": "Japan",
    "399001.SZ": "China",
    "GDAXI": "Germany",
    "IXIC": "United States",
    "NSEI": "India",
    "J203.JO": "South Africa",
    "TWII": "Taiwan",
    "KS11": "South Korea",
    "SSMI": "Switzerland",
    "DJI": "United States",
    "SPX": "United States",
    "TSX": "Canada",
    "FCHI": "France",
    "STOXX50E": "Europe" 
}

final_result = []
for index, return_val in top_5_indices:
    country = index_to_country.get(index, "Unknown")
    final_result.append({"Index": index, "Overall Return": return_val, "Country": country})

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-7948131773756513851': 'file_storage/function-call-7948131773756513851.json', 'var_function-call-13250496787799692278': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
