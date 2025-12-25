code = """import json

with open(locals()['var_function-call-7175199923807763808'], 'r') as f:
    candidates = json.load(f)

symbols = [c['Symbol'] for c in candidates]
# clean symbols (some might have quotes or weird chars, though usually just letters)
# DuckDB identifiers with special chars need double quotes.

batches = []
batch_size = 50
for i in range(0, len(symbols), batch_size):
    batch_syms = symbols[i:i+batch_size]
    sub_queries = []
    for sym in batch_syms:
        # Escape double quotes in symbol if any (rare)
        safe_sym = sym.replace('"', '""')
        q = f"SELECT '{safe_sym}' as Symbol, Open, Close FROM \"{safe_sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    # Wrap in aggregation to minimize result size
    final_query = f"SELECT Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM ({full_query}) AS T GROUP BY Symbol"
    batches.append(final_query)

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-8419409271616832498': 'file_storage/function-call-8419409271616832498.json', 'var_function-call-4151914565756568448': 'file_storage/function-call-4151914565756568448.json', 'var_function-call-7175199923807763808': 'file_storage/function-call-7175199923807763808.json', 'var_function-call-1526171119472406754': 234, 'var_function-call-761790631451459462': [{'Date': '1987-09-30'}]}

exec(code, env_args)
