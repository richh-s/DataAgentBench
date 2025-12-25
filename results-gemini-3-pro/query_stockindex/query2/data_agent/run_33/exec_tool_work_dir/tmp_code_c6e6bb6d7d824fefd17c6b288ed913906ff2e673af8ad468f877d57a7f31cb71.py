code = """import json
import pandas as pd

# Load the data
file_path = locals()['var_function-call-10884324450995296695']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate Up/Down days
results = []
for index_name, group in df.groupby('Index'):
    up_days = group[group['Close'] > group['Open']].shape[0]
    down_days = group[group['Close'] < group['Open']].shape[0]
    
    if up_days > down_days:
        results.append(index_name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5716163376028186408': ['index_info'], 'var_function-call-17427906059631237496': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-2785288086087205008': [{'IndexSymbol': 'N225'}, {'IndexSymbol': 'GSPTSE'}, {'IndexSymbol': 'NSEI'}, {'IndexSymbol': 'GDAXI'}, {'IndexSymbol': 'IXIC'}, {'IndexSymbol': 'HSI'}, {'IndexSymbol': 'NYA'}, {'IndexSymbol': '000001.SS'}, {'IndexSymbol': 'SSMI'}, {'IndexSymbol': 'TWII'}, {'IndexSymbol': 'N100'}, {'IndexSymbol': '399001.SZ'}, {'IndexSymbol': 'J203.JO'}], 'var_function-call-10884324450995296695': 'file_storage/function-call-10884324450995296695.json'}

exec(code, env_args)
