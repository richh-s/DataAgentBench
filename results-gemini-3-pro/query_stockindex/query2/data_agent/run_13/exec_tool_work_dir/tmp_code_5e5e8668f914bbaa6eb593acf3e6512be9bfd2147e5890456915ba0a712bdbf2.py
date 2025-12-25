code = """import json
import pandas as pd

# Load the result from the file
file_path = locals()['var_function-call-1763679842366530409']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Drop rows with missing values
df = df.dropna(subset=['Open', 'Close'])

# Calculate Up and Down
df['Up'] = df['Close'] > df['Open']
df['Down'] = df['Close'] < df['Open']

# Group by Index and sum
result = df.groupby('Index')[['Up', 'Down']].sum()

# Filter indices where Up > Down
more_up_than_down = result[result['Up'] > result['Down']].index.tolist()

print("__RESULT__:")
print(json.dumps(more_up_than_down))"""

env_args = {'var_function-call-8537970027271755604': ['index_info'], 'var_function-call-8537970027271756553': ['index_trade'], 'var_function-call-12801114533068702233': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-12801114533068704846': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16347643357106078236': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-1763679842366530409': 'file_storage/function-call-1763679842366530409.json'}

exec(code, env_args)
