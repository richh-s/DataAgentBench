code = """import json
import pandas as pd

# Load data from the file path stored in the variable
file_path = locals()['var_function-call-17287186935468181771']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate daily movement
# Up: Close > Open
# Down: Close < Open
# We ignore Flat for the comparison as per standard definition, or treat as neither.
df['Movement'] = df.apply(lambda row: 'Up' if row['Close'] > row['Open'] else ('Down' if row['Close'] < row['Open'] else 'Flat'), axis=1)

# Group by Index and count
results = df.groupby(['Index', 'Movement']).size().unstack(fill_value=0)

# Print the full stats for debugging purposes (will be captured in tool output but I need to parse it for final answer)
print("Stats:")
print(results)

# Filter
qualified = []
for idx in results.index:
    up = results.loc[idx, 'Up'] if 'Up' in results.columns else 0
    down = results.loc[idx, 'Down'] if 'Down' in results.columns else 0
    if up > down:
        qualified.append(idx)

print('__RESULT__:')
print(json.dumps(qualified))"""

env_args = {'var_function-call-14672061501243724909': ['index_info'], 'var_function-call-14672061501243726034': ['index_trade'], 'var_function-call-1898954456775438105': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1898954456775436556': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-8829736518976379013': [{'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-409892411428070648': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-2362424760755879468': [{'Date': 'January 02, 2018 at 12:00 AM'}, {'Date': 'January 03, 2018 at 12:00 AM'}, {'Date': '04 Jan 2018, 00:00'}, {'Date': '05 Jan 2018, 00:00'}, {'Date': 'January 08, 2018 at 12:00 AM'}, {'Date': '2018-01-09 00:00:00'}, {'Date': '10 Jan 2018, 00:00'}, {'Date': '11 Jan 2018, 00:00'}, {'Date': 'January 12, 2018 at 12:00 AM'}, {'Date': '2018-01-16 00:00:00'}], 'var_function-call-17287186935468181771': 'file_storage/function-call-17287186935468181771.json'}

exec(code, env_args)
