code = """import json
import pandas as pd

# Load the query result from the stored file path variable
fp = var_call_g2STwoRQSqxyY8RQ6Z5zvjqn
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
# Drop rows with missing Open or Close
df = df.dropna(subset=['Open', 'Close'])

# Compute up/down
df['up'] = (df['Close'] > df['Open']).astype(int)
df['down'] = (df['Close'] < df['Open']).astype(int)

# Group by Index and sum
grouped = df.groupby('Index').agg({'up': 'sum', 'down': 'sum'}).reset_index()

# Find indices with more up days than down days
winning = grouped[grouped['up'] > grouped['down']]['Index'].tolist()

import json
print('__RESULT__:')
print(json.dumps(winning))"""

env_args = {'var_call_zTbw2wThMVGyGPd1TkspOpEa': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_g2STwoRQSqxyY8RQ6Z5zvjqn': 'file_storage/call_g2STwoRQSqxyY8RQ6Z5zvjqn.json'}

exec(code, env_args)
