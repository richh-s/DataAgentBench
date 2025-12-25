code = """import json, pandas as pd

# Load full index_trade data from file
path = var_call_Leb2lwepiD6nugWEiTh6XXfE
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Parse date flexibly and filter since 2020-01-01
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date'] >= '2020-01-01']

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Average by index
res = df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = res.reset_index().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LiNftm3xDvZpthPiztM1rb9L': ['index_info'], 'var_call_o1S1rgfgrsXSPYu4mytkM9XP': ['index_trade'], 'var_call_QlkJCy3DxZtZ0859RgnrwBAl': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_Leb2lwepiD6nugWEiTh6XXfE': 'file_storage/call_Leb2lwepiD6nugWEiTh6XXfE.json'}

exec(code, env_args)
