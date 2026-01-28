code = """import json
path = var_call_0iR8WlQ5ARF8bgujNkAIgkQb
if isinstance(path, str) and path.endswith('.json'):
    with open(path,'r') as f:
        payload = json.load(f)
else:
    payload = path
symbols = payload['symbols']

# chunk symbols for SQL generation
chunks = [symbols[i:i+300] for i in range(0, len(symbols), 300)]

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        t = sym.replace('"','""')
        parts.append(f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_chunks': len(queries), 'n_symbols': len(symbols)}))"""

env_args = {'var_call_y7ZF0nkKnhjCsARv9z2cAVOg': 'file_storage/call_y7ZF0nkKnhjCsARv9z2cAVOg.json', 'var_call_meoUs7y7uUlDfzjL99xuAS8N': 'file_storage/call_meoUs7y7uUlDfzjL99xuAS8N.json', 'var_call_0iR8WlQ5ARF8bgujNkAIgkQb': 'file_storage/call_0iR8WlQ5ARF8bgujNkAIgkQb.json'}

exec(code, env_args)
