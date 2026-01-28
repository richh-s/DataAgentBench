code = """import json
import pandas as pd

# Load the data from the query result
result_key = 'var_functions.query_db:10'
raw_data = locals()[result_key]

# If it's a file path, read from file
if isinstance(raw_data, str) and '.json' in raw_data:
    with open(raw_data, 'r') as f:
        data = json.load(f)
else:
    data = raw_data

# Create DataFrame
df = pd.DataFrame(data)

# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Classify days
conditions = [
    df['Close'] > df['Open'],
    df['Close'] < df['Open']
]
choices = ['Up', 'Down']
df['Day_Type'] = pd.select(conditions, choices, default='Flat')

# Count by index
results = []
for idx in ['IXIC', 'NYA', 'GSPTSE']:
    idx_data = df[df['Index'] == idx]
    up_days = (idx_data['Day_Type'] == 'Up').sum()
    down_days = (idx_data['Day_Type'] == 'Down').sum()
    flat_days = (idx_data['Day_Type'] == 'Flat').sum()
    net_days = up_days - down_days
    
    results.append({
        'Index': idx,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Flat_Days': int(flat_days),
        'Net_Days': int(net_days),
        'Has_More_Up': net_days > 0
    })

# Find indices with more up days than down days
indices_more_up = [r['Index'] for r in results if r['Has_More_Up']]

# Prepare output
output = ', '.join(indices_more_up) if indices_more_up else 'None'

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:5': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
