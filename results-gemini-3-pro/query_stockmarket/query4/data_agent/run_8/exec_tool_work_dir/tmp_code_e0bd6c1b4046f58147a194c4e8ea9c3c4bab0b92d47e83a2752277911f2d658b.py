code = """import json

file_path = locals()['var_function-call-16454938009871797883']
with open(file_path, 'r') as f:
    data = json.load(f)

symbols = [item['Symbol'] for item in data]

sub_parts = []
for sym in symbols:
    part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date LIKE '2017-%'"
    sub_parts.append(part)

full_query = " UNION ALL ".join(sub_parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16454938009871797883': 'file_storage/function-call-16454938009871797883.json', 'var_function-call-10799014059080565467': 234, 'var_function-call-9461046351128459538': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'High': '15.701873779296877', 'Low': '14.988152503967283', 'Close': '15.107105255126951', 'Adj Close': '8.918145179748535', 'Volume': '2292200'}, {'Date': '1987-10-01', 'Open': '15.107105255126951', 'High': '15.345012664794922', 'Low': '14.988152503967283', 'Close': '15.345012664794922', 'Adj Close': '9.05859375', 'Volume': '468200'}, {'Date': '1987-10-02', 'Open': '15.345012664794922', 'High': '15.701873779296877', 'Low': '15.107105255126951', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '371600'}, {'Date': '1987-10-05', 'Open': '15.701873779296877', 'High': '15.701873779296877', 'Low': '15.226058959960938', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '121300'}, {'Date': '1987-10-06', 'Open': '15.58292007446289', 'High': '15.58292007446289', 'Low': '15.226058959960938', 'Close': '15.463966369628906', 'Adj Close': '9.128814697265623', 'Volume': '159300'}], 'var_function-call-16114058926543819225': 'file_storage/function-call-16114058926543819225.json', 'var_function-call-8823083836591245832': 'file_storage/function-call-8823083836591245832.json'}

exec(code, env_args)
