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

result = {'symbols': symbols, 'mapping': mapping}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rwOJereR8qOI65rlN6SVglQB': 'file_storage/call_rwOJereR8qOI65rlN6SVglQB.json', 'var_call_9cefhE5EDW9Xz32spWSvllKi': 'file_storage/call_9cefhE5EDW9Xz32spWSvllKi.json'}

exec(code, env_args)
