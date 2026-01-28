code = """import json
with open(var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g, 'r') as f:
    symbols = json.load(f)
chunks = [symbols[i:i+20] for i in range(0, len(symbols), 20)]
sqls = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append("SELECT '{0}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{0}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'".format(s))
    sql = "\nUNION ALL\n".join(parts) + ";"
    sqls.append(sql)
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_Cqc50H7gOaxK4opWuAJHG9ou': 'file_storage/call_Cqc50H7gOaxK4opWuAJHG9ou.json', 'var_call_sLwBJkaPyOb6PONpT7TKbMr9': 'file_storage/call_sLwBJkaPyOb6PONpT7TKbMr9.json', 'var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g': 'file_storage/call_4WNVMgKtu1LrMmZ3ZkmiNL3g.json', 'var_call_znkBLxHwEGl9Xj2qekm7CrNo': {'count': 1435, 'first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_CJlfK6SD45OQCmjEnKyzUYJB': [{'Symbol': 'SPY', 'max_adj': '193.3121490478516'}], 'var_call_b9GueMyXDbSVBbXyautRtE2S': [{'Symbol': 'DIA', 'max_adj': '163.6190185546875'}], 'var_call_cL9qDfVdqO6ZMpLyuntQsKun': [{'Symbol': 'GLD', 'max_adj': '125.2300033569336'}]}

exec(code, env_args)
