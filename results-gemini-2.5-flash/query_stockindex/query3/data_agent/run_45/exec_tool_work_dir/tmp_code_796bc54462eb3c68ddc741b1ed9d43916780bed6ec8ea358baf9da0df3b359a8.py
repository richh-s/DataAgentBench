code = """import pandas as pd
import json

df_path = locals()['var_function-call-5945128186317195746']
with open(df_path, 'r') as f:
    df = pd.DataFrame(json.load(f))

df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter out any rows where Date conversion failed (NaT)
df.dropna(subset=['Date'], inplace=True)

# Get the last trading day of each month for each index
monthly_close = df.groupby(['Index', pd.Grouper(key='Date', freq='M')])['CloseUSD'].last().reset_index()

returns = {}
for index in monthly_close['Index'].unique():
    index_data = monthly_close[monthly_close['Index'] == index].sort_values(by='Date')
    
    # Ensure there are at least two data points to calculate a return
    if len(index_data) < 2:
        continue

    # Assuming monthly investment of 1 unit
    initial_investment = 1
    total_value = initial_investment

    for i in range(1, len(index_data)):
        current_close = index_data.iloc[i]['CloseUSD']
        previous_close = index_data.iloc[i-1]['CloseUSD']
        
        # Calculate monthly return
        monthly_return = (current_close - previous_close) / previous_close
        
        # Apply the return to the total value, and add another 1 unit for the new monthly investment
        total_value = total_value * (1 + monthly_return) + 1 
    
    returns[index] = total_value - (len(index_data) * initial_investment) # total return considering initial investments

# Sort by returns and get the top 5
top_5_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)[:5]

# Map indices to countries
exchange_info = locals()['var_function-call-11030085911176704423']
exchange_to_country = {
    "New York Stock Exchange": "United States",
    "NASDAQ": "United States",
    "Hong Kong Stock Exchange": "Hong Kong",
    "Shanghai Stock Exchange": "China",
    "Tokyo Stock Exchange": "Japan",
    "Euronext": "Europe (Multiple Countries)", # Euronext operates in multiple European countries
    "Shenzhen Stock Exchange": "China",
    "Toronto Stock Exchange": "Canada",
    "National Stock Exchange of India": "India",
    "Frankfurt Stock Exchange": "Germany",
    "Korea Exchange": "South Korea",
    "SIX Swiss Exchange": "Switzerland",
    "Taiwan Stock Exchange": "Taiwan",
    "Johannesburg Stock Exchange": "South Africa"
}

index_to_exchange = {
    "^GSPC": "New York Stock Exchange", # S&P 500
    "^IXIC": "NASDAQ", # NASDAQ Composite
    "HSI": "Hong Kong Stock Exchange", # Hang Seng Index
    "000001.SS": "Shanghai Stock Exchange", # SSE Composite Index
    "N225": "Tokyo Stock Exchange", # Nikkei 225
    "^STOXX50E": "Euronext", # EURO STOXX 50
    "399001.SZ": "Shenzhen Stock Exchange", # SZSE Component Index
    "^GSPTSE": "Toronto Stock Exchange", # S&P/TSX Composite Index
    "^NSEI": "National Stock Exchange of India", # Nifty 50
    "^GDAXI": "Frankfurt Stock Exchange", # DAX Performance-Index
    "^KS11": "Korea Exchange", # KOSPI Composite Index
    "^SSMI": "SIX Swiss Exchange", # Swiss Market Index
    "^TWII": "Taiwan Stock Exchange", # Taiwan Weighted Index
    "^J203.JO": "Johannesburg Stock Exchange" # FTSE/JSE Top 40
}

result_list = []
for index_symbol, total_return in top_5_indices:
    exchange_name = index_to_exchange.get(index_symbol, "Unknown Exchange")
    country = exchange_to_country.get(exchange_name, "Unknown Country")
    result_list.append({"Index": index_symbol, "Total Return": total_return, "Country": country})

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-5945128186317195746': 'file_storage/function-call-5945128186317195746.json', 'var_function-call-11030085911176704423': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
