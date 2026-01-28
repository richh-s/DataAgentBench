code = """import json
with open(var_call_hqaevLm2GZg0QXOPaasZEXkb, 'r') as f:
    symbols = json.load(f)
parts = []
for s in symbols:
    # wrap symbol in double quotes for table name and in single quotes for literal
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'")
sql = ' UNION ALL '.join(parts) + ';'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_xtcHZxFlp2AioHUoeqxRk0n8': 'file_storage/call_xtcHZxFlp2AioHUoeqxRk0n8.json', 'var_call_Eu1b0Hrj3zvFAG0mEuXaHaO3': 'file_storage/call_Eu1b0Hrj3zvFAG0mEuXaHaO3.json', 'var_call_hqaevLm2GZg0QXOPaasZEXkb': 'file_storage/call_hqaevLm2GZg0QXOPaasZEXkb.json', 'var_call_BIG0WvhipHSN5WRnPyP1uMyM': [{'Symbol': 'SPY', 'max_adj': '193.3121490478516'}], 'var_call_2tFJ0zT8uGViUe7LRDYjP7nl': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
