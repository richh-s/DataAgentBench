code = """import json

candidates_key = 'var_function-call-13463588165360546647'
candidates_path = locals()[candidates_key]
with open(candidates_path, 'r') as f:
    candidates = json.load(f)

dq = chr(34) # double quote
sq = chr(39) # single quote

queries = []
batch_size = 200

for i in range(0, len(candidates), batch_size):
    batch = candidates[i:i+batch_size]
    parts = []
    for sym in batch:
        # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015%' LIMIT 1
        part = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date LIKE " + sq + "2015%" + sq + " LIMIT 1"
        parts.append(part)
    
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-1439893960657579719': 'file_storage/function-call-1439893960657579719.json', 'var_function-call-8649986010323061245': 'file_storage/function-call-8649986010323061245.json', 'var_function-call-13463588165360546647': 'file_storage/function-call-13463588165360546647.json', 'var_function-call-17317458862947975022': 1435, 'var_function-call-509651819832341598': 'test', 'var_function-call-11057029886172491952': 1435, 'var_function-call-10726267296708852649': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}

exec(code, env_args)
