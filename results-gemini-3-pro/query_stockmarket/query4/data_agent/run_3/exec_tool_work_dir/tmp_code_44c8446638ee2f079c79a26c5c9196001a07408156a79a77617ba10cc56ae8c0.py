code = """import json

path_stock_info = locals()['var_function-call-6994133641640717647']
path_table_list = locals()['var_function-call-7500770919421141587']

with open(path_stock_info, 'r') as f:
    stock_info = json.load(f)

with open(path_table_list, 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)

valid_stocks = []
for item in stock_info:
    sym = item['Symbol']
    if sym in table_set:
        valid_stocks.append(item['Symbol'])

# Batch 1: 0-50
batch1 = valid_stocks[0:50]
print("__RESULT__:")
print(json.dumps(batch1))"""

env_args = {'var_function-call-13244064727740908215': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-6994133641640717647': 'file_storage/function-call-6994133641640717647.json', 'var_function-call-7500770919421141587': 'file_storage/function-call-7500770919421141587.json', 'var_function-call-14226490353414640844': 'file_storage/function-call-14226490353414640844.json', 'var_function-call-17306934327563602439': 'file_storage/function-call-17306934327563602439.json', 'var_function-call-15177514065940846099': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIV' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 EN", 'var_function-call-17941359181254689150': 'file_storage/function-call-17941359181254689150.json', 'var_function-call-16315239115940050316': 'file_storage/function-call-16315239115940050316.json'}

exec(code, env_args)
