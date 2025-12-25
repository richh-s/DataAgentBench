code = """import json
import pandas as pd

# Load the data
file_path = locals()['var_function-call-10691662813884849147']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate Up and Down days
results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx]
    up_days = len(sub_df[sub_df['Close'] > sub_df['Open']])
    down_days = len(sub_df[sub_df['Close'] < sub_df['Open']])
    
    if up_days > down_days:
        results.append({
            "Index": idx,
            "Up Days": up_days,
            "Down Days": down_days
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9786205905245708340': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-9786205905245709851': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10691662813884849147': 'file_storage/function-call-10691662813884849147.json'}

exec(code, env_args)
