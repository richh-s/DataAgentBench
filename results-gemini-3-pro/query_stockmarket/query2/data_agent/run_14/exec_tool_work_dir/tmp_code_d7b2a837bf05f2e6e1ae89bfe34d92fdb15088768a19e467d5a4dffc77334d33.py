code = """import json

try:
    path = locals()['var_function-call-795890950430017818']
    with open(path, 'r') as f:
        symbols = json.load(f)

    batch_size = 300
    batches = [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]

    queries = []
    for batch in batches:
        parts = []
        for sym in batch:
            # Escape double quotes in symbol if any (unlikely for tickers but safe)
            safe_sym = sym.replace('"', '""')
            part = f"SELECT '{safe_sym}' as Symbol FROM \"{safe_sym}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1"
            parts.append(part)
        query = " UNION ALL ".join(parts)
        queries.append(query)

    print("__RESULT__:")
    print(json.dumps(queries))
except Exception as e:
    print("__RESULT__:")
    print(json.dumps(str(e)))"""

env_args = {'var_function-call-3949593977033921261': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12916805806640155023': 'file_storage/function-call-12916805806640155023.json', 'var_function-call-118847342532788354': 'file_storage/function-call-118847342532788354.json', 'var_function-call-795890950430017818': 'file_storage/function-call-795890950430017818.json', 'var_function-call-14536564358681273316': 1435}

exec(code, env_args)
