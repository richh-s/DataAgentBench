code = """import json, pandas as pd
from pathlib import Path

file_path = var_call_NOJ0c1QGDoSUPK9z1e6oAuUs
symbols = pd.read_json(file_path)

tickers = symbols['Symbol'].tolist()

queries = []
for sym in tickers:
    q = f"SELECT '{sym}' AS Symbol, Date, \"Adj Close\" FROM '{sym}' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1;"
    queries.append(q)

union_query = " UNION ALL ".join(queries)

result = union_query
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NOJ0c1QGDoSUPK9z1e6oAuUs': 'file_storage/call_NOJ0c1QGDoSUPK9z1e6oAuUs.json', 'var_call_GeAFYgJgfZcZO7EUXTbvTAGm': 'file_storage/call_GeAFYgJgfZcZO7EUXTbvTAGm.json'}

exec(code, env_args)
