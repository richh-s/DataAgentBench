code = """import json
p = var_call_LiP5pKZJgLLgTX8gZdQpcYYr
with open(p, 'r') as f:
    syms = json.load(f)
parts = []
for s in syms:
    sym_literal = repr(s)
    q = "SELECT " + sym_literal + " AS Symbol FROM \"" + s + "\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    parts.append(q)
sql = "\nUNION ALL\n".join(parts) + ";"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Lb6wOudI1vGIvlWeFmRfaMcq': 'file_storage/call_Lb6wOudI1vGIvlWeFmRfaMcq.json', 'var_call_DT0diiPjDs1dAAdc2zRjJVxt': 'file_storage/call_DT0diiPjDs1dAAdc2zRjJVxt.json', 'var_call_LiP5pKZJgLLgTX8gZdQpcYYr': 'file_storage/call_LiP5pKZJgLLgTX8gZdQpcYYr.json'}

exec(code, env_args)
