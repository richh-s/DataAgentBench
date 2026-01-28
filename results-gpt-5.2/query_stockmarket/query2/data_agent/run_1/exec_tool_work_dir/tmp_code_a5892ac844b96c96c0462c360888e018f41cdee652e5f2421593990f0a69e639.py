code = """import json, pandas as pd

# Load stockinfo ETF list (NYSE Arca)
path_info = var_call_Bwf6IfMILxz6M6L9VEXSIh1T
with open(path_info, 'r') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)
etf_symbols = set(df_info['Symbol'].astype(str))

# Load available trade tables
path_tables = var_call_fzLKq8IlpgPul9fghWeKKYUT
with open(path_tables, 'r') as f:
    tables = json.load(f)
df_tables = pd.DataFrame(tables)
avail_tables = set(df_tables['name'].astype(str))

# Candidate symbols that have price tables
candidates = sorted(etf_symbols.intersection(avail_tables))

# Build per-table queries to get max Adj Close in 2015
queries = []
for sym in candidates:
    # DuckDB identifiers need quoting if special chars; assume simple tickers here.
    q = f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01';"
    queries.append(q)

# Chunk UNION ALL to keep query size manageable
chunks = []
chunk_size = 200
for i in range(0, len(queries), chunk_size):
    union_q = " UNION ALL ".join(queries[i:i+chunk_size])
    chunks.append(union_q)

out = {
    "candidates_count": len(candidates),
    "chunks": chunks,
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Bwf6IfMILxz6M6L9VEXSIh1T': 'file_storage/call_Bwf6IfMILxz6M6L9VEXSIh1T.json', 'var_call_fzLKq8IlpgPul9fghWeKKYUT': 'file_storage/call_fzLKq8IlpgPul9fghWeKKYUT.json'}

exec(code, env_args)
