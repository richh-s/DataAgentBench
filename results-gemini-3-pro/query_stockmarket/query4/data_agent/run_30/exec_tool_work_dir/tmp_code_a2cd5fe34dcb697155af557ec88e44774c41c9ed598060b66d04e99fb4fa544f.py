code = """import json

with open(locals()['var_function-call-5259012974841646173'], 'r') as f:
    stock_info = json.load(f)

with open(locals()['var_function-call-1379129277910281588'], 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

valid_symbols = [x['Symbol'] for x in stock_info if x['Symbol'] in tables_set]
valid_symbols.sort()

batch_size = 40
batches = []
for i in range(0, len(valid_symbols), batch_size):
    batches.append(valid_symbols[i:i+batch_size])

d_start = "2017-01-01"
d_end = "2017-12-31"
sq = chr(39)
dq = chr(34)

queries = []
for batch in batches:
    sqls = []
    for sym in batch:
        q = "SELECT " + sq + sym + sq + " AS Symbol, " + \
            "SUM(CASE WHEN " + dq + "Close" + dq + " > " + dq + "Open" + dq + " THEN 1 ELSE 0 END) AS UpDays, " + \
            "SUM(CASE WHEN " + dq + "Close" + dq + " < " + dq + "Open" + dq + " THEN 1 ELSE 0 END) AS DownDays " + \
            "FROM " + dq + sym + dq + " " + \
            "WHERE " + dq + "Date" + dq + " >= " + sq + d_start + sq + " AND " + dq + "Date" + dq + " <= " + sq + d_end + sq
        sqls.append(q)
    queries.append(" UNION ALL ".join(sqls))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-1631585382517793162': [{'ETF': 'N', 'Listing Exchange': 'A', 'COUNT(*)': '27'}, {'ETF': 'N', 'Listing Exchange': 'N', 'COUNT(*)': '234'}, {'ETF': 'N', 'Listing Exchange': 'P', 'COUNT(*)': '9'}, {'ETF': 'N', 'Listing Exchange': 'Q', 'COUNT(*)': '315'}, {'ETF': 'N', 'Listing Exchange': 'Z', 'COUNT(*)': '2'}, {'ETF': 'Y', 'Listing Exchange': 'A', 'COUNT(*)': '1'}, {'ETF': 'Y', 'Listing Exchange': 'P', 'COUNT(*)': '1435'}, {'ETF': 'Y', 'Listing Exchange': 'Q', 'COUNT(*)': '395'}, {'ETF': 'Y', 'Listing Exchange': 'Z', 'COUNT(*)': '334'}], 'var_function-call-5259012974841646173': 'file_storage/function-call-5259012974841646173.json', 'var_function-call-1379129277910281588': 'file_storage/function-call-1379129277910281588.json', 'var_function-call-12960593275565699327': 'test', 'var_function-call-10003054391359112268': 234, 'var_function-call-369512805512173966': 'file_storage/function-call-369512805512173966.json'}

exec(code, env_args)
