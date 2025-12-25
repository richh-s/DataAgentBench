code = """import json
path = locals()['var_function-call-3295962867968348472']
with open(path) as f: s = json.load(f)

# Batch 1: 0-60 (approx 9000 chars)
batch = s[0:60]
dq = chr(34)
sq = chr(39)
template = "(SELECT {sq}{{0}}{sq} as Symbol FROM {dq}{{0}}{dq} WHERE {dq}Date{dq} BETWEEN {sq}2015-01-01{sq} AND {sq}2015-12-31{sq} AND {dq}Adj Close{dq} > 200 LIMIT 1)"
template = template.format(sq=sq, dq=dq)
q_list = [template.format(x) for x in batch]
full = " UNION ALL ".join(q_list)
print("__RESULT__:")
print(json.dumps(full))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json', 'var_function-call-3295962867968348472': 'file_storage/function-call-3295962867968348472.json', 'var_function-call-11530623601656083675': 1435, 'var_function-call-3709276694871422927': [{'Date': '2018-08-15'}], 'var_function-call-4537489530168145434': [], 'var_function-call-3348924272892652015': 'file_storage/function-call-3348924272892652015.json'}

exec(code, env_args)
