code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-16704713962305138576']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Sort
df = df.sort_values(['Index', 'Date'])

# Filter out indices that started significantly after 2000-01-01?
# The user says "investments in all indices since 2000".
# If an index started later, should we count it from its start or from 2000?
# "investments in all indices since 2000" implies starting in 2000.
# If an index doesn't have data in 2000, maybe it shouldn't be considered or investment starts later.
# But for comparison, usually we want the same time period.
# However, if data is missing, I will assume investment starts when data is available,
# but strictly speaking, "since 2000" implies the index existed in 2000.
# Let's check start dates.
start_dates = df.groupby('Index')['Date'].min()
# print(start_dates) 

# For the calculation:
# We simulate monthly investment.
# Group by Index, Year, Month. Take the first entry.
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

monthly_data = df.groupby(['Index', 'Year', 'Month']).first().reset_index()

# Calculate returns for each index
results = []
for idx in monthly_data['Index'].unique():
    idx_data = monthly_data[monthly_data['Index'] == idx]
    
    # Check if index existed in 2000
    if idx_data['Year'].min() > 2000:
        # Skip or include? "since 2000" implies starting 2000.
        # If it starts later, the return might be skewed (shorter period).
        # Let's check the start dates first to decide.
        pass
        
    # Investment simulation
    total_invested = 0
    total_units = 0
    
    for _, row in idx_data.iterrows():
        price = row['Adj Close']
        if price > 0:
            units = 100 / price # Invest $100
            total_units += units
            total_invested += 100
            
    # Final value
    # Get the latest price from the original daily dataframe (to be precise)
    last_price = df[df['Index'] == idx].iloc[-1]['Adj Close']
    
    final_value = total_units * last_price
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'Start Date': idx_data['Date'].min(),
        'Total Invested': total_invested,
        'Final Value': final_value
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
print('__RESULT__:')
print(results_df.to_json(orient='records', date_format='iso'))"""

env_args = {'var_function-call-13676583938269227752': ['index_info'], 'var_function-call-13676583938269226625': ['index_trade'], 'var_function-call-15196452907809386304': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-15196452907809383827': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-16704713962305138576': 'file_storage/function-call-16704713962305138576.json'}

exec(code, env_args)
