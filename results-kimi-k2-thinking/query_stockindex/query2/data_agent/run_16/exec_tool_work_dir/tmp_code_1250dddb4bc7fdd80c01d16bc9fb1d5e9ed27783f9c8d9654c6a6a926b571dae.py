code = """import json
import pandas as pd

file_path = var_functions.query_db:8

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Create up/down indicator (1 for up, -1 for down)

df['direction'] = df.apply(lambda x: 1 if x['Close'] > x['Open'] else (-1 if x['Close'] < x['Open'] else 0), axis=1)

# Group by index and count up/down days
results = []
for index in df['Index'].unique():
    idx_data = df[df['Index'] == index]
    up_days = (idx_data['direction'] == 1).sum()
    down_days = (idx_data['direction'] == -1).sum()
    flat_days = (idx_data['direction'] == 0).sum()
    
    results.append({
        'Index': index,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Flat_Days': int(flat_days),
        'Total_Days': len(idx_data),
        'Net_Up_vs_Down': int(up_days - down_days)
    })

# Create DataFrame and sort by Net_Up_vs_Down descending
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Net_Up_vs_Down', ascending=False)

# Identify indices with more up days than down days
indices_with_more_up = results_df[results_df['Net_Up_vs_Down'] > 0]

print('__RESULT__:')
print(json.dumps({
    'all_indices_summary': results_df.to_dict('records'),
    'indices_with_more_up': indices_with_more_up[['Index', 'Up_Days', 'Down_Days', 'Net_Up_vs_Down']].to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
