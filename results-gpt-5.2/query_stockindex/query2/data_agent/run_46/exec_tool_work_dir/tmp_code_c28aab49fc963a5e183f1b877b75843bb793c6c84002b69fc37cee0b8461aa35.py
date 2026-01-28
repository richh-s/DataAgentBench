code = """import json
records = var_call_ezAih6a9VmfYSPu6jejAiSpo
# Determine indices with more up than down days
res = [r['Index'] for r in records if float(r['up_days']) > float(r['down_days'])]
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_3NTO79dbZnwlIUIWMq4SoRDC': ['index_info'], 'var_call_9mMeANCzHo4PAq3hoBMcq3dW': ['index_trade'], 'var_call_2fdVIViRqfsMjXgjEApcmCB0': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_ezAih6a9VmfYSPu6jejAiSpo': [{'Index': 'GSPTSE', 'n_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'n_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'n_days': '79', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
