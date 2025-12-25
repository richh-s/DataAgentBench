code = """import json

key = 'var_function-call-17759206541062733528'
data = locals()[key]
with open(data, 'r') as f:
    valid_symbols = json.load(f)

start = 0
size = 100
end = start + size
batch = valid_symbols[start:end]

parts = []
for s in batch:
    # Use format to avoid messy concatenation
    # Python string delimited by single quotes
    # SQL: SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date GLOB '2015*' LIMIT 1
    # We need to escape single quotes inside the python string
    q = 'SELECT \'{0}\' as Symbol FROM "{0}" WHERE "Adj Close" > 200 AND Date GLOB \'2015*\' LIMIT 1'.format(s)
    parts.append(q)

final_query = ' UNION ALL '.join(parts)

print('__RESULT__:')
print(json.dumps({'query': final_query, 'next': end}))"""

env_args = {'var_function-call-2090132530202969507': 'file_storage/function-call-2090132530202969507.json', 'var_function-call-2090132530202970712': 'file_storage/function-call-2090132530202970712.json', 'var_function-call-17759206541062733528': 'file_storage/function-call-17759206541062733528.json', 'var_function-call-11518138145490088997': 1435, 'var_function-call-8082552596352152953': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}]}

exec(code, env_args)
