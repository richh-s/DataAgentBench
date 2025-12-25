code = """import json

with open(locals()['var_function-call-5259012974841646173'], 'r') as f:
    stock_info = json.load(f)

with open(locals()['var_function-call-1379129277910281588'], 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

valid_symbols = [x['Symbol'] for x in stock_info if x['Symbol'] in tables_set]
valid_symbols.sort()

batch = valid_symbols[:60]
d_start = "2017-01-01"
d_end = "2017-12-31"

sqls = []
for sym in batch:
    # Construct query using f-string with mixed quotes, careful with escaping
    # We want: SELECT 'SYM' AS Symbol, SUM(...) ... FROM "SYM" WHERE "Date" >= '2017-01-01' ...
    # Python string: "..."
    # Inside: 'SYM' -> '{sym}'
    # Inside: "SYM" -> \"{sym}\"
    # Inside: "Date" -> \"Date\"
    # Inside: '2017-01-01' -> '{d_start}'
    q = "SELECT '{0}' AS Symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS UpDays, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS DownDays FROM \"{0}\" WHERE \"Date\" >= '{1}' AND \"Date\" <= '{2}'".format(sym, d_start, d_end)
    sqls.append(q)

query = " UNION ALL ".join(sqls)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1631585382517793162': [{'ETF': 'N', 'Listing Exchange': 'A', 'COUNT(*)': '27'}, {'ETF': 'N', 'Listing Exchange': 'N', 'COUNT(*)': '234'}, {'ETF': 'N', 'Listing Exchange': 'P', 'COUNT(*)': '9'}, {'ETF': 'N', 'Listing Exchange': 'Q', 'COUNT(*)': '315'}, {'ETF': 'N', 'Listing Exchange': 'Z', 'COUNT(*)': '2'}, {'ETF': 'Y', 'Listing Exchange': 'A', 'COUNT(*)': '1'}, {'ETF': 'Y', 'Listing Exchange': 'P', 'COUNT(*)': '1435'}, {'ETF': 'Y', 'Listing Exchange': 'Q', 'COUNT(*)': '395'}, {'ETF': 'Y', 'Listing Exchange': 'Z', 'COUNT(*)': '334'}], 'var_function-call-5259012974841646173': 'file_storage/function-call-5259012974841646173.json', 'var_function-call-1379129277910281588': 'file_storage/function-call-1379129277910281588.json', 'var_function-call-12960593275565699327': 'test', 'var_function-call-10003054391359112268': 234}

exec(code, env_args)
