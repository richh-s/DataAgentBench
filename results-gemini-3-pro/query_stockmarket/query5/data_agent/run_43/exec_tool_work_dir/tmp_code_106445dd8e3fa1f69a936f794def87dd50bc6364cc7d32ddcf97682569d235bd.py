code = """import json

with open(locals()['var_function-call-16716209027256917724'], 'r') as f:
    valid_stocks = json.load(f)

# Construct the UNION query
queries = []
for stock in valid_stocks:
    symbol = stock['Symbol']
    # Use double quotes for table identifiers
    q = f"""SELECT '{symbol}' as Symbol, COUNT(*) as Days FROM "{symbol}" WHERE "Date" >= '2019-01-01' AND "Date" <= '2019-12-31' AND ("High" - "Low") > 0.20 * "Low" """
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(full_query)"""

env_args = {'var_function-call-5873850458865278019': 'file_storage/function-call-5873850458865278019.json', 'var_function-call-10785221419564258441': 'file_storage/function-call-10785221419564258441.json', 'var_function-call-16716209027256917724': 'file_storage/function-call-16716209027256917724.json', 'var_function-call-139130541756909283': 86}

exec(code, env_args)
