code = """import json

path = locals()['var_function-call-6178811675160687356']
with open(path, 'r') as f:
    valid_stocks = json.load(f)

# Batch 1: 0-30
batch = valid_stocks[0:30]
symbols = [s['Symbol'] for s in batch]

parts = []
for sym in symbols:
    part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    parts.append(part)

full_query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-305604398678755186': 'file_storage/function-call-305604398678755186.json', 'var_function-call-2255113569688009603': 'file_storage/function-call-2255113569688009603.json', 'var_function-call-6178811675160687356': 'file_storage/function-call-6178811675160687356.json', 'var_function-call-8115388233719900790': 234, 'var_function-call-15435093583648170680': 'file_storage/function-call-15435093583648170680.json', 'var_function-call-8942524775287786217': 'file_storage/function-call-8942524775287786217.json', 'var_function-call-18114813024732574471': 'file_storage/function-call-18114813024732574471.json'}

exec(code, env_args)
