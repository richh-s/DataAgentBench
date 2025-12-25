code = """import pandas as pd
import json
import io

df_trade = pd.read_json(locals()['var_function-call-15735413083344890865'])

df_info_list = locals()['var_function-call-15933026684059475808']
df_info = pd.read_json(io.StringIO(json.dumps(df_info_list)))

df_trade['Date'] = pd.to_datetime(df_trade['Date'], errors='coerce')
df_trade = df_trade.dropna(subset=['Date', 'CloseUSD'])
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])
df_trade = df_trade[df_trade['Date'].dt.year >= 2000]

# Sort by Index and Date to easily get the first day of each month
df_trade = df_trade.sort_values(by=['Index', 'Date'])

# Get the first trading day of each month for each index
df_trade['year_month'] = df_trade['Date'].dt.to_period('M')
monthly_data = df_trade.groupby(['Index', 'year_month']).first().reset_index()

# Calculate the return for each index
returns = {}
for index_symbol in monthly_data['Index'].unique():
    index_df = monthly_data[monthly_data['Index'] == index_symbol].copy()
    if len(index_df) > 0:
        total_invested = len(index_df)
        total_value = index_df['CloseUSD'].sum()
        overall_return = (total_value - total_invested) / total_invested
        returns[index_symbol] = overall_return

# Sort by return and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices_returns = sorted_returns[:5]

# Map indices to countries
index_to_country = {
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China',
    'N225': 'Japan',
    '^GSPC': 'USA',
    '399001.SZ': 'China',
    '^DJI': 'USA',
    '^IXIC': 'USA',
    'GDAXI': 'Germany',
    'TSX': 'Canada',
    'KOSPI': 'South Korea',
    '^TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    '^FCHI': 'France',
    '^BSESN': 'India',
    'GSPTSE': 'Canada', # S&P/TSX Composite Index
    'NYA': 'USA', # NYSE Composite Index
    'IXIC': 'USA', # NASDAQ Composite Index (Corrected from previous to match ^IXIC where ^ might be missing)
    'SSMI': 'Switzerland', # Swiss Market Index
}

final_result = []
for index, ret in top_5_indices_returns:
    country = index_to_country.get(index, 'Unknown')
    final_result.append({'Index': index, 'Return': ret, 'Country': country})

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-15735413083344890865': 'file_storage/function-call-15735413083344890865.json', 'var_function-call-15933026684059475808': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1196391104323515210': [{'Index': 'GSPTSE', 'Return': 10190.113005626808, 'Country': 'Unknown'}, {'Index': 'GDAXI', 'Return': 9514.918771284436, 'Country': 'Germany'}, {'Index': 'NYA', 'Return': 8915.767954428016, 'Country': 'Unknown'}, {'Index': 'SSMI', 'Return': 8371.399983740468, 'Country': 'Switzerland'}, {'Index': 'IXIC', 'Return': 3965.2701995564203, 'Country': 'Unknown'}]}

exec(code, env_args)
