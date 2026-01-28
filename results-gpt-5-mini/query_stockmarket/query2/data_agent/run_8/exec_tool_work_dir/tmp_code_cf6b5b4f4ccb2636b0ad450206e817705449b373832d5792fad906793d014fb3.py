code = """import json
p = var_call_LiP5pKZJgLLgTX8gZdQpcYYr
with open(p, 'r') as f:
    syms = json.load(f)
parts = []
for s in syms:
    parts.append("SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS maxadj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s=s))
sql = "\nUNION ALL\n".join(parts) + ';'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_Lb6wOudI1vGIvlWeFmRfaMcq': 'file_storage/call_Lb6wOudI1vGIvlWeFmRfaMcq.json', 'var_call_DT0diiPjDs1dAAdc2zRjJVxt': 'file_storage/call_DT0diiPjDs1dAAdc2zRjJVxt.json', 'var_call_LiP5pKZJgLLgTX8gZdQpcYYr': 'file_storage/call_LiP5pKZJgLLgTX8gZdQpcYYr.json'}

exec(code, env_args)
