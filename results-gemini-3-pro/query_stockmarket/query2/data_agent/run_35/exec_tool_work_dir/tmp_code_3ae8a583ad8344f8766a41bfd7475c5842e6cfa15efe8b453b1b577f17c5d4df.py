code = """import json

key = 'var_function-call-17759206541062733528'
path = locals()[key]

with open(path, 'r') as f:
    data = json.load(f)

items = data[:90]
qs = []
sq = chr(39) # single quote
dq = chr(34) # double quote

for i in items:
    # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date GLOB '2015*' LIMIT 1
    # GLOB '2015*' -> GLOB '2015*'
    q = "SELECT " + sq + i + sq + " as Symbol FROM " + dq + i + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date GLOB " + sq + "2015*" + sq + " LIMIT 1"
    qs.append(q)

res = " UNION ALL ".join(qs)
print("__RESULT__:")
print(json.dumps({"query": res, "count": len(items)}))"""

env_args = {'var_function-call-2090132530202969507': 'file_storage/function-call-2090132530202969507.json', 'var_function-call-2090132530202970712': 'file_storage/function-call-2090132530202970712.json', 'var_function-call-17759206541062733528': 'file_storage/function-call-17759206541062733528.json', 'var_function-call-11518138145490088997': 1435, 'var_function-call-8082552596352152953': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}], 'var_function-call-9817004090254500701': 1, 'var_function-call-134130093027841769': 'ok', 'var_function-call-9300895540609122547': 'file_storage/function-call-17759206541062733528.json'}

exec(code, env_args)
