code = """import json
with open(var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g, 'r') as f:
    symbols = json.load(f)
# chunk into 100
chunks = [symbols[i:i+100] for i in range(0, len(symbols), 100)]
queries = []
for idx,chunk in enumerate(chunks):
    parts = []
    for s in chunk:
        # Safe SQL: quote table name and column
        part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'"
        parts.append(part)
    sql = "\nUNION ALL\n".join(parts)+";"
    queries.append({'id': idx, 'sql': sql, 'count': len(chunk)})
result = json.dumps(queries)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Cqc50H7gOaxK4opWuAJHG9ou': 'file_storage/call_Cqc50H7gOaxK4opWuAJHG9ou.json', 'var_call_sLwBJkaPyOb6PONpT7TKbMr9': 'file_storage/call_sLwBJkaPyOb6PONpT7TKbMr9.json', 'var_call_4WNVMgKtu1LrMmZ3ZkmiNL3g': 'file_storage/call_4WNVMgKtu1LrMmZ3ZkmiNL3g.json'}

exec(code, env_args)
