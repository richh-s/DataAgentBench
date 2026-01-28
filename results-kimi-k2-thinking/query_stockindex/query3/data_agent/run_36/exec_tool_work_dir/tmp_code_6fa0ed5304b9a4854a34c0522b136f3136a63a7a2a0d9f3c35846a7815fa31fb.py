code = """import pandas as pd
import json
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load the trade data file
trade_data_file = locals()['var_functions.query_db:8']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert string values to float for price columns
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter data from 2000 onward
df_filtered = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Create a month identifier
df_filtered['Year'] = df_filtered['Date'].dt.year
df_filtered['Month'] = df_filtered['Date'].dt.month
df_filtered['YearMonth'] = df_filtered['Year'] * 100 + df_filtered['Month']

# For each index and month, get the last trading day's CloseUSD
monthly_prices = df_filtered.sort_values(['Index', 'Date']).groupby(['Index', 'YearMonth']).last().reset_index()

# Country mapping
index_to_country = {
    '000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany',
    'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'United States',
    'J203.JO': 'South Africa', 'N100': 'Netherlands', 'N225': 'Japan',
    'NSEI': 'India', 'NYA': 'United States', 'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Simulate monthly dollar-cost averaging for each index
results = []
monthly_investment = 100  # USD

for index in monthly_prices['Index'].unique():
    index_data = monthly_prices[monthly_prices['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    if len(index_data) < 12:  # Need at least 12 months of data
        continue
    
    total_shares = 0
    total_invested = 0
    
    # Invest monthly for all available months
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
    
    # Calculate final portfolio value
    final_price = index_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    
    # Calculate total return
    total_return = (final_value - total_invested) / total_invested
    total_return_pct = total_return * 100
    
    # Get number of years
    start_date = index_data.iloc[0]['Date']
    end_date = index_data.iloc[-1]['Date']
    years = (end_date - start_date).days / 365.25
    
    # Annualized return
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1 / years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'Index': index,
        'Country': index_to_country.get(index, 'Unknown'),
        'Start_Date': start_date.strftime('%Y-%m-%d'),
        'End_Date': end_date.strftime('%Y-%m-%d'),
        'Months': len(index_data),
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return_Pct': total_return_pct,
        'Annualized_Return_Pct': annualized_return
    })

# Convert to DataFrame and sort by Total_Return_Pct
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)

# Get top 5 indices
top_5_indices = results_df.head(5)

print('__RESULT__:')
print(top_5_indices.to_json(orient='records', date_format='iso'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [{'Index': '000001.SS', 'First_Date': '2000-01-04T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1710}, {'Index': '399001.SZ', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-06-02T00:00:00.000', 'Trading_Days': 1758}, {'Index': 'GDAXI', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1833}, {'Index': 'GSPTSE', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-13T00:00:00.000', 'Trading_Days': 1802}, {'Index': 'HSI', 'First_Date': '2000-01-14T00:00:00.000', 'Last_Date': '2021-05-24T00:00:00.000', 'Trading_Days': 1706}, {'Index': 'IXIC', 'First_Date': '2000-01-06T00:00:00.000', 'Last_Date': '2021-05-27T00:00:00.000', 'Trading_Days': 1853}, {'Index': 'J203.JO', 'First_Date': '2012-02-08T00:00:00.000', 'Last_Date': '2021-05-28T00:00:00.000', 'Trading_Days': 764}, {'Index': 'N100', 'First_Date': '2000-01-10T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1786}, {'Index': 'N225', 'First_Date': '2000-01-04T00:00:00.000', 'Last_Date': '2021-06-01T00:00:00.000', 'Trading_Days': 1730}, {'Index': 'NSEI', 'First_Date': '2007-09-25T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1083}, {'Index': 'NYA', 'First_Date': '2000-01-03T00:00:00.000', 'Last_Date': '2021-05-24T00:00:00.000', 'Trading_Days': 1817}, {'Index': 'SSMI', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-21T00:00:00.000', 'Trading_Days': 1746}, {'Index': 'TWII', 'First_Date': '2000-01-17T00:00:00.000', 'Last_Date': '2021-05-26T00:00:00.000', 'Trading_Days': 1754}], 'var_functions.execute_python:16': {'000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'United States', 'J203.JO': 'South Africa', 'N100': 'Netherlands', 'N225': 'Japan', 'NSEI': 'India', 'NYA': 'United States', 'SSMI': 'Switzerland', 'TWII': 'Taiwan'}, 'var_functions.execute_python:20': [{'Index': '000001.SS', 'YearMonth': 200001, 'Date': '2000-01-28T00:00:00.000', 'Open': 1514.557983, 'High': 1536.345947, 'Low': 1510.744995, 'Close': 1534.996948, 'Adj Close': 1534.996948, 'CloseUSD': 245.59951168, 'Year': 2000, 'Month': 1}, {'Index': '000001.SS', 'YearMonth': 200002, 'Date': '2000-02-29T00:00:00.000', 'Open': 1728.135986, 'High': 1733.140991, 'Low': 1678.349976, 'Close': 1714.578003, 'Adj Close': 1714.578003, 'CloseUSD': 274.33248048, 'Year': 2000, 'Month': 2}, {'Index': '000001.SS', 'YearMonth': 200003, 'Date': '2000-03-31T00:00:00.000', 'Open': 1810.552979, 'High': 1810.896973, 'Low': 1780.411011, 'Close': 1800.224976, 'Adj Close': 1800.224976, 'CloseUSD': 288.03599616, 'Year': 2000, 'Month': 3}, {'Index': '000001.SS', 'YearMonth': 200004, 'Date': '2000-04-28T00:00:00.000', 'Open': 1805.503052, 'High': 1836.328979, 'Low': 1797.713013, 'Close': 1836.321045, 'Adj Close': 1836.321045, 'CloseUSD': 293.8113672, 'Year': 2000, 'Month': 4}, {'Index': '000001.SS', 'YearMonth': 200005, 'Date': '2000-05-30T00:00:00.000', 'Open': 1903.530029, 'High': 1908.30603, 'Low': 1868.609985, 'Close': 1877.470947, 'Adj Close': 1877.470947, 'CloseUSD': 300.39535152, 'Year': 2000, 'Month': 5}, {'Index': '000001.SS', 'YearMonth': 200006, 'Date': '2000-06-29T00:00:00.000', 'Open': 1949.847046, 'High': 1951.125977, 'Low': 1924.473022, 'Close': 1937.260986, 'Adj Close': 1937.260986, 'CloseUSD': 309.96175776, 'Year': 2000, 'Month': 6}, {'Index': '000001.SS', 'YearMonth': 200007, 'Date': '2000-07-21T00:00:00.000', 'Open': 1994.422974, 'High': 1998.347046, 'Low': 1991.838013, 'Close': 1996.33606, 'Adj Close': 1996.33606, 'CloseUSD': 319.4137696, 'Year': 2000, 'Month': 7}, {'Index': '000001.SS', 'YearMonth': 200008, 'Date': '2000-08-22T00:00:00.000', 'Open': 2112.01709, 'High': 2114.521973, 'Low': 2074.52002, 'Close': 2074.702881, 'Adj Close': 2074.702881, 'CloseUSD': 331.95246096, 'Year': 2000, 'Month': 8}, {'Index': '000001.SS', 'YearMonth': 200009, 'Date': '2000-09-29T00:00:00.000', 'Open': 1888.20105, 'High': 1910.485962, 'Low': 1888.069946, 'Close': 1910.161011, 'Adj Close': 1910.161011, 'CloseUSD': 305.62576176, 'Year': 2000, 'Month': 9}, {'Index': '000001.SS', 'YearMonth': 200010, 'Date': '2000-10-24T00:00:00.000', 'Open': 1960.365967, 'High': 1962.130005, 'Low': 1945.526978, 'Close': 1956.343994, 'Adj Close': 1956.343994, 'CloseUSD': 313.01503904, 'Year': 2000, 'Month': 10}]}

exec(code, env_args)
