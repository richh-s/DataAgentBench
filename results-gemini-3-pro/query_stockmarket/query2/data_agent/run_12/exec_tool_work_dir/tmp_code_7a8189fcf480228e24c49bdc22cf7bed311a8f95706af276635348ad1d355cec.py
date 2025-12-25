code = """import json

k1 = 'var_function-call-13379061347181110174'
k2 = 'var_function-call-6559325847238713717'

path1 = locals().get(k1)
path2 = locals().get(k2)

if path1 is None or path2 is None:
    print("__RESULT__:")
    print(json.dumps({"error": "Keys not found", "keys": list(locals().keys())}))
else:
    with open(path1, 'r') as f:
        etfs = json.load(f)
    
    with open(path2, 'r') as f:
        tables = json.load(f)
        
    etf_syms = set(e['Symbol'] for e in etfs)
    tbl_syms = set(tables)
    
    valid = sorted([s for s in etf_syms if s in tbl_syms])
    
    qs = []
    chunk = []
    for s in valid:
        q = "SELECT '" + s + "' as Symbol FROM \"" + s + "\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
        chunk.append(q)
        if len(chunk) >= 50:
            qs.append(" UNION ALL ".join(chunk))
            chunk = []
            
    if chunk:
        qs.append(" UNION ALL ".join(chunk))
        
    print("__RESULT__:")
    print(json.dumps({"count": len(valid), "queries": qs}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json'}

exec(code, env_args)
