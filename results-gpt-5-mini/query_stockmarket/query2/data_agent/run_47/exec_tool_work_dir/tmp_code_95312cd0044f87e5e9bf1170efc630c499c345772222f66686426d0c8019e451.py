code = """import json
with open(var_call_3Lkt6GYhqGVwnJChU7sGIU2y, 'r') as f:
    symbols = json.load(f)

symbols = sorted(set(symbols))
parts = []
for s in symbols:
    sval = s.replace("'", "''")
    part = "SELECT '{}' AS symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sval, s)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + ';'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_BZ0vbjInUsrjIR40BDpeJO2j': 'file_storage/call_BZ0vbjInUsrjIR40BDpeJO2j.json', 'var_call_ETnWX20FaLVdAYR2akuYOwgE': 'file_storage/call_ETnWX20FaLVdAYR2akuYOwgE.json', 'var_call_FHdvyaEFB6c41YjYzxoiKKZg': 'file_storage/call_FHdvyaEFB6c41YjYzxoiKKZg.json', 'var_call_3Lkt6GYhqGVwnJChU7sGIU2y': 'file_storage/call_3Lkt6GYhqGVwnJChU7sGIU2y.json'}

exec(code, env_args)
