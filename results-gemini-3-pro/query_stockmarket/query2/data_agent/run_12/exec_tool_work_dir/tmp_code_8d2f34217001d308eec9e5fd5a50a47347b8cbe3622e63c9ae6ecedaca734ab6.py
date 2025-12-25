code = """import json

k1 = 'var_function-call-13379061347181110174'
k2 = 'var_function-call-6559325847238713717'

try:
    with open(locals()[k1], 'r') as f:
        etfs = json.load(f)
    with open(locals()[k2], 'r') as f:
        tables = json.load(f)

    s1 = set(e['Symbol'] for e in etfs)
    s2 = set(tables)
    valid = sorted(list(s1.intersection(s2)))

    parts = []
    
    t1 = "SELECT 'REPL_S' as Symbol FROM "
    t2 = '"REPL_T"'
    t3 = ' WHERE "Adj Close" > 200 AND Date >= '
    t4 = "'2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    
    tmpl = t1 + t2 + t3 + t4
    
    for s in valid:
        if "'" in s or '"' in s or "\\" in s:
            continue
        q = tmpl.replace("REPL_S", s).replace("REPL_T", s)
        parts.append(q)

    full_query = " UNION ALL ".join(parts)
    
    print("__RESULT__:")
    print(json.dumps({"query": full_query}))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json', 'var_function-call-14816739761886936635': ['var_function-call-13379061347181110174', 'var_function-call-6559325847238713717', '__builtins__', 'json'], 'var_function-call-11850539345965912126': {'count': 1435}, 'var_function-call-2281720184919499494': {'status': 'OK', 'len': 1435}, 'var_function-call-2792830708625809368': 'file_storage/function-call-2792830708625809368.json'}

exec(code, env_args)
