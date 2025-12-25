code = """import json
path = locals()['var_function-call-8543336388924568308']
with open(path, 'r') as f:
    d = json.load(f)
syms = d['valid_symbols']
qs = []
for i, s in enumerate(syms):
    # Shorten query
    # substr(Date,1,4)='2019' is safer than LIKE
    cond = "substr(Date,1,4)='2019' AND (High-Low)>(0.2*Low)"
    if i == 0:
        q = "SELECT '" + s + "' s, COUNT(*) c FROM \"" + s + "\" WHERE " + cond
    else:
        q = "SELECT '" + s + "', COUNT(*) FROM \"" + s + "\" WHERE " + cond
    qs.append(q)

final_q = " UNION ALL ".join(qs) + " ORDER BY c DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json', 'var_function-call-8543336388924568308': 'file_storage/function-call-8543336388924568308.json', 'var_function-call-18149381421604452659': 'file_storage/function-call-18149381421604452659.json', 'var_function-call-9516611570051908901': 'file_storage/function-call-9516611570051908901.json'}

exec(code, env_args)
