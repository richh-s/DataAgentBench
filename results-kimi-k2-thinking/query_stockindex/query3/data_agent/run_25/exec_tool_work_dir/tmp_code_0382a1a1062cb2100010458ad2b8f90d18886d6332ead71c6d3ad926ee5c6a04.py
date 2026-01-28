code = """import json
import pandas as pd

# Read the query result from the file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove missing data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter from 2000 onward
df_2000 = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

print(f"Data loaded: {len(df_2000)} records from {len(df_2000['Index'].unique())} indices")

# Map indices to countries
index_mapping = {
    'N225': {'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan'},
    'HSI': {'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong'},
    '000001.SS': {'Exchange': 'Shanghai Stock Exchange', 'Country': 'China'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'},
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'NYA': {'Exchange': 'New York Stock Exchange', 'Country': 'USA'},
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'USA'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'}
}

# Calculate returns for each index
results = []
for index_symbol in index_mapping.keys():
    index_data = df_2000[df_2000['Index'] == index_symbol].copy()
    
    if len(index_data) < 10:
        continue
    
    # Get monthly first trading days
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_first = index_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_first) < 12:
        continue
    
    investment = 100
    total_invested = len(monthly_first) * investment
    total_shares = 0
    
    for _, row in monthly_first.iterrows():
        shares_bought = investment / row['CloseUSD']
        total_shares += shares_bought
    
    final_close = index_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_close
    total_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': index_symbol,
        'Country': index_mapping[index_symbol]['Country'],
        'Total_Return': total_return
    })

# Sort by return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return', ascending=False)

# Create top 5 list
if len(results_df) >= 5:
    top_5 = results_df.head(5)
    answer_lines = []
    for _, row in top_5.iterrows():
        return_pct = row['Total_Return'] * 100
        line = f"{row['Index']} from {row['Country']}: {return_pct:.1f}% total return"
        answer_lines.append(line)
    
    final_answer = '; '.join(answer_lines)
else:
    final_answer = 'Insufficient data for analysis'

# Print in required format
print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
