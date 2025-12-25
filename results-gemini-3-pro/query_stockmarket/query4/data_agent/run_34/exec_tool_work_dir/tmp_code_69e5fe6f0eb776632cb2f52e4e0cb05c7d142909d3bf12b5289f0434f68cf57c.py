code = """import json

stock_info_path = locals()['var_function-call-392181113941230713']
table_list_path = locals()['var_function-call-4237662191302365216']

with open(stock_info_path, 'r') as f:
    stock_info_list = json.load(f)

with open(table_list_path, 'r') as f:
    table_list = json.load(f)

tables_set = set(table_list)
valid_stocks = [s for s in stock_info_list if s['Symbol'] in tables_set]

batches = []
batch_size = 30
current_batch = []

q_quote = '"'

for stock in valid_stocks:
    sym = stock['Symbol']
    # Explicitly construct string
    # SELECT 'SYM' ... FROM "SYM" ...
    query_part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM " + q_quote + sym + q_quote + " WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'"
    
    current_batch.append(query_part)
    
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-392181113941230713': 'file_storage/function-call-392181113941230713.json', 'var_function-call-4237662191302365216': 'file_storage/function-call-4237662191302365216.json', 'var_function-call-8581997054017550761': 'file_storage/function-call-8581997054017550761.json', 'var_function-call-8534971037616957309': 5, 'var_function-call-567110415672703925': 'file_storage/function-call-567110415672703925.json', 'var_function-call-16210328402544364133': 1, 'var_function-call-4836066797045152': 49867, 'var_function-call-7784901137825621263': 'file_storage/function-call-7784901137825621263.json', 'var_function-call-17382793757603389943': 3, 'var_function-call-12942682433609470340': 'file_storage/function-call-12942682433609470340.json', 'var_function-call-8095609401205535600': 'file_storage/function-call-8095609401205535600.json', 'var_function-call-3459103335512213665': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date BETWEEN '2017-01-01' AND '2017-12-31' UNION ALL SELECT 'AIN' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date BETWEEN '2017-01-01' AND '2017-12-31' UNION ALL SELECT 'AIV' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as "}

exec(code, env_args)
