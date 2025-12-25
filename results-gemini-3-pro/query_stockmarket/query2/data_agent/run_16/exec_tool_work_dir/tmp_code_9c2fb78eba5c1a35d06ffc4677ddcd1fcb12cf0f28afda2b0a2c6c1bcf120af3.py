code = """import json
k1 = 'var_function-call-17042838615002828598'
k2 = 'var_function-call-1654927262755686554'
f1 = locals()[k1]
f2 = locals()[k2]
with open(f1, 'r') as f:
    d1 = json.load(f)
with open(f2, 'r') as f:
    d2 = json.load(f)
s1 = set([x['Symbol'] for x in d1])
s2 = set(d2)
inter = sorted(list(s1.intersection(s2)))

batch = inter[0:150]
parts = []
sq = chr(39)
dq = chr(34)

for sym in batch:
    # "SELECT 'sym' s, MAX("Adj Close") m FROM "sym" WHERE Date GLOB '2015*'"
    s = "SELECT " + sq + sym + sq + " s, MAX(" + dq + "Adj Close" + dq + ") m FROM " + dq + sym + dq + " WHERE Date GLOB " + sq + "2015*" + sq
    parts.append(s)

res = "SELECT s FROM (" + " UNION ALL ".join(parts) + ") WHERE m > 200"
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435, 'var_function-call-13265981638886937521': 'OK', 'var_function-call-13755778364282999090': 'HELLO', 'var_function-call-406986697932423198': 1435, 'var_function-call-15787267455676848569': 1435}

exec(code, env_args)
