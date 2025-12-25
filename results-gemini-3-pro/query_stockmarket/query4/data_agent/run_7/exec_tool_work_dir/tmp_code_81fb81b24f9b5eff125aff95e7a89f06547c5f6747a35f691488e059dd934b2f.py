code = """import json

k1 = 'var_function-call-7866507991507907549'
k2 = 'var_function-call-10532225946016359418'

with open(locals()[k1], 'r') as f:
    stock_info = json.load(f)
with open(locals()[k2], 'r') as f:
    trade_tables = json.load(f)

trade_table_set = set(trade_tables)
valid_stocks = [s for s in stock_info if s['Symbol'] in trade_table_set]

batch_size = 40
batches = []
current_batch = []
for s in valid_stocks:
    current_batch.append(s)
    if len(current_batch) == batch_size:
        batches.append(current_batch)
        current_batch = []
if current_batch:
    batches.append(current_batch)

queries = []
for batch in batches:
    q_parts = []
    for s in batch:
        sym = s['Symbol']
        # Concatenation to avoid f-string quote issues
        part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        q_parts.append(part)
    queries.append(" UNION ALL ".join(q_parts))

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-9385571556607626088': [{'Listing Exchange': 'P', 'ETF': 'Y'}, {'Listing Exchange': 'Q', 'ETF': 'N'}, {'Listing Exchange': 'Q', 'ETF': 'Y'}, {'Listing Exchange': 'Z', 'ETF': 'Y'}, {'Listing Exchange': 'A', 'ETF': 'N'}, {'Listing Exchange': 'N', 'ETF': 'N'}, {'Listing Exchange': 'Z', 'ETF': 'N'}, {'Listing Exchange': 'P', 'ETF': 'N'}, {'Listing Exchange': 'A', 'ETF': 'Y'}], 'var_function-call-7866507991507907549': 'file_storage/function-call-7866507991507907549.json', 'var_function-call-10532225946016359418': 'file_storage/function-call-10532225946016359418.json', 'var_function-call-8481153809243930007': 'file_storage/function-call-8481153809243930007.json', 'var_function-call-8913912655945995998': 'OK', 'var_function-call-10355738453148462456': {'count': 234, 'length': 48697}, 'var_function-call-1951639193161404054': 'file_storage/function-call-1951639193161404054.json', 'var_function-call-4615786134177112358': 'file_storage/function-call-4615786134177112358.json', 'var_function-call-2099965776381648769': 10402}

exec(code, env_args)
