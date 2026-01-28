code = """import json
with open(var_call_3Lkt6GYhqGVwnJChU7sGIU2y, 'r') as f:
    symbols = json.load(f)
symbols = sorted(set(symbols))

batch_size = 50
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]
sql_list = []
for batch in batches:
    parts = []
    for s in batch:
        sval = s.replace("'", "''")
        part = "SELECT '{}' AS symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sval, s)
        parts.append(part)
    sql = '\nUNION ALL\n'.join(parts) + ';'
    sql_list.append(sql)
print('__RESULT__:')
print(json.dumps(sql_list))"""

env_args = {'var_call_BZ0vbjInUsrjIR40BDpeJO2j': 'file_storage/call_BZ0vbjInUsrjIR40BDpeJO2j.json', 'var_call_ETnWX20FaLVdAYR2akuYOwgE': 'file_storage/call_ETnWX20FaLVdAYR2akuYOwgE.json', 'var_call_FHdvyaEFB6c41YjYzxoiKKZg': 'file_storage/call_FHdvyaEFB6c41YjYzxoiKKZg.json', 'var_call_3Lkt6GYhqGVwnJChU7sGIU2y': 'file_storage/call_3Lkt6GYhqGVwnJChU7sGIU2y.json', 'var_call_uXTcA9BnNvZsoO4ruadrLg43': [], 'var_call_8T3jD7vhT3Jy4N8aitDEtGlG': [{'symbol': 'MDY'}], 'var_call_PtLsvJVEU806GN2QsjbcLsl4': {'count': 1435}}

exec(code, env_args)
