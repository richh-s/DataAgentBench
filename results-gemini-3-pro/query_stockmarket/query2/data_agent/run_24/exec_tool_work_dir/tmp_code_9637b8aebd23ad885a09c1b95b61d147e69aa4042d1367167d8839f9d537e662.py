code = """import json
k1 = 'var_function-call-17981552509113141854'
k2 = 'var_function-call-3218142005520764474'
f1 = locals().get(k1)
f2 = locals().get(k2)

with open(f1) as fo:
    d1 = json.load(fo)
with open(f2) as fo:
    d2 = json.load(fo)

s2 = set(d2)
syms = [x['Symbol'] for x in d1 if x['Symbol'] in s2]
syms.sort()

batch = syms[:500]
qs = []
sq = chr(39) # single quote
dq = chr(34) # double quote

for s in batch:
    # SELECT 's' as Symbol FROM "s" WHERE "Adj Close" > 200 AND Date LIKE '2015-%' LIMIT 1
    # Note: "Adj Close" needs quotes.
    q = "SELECT " + sq + s + sq + " as Symbol FROM " + dq + s + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date LIKE " + sq + "2015-%" + sq + " LIMIT 1"
    qs.append(q)

res = " UNION ALL ".join(qs)
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-5455133501503104484': ['stockinfo'], 'var_function-call-17981552509113141854': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-3218142005520764474': 'file_storage/function-call-3218142005520764474.json', 'var_function-call-13141348390779095294': {'count': 1435}, 'var_function-call-17805212614560321345': 'Hello', 'var_function-call-16314234235450674680': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-15222747337469196376': {'len1': 1435, 'len2': 2753}, 'var_function-call-6762066662681141806': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-11479311752232342317': 1435, 'var_function-call-12230445017966649940': 1435}

exec(code, env_args)
