code = """import json

keys = list(locals().keys())
target_key = None
for k in keys:
    if str(k).endswith('6636'):
        target_key = k
        break

if not target_key:
    # Just in case
    print('__RESULT__:')
    print(json.dumps(["Error: key not found"]))
else:
    path = locals()[target_key]
    with open(path, 'r') as f:
        data = json.load(f)

    symbols = data['symbols']
    chunks = []
    # Manual chunking to avoid range() syntax issues if any (though unlikely)
    current_chunk = []
    for s in symbols:
        current_chunk.append(s)
        if len(current_chunk) == 50:
            chunks.append(current_chunk)
            current_chunk = []
    if current_chunk:
        chunks.append(current_chunk)

    queries = []
    s_date = '2017-01-01'
    e_date = '2017-12-31'

    for chunk in chunks:
        parts = []
        for sym in chunk:
            # Construct parts
            p = "SELECT '" + sym + "' as symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) as down_days FROM \"" + sym + "\" WHERE \"Date\" >= '" + s_date + "' AND \"Date\" <= '" + e_date + "'"
            parts.append(p)
        
        full = " UNION ALL ".join(parts)
        q = "SELECT symbol, up_days, down_days, (up_days - down_days) as diff FROM (" + full + ") WHERE up_days > down_days ORDER BY diff DESC LIMIT 5"
        queries.append(q)

    print('__RESULT__:')
    print(json.dumps(queries))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}, 'var_function-call-5645677206837916636': 'file_storage/function-call-5645677206837916636.json', 'var_function-call-16652445998382813743': {'d1': '2017-01-01', 'd2': '2017-12-31'}}

exec(code, env_args)
