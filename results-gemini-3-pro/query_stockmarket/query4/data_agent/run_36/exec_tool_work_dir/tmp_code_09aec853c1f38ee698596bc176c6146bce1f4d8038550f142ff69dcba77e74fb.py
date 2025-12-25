code = """import json

path = locals()['var_function-call-2661790456130058223']
with open(path, 'r') as f:
    data = json.load(f)

symbols = data['valid_symbols']
chunk_size = 50
queries = []

for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i + chunk_size]
    union_parts = []
    for sym in chunk:
        # Construct query using format
        # query: SELECT 'SYM' as Symbol, SUM(...) as Up, SUM(...) as Down FROM "SYM" WHERE Date LIKE '2017%'
        part = "SELECT '{0}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{0}\" WHERE Date LIKE '2017%'".format(sym)
        union_parts.append(part)
    
    full_query = " UNION ALL ".join(union_parts)
    queries.append(full_query)

print(queries[0][:500])
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17110094942828308105': 'file_storage/function-call-17110094942828308105.json', 'var_function-call-769695609142017775': 'file_storage/function-call-769695609142017775.json', 'var_function-call-2661790456130058223': 'file_storage/function-call-2661790456130058223.json', 'var_function-call-3680617775405342251': 'file_storage/function-call-3680617775405342251.json'}

exec(code, env_args)
