code = """import json, pandas as pd
from pathlib import Path

file_path = Path(var_call_pXMbR65hIelfL41W7JEhFPOL)
etf_symbols = pd.read_json(file_path)["Symbol"].tolist()
all_tables = var_call_hLVuPI6L7xONlRdbOgimE7aI
valid_symbols = sorted(set(etf_symbols).intersection(set(all_tables)))

chunk_size = 50
chunks = [valid_symbols[i:i+chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

subqueries = []
for s in valid_symbols:
    subqueries.append("SELECT '" + s + "' AS symbol FROM '" + s + "' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200")

full_query = "SELECT DISTINCT symbol FROM (" + " UNION ALL ".join(subqueries) + ") ORDER BY symbol;"

result = {"num_valid_symbols": len(valid_symbols), "full_query_preview": full_query[:1000]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pXMbR65hIelfL41W7JEhFPOL': 'file_storage/call_pXMbR65hIelfL41W7JEhFPOL.json', 'var_call_hLVuPI6L7xONlRdbOgimE7aI': 'file_storage/call_hLVuPI6L7xONlRdbOgimE7aI.json'}

exec(code, env_args)
