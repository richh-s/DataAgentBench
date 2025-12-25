code = """import json

prev_res = locals()['var_function-call-17161419678548834227']
data = json.loads(prev_res)
target_symbols = data['symbols']

table_file = locals()['var_function-call-7632084380373401256']
with open(table_file, 'r') as f:
    tables = json.load(f)

existing_tables = set(tables)
valid_symbols = [s for s in target_symbols if s in existing_tables]

sub_queries = []
for sym in valid_symbols:
    # Use .format to avoid f-string complexity
    # query: SELECT 'SYM' as Symbol, COUNT(*) as Days FROM "SYM" WHERE ...
    q = 'SELECT \'{0}\' as Symbol, COUNT(*) as Days FROM "{0}" WHERE Date LIKE \'2019-%\' AND (High - Low) > 0.2 * Low'.format(sym)
    sub_queries.append(q)

if not sub_queries:
    final_query = "SELECT 'None' as Symbol, 0 as Days"
else:
    final_query = " UNION ALL ".join(sub_queries)
    final_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-8819135185628577805': 'file_storage/function-call-8819135185628577805.json', 'var_function-call-17161419678548834227': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-7632084380373401256': 'file_storage/function-call-7632084380373401256.json'}

exec(code, env_args)
