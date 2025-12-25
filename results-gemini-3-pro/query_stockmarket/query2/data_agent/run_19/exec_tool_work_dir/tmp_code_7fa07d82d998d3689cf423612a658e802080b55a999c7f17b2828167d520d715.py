code = """import json

file_path = locals()['var_function-call-5272747618015611523']
with open(file_path, 'r') as f:
    symbols = json.load(f)

batch_size = 100
batch_index = 0
current_batch = symbols[batch_index * batch_size : (batch_index + 1) * batch_size]

sqls = []
for sym in current_batch:
    sql = 'SELECT \'' + sym + '\' as Symbol FROM "' + sym + '" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
    sqls.append(sql)

full_query = ' UNION ALL '.join(sqls)
print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-15019476064265417806': 'file_storage/function-call-15019476064265417806.json', 'var_function-call-12714238496890411672': 'file_storage/function-call-12714238496890411672.json', 'var_function-call-3672506294669525336': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}, {'Date': '1993-02-03', 'Open': '44.40625', 'High': '44.84375', 'Low': '44.375', 'Close': '44.8125', 'Adj Close': '26.822998046875', 'Volume': '529400'}, {'Date': '1993-02-04', 'Open': '44.96875', 'High': '45.09375', 'Low': '44.46875', 'Close': '45.0', 'Adj Close': '26.93523979187012', 'Volume': '531500'}], 'var_function-call-1344159288898466446': 'file_storage/function-call-1344159288898466446.json', 'var_function-call-5272747618015611523': 'file_storage/function-call-5272747618015611523.json', 'var_function-call-610833976628790432': 'ok'}

exec(code, env_args)
