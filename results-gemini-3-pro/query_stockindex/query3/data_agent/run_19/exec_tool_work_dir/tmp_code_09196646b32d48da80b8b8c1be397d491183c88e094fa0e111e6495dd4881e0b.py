code = """import pandas as pd
import json

file_path = locals()['var_function-call-16704713962305138576']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Date', 'Adj Close'])
df = df.sort_values(['Index', 'Date'])

df = df[df['Date'] >= '2000-01-01']

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
monthly_data = df.groupby(['Index', 'Year', 'Month']).first().reset_index()

results = []
for idx in monthly_data['Index'].unique():
    idx_data = monthly_data[monthly_data['Index'] == idx]
    
    # Check start date
    start_date = idx_data['Date'].min()
    
    units = (1 / idx_data['Adj Close']).sum()
    total_invested = len(idx_data)
    
    last_row = df[df['Index'] == idx].iloc[-1]
    final_value = units * last_row['Adj Close']
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'Start Date': start_date.strftime('%Y-%m-%d'),
        'End Date': last_row['Date'].strftime('%Y-%m-%d')
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
print('__RESULT__:')
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-13676583938269227752': ['index_info'], 'var_function-call-13676583938269226625': ['index_trade'], 'var_function-call-15196452907809386304': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-15196452907809383827': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-16704713962305138576': 'file_storage/function-call-16704713962305138576.json', 'var_function-call-18123095409977777073': [{'Index': 'IXIC', 'Return': 3.8220467671, 'Start Date': '2000-01-06', 'Last Date': '2021-05-27', 'Total Months': 257}, {'Index': 'NSEI', 'Return': 1.3608849755, 'Start Date': '2007-09-25', 'Last Date': '2021-05-31', 'Total Months': 165}, {'Index': 'GDAXI', 'Return': 1.3474623836, 'Start Date': '2000-01-05', 'Last Date': '2021-05-31', 'Total Months': 257}, {'Index': '399001.SZ', 'Return': 1.3445691587, 'Start Date': '2000-01-05', 'Last Date': '2021-06-02', 'Total Months': 258}, {'Index': 'TWII', 'Return': 1.2374132693, 'Start Date': '2000-01-17', 'Last Date': '2021-05-26', 'Total Months': 257}, {'Index': 'N225', 'Return': 1.1545960543, 'Start Date': '2000-01-04', 'Last Date': '2021-06-01', 'Total Months': 258}, {'Index': 'NYA', 'Return': 1.0065591545, 'Start Date': '2000-01-03', 'Last Date': '2021-05-24', 'Total Months': 257}, {'Index': 'GSPTSE', 'Return': 0.6754596567, 'Start Date': '2000-01-05', 'Last Date': '2021-05-13', 'Total Months': 256}, {'Index': '000001.SS', 'Return': 0.6416057718, 'Start Date': '2000-01-04', 'Last Date': '2021-05-31', 'Total Months': 257}, {'Index': 'N100', 'Return': 0.5986654389, 'Start Date': '2000-01-10', 'Last Date': '2021-05-31', 'Total Months': 257}]}

exec(code, env_args)
