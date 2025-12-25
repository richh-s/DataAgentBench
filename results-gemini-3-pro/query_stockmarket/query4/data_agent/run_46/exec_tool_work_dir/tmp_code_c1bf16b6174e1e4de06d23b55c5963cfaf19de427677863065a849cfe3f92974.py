code = """import json

path = locals()['var_function-call-7175199923807763808']
with open(path, 'r') as f:
    candidates = json.load(f)

symbols = [c['Symbol'] for c in candidates]
dq = chr(34)
batches = []
batch_size = 50
for i in range(0, len(symbols), batch_size):
    batch_syms = symbols[i:i+batch_size]
    sub_queries = []
    for s in batch_syms:
        # Use chr(34) for double quotes
        q = "SELECT '{0}' as Symbol, Open, Close FROM {1}{0}{1} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s, dq)
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    final_query = "SELECT Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM (" + full_query + ") AS T GROUP BY Symbol"
    batches.append(final_query)

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-8419409271616832498': 'file_storage/function-call-8419409271616832498.json', 'var_function-call-4151914565756568448': 'file_storage/function-call-4151914565756568448.json', 'var_function-call-7175199923807763808': 'file_storage/function-call-7175199923807763808.json', 'var_function-call-1526171119472406754': 234, 'var_function-call-761790631451459462': [{'Date': '1987-09-30'}], 'var_function-call-13952986258041756676': 'file_storage/function-call-13952986258041756676.json', 'var_function-call-10146214134899326186': 'file_storage/function-call-10146214134899326186.json', 'var_function-call-14865291104312683632': 'test', 'var_function-call-18363194978560378977': 234, 'var_function-call-16116604006856398769': "SELECT 'AEFC' FROM  + s + ", 'var_function-call-7692130935674395296': 'SELECT \'AEFC\' FROM "AEFC"'}

exec(code, env_args)
