code = """import json, pandas as pd

# load stockinfo results
path_info = var_call_lsWEadc109kwWv5jdXkUgWbB
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load trade tables list
path_tbl = var_call_VDn7pDm6A1YBRdsQaIjs0gEy
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

# keep only symbols that have price tables
info_df = info_df[info_df['Symbol'].isin(tbls_set)].copy()
syms = info_df['Symbol'].tolist()

# Build UNION ALL query to compute up/down counts for year 2017 for each symbol
parts = []
for s in syms:
    # DuckDB identifiers: wrap in double quotes; tables are uppercase/lowercase as given
    parts.append(f"SELECT '{s}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")

query = "\nUNION ALL\n".join(parts)

# To avoid too-long queries, chunk into batches
batch_size = 200
batches = [parts[i:i+batch_size] for i in range(0, len(parts), batch_size)]

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_batches': len(batches), 'first_symbol': syms[0] if syms else None}))"""

env_args = {'var_call_lsWEadc109kwWv5jdXkUgWbB': 'file_storage/call_lsWEadc109kwWv5jdXkUgWbB.json', 'var_call_VDn7pDm6A1YBRdsQaIjs0gEy': 'file_storage/call_VDn7pDm6A1YBRdsQaIjs0gEy.json'}

exec(code, env_args)
