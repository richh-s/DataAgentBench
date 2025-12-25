code = """import json

key1 = 'var_function-call-17394221856263559090'
key2 = 'var_function-call-11377308254159750354'

path1 = locals()[key1]
path2 = locals()[key2]

with open(path1, 'r') as f:
    stocks_data = json.load(f)

with open(path2, 'r') as f:
    all_tables = json.load(f)

stock_symbols = [item['Symbol'] for item in stocks_data]
all_tables_set = set(all_tables)

valid_symbols = [s for s in stock_symbols if s in all_tables_set]

subqueries = []
for sym in valid_symbols:
    # Construct query parts
    # Ensure sym is safe? They are stock symbols, usually alphanum.
    # We wrap table name in double quotes.
    part = "SELECT '{0}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{0}\" WHERE Date LIKE '2017-%'".format(sym)
    subqueries.append(part)

# Join with UNION ALL
union_part = " UNION ALL ".join(subqueries)
full_query = "SELECT Symbol, UpDays, DownDays, (UpDays - DownDays) as Diff FROM (" + union_part + ") AS T WHERE UpDays > DownDays ORDER BY Diff DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17394221856263559090': 'file_storage/function-call-17394221856263559090.json', 'var_function-call-10593744191349081676': 234, 'var_function-call-11377308254159750354': 'file_storage/function-call-11377308254159750354.json', 'var_function-call-3964402186895143147': 'file_storage/function-call-3964402186895143147.json'}

exec(code, env_args)
