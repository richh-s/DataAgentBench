code = """import json
s='AEFC'
q = "SELECT '{s}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(s=s)
print('__RESULT__:')
print(json.dumps({'q': q}))"""

env_args = {'var_call_YGhympfwGa77IINj2W696UPj': ['stockinfo'], 'var_call_B341fO4iHaEslwCWjtPTsjZT': 'file_storage/call_B341fO4iHaEslwCWjtPTsjZT.json', 'var_call_OSi3UoiWvjZY8X5Bm2v9eKP5': 'file_storage/call_OSi3UoiWvjZY8X5Bm2v9eKP5.json', 'var_call_Rq8Of7m3hpZRIvUMdY0uVbTV': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_BfwtF5fXX6Mv1xcmRWiAwqgz': {'ok': True}}

exec(code, env_args)
