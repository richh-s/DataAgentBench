code = """import json
from string import Template

path = locals()['var_function-call-16488807000991432586']
with open(path, 'r') as f:
    valid_stocks = json.load(f)

t = Template("SELECT '$sym' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"$sym\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'")

queries = []
idx = 0
limit = len(valid_stocks)
while idx < limit:
    batch = valid_stocks[idx : idx+10]
    subs = []
    for s in batch:
        sym = s['Symbol']
        q = t.substitute(sym=sym)
        subs.append(q)
    full = " UNION ALL ".join(subs)
    queries.append(full)
    idx += 10

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json', 'var_function-call-16488807000991432586': 'file_storage/function-call-16488807000991432586.json', 'var_function-call-8713500348890617850': 'file_storage/function-call-8713500348890617850.json', 'var_function-call-17926699237147091837': 'file_storage/function-call-17926699237147091837.json', 'var_function-call-7020907782818588183': 'file_storage/function-call-7020907782818588183.json', 'var_function-call-7283447733642380468': 'file_storage/function-call-7283447733642380468.json', 'var_function-call-12899865857835714171': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIV' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIZP' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AJRD' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AL' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMP' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMT' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'ARD' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'", 'var_function-call-4904435431116269525': 'file_storage/function-call-4904435431116269525.json'}

exec(code, env_args)
