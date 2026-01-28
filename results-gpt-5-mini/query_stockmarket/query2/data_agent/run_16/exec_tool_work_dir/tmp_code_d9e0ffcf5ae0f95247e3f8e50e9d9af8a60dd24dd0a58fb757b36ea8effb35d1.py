code = """import json
# load available symbols list from previous execute_python result file
with open(var_call_qmvmcRybdZcFdW5SX1SGgE7P, 'r') as f:
    data = json.load(f)
available_symbols = data['available_symbols']
# For safety, limit to symbols count to avoid overly large SQL; but we need all. We'll proceed with all.
selects = []
for s in available_symbols:
    # ensure symbol is safe
    sel = "SELECT '%s' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"%s\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX(\"Adj Close\") > 200" % (s, s)
    selects.append(sel)
sql = '\nUNION ALL\n'.join(selects) + '\nORDER BY symbol;'
result = {'sql': sql}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json', 'var_call_qmvmcRybdZcFdW5SX1SGgE7P': 'file_storage/call_qmvmcRybdZcFdW5SX1SGgE7P.json'}

exec(code, env_args)
