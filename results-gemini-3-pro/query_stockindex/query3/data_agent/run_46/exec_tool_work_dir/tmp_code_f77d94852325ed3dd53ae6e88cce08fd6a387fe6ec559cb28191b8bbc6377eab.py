code = """import json
import pandas as pd

# Load data
file_path = locals()['var_function-call-5900596531419111934']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])
df = df.sort_values(['Index', 'Date'])

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

results = []

for index_name, group in df.groupby('Index'):
    # Resample to get the first trading day of each month
    # Create YearMonth
    group = group.copy()
    group['YearMonth'] = group['Date'].dt.to_period('M')
    # Take first entry per month
    monthly_investments = group.drop_duplicates(subset=['YearMonth'], keep='first')
    
    # Investment simulation
    # Invest 1 unit of currency each month
    monthly_investments['Units_Bought'] = 1 / monthly_investments['Adj Close']
    
    total_units = monthly_investments['Units_Bought'].sum()
    total_invested = len(monthly_investments)
    
    # Final value: Total Units * Last available price in the dataset (daily)
    # Get the very last price available for this index
    last_price = group.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': index_name,
        'ROI': roi,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': monthly_investments['Date'].min(),
        'End_Date': group['Date'].max()
    })

results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)

print("__RESULT__:")
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-13501008299029343830': ['index_info'], 'var_function-call-13501008299029341129': ['index_trade'], 'var_function-call-17345393264304504446': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-17345393264304504609': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5900596531419111934': 'file_storage/function-call-5900596531419111934.json'}

exec(code, env_args)
