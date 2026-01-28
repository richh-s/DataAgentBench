code = """import json
import pandas as pd

# Read the full result from the file
result_file = var_functions.query_db:10
with open(result_file, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert price columns to float for comparison
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Classify each day as Up, Down, or Flat
df['Day_Type'] = 'Flat'
df.loc[df['Close'] > df['Open'], 'Day_Type'] = 'Up'
df.loc[df['Close'] < df['Open'], 'Day_Type'] = 'Down'

# Count up and down days by index
results = []
for idx in ['IXIC', 'NYA', 'GSPTSE']:
    idx_data = df[df['Index'] == idx]
    up_days = len(idx_data[idx_data['Day_Type'] == 'Up'])
    down_days = len(idx_data[idx_data['Day_Type'] == 'Down'])
    flat_days = len(idx_data[idx_data['Day_Type'] == 'Flat'])
    
    results.append({
        'Index': idx,
        'Up_Days': up_days,
        'Down_Days': down_days,
        'Flat_Days': flat_days,
        'Net_Days': up_days - down_days
    })

# Identify indices with more up days than down days
indices_more_up = [r['Index'] for r in results if r['Net_Days'] > 0]

output = {
    'indices_more_up': indices_more_up,
    'detailed_results': results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:5': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
