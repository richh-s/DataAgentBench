code = """import json
import pandas as pd

# Read data
index_info = locals()['var_functions.query_db:5']

# Read full price data
price_data_file = "file_storage/functions.query_db:8.json"
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(price_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get first and last price for each index since 2000
df_2000 = df[df['Date'] >= '2000-01-01']

# Group by index to get first and last prices
returns = []
for index in df_2000['Index'].unique():
    index_data = df_2000[df_2000['Index'] == index].sort_values('Date')
    if len(index_data) > 1:
        first_price = index_data.iloc[0]['CloseUSD']
        last_price = index_data.iloc[-1]['CloseUSD']
        first_date = index_data.iloc[0]['Date']
        last_date = index_data.iloc[-1]['Date']
        
        total_return = (last_price - first_price) / first_price
        years = (last_date - first_date).days / 365.25
        annualized_return = (1 + total_return) ** (1/years) - 1 if years > 0 else 0
        
        returns.append({
            'Index': index,
            'FirstPrice': first_price,
            'LastPrice': last_price,
            'TotalReturn': total_return,
            'AnnualizedReturn': annualized_return,
            'StartDate': first_date.strftime('%Y-%m-%d'),
            'EndDate': last_date.strftime('%Y-%m-%d'),
            'Years': years
        })

returns_df = pd.DataFrame(returns)
returns_df = returns_df.sort_values('TotalReturn', ascending=False)

# Exchange to index mapping
exchange_to_index = {
    "Tokyo Stock Exchange": "N225",
    "Hong Kong Stock Exchange": "HSI", 
    "New York Stock Exchange": "NYA",
    "NASDAQ": "IXIC",
    "Shanghai Stock Exchange": "000001.SS",
    "Shenzhen Stock Exchange": "399001.SZ",
    "Frankfurt Stock Exchange": "GDAXI",
    "Toronto Stock Exchange": "GSPTSE",
    "National Stock Exchange of India": "NSEI",
    "Euronext": "N100",
    "Johannesburg Stock Exchange": "J203.JO",
    "SWX Swiss Exchange": "SSMI",
    "Taiwan Stock Exchange": "TWII"
}

# Country mapping
index_to_country = {}
for exchange, currency in index_info:
    index_symbol = exchange_to_index.get(exchange, None)
    if index_symbol:
        if "Tokyo" in exchange:
            index_to_country[index_symbol] = "Japan"
        elif "Hong Kong" in exchange:
            index_to_country[index_symbol] = "Hong Kong (China)"
        elif "New York" in exchange or "NASDAQ" in exchange:
            index_to_country[index_symbol] = "United States"
        elif "Shanghai" in exchange or "Shenzhen" in exchange:
            index_to_country[index_symbol] = "China"
        elif "Frankfurt" in exchange:
            index_to_country[index_symbol] = "Germany"
        elif "Toronto" in exchange:
            index_to_country[index_symbol] = "Canada"
        elif "India" in exchange:
            index_to_country[index_symbol] = "India"
        elif "Johannesburg" in exchange:
            index_to_country[index_symbol] = "South Africa"
        elif "Swiss" in exchange:
            index_to_country[index_symbol] = "Switzerland"
        elif "Taiwan" in exchange:
            index_to_country[index_symbol] = "Taiwan"
        elif "Euronext" in exchange:
            index_to_country[index_symbol] = "Multi-country (Europe)"

print("__RESULT__:")
print(json.dumps({
    "top_indices": returns_df.head(10).to_dict('records'),
    "country_mapping": index_to_country,
    "total_indices": len(returns_df)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'index_info_count': 10, 'price_data_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.execute_python:14': {'price_records_count': 67948, 'mapped_exchanges': 10, 'exchange_sample': [['Tokyo Stock Exchange', 'N225'], ['Hong Kong Stock Exchange', 'HSI'], ['New York Stock Exchange', 'NYA']]}}

exec(code, env_args)
