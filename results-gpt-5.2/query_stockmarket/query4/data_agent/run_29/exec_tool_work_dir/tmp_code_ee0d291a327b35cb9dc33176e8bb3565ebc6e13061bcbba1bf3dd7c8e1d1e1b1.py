code = """import json, pandas as pd

# load nyse non-etf symbols
path_syms = var_call_FkIcp45dYkD0AfIXWtu9qwon
with open(path_syms,'r') as f:
    syms = json.load(f)
df_syms = pd.DataFrame(syms)
nyse_symbols = set(df_syms['Symbol'].astype(str))

# load trade tables
path_tables = var_call_095dKGkyaTg3X8vySvAxz7Nb
with open(path_tables,'r') as f:
    tabs = json.load(f)
df_tabs = pd.DataFrame(tabs)
trade_tables = set(df_tabs['table_name'].astype(str))

symbols = sorted(nyse_symbols & trade_tables)

# create union-all SQL to compute up/down days for 2017
parts = []
for s in symbols:
    # quote table name for duckdb; escape any embedded quotes
    tbl = '"' + s.replace('"','""') + '"'
    parts.append(f"SELECT '{s}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl} WHERE Date>='2017-01-01' AND Date<='2017-12-31'")

# chunk to avoid overly long query
chunks = []
chunk_size = 200
for i in range(0, len(parts), chunk_size):
    chunks.append(" UNION ALL ".join(parts[i:i+chunk_size]))

queries = ["SELECT * FROM ("+c+")" for c in chunks]

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_FkIcp45dYkD0AfIXWtu9qwon': 'file_storage/call_FkIcp45dYkD0AfIXWtu9qwon.json', 'var_call_095dKGkyaTg3X8vySvAxz7Nb': 'file_storage/call_095dKGkyaTg3X8vySvAxz7Nb.json'}

exec(code, env_args)
