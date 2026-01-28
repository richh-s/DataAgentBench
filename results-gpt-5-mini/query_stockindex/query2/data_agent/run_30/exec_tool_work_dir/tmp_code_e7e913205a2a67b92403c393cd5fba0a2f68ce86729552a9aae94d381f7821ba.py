code = """import json
import pandas as pd

# Load the query result from the storage file path
path = var_call_OMf9NCERY3qHJ8IkqfOYZOlA
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Determine up/down
df['up'] = df['Close'] > df['Open']
df['down'] = df['Close'] < df['Open']

summary = df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()
summary['more_up'] = summary['up_days'] > summary['down_days']

# Convert to JSON-serializable structure
result = {row['Index']: {'up_days': int(row['up_days']), 'down_days': int(row['down_days']), 'more_up': bool(row['more_up'])} for _, row in summary.iterrows()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_06LRfVVakaUsymu2t5RX7jvq': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_OMf9NCERY3qHJ8IkqfOYZOlA': 'file_storage/call_OMf9NCERY3qHJ8IkqfOYZOlA.json'}

exec(code, env_args)
