code = """import json
import pandas as pd

# Load the data
with open(locals()['var_function-call-427084795695787883'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate Up and Down days
results = []
indices = df['Index'].unique()

for idx in indices:
    idx_data = df[df['Index'] == idx]
    up_days = idx_data[idx_data['Close'] > idx_data['Open']].shape[0]
    down_days = idx_data[idx_data['Close'] < idx_data['Open']].shape[0]
    
    if up_days > down_days:
        results.append(idx)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7008452991918361793': ['index_info'], 'var_function-call-7008452991918361172': ['index_trade'], 'var_function-call-8434680092391442613': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-17478042442785521087': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-427084795695787883': 'file_storage/function-call-427084795695787883.json'}

exec(code, env_args)
