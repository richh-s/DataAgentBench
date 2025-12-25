code = """import json
with open(locals()['var_function-call-16362459510034057729'], 'r') as f:
    batches = json.load(f)
print("__RESULT__:")
print(len(batches))"""

env_args = {'var_function-call-392181113941230713': 'file_storage/function-call-392181113941230713.json', 'var_function-call-4237662191302365216': 'file_storage/function-call-4237662191302365216.json', 'var_function-call-8581997054017550761': 'file_storage/function-call-8581997054017550761.json', 'var_function-call-8534971037616957309': 5, 'var_function-call-567110415672703925': 'file_storage/function-call-567110415672703925.json', 'var_function-call-16210328402544364133': 1, 'var_function-call-4836066797045152': 49867, 'var_function-call-7784901137825621263': 'file_storage/function-call-7784901137825621263.json', 'var_function-call-17382793757603389943': 3, 'var_function-call-12942682433609470340': 'file_storage/function-call-12942682433609470340.json', 'var_function-call-8095609401205535600': 'file_storage/function-call-8095609401205535600.json', 'var_function-call-3459103335512213665': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date BETWEEN '2017-01-01' AND '2017-12-31' UNION ALL SELECT 'AIN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date BETWEEN '2017-01-01' AND '2017-12-31' UNION ALL SELECT 'AIV' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as ", 'var_function-call-16362459510034057729': 'file_storage/function-call-16362459510034057729.json'}

exec(code, env_args)
