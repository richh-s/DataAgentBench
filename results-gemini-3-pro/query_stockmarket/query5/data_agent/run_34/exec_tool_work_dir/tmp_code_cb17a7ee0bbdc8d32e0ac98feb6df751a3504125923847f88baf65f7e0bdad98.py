code = """import json

# Stock info file
k_stockinfo = 'var_function-call-8819135185628577805'
# Tables file
k_tables = 'var_function-call-7632084380373401256'

with open(locals()[k_stockinfo], 'r') as f:
    companies = json.load(f)
target_symbols = [c['Symbol'] for c in companies]

with open(locals()[k_tables], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

valid_symbols = [s for s in target_symbols if s in existing_tables]

# Create batches
batch_size = 20
batches = [valid_symbols[i:i + batch_size] for i in range(0, len(valid_symbols), batch_size)]

queries = []
for batch in batches:
    sub_qs = []
    for s in batch:
        q = "SELECT '" + s + "' as Symbol, COUNT(*) as Days FROM " + '"' + s + '"' + " WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
        sub_qs.append(q)
    
    full_q = " UNION ALL ".join(sub_qs) + " ORDER BY Days DESC"
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-8819135185628577805': 'file_storage/function-call-8819135185628577805.json', 'var_function-call-17161419678548834227': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-7632084380373401256': 'file_storage/function-call-7632084380373401256.json', 'var_function-call-6572907001312719127': 'test', 'var_function-call-6969111824348634713': 'file_storage/function-call-6969111824348634713.json'}

exec(code, env_args)
