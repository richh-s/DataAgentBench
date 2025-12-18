code = """import pandas as pd
import json

# Load the full trade data from the JSON file
with open(locals()['var_function-call-16208021434012948974'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)

# Convert 'Date' to datetime objects, handling mixed formats with 'mixed' format inference
df_trade['Date'] = pd.to_datetime(df_trade['Date'], format='mixed')

# Filter data from January 1, 2000 onwards (already filtered in query, but good to ensure)
df_trade = df_trade[df_trade['Date'] >= '2000-01-01']

# Convert 'CloseUSD' to numeric
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])

# Get the last trading day of each month for each index for investment and last close price
monthly_data = df_trade.loc[df_trade.groupby([df_trade['Index'], df_trade['Date'].dt.to_period('M')])['Date'].idxmax()]
monthly_data = monthly_data.sort_values(by=['Index', 'Date'])

overall_returns = {}
for index_symbol in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index_symbol].copy()

    if not index_data.empty:
        # The last closing price of the index represents the current value for all investments
        last_close = index_data['CloseUSD'].iloc[-1]
            
        total_invested_amount = 0
        total_current_value = 0

        for i in range(len(index_data)):
            investment_month_end_price = index_data['CloseUSD'].iloc[i]
            
            # Assume a fixed investment amount, e.g., 1 unit of currency (or $1), at the end of each month.
            # The number of index shares bought with $1 at that time is 1 / investment_month_end_price
            shares_bought = 1 / investment_month_end_price if investment_month_end_price != 0 else 0
            
            # The current value of these shares is shares_bought * last_close
            total_current_value += shares_bought * last_close
            total_invested_amount += 1 # 1 unit of currency invested each month

        if total_invested_amount > 0:
            overall_returns[index_symbol] = (total_current_value / total_invested_amount) - 1
        else:
            overall_returns[index_symbol] = 0
    else:
        overall_returns[index_symbol] = 0


# Sort indices by overall return
sorted_returns = sorted(overall_returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Define the mapping based on common knowledge as hinted.
index_exchange_mapping = {
    "N225": "Tokyo Stock Exchange",
    "HSI": "Hong Kong Stock Exchange",
    "000001.SS": "Shanghai Stock Exchange",
    "GDAXI": "Xetra", # Deutsche Börse (Xetra)
    "IXIC": "NASDAQ",
    "^DJI": "New York Stock Exchange",
    "^GSPC": "New York Stock Exchange",
    "OSEAX": "Oslo Stock Exchange",
    "OMXSPI": "Nasdaq Stockholm",
    "TSX": "Toronto Stock Exchange",
    "J203.JO": "Johannesburg Stock Exchange",
    "XU100.IS": "Borsa Istanbul",
    "AS51.AX": "Australian Securities Exchange",
    "TWII": "Taiwan Stock Exchange",
    "399001.SZ": "Shenzhen Stock Exchange",
    "STI": "Singapore Exchange",
    "KS11": "Korea Exchange",
    "FCHI": "Euronext Paris",
    "FTSE": "London Stock Exchange",
    "MXX": "Mexican Stock Exchange",
    "BVSP": "B3 (formerly BM&F Bovespa)",
    "RTS.RS": "Moscow Exchange",
    "TA125.TA": "Tel Aviv Stock Exchange",
    "NIFTY": "National Stock Exchange of India",
    "IMOEX.ME": "Moscow Exchange",
    "SSMI": "SIX Swiss Exchange",
    "JKSE": "Indonesia Stock Exchange",
    "SAX": "Saudi Exchange"
}

exchange_country_mapping = {
    "Tokyo Stock Exchange": "Japan",
    "Hong Kong Stock Exchange": "Hong Kong",
    "Shanghai Stock Exchange": "China",
    "Xetra": "Germany",
    "NASDAQ": "United States",
    "New York Stock Exchange": "United States",
    "Oslo Stock Exchange": "Norway",
    "Nasdaq Stockholm": "Sweden",
    "Toronto Stock Exchange": "Canada",
    "Johannesburg Stock Exchange": "South Africa",
    "Borsa Istanbul": "Turkey",
    "Australian Securities Exchange": "Australia",
    "Taiwan Stock Exchange": "Taiwan",
    "Shenzhen Stock Exchange": "China",
    "Singapore Exchange": "Singapore",
    "Korea Exchange": "South Korea",
    "Euronext Paris": "France",
    "London Stock Exchange": "United Kingdom",
    "Mexican Stock Exchange": "Mexico",
    "B3 (formerly BM&F Bovespa)": "Brazil",
    "Moscow Exchange": "Russia",
    "Tel Aviv Stock Exchange": "Israel",
    "National Stock Exchange of India": "India",
    "SIX Swiss Exchange": "Switzerland",
    "Indonesia Stock Exchange": "Indonesia",
    "Saudi Exchange": "Saudi Arabia"
}


results = []
for index_symbol, return_value in top_5_indices:
    exchange = index_exchange_mapping.get(index_symbol, "Unknown Exchange")
    country = exchange_country_mapping.get(exchange, "Unknown Country")
    results.append({
        "Index": index_symbol,
        "Overall_Return": return_value,
        "Country": country
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-13071133573817807683': ['index_info'], 'var_function-call-16208021434012948974': 'file_storage/function-call-16208021434012948974.json'}

exec(code, env_args)
