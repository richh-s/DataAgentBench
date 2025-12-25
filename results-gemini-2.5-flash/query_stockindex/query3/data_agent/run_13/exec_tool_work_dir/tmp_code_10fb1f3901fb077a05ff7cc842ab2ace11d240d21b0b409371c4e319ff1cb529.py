code = """import pandas as pd
import json

# Load the full trade data from the JSON file
with open(locals()['var_function-call-16208021434012948974'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)

# Convert 'Date' to datetime objects, handling mixed formats
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
    except ValueError:
        return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')

df_trade['Date'] = df_trade['Date'].apply(parse_date)

# Filter data from January 1, 2000 onwards
df_trade = df_trade[df_trade['Date'] >= '2000-01-01']

# Convert 'CloseUSD' to numeric
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])

# Get the last trading day of each month for each index
monthly_data = df_trade.loc[df_trade.groupby([df_trade['Index'], df_trade['Date'].dt.to_period('M')])['Date'].idxmax()]

# Calculate monthly returns (percentage change from the start of the month to the end of the month)
monthly_data = monthly_data.sort_values(by=['Index', 'Date'])

# Calculate overall returns with monthly investments
overall_returns = {}
for index_symbol in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index_symbol].copy()
    
    # Calculate initial investment
    initial_investment = index_data['CloseUSD'].iloc[0] if not index_data.empty else 0

    # Calculate the sum of all monthly close prices in USD
    total_invested = index_data['CloseUSD'].sum() if not index_data.empty else 0

    # Calculate the total value assuming monthly investments and appreciation
    if not index_data.empty:
        # Assuming an investment of 1 unit of currency per month, and that it grows with the index
        # The total return is the sum of the last 'CloseUSD' price for each monthly investment unit
        # A simpler way to approximate this is to sum up the growth of each unit of investment.
        # If we invest 1 unit every month, the return is calculated from the perspective of how many 'current' units
        # a constant monthly investment would yield.
        
        # Here we calculate the "total return" as if someone invested the last recorded price in USD
        # for each month they invested. This is a common way to calculate the return of a recurring investment.
        # This simplified approach assumes that monthly investment amount is proportional to the index value.
        
        # Let's consider a simpler approach: calculate the percentage change from the first close to the last close.
        # This isn't exactly "regular monthly investments" but rather the total appreciation if someone bought once.
        # To accurately calculate regular monthly investments, we'd need to simulate the investment.

        # Let's try to simulate regular monthly investments:
        # Assume a fixed amount (e.g., $100) is invested at the close of the first day of each month.
        # This requires finding the *first* close of each month, not the last.

        # Let's re-think the "overall returns" for "regular monthly investments".
        # If an investor made regular monthly investments in all indices since 2000,
        # it means they put a fixed amount of money (e.g., $1) into the index at the end of each month.
        # We need to calculate the final value of all these investments.

        # Get the first trading day of each month for each index
        first_monthly_data = df_trade.loc[df_trade.groupby([df_trade['Index'], df_trade['Date'].dt.to_period('M')])['Date'].idxmin()]
        first_monthly_data = first_monthly_data.sort_values(by=['Index', 'Date'])

        index_first_monthly_data = first_monthly_data[first_monthly_data['Index'] == index_symbol].copy()

        if not index_first_monthly_data.empty:
            # We need the last closing price of the index to calculate the final value of each investment.
            last_close = index_data['CloseUSD'].iloc[-1]
            
            total_invested_amount = 0
            total_current_value = 0

            for i in range(len(index_first_monthly_data)):
                investment_month_start_price = index_first_monthly_data['CloseUSD'].iloc[i]
                
                # Assume a fixed investment amount, e.g., 1 unit of currency (or $1).
                # The number of index shares bought with $1 at that time is 1 / investment_month_start_price
                shares_bought = 1 / investment_month_start_price if investment_month_start_price != 0 else 0
                
                # The current value of these shares is shares_bought * last_close
                total_current_value += shares_bought * last_close
                total_invested_amount += 1 # 1 unit of currency invested each month

            if total_invested_amount > 0:
                overall_returns[index_symbol] = (total_current_value / total_invested_amount) - 1
            else:
                overall_returns[index_symbol] = 0
        else:
            overall_returns[index_symbol] = 0
    else:
        overall_returns[index_symbol] = 0


# Sort indices by overall return
sorted_returns = sorted(overall_returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Now, retrieve country information for these top 5 indices
# We need to map index symbols to exchange names, then to countries.
# This requires querying indexinfo_database.
# We also need to define the mapping between index symbols and exchanges.

# Let's define the mapping based on common knowledge as hinted.
# This is a manual mapping, as no direct join key exists in the databases.
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
