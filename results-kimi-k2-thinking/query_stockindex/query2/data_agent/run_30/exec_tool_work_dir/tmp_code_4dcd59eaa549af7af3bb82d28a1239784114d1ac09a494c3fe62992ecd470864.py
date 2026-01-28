code = """import json
import pandas as pd

# Load data from file
data_file = var_functions.query_db:8
with open(data_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Remove rows where Open equals Close (no change days)
df = df[df['Open'] != df['Close']]

# Determine up vs down days
df['day_type'] = df.apply(lambda row: 'up' if float(row['Close']) > float(row['Open']) else 'down', axis=1)

# Count up and down days per index
summary = df.groupby(['Index', 'day_type']).size().unstack(fill_value=0)

# Calculate net days (up - down)
summary['net_days'] = summary.get('up', 0) - summary.get('down', 0)
summary['more_up_than_down'] = summary['net_days'] > 0

# Filter indices with more up days than down days
result_indices = summary[summary['more_up_than_down']].index.tolist()

# Prepare output
output = {
    'indices_with_more_up_days': result_indices,
    'summary': summary.to_dict('index')
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS', 'cnt': '5791'}, {'Index': '399001.SZ', 'cnt': '5760'}, {'Index': 'GDAXI', 'cnt': '8438'}, {'Index': 'GSPTSE', 'cnt': '10526'}, {'Index': 'HSI', 'cnt': '8492'}, {'Index': 'IXIC', 'cnt': '12690'}, {'Index': 'J203.JO', 'cnt': '2346'}, {'Index': 'N100', 'cnt': '5474'}, {'Index': 'N225', 'cnt': '13874'}, {'Index': 'NSEI', 'cnt': '3346'}, {'Index': 'NYA', 'cnt': '13947'}, {'Index': 'SSMI', 'cnt': '7671'}, {'Index': 'TWII', 'cnt': '5869'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
