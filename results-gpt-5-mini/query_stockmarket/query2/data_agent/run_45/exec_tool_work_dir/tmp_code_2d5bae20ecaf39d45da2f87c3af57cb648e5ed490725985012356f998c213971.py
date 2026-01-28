code = """import json
with open(var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g, 'r') as f:
    symbols = json.load(f)
parts = []
for s in symbols:
    parts.append("SELECT \"{}\" AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'".format(s, s))
sql = "\nUNION ALL\n".join(parts) + ";"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_Cqc50H7gOaxK4opWuAJHG9ou': 'file_storage/call_Cqc50H7gOaxK4opWuAJHG9ou.json', 'var_call_sLwBJkaPyOb6PONpT7TKbMr9': 'file_storage/call_sLwBJkaPyOb6PONpT7TKbMr9.json', 'var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g': 'file_storage/call_4WNVMgKtu1LrMmZ3ZkmiNL3g.json'}

exec(code, env_args)
