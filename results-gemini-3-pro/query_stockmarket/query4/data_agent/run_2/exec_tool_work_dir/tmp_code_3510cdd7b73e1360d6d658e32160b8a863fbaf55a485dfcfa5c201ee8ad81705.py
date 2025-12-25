code = """import json

key_info = 'var_function-call-6223047370472614305'
key_tables = 'var_function-call-14531105657415532109'

with open(locals()[key_info], 'r') as f:
    stock_info = json.load(f)

with open(locals()[key_tables], 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
valid_stocks = [s for s in stock_info if s['Symbol'] in tables_set]

batch_size = 40
batches = []
for i in range(0, len(valid_stocks), batch_size):
    batch_stocks = valid_stocks[i:i+batch_size]
    queries = []
    for s in batch_stocks:
        sym = s['Symbol']
        part1 = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "
        part2 = '"' + sym + '"'
        part3 = " WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        q = part1 + part2 + part3
        queries.append(q)
    
    full_query = " UNION ALL ".join(queries)
    batches.append(full_query)

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-5334989958488010331': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-6223047370472614305': 'file_storage/function-call-6223047370472614305.json', 'var_function-call-14531105657415532109': 'file_storage/function-call-14531105657415532109.json', 'var_function-call-202123142740787655': 'file_storage/function-call-202123142740787655.json', 'var_function-call-8729269538483017222': 'file_storage/function-call-8729269538483017222.json', 'var_function-call-1757640261265007625': 'file_storage/function-call-1757640261265007625.json', 'var_function-call-16867911136147506242': {'test_query': 'SELECT \'AEFC\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "AEFC" WHERE Date >= \'2017-01-01\' AND Date <= \'2017-12-31\' UNION ALL SELECT \'AIN\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "AIN" WHERE Date >= \'2017-01-01\' AND Date <= \'2017-12-31\' UNION ALL SELECT \'AIV\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "AIV" WHERE Date >= \'2017-01-01\' AND Date <= \'2017-12-31\' UNION ALL SELECT \'AIZP\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "AIZP" WHERE Date >= \'2017-01-01\' AND Date <= \'2017-12-31\' UNION ALL SELECT \'AJRD\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "AJRD" WHERE Date >= \'2017-01-01\' AND Date <= \'2017-12-31\'', 'count': 234}, 'var_function-call-14227305067111493734': 'file_storage/function-call-14227305067111493734.json', 'var_function-call-72107816898648281': 'file_storage/function-call-72107816898648281.json'}

exec(code, env_args)
