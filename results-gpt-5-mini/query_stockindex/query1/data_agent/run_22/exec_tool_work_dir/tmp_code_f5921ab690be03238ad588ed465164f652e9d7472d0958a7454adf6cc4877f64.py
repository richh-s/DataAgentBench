code = """import json
# Access the query result stored in var_call_a9texYeSJ5Cjjj5Ww430GvuR
data = var_call_a9texYeSJ5Cjjj5Ww430GvuR
# Convert avg_vol strings to float
for rec in data:
    rec['avg_vol'] = float(rec['avg_vol'])
# Find the index with maximum avg_vol
top = max(data, key=lambda r: r['avg_vol'])
answer = f"{top['Index']} has the highest average intraday volatility since 2020 with average volatility = {top['avg_vol']} (≈{top['avg_vol']*100:.4f}%)."
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_TcjYsX7EAqRx5DxdFjOxWUlB': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_a9texYeSJ5Cjjj5Ww430GvuR': [{'Index': '399001.SZ', 'avg_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_vol': '0.008720764073041308'}]}

exec(code, env_args)
