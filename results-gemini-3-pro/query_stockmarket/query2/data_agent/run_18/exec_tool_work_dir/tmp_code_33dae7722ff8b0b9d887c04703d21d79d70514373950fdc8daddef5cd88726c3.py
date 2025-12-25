code = """import json
path = locals()['var_function-call-3767063324109208335']
with open(path, 'r') as f:
    valid_etfs = json.load(f)

batch = valid_etfs[0:300]
parts = []
q_mark = '"'
for sym in batch:
    part = "SELECT '" + sym + "' as Symbol FROM " + q_mark + sym + q_mark + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND " + q_mark + "Adj Close" + q_mark + " > 200 LIMIT 1"
    parts.append(part)

query = ' UNION ALL '.join(parts)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4802881243625228792': 'file_storage/function-call-4802881243625228792.json', 'var_function-call-16540620887605966298': 'file_storage/function-call-16540620887605966298.json', 'var_function-call-3767063324109208335': 'file_storage/function-call-3767063324109208335.json', 'var_function-call-15698500669381180607': 1435, 'var_function-call-5404336224704908885': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}], 'var_function-call-10637479535566839517': [{'Date': '2018-08-17', 'Open': '11.800000190734863', 'High': '11.81999969482422', 'Low': '11.770000457763672', 'Close': '11.81999969482422', 'Adj Close': '11.81999969482422', 'Volume': '52400'}], 'var_function-call-13395018073721231966': 'Hello', 'var_function-call-1413160523034434505': 1435, 'var_function-call-13211935562279750912': 'SELECT \'AAAU\' as Symbol FROM "AAAU" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1 UNION ALL SELECT \'AADR\' as Symbol FROM "AADR" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1 UNION ALL SELECT \'ABEQ\' as Symbol FROM "ABEQ" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1 UNION ALL SELECT \'ACSG\' as Symbol FROM "ACSG" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1 UNION ALL SELECT \'ACWF\' as Symbol FROM "ACWF" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'}

exec(code, env_args)
