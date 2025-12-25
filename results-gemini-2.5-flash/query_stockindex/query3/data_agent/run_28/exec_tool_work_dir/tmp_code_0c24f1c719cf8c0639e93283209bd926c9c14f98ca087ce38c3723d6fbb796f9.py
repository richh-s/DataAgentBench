code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-7326152765868364010'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') # Handle parsing errors
df.dropna(subset=['Date'], inplace=True) # Remove rows with invalid dates
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_first_day_dates = df.groupby(['Index', 'YearMonth'])['Date'].min().reset_index()

# Merge to get the CloseUSD for the first trading day of each month
monthly_data_points = pd.merge(df, monthly_first_day_dates, on=['Index', 'Date'], how='inner')

returns = {}
for index_symbol in monthly_data_points['Index'].unique():
    index_df = monthly_data_points[monthly_data_points['Index'] == index_symbol].sort_values(by='Date').reset_index(drop=True)

    if len(index_df) < 2: # Need at least two data points for a return calculation
        continue

    # Get the latest closing price for this index from the entire dataset
    last_date_for_index = df[df['Index'] == index_symbol]['Date'].max()
    final_close_price = df[(df['Index'] == index_symbol) & (df['Date'] == last_date_for_index)]['CloseUSD'].iloc[0]

    total_units = 0
    investment_amount_per_month = 1 # $1 investment each month
    total_invested_amount = 0

    for _, row in index_df.iterrows():
        if row['CloseUSD'] > 0: # Avoid division by zero
            units_purchased = investment_amount_per_month / row['CloseUSD']
            total_units += units_purchased
            total_invested_amount += investment_amount_per_month
        else:
            # If CloseUSD is 0 or less, we cannot invest, so skip this month's investment for this index.
            pass

    if total_invested_amount > 0:
        total_final_value = total_units * final_close_price
        overall_return = ((total_final_value - total_invested_amount) / total_invested_amount) * 100
        returns[index_symbol] = overall_return
    else:
        returns[index_symbol] = 0 # No investments made, so return is 0

# Sort by return and get the top 5
top_5_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)[:5]

# Map indices to countries
index_country_map = {
    "000001.SS": "China",
    "399001.SZ": "China",
    "HSI": "Hong Kong", # Hong Kong is part of China
    "N225": "Japan",
    "GDAXI": "Germany",
    "DJI": "USA",
    "SPX": "USA",
    "NDAQ": "USA",
    "IXIC": "USA", # NASDAQ Composite
    "TSX": "Canada",
    "NSEI": "India",
    "KOSPI": "South Korea",
    "SIX": "Switzerland",
    "TWII": "Taiwan",
    "J203.JO": "South Africa",
    "FCHI": "France",
    "AS51": "Australia",
    "FTSE": "United Kingdom"
}

result_with_countries = []
for index_symbol, return_value in top_5_indices:
    country = index_country_map.get(index_symbol, "Unknown")
    result_with_countries.append({"Index": index_symbol, "Return": return_value, "Country": country})

print("__RESULT__:")
print(json.dumps(result_with_countries))"""

env_args = {'var_function-call-7326152765868364010': 'file_storage/function-call-7326152765868364010.json', 'var_function-call-3703390097503093797': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15481160904603790552': [{'Index': 'IXIC', 'Return': 382.20467671180944, 'Country': 'Unknown'}, {'Index': 'NSEI', 'Return': 136.0884975512849, 'Country': 'India'}, {'Index': 'GDAXI', 'Return': 134.74623836455376, 'Country': 'Germany'}, {'Index': '399001.SZ', 'Return': 134.4545336356674, 'Country': 'China'}, {'Index': 'TWII', 'Return': 123.74061754244661, 'Country': 'Taiwan'}]}

exec(code, env_args)
