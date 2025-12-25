code = """import json

with open(locals()['var_function-call-16142873375800227589'], 'r') as f:
    valid_stocks = json.load(f)

queries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    table_name = f'"{sym}"'
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM {table_name} WHERE Date LIKE '2017%'"
    queries.append(q)

chunks = []
chunk_size = 50
current_chunk = []
for i, q in enumerate(queries):
    current_chunk.append(q)
    if (i + 1) % chunk_size == 0:
        chunks.append(" UNION ALL ".join(current_chunk))
        current_chunk = []
if current_chunk:
    chunks.append(" UNION ALL ".join(current_chunk))

print(f"Number of chunks: {len(chunks)}")
print("__RESULT__:")
print(json.dumps(chunks))"""

env_args = {'var_function-call-13183360315961424541': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8321990054734025246': 'file_storage/function-call-8321990054734025246.json', 'var_function-call-10055054036662575247': 'file_storage/function-call-10055054036662575247.json', 'var_function-call-16142873375800227589': 'file_storage/function-call-16142873375800227589.json', 'var_function-call-2297670517589288414': 'file_storage/function-call-2297670517589288414.json'}

exec(code, env_args)
