code = """import json
with open(var_call_rwOJereR8qOI65rlN6SVglQB, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_9cefhE5EDW9Xz32spWSvllKi, 'r') as f:
    tables = json.load(f)
symbols = []
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym and sym in tables:
        symbols.append(sym)
        mapping[sym] = desc
parts = []
for s in symbols:
    part = "SELECT '{}' as symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) as up, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) as down FROM \"{}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'".format(s, s)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts)
result = {'sql': sql, 'mapping': mapping}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rwOJereR8qOI65rlN6SVglQB': 'file_storage/call_rwOJereR8qOI65rlN6SVglQB.json', 'var_call_9cefhE5EDW9Xz32spWSvllKi': 'file_storage/call_9cefhE5EDW9Xz32spWSvllKi.json'}

exec(code, env_args)
