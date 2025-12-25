code = """import json

# Load stocks from the first tool result
with open(locals()['var_function-call-17394221856263559090'], 'r') as f:
    stocks_data = json.load(f)

stock_symbols = set()
for item in stocks_data:
    stock_symbols.add(item['Symbol'])

# Load table list from the second tool result
with open(locals()['var_function-call-11377308254159750354'], 'r') as f:
    all_tables = json.load(f)

all_tables_set = set(all_tables)

valid_symbols = [s for s in stock_symbols if s in all_tables_set]

subqueries = []
for sym in valid_symbols:
    # Use .format() to avoid concatenation issues
    q = "SELECT '{0}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{0}\" WHERE Date LIKE '2017-%'".format(sym)
    subqueries.append(q)

full_query = "SELECT Symbol, UpDays, DownDays, (UpDays - DownDays) as Diff FROM (" + " UNION ALL ".join(subqueries) + ") AS T WHERE UpDays > DownDays ORDER BY Diff DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17394221856263559090': 'file_storage/function-call-17394221856263559090.json', 'var_function-call-10593744191349081676': 234, 'var_function-call-11377308254159750354': 'file_storage/function-call-11377308254159750354.json', 'var_function-call-3964402186895143147': 'file_storage/function-call-3964402186895143147.json'}

exec(code, env_args)
