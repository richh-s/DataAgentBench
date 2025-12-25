code = """import json

# Load symbols
with open(locals()['var_function-call-5259012974841646173'], 'r') as f:
    stock_info = json.load(f)

# Load tables
with open(locals()['var_function-call-1379129277910281588'], 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

valid_symbols = []
for item in stock_info:
    sym = item['Symbol']
    if sym in tables_set:
        valid_symbols.append(sym)

valid_symbols.sort()

# Batch 1: 0 to 60
batch_symbols = valid_symbols[0:60]

subqueries = []
for sym in batch_symbols:
    # SQL query construction
    # We use single quotes for python string literal
    q = 'SELECT \'' + sym + '\' AS Symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) AS UpDays, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) AS DownDays FROM "' + sym + '" WHERE "Date" >= \'2017-01-01\' AND "Date" <= \'2017-12-31\''
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-1631585382517793162': [{'ETF': 'N', 'Listing Exchange': 'A', 'COUNT(*)': '27'}, {'ETF': 'N', 'Listing Exchange': 'N', 'COUNT(*)': '234'}, {'ETF': 'N', 'Listing Exchange': 'P', 'COUNT(*)': '9'}, {'ETF': 'N', 'Listing Exchange': 'Q', 'COUNT(*)': '315'}, {'ETF': 'N', 'Listing Exchange': 'Z', 'COUNT(*)': '2'}, {'ETF': 'Y', 'Listing Exchange': 'A', 'COUNT(*)': '1'}, {'ETF': 'Y', 'Listing Exchange': 'P', 'COUNT(*)': '1435'}, {'ETF': 'Y', 'Listing Exchange': 'Q', 'COUNT(*)': '395'}, {'ETF': 'Y', 'Listing Exchange': 'Z', 'COUNT(*)': '334'}], 'var_function-call-5259012974841646173': 'file_storage/function-call-5259012974841646173.json', 'var_function-call-1379129277910281588': 'file_storage/function-call-1379129277910281588.json'}

exec(code, env_args)
