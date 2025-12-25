code = """import json, pandas as pd
from pathlib import Path

symbols_file = Path(var_call_tbB0p7fD7qBqdk6JWhPTBi7a)
all_symbols = json.loads(symbols_file.read_text())

nyse_meta_file = Path(var_call_VXY93cvngCXxTpY6a7LHv1KV)
nyse_meta = pd.read_json(nyse_meta_file)

valid_syms = set(nyse_meta['Symbol']) & set(all_symbols)

queries = []
for sym in sorted(valid_syms):
    queries.append(f"SELECT '" + sym + "' AS Symbol, Date, Open, Close FROM '" + sym + "' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31';")

batch_size = 200
batches = []
for i in range(0, len(queries), batch_size):
    batch = " UNION ALL ".join(queries[i:i+batch_size])
    batches.append(batch)

result = json.dumps(batches)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_tbB0p7fD7qBqdk6JWhPTBi7a': 'file_storage/call_tbB0p7fD7qBqdk6JWhPTBi7a.json', 'var_call_VXY93cvngCXxTpY6a7LHv1KV': 'file_storage/call_VXY93cvngCXxTpY6a7LHv1KV.json'}

exec(code, env_args)
