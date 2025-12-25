code = """import pandas as pd
import json

file_path = locals()['var_function-call-7452276645848962053']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert numeric columns
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert Date
# Using format='mixed' to handle various formats efficiently
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except ValueError:
    # Fallback if mixed is not supported or fails
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter since 2020
df = df[df['Date'] >= '2020-01-01']

# Filter valid data
df = df.dropna(subset=['Open', 'High', 'Low'])
df = df[df['Open'] > 0]

# Calculate Intraday Volatility
df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Average per index
avg_volatility = df.groupby('Index')['Volatility'].mean()

# Convert to dictionary for output
# avg_volatility is a Series, to_dict() makes it {index: value}
result_dict = avg_volatility.to_dict()

# Find the max for the answer
max_index = avg_volatility.idxmax()
max_val = avg_volatility.max()

print("__RESULT__:")
print(json.dumps({"average_volatility": result_dict, "highest_index": max_index, "highest_value": max_val}))"""

env_args = {'var_function-call-3352551645535873114': ['index_info'], 'var_function-call-3352551645535871329': ['index_trade'], 'var_function-call-7674652311321410307': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-7674652311321408508': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-4901037072673261267': 'file_storage/function-call-4901037072673261267.json', 'var_function-call-7452276645848962053': 'file_storage/function-call-7452276645848962053.json'}

exec(code, env_args)
