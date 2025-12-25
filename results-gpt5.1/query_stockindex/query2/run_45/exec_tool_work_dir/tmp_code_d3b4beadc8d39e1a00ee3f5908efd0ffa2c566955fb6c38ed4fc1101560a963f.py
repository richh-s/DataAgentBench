code = """import json, pandas as pd
import os
# Load full result from file
file_path = var_call_fqTSW1oklhf33uSjjMmP6Rla
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine up and down days per index
summary = []
for idx, g in df.groupby('Index'):
    up_days = (g['Close'] > g['Open']).sum()
    down_days = (g['Close'] < g['Open']).sum()
    summary.append({'Index': idx, 'up_days': int(up_days), 'down_days': int(down_days), 'more_up_than_down': bool(up_days > down_days)})

result = json.dumps(summary)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_WHOQ7sXfNfQ7OjCG5EOK49MC': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_svKcXyKakN1yZcbtiIHC1bUR': ['IXIC', 'NYA', 'GSPTSE'], 'var_call_fqTSW1oklhf33uSjjMmP6Rla': 'file_storage/call_fqTSW1oklhf33uSjjMmP6Rla.json'}

exec(code, env_args)
