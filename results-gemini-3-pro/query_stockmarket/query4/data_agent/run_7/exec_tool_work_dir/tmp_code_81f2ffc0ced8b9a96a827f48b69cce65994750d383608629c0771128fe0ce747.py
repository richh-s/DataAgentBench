code = """import json

k1 = 'var_function-call-7866507991507907549'
k2 = 'var_function-call-10532225946016359418'
# Using global access or locals
val1 = locals().get(k1)
val2 = locals().get(k2)

if not val1 or not val2:
    print('__RESULT__:')
    print(json.dumps('ERROR: Keys not found'))
else:
    with open(val1, 'r') as f:
        stock_info = json.load(f)
    with open(val2, 'r') as f:
        trade_tables = json.load(f)

    trade_table_set = set(trade_tables)
    valid_stocks = [s for s in stock_info if s['Symbol'] in trade_table_set]

    # Construct query
    queries = []
    for s in valid_stocks:
        sym = s['Symbol']
        # avoiding backslash quote if possible
        part1 = "SELECT '" + sym + "' as Symbol, "
        part2 = "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, "
        part3 = "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down "
        part4 = "FROM \"" + sym + "\" "
        part5 = "WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        q = part1 + part2 + part3 + part4 + part5
        queries.append(q)

    full_query = ' UNION ALL '.join(queries)
    
    # Check length
    if len(full_query) > 200000:
        res = {'status': 'TOO_LONG', 'queries': queries}
    else:
        res = full_query

    print('__RESULT__:')
    print(json.dumps(res))"""

env_args = {'var_function-call-9385571556607626088': [{'Listing Exchange': 'P', 'ETF': 'Y'}, {'Listing Exchange': 'Q', 'ETF': 'N'}, {'Listing Exchange': 'Q', 'ETF': 'Y'}, {'Listing Exchange': 'Z', 'ETF': 'Y'}, {'Listing Exchange': 'A', 'ETF': 'N'}, {'Listing Exchange': 'N', 'ETF': 'N'}, {'Listing Exchange': 'Z', 'ETF': 'N'}, {'Listing Exchange': 'P', 'ETF': 'N'}, {'Listing Exchange': 'A', 'ETF': 'Y'}], 'var_function-call-7866507991507907549': 'file_storage/function-call-7866507991507907549.json', 'var_function-call-10532225946016359418': 'file_storage/function-call-10532225946016359418.json'}

exec(code, env_args)
