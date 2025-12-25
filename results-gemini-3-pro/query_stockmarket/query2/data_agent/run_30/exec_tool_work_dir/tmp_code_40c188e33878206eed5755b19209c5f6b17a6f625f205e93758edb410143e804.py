code = """import json

path_c = locals()['var_function-call-2542358163233930626']
path_t = locals()['var_function-call-17634865684080335630']

with open(path_c, 'r') as f:
    cand_data = json.load(f)

with open(path_t, 'r') as f:
    table_data = json.load(f)

cands = set(x['Symbol'] for x in cand_data)
tabs = set(table_data)
syms = sorted(list(cands.intersection(tabs)))

# Batch 1: 0 to 120
batch = syms[0:120]

sqls = []
quote = chr(39)
dquote = chr(34)

for s in batch:
    q = "SELECT " + quote + s + quote + " AS Symbol FROM " + dquote + s + dquote + " WHERE " + dquote + "Adj Close" + dquote + " > 200 AND " + dquote + "Date" + dquote + " LIKE " + quote + "2015%" + quote + " LIMIT 1"
    sqls.append(q)

final_query = " UNION ALL ".join(sqls)

print('__RESULT__:')
print(json.dumps(final_query))"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json', 'var_function-call-753327868909953960': 'test', 'var_function-call-12299234845045051635': "['var_function-call-2542358163233930626', 'var_function-call-17634865684080335630', 'var_function-call-753327868909953960', '__builtins__', 'json']", 'var_function-call-9682706456629382445': 1435, 'var_function-call-12846830218658487781': 'file_storage/function-call-12846830218658487781.json'}

exec(code, env_args)
