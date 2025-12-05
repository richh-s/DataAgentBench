code = """import json
import pandas as pd

symbols_info = json.load(open(var_call_Cc3eRRR6J0KHUKBg4fNL3Eu0))
nyse_symbols = [row["Symbol"] for row in symbols_info]

# Prepare queries for a manageable subset: we'll compute per-symbol stats via DuckDB SQL later.
# Build a DuckDB SQL that unions all symbol tables with a symbol column.

parts = []
for sym in nyse_symbols:
    safe = sym.replace('"','')
    parts.append(f"SELECT '{safe}' AS Symbol, Date, Open, Close FROM '{safe}' WHERE substr(Date,1,4) = '2017'")

union_sql = " UNION ALL ".join(parts)

result = {
  "union_sql_prefix": "WITH all_data AS (" + union_sql + ") ",
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Q4TUNNhQcj1EUic3uk4c7EwM': 'file_storage/call_Q4TUNNhQcj1EUic3uk4c7EwM.json', 'var_call_Cc3eRRR6J0KHUKBg4fNL3Eu0': 'file_storage/call_Cc3eRRR6J0KHUKBg4fNL3Eu0.json'}

exec(code, env_args)
