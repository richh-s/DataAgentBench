code = """import json
with open(var_call_sZAGNYAXSYFDLS9xacqpJJlL, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
parts = []
for s in symbols:
    part = (
        'SELECT ' + repr(s) + ' as symbol, '
        + 'SUM(CASE WHEN ' + chr(34) + 'Close' + chr(34) + '>' + chr(34) + 'Open' + chr(34) + ' THEN 1 ELSE 0 END) as up, '
        + 'SUM(CASE WHEN ' + chr(34) + 'Close' + chr(34) + '<' + chr(34) + 'Open' + chr(34) + ' THEN 1 ELSE 0 END) as down '
        + 'FROM ' + chr(34) + s + chr(34) + ' '
        + 'WHERE ' + chr(34) + 'Date' + chr(34) + ' >= ' + repr('2017-01-01') + ' AND ' + chr(34) + 'Date' + chr(34) + ' <= ' + repr('2017-12-31')
    )
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + ';'
result = {'sql': sql}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rwOJereR8qOI65rlN6SVglQB': 'file_storage/call_rwOJereR8qOI65rlN6SVglQB.json', 'var_call_9cefhE5EDW9Xz32spWSvllKi': 'file_storage/call_9cefhE5EDW9Xz32spWSvllKi.json', 'var_call_sZAGNYAXSYFDLS9xacqpJJlL': 'file_storage/call_sZAGNYAXSYFDLS9xacqpJJlL.json'}

exec(code, env_args)
