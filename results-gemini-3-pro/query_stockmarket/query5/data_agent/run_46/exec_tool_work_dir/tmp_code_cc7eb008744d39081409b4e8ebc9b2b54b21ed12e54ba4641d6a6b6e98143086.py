code = """import json
path = locals()['var_function-call-8543336388924568308']
with open(path, 'r') as f:
    d = json.load(f)
syms = d['valid_symbols']
qs = []
for s in syms:
    part1 = "SELECT '" + s + "' as Symbol, COUNT(*) as C FROM "
    part2 = '"' + s + '"'
    part3 = " WHERE substr(Date,1,4)='2019' AND (High-Low)>(0.2*Low)"
    qs.append(part1 + part2 + part3)
final_q = " UNION ALL ".join(qs) + " ORDER BY C DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json', 'var_function-call-8543336388924568308': 'file_storage/function-call-8543336388924568308.json', 'var_function-call-18149381421604452659': 'file_storage/function-call-18149381421604452659.json'}

exec(code, env_args)
