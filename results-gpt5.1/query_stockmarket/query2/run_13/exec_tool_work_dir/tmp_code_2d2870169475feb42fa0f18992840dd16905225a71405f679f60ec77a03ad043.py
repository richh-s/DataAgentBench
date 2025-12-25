code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols from file
path = Path(var_call_8fugLBnQ9hPzZnyDtj0FZ5Ub)
with open(path, 'r') as f:
    etf_records = json.load(f)

symbols = [r['Symbol'] for r in etf_records]

# We'll build a DuckDB SQL query that unions over all relevant symbol tables
# condition: any day in 2015 with "Adj Close" > 200

# To avoid excessively long SQL, keep all and let DuckDB handle it via UNION ALL
union_queries = []
for sym in symbols:
    sym_escaped = sym.replace('"', '""')
    union_queries.append(f"SELECT DISTINCT '{sym_escaped}' AS Symbol FROM '{sym_escaped}' WHERE substr(Date,1,4) = '2015' AND ""Adj Close"" > 200")

final_query = " UNION ALL ".join(union_queries)

result = {
    'duckdb_query': final_query,
}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_13PT3WdOk3xeuZ0YoXo7shas': 'file_storage/call_13PT3WdOk3xeuZ0YoXo7shas.json', 'var_call_8fugLBnQ9hPzZnyDtj0FZ5Ub': 'file_storage/call_8fugLBnQ9hPzZnyDtj0FZ5Ub.json'}

exec(code, env_args)
