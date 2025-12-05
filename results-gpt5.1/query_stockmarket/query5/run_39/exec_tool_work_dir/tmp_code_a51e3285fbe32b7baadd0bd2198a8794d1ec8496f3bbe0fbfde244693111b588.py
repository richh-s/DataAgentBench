code = """import json
import pandas as pd

path = var_call_3KyktpZgnMcbPjsPWe4HOmrP
with open(path, 'r') as f:
    symbols = json.load(f)

path2 = var_call_PwQrdg3QQTTSgKtPFJW7Iqa0
with open(path2, 'r') as f:
    info = json.load(f)

s_df = pd.DataFrame(symbols, columns=['Symbol'])
info_df = pd.DataFrame(info)
merged = pd.merge(s_df, info_df, on='Symbol', how='inner')

result = merged['Symbol'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3KyktpZgnMcbPjsPWe4HOmrP': 'file_storage/call_3KyktpZgnMcbPjsPWe4HOmrP.json', 'var_call_PwQrdg3QQTTSgKtPFJW7Iqa0': 'file_storage/call_PwQrdg3QQTTSgKtPFJW7Iqa0.json'}

exec(code, env_args)
