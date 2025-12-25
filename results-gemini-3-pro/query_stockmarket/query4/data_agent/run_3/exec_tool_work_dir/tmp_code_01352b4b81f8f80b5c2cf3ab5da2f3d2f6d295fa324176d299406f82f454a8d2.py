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

# Batch 2: 50-100
batch2 = valid_stocks[50:100]
print("__RESULT__:")
print(json.dumps(batch2))"""

env_args = {'var_function-call-13244064727740908215': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-6994133641640717647': 'file_storage/function-call-6994133641640717647.json', 'var_function-call-7500770919421141587': 'file_storage/function-call-7500770919421141587.json', 'var_function-call-14226490353414640844': 'file_storage/function-call-14226490353414640844.json', 'var_function-call-17306934327563602439': 'file_storage/function-call-17306934327563602439.json', 'var_function-call-15177514065940846099': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIV' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 EN", 'var_function-call-17941359181254689150': 'file_storage/function-call-17941359181254689150.json', 'var_function-call-16315239115940050316': 'file_storage/function-call-16315239115940050316.json', 'var_function-call-3967640887820786759': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_function-call-14362589638182063743': [{'Symbol': 'AEFC', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'AIN', 'UpDays': '143.0', 'DownDays': '101.0'}, {'Symbol': 'AIV', 'UpDays': '118.0', 'DownDays': '128.0'}, {'Symbol': 'AIZP', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'AJRD', 'UpDays': '123.0', 'DownDays': '123.0'}, {'Symbol': 'AL', 'UpDays': '131.0', 'DownDays': '117.0'}, {'Symbol': 'AMN', 'UpDays': '134.0', 'DownDays': '111.0'}, {'Symbol': 'AMP', 'UpDays': '141.0', 'DownDays': '110.0'}, {'Symbol': 'AMT', 'UpDays': '128.0', 'DownDays': '123.0'}, {'Symbol': 'ARD', 'UpDays': '80.0', 'DownDays': '119.0'}, {'Symbol': 'ARGD', 'UpDays': '133.0', 'DownDays': '82.0'}, {'Symbol': 'ARLO', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'ASG', 'UpDays': '110.0', 'DownDays': '110.0'}, {'Symbol': 'AVA', 'UpDays': '134.0', 'DownDays': '112.0'}, {'Symbol': 'BANC', 'UpDays': '108.0', 'DownDays': '119.0'}, {'Symbol': 'BBU', 'UpDays': '129.0', 'DownDays': '120.0'}, {'Symbol': 'BBVA', 'UpDays': '126.0', 'DownDays': '104.0'}, {'Symbol': 'BDXA', 'UpDays': '83.0', 'DownDays': '77.0'}, {'Symbol': 'BKH', 'UpDays': '134.0', 'DownDays': '115.0'}, {'Symbol': 'BKT', 'UpDays': '105.0', 'DownDays': '97.0'}, {'Symbol': 'BLD', 'UpDays': '131.0', 'DownDays': '120.0'}, {'Symbol': 'BNS', 'UpDays': '132.0', 'DownDays': '117.0'}, {'Symbol': 'BV', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'BZH', 'UpDays': '127.0', 'DownDays': '123.0'}, {'Symbol': 'CADE', 'UpDays': '88.0', 'DownDays': '83.0'}, {'Symbol': 'CAE', 'UpDays': '122.0', 'DownDays': '117.0'}, {'Symbol': 'CAF', 'UpDays': '131.0', 'DownDays': '113.0'}, {'Symbol': 'CBT', 'UpDays': '128.0', 'DownDays': '122.0'}, {'Symbol': 'CCC', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'CCZ', 'UpDays': '17.0', 'DownDays': '10.0'}, {'Symbol': 'CHAP', 'UpDays': '34.0', 'DownDays': '23.0'}, {'Symbol': 'CIA', 'UpDays': '130.0', 'DownDays': '112.0'}, {'Symbol': 'CMA', 'UpDays': '124.0', 'DownDays': '124.0'}, {'Symbol': 'CMI', 'UpDays': '127.0', 'DownDays': '123.0'}, {'Symbol': 'CMSA', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'CNK', 'UpDays': '128.0', 'DownDays': '122.0'}, {'Symbol': 'COTY', 'UpDays': '124.0', 'DownDays': '123.0'}, {'Symbol': 'CRC', 'UpDays': '121.0', 'DownDays': '128.0'}, {'Symbol': 'CRM', 'UpDays': '137.0', 'DownDays': '113.0'}, {'Symbol': 'CRS', 'UpDays': '121.0', 'DownDays': '128.0'}, {'Symbol': 'CSL', 'UpDays': '131.0', 'DownDays': '119.0'}, {'Symbol': 'CTS', 'UpDays': '113.0', 'DownDays': '122.0'}, {'Symbol': 'CUBE', 'UpDays': '133.0', 'DownDays': '113.0'}, {'Symbol': 'CURO', 'UpDays': '9.0', 'DownDays': '7.0'}, {'Symbol': 'CVIA', 'UpDays': 'nan', 'DownDays': 'nan'}, {'Symbol': 'CVX', 'UpDays': '118.0', 'DownDays': '132.0'}, {'Symbol': 'CXH', 'UpDays': '126.0', 'DownDays': '91.0'}, {'Symbol': 'DAC', 'UpDays': '66.0', 'DownDays': '115.0'}, {'Symbol': 'DDS', 'UpDays': '128.0', 'DownDays': '123.0'}, {'Symbol': 'DDT', 'UpDays': '118.0', 'DownDays': '119.0'}]}

exec(code, env_args)
