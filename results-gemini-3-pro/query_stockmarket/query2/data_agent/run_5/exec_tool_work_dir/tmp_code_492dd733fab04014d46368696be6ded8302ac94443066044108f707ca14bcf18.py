code = """import json

s = 'AAAU'
d1 = '2015-01-01'
d2 = '2015-12-31'
q = 'SELECT \'%s\' as Symbol FROM "%s" WHERE "Adj Close" > 200 AND Date >= \'%s\' AND Date <= \'%s\' LIMIT 1' % (s, s, d1, d2)

print("__RESULT__:")
print(json.dumps(q))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435}

exec(code, env_args)
