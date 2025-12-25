code = """import json, pandas as pd
from datetime import datetime

path = var_call_cmY1EYc6USuwalwuipiyYYv3
with open(path) as f:
    stocks = json.load(f)

symbols = [s['Symbol'] for s in stocks]

# build DuckDB query to count days in 2019 with (High-Low)/Low>0.2 per symbol
cases = []
for sym in symbols:
    cases.append(f"SELECT '{sym}' AS Symbol, COUNT(*) AS cnt FROM '{sym}' WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND Low>0 AND (High-Low)/Low>0.2")
union_query = " UNION ALL ".join(cases)
wrapped = f"SELECT Symbol, cnt FROM ({union_query}) WHERE cnt>0 ORDER BY cnt DESC LIMIT 20;"

result = {'query': wrapped}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cmY1EYc6USuwalwuipiyYYv3': 'file_storage/call_cmY1EYc6USuwalwuipiyYYv3.json', 'var_call_TDVsp11drIRDNtzkNNjX1In5': 'file_storage/call_TDVsp11drIRDNtzkNNjX1In5.json'}

exec(code, env_args)
