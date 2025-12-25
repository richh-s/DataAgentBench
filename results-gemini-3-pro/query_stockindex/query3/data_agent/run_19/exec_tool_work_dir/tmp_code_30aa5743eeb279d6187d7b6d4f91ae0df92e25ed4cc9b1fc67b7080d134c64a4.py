code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-16704713962305138576']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Use errors='coerce' to handle bad dates, and infer format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates or prices
df = df.dropna(subset=['Date', 'Adj Close'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

# Sort
df = df.sort_values(['Index', 'Date'])

# Filter for start date >= 2000-01-01 (already done in SQL, but good to ensure)
df = df[df['Date'] >= '2000-01-01']

# Group by Index, Year, Month to simulate monthly buy
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Take the first trading day of each month
monthly_data = df.groupby(['Index', 'Year', 'Month']).first().reset_index()

results = []
for idx in monthly_data['Index'].unique():
    idx_data = monthly_data[monthly_data['Index'] == idx]
    
    # Calculate investment
    # Invest 1 unit each month
    units_bought = (1 / idx_data['Adj Close']).sum()
    total_invested = len(idx_data) # 1 * count
    
    # Final value
    last_row = df[df['Index'] == idx].iloc[-1]
    last_price = last_row['Adj Close']
    final_value = units_bought * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'Start Date': idx_data['Date'].min().strftime('%Y-%m-%d'),
        'Last Date': last_row['Date'].strftime('%Y-%m-%d'),
        'Total Months': int(total_invested)
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

print('__RESULT__:')
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-13676583938269227752': ['index_info'], 'var_function-call-13676583938269226625': ['index_trade'], 'var_function-call-15196452907809386304': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-15196452907809383827': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-16704713962305138576': 'file_storage/function-call-16704713962305138576.json'}

exec(code, env_args)
