code = """import json
with open(var_call_sZAGNYAXSYFDLS9xacqpJJlL, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
# Build SQL union query
parts = []
for s in symbols:
    part = "SELECT '{}' as symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) as up, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) as down FROM \"{}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'".format(s, s)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + ';'
result = {'sql': sql}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rwOJereR8qOI65rlN6SVglQB': 'file_storage/call_rwOJereR8qOI65rlN6SVglQB.json', 'var_call_9cefhE5EDW9Xz32spWSvllKi': 'file_storage/call_9cefhE5EDW9Xz32spWSvllKi.json', 'var_call_sZAGNYAXSYFDLS9xacqpJJlL': 'file_storage/call_sZAGNYAXSYFDLS9xacqpJJlL.json'}

exec(code, env_args)
