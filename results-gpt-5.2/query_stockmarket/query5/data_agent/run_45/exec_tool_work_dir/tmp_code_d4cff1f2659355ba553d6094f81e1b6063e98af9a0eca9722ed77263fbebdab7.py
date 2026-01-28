code = """import json, pandas as pd

# load full symbols list
path = var_call_amLl3egspmPXOWcjN0p7lmdH
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# keep unique symbols
symbols = sorted(df['Symbol'].dropna().unique().tolist())
# output chunks for querying duckdb
chunk_size = 200
chunks = [symbols[i:i+chunk_size] for i in range(0, len(symbols), chunk_size)]

out = {
    'n_symbols': len(symbols),
    'chunk_size': chunk_size,
    'n_chunks': len(chunks),
    'chunks': chunks
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_amLl3egspmPXOWcjN0p7lmdH': 'file_storage/call_amLl3egspmPXOWcjN0p7lmdH.json'}

exec(code, env_args)
