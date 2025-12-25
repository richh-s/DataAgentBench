code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols from NYSE Arca
file_path = Path(var_call_pXMbR65hIelfL41W7JEhFPOL)
etf_symbols = pd.read_json(file_path).Symbol.tolist()

# Keep only symbols that exist as tables in stocktrade_database
all_tables = var_call_hLVuPI6L7xONlRdbOgimE7aI
valid_symbols = sorted(set(etf_symbols).intersection(set(all_tables)))

# Prepare chunks to query in SQL IN() lists (DuckDB supports reasonably large lists, but we'll chunk to be safe)
chunk_size = 200
chunks = [valid_symbols[i:i+chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
for ch in chunks:
    in_list = ', '.join([f'"{s}"' for s in ch])
    # each subquery checks for any 2015 date with Adj Close > 200 and returns distinct symbol
    q = f"SELECT DISTINCT symbol FROM (" + " UNION ALL ".join([
        f"SELECT '{s}' AS symbol FROM '{s}' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200" for s in ch
    ]) + ")"
    queries.append(q)

result = {
    'valid_symbols': valid_symbols,
    'queries': queries[:3],  # preview first few queries for debugging
    'num_queries': len(queries)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pXMbR65hIelfL41W7JEhFPOL': 'file_storage/call_pXMbR65hIelfL41W7JEhFPOL.json', 'var_call_hLVuPI6L7xONlRdbOgimE7aI': 'file_storage/call_hLVuPI6L7xONlRdbOgimE7aI.json'}

exec(code, env_args)
