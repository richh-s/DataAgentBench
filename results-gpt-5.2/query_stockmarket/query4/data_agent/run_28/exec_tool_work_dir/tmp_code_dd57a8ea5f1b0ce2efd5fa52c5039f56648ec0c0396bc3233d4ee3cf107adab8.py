code = """import json, pandas as pd

# Load NYSE non-ETF symbols from stockinfo query
v = var_call_8Rmh6nq21wxXn4UkriQTxNnE
if isinstance(v, str):
    with open(v, 'r') as f:
        info = json.load(f)
else:
    info = v
info_df = pd.DataFrame(info)

# Load available trade tables
t = var_call_53fSB6wCGArWqzaRLsIKLcr4
if isinstance(t, str):
    with open(t, 'r') as f:
        tables = json.load(f)
else:
    tables = t
trade_set = set(tables)

# intersect
symbols = sorted(set(info_df['Symbol']).intersection(trade_set))

# limit for SQL IN clause chunking
chunks = [symbols[i:i+400] for i in range(0, len(symbols), 400)]
chunk_queries = []
for ch in chunks:
    in_list = ','.join(["'"+s.replace("'","''")+"'" for s in ch])
    # build union all per chunk using DuckDB information_schema.tables doesn't help; we need per-table queries. We'll generate later.

# Instead of huge SQL, we'll compute per symbol by querying DuckDB per table? too slow.
# We'll pick a manageable subset by requiring table has 2017 data using a lightweight query per table with LIMIT 1 for 2017.
# Do in python by selecting candidates up to 300 and then full counts; but need accurate top5 across all.
# We'll generate one big UNION ALL with aggregated counts per table.

# Create SQL with UNION ALL aggregate for each symbol
parts = []
for sym in symbols:
    # quote table name with double quotes for DuckDB if special chars
    tbl = '"' + sym.replace('"','""') + '"'
    parts.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")

# Chunk UNION to avoid overly long query; we'll return as list of SQL strings to run sequentially outside.
max_parts = 120
sqls = []
for i in range(0, len(parts), max_parts):
    union_sql = " UNION ALL ".join(parts[i:i+max_parts])
    sqls.append(union_sql)

print('__RESULT__:')
print(json.dumps({'sqls': sqls, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_8Rmh6nq21wxXn4UkriQTxNnE': 'file_storage/call_8Rmh6nq21wxXn4UkriQTxNnE.json', 'var_call_53fSB6wCGArWqzaRLsIKLcr4': 'file_storage/call_53fSB6wCGArWqzaRLsIKLcr4.json'}

exec(code, env_args)
