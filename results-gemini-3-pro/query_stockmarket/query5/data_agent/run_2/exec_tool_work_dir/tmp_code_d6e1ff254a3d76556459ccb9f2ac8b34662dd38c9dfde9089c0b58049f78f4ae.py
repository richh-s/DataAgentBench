code = """import json

k1 = 'var_function-call-13405563423262500002'
k2 = 'var_function-call-13405563423262501427'
p1 = locals().get(k1)
p2 = locals().get(k2)

if not p1 or not p2:
    print("__RESULT__:")
    print(json.dumps({"error": "Missing keys", "keys": list(locals().keys())}))
else:
    with open(p1, 'r') as f:
        i_data = json.load(f)
    with open(p2, 'r') as f:
        t_data = json.load(f)
    
    valid = []
    t_set = set(t_data)
    for x in i_data:
        if x['Symbol'] in t_set:
            valid.append(x['Symbol'])
            
    parts = []
    for s in valid:
        # q = SELECT 's' as Symbol, COUNT(*) as Days FROM "s" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)
        q = 'SELECT \'' + s + '\' as Symbol, COUNT(*) as Days FROM "' + s + '" WHERE Date LIKE \'2019%\' AND (High - Low) > (0.2 * Low)'
        parts.append(q)
        
    full = ' UNION ALL '.join(parts)
    final = 'SELECT Symbol, Days FROM (' + full + ') ORDER BY Days DESC LIMIT 5'
    
    print("__RESULT__:")
    print(json.dumps({"query": final}))"""

env_args = {'var_function-call-13405563423262500002': 'file_storage/function-call-13405563423262500002.json', 'var_function-call-13405563423262501427': 'file_storage/function-call-13405563423262501427.json', 'var_function-call-7452566899761960412': 'file_storage/function-call-7452566899761960412.json'}

exec(code, env_args)
