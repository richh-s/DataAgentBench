code = """import json
import pandas as pd

path = var_call_CchlP4KgPuUC6frHwkDdNyxb
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# convert numeric
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

grp = df.groupby('Index').apply(lambda g: pd.Series({'up': int((g['Close'] > g['Open']).sum()), 'down': int((g['Close'] < g['Open']).sum())}))

indices = [idx for idx, row in grp.iterrows() if row['up'] > row['down']]

counts = {idx: {'up': int(row['up']), 'down': int(row['down'])} for idx, row in grp.iterrows()}

result = {'indices_more_up_than_down': indices, 'counts': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_D4frt56qZDbzxYaSlsaozeuw': ['index_trade'], 'var_call_XahjbyvRM3gYK9T0yuppoUX7': ['index_info'], 'var_call_Hu6YImmYoGzVoM7mqoVJngly': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_CchlP4KgPuUC6frHwkDdNyxb': 'file_storage/call_CchlP4KgPuUC6frHwkDdNyxb.json'}

exec(code, env_args)
