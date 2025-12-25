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
valid_etfs = sorted(list(s1.intersection(s2)))

batch = valid_etfs[0:80]
parts = []
sq = chr(39)
dq = chr(34)
# Minimal query to save space
for sym in batch:
    # SELECT 'SYM',MAX("Adj Close")FROM "SYM" WHERE Date GLOB '2015*'
    s = "SELECT " + sq + sym + sq + ",MAX(" + dq + "Adj Close" + dq + ")FROM " + dq + sym + dq + " WHERE Date GLOB " + sq + "2015*" + sq
    parts.append(s)

res = "SELECT * FROM (" + " UNION ALL ".join(parts) + ") WHERE MAX > 200"
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435, 'var_function-call-13265981638886937521': 'OK', 'var_function-call-13755778364282999090': 'HELLO', 'var_function-call-406986697932423198': 1435, 'var_function-call-15787267455676848569': 1435, 'var_function-call-11378392089900453441': 'file_storage/function-call-11378392089900453441.json'}

exec(code, env_args)
