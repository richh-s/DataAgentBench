code = """import json

with open(locals()['var_function-call-7696497825496925581'], 'r') as f:
    valid_etfs = json.load(f)

# Batch size
batch_size = 200
queries = []

for i in range(0, len(valid_etfs), batch_size):
    batch = valid_etfs[i:i+batch_size]
    subqueries = []
    for sym in batch:
        # DuckDB table names are the symbols. Double quote them just in case.
        # Check date format. The description says Date is str. Usually 'YYYY-MM-DD'.
        # Using SUBSTR or LIKE or BETWEEN string comparison works for ISO dates.
        subqueries.append(f"SELECT '{sym}' as Symbol, MAX(\"Adj Close\") as max_price FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    
    full_query = "SELECT Symbol FROM (" + " UNION ALL ".join(subqueries) + ") WHERE max_price > 200"
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-11251300445025460794': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-3995568477858160008': 'file_storage/function-call-3995568477858160008.json', 'var_function-call-16997364755516220008': 'file_storage/function-call-16997364755516220008.json', 'var_function-call-7696497825496925581': 'file_storage/function-call-7696497825496925581.json', 'var_function-call-14061231607560525758': 1435}

exec(code, env_args)
