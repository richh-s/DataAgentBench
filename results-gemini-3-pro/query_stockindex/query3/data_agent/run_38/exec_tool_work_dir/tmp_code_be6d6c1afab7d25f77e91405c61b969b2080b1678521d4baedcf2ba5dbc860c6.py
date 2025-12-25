code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-11112950162314494458'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.dropna(subset=['Date', 'Close'])
df = df[df['Date'] >= '2000-01-01']

def calculate_dca_return(group):
    group = group.sort_values('Date')
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_investments = group.groupby('YearMonth').first().reset_index()
    
    units_accumulated = 0
    months_invested = 0
    
    for _, row in monthly_investments.iterrows():
        price = row['Close']
        if pd.notnull(price) and price > 0:
            units = 1.0 / price
            units_accumulated += units
            months_invested += 1
            
    if len(group) > 0 and months_invested > 0:
        last_price = group.iloc[-1]['Close']
        total_value = units_accumulated * last_price
        overall_return = (total_value - months_invested) / months_invested
    else:
        overall_return = 0
        
    return overall_return

results = []
indices = df['Index'].unique()

for idx in indices:
    group = df[df['Index'] == idx].copy()
    ret = calculate_dca_return(group)
    results.append({'Index': idx, 'Return': ret})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-8000534823580807906': ['index_info'], 'var_function-call-8000534823580808341': ['index_trade'], 'var_function-call-9672975509357680590': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-9672975509357679569': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_function-call-11112950162314494458': 'file_storage/function-call-11112950162314494458.json', 'var_function-call-4552489432409127524': [{'Index': 'IXIC', 'Return': 3.8267206897}, {'Index': 'NSEI', 'Return': 1.3584343633}, {'Index': 'GDAXI', 'Return': 1.3482393079}, {'Index': '399001.SZ', 'Return': 1.3479288232}, {'Index': 'TWII', 'Return': 1.296645022}, {'Index': 'N225', 'Return': 1.1702659032}, {'Index': 'NYA', 'Return': 1.015032072}, {'Index': 'GSPTSE', 'Return': 0.7295061267}, {'Index': '000001.SS', 'Return': 0.6421953032}, {'Index': 'N100', 'Return': 0.6125512204}]}

exec(code, env_args)
