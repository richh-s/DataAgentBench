code = """import json

p1 = locals()['var_function-call-17394221856263559090']
with open(p1, 'r') as f:
    data = json.load(f)

syms = []
for x in data:
    syms.append(x['Symbol'])

p2 = locals()['var_function-call-11377308254159750354']
with open(p2, 'r') as f:
    tables = json.load(f)

table_set = set(tables)

valid = []
for s in syms:
    if s in table_set:
        valid.append(s)

parts = []
for s in valid:
    q = 'SELECT \'' + s + '\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "' + s + '" WHERE Date LIKE \'2017-%\''
    parts.append(q)

query = 'SELECT Symbol, UpDays, DownDays, (UpDays - DownDays) as Diff FROM (' + ' UNION ALL '.join(parts) + ') AS T WHERE UpDays > DownDays ORDER BY Diff DESC LIMIT 5'

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-17394221856263559090': 'file_storage/function-call-17394221856263559090.json', 'var_function-call-10593744191349081676': 234, 'var_function-call-11377308254159750354': 'file_storage/function-call-11377308254159750354.json', 'var_function-call-3964402186895143147': 'file_storage/function-call-3964402186895143147.json', 'var_function-call-4874700308804664864': "SELECT Symbol, UpDays, DownDays, (UpDays - DownDays) as Diff FROM (SELECT 'RES' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date LIKE '2017-%' UNION ALL SELECT 'SCU' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date LIKE '2017-%' UNION ALL SELECT 'EMP' as Symbol, SUM(CASE WHEN Close > Open THEN", 'var_function-call-16688584209313452893': 'Success'}

exec(code, env_args)
