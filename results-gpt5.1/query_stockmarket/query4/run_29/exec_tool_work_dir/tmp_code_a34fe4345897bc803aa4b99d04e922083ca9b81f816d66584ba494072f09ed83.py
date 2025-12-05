code = """import json, pandas as pd

syms_path = var_call_c185ZfsphGg2N9S84GSJJzak
with open(syms_path) as f:
    syms = json.load(f)

meta_path = var_call_4F6RFKv6SwOftsAiMNahR51z
with open(meta_path) as f:
    meta = json.load(f)

meta_df = pd.DataFrame(meta)
nyse_non_etf = set(meta_df['Symbol'])

valid = [s for s in syms if s in nyse_non_etf]

result = json.dumps(valid[:50])
print('__RESULT__:')
print(result)"""

env_args = {'var_call_dF90d4hPpCsyhvWdXjJUQa96': 'file_storage/call_dF90d4hPpCsyhvWdXjJUQa96.json', 'var_call_4F6RFKv6SwOftsAiMNahR51z': 'file_storage/call_4F6RFKv6SwOftsAiMNahR51z.json', 'var_call_c185ZfsphGg2N9S84GSJJzak': 'file_storage/call_c185ZfsphGg2N9S84GSJJzak.json'}

exec(code, env_args)
