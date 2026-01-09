code = """import json, pandas as pd

# load NYSE Arca ETFs
arca_path = var_call_SfzowiPGo9Cwx7lWlMWFey8F
with open(arca_path, 'r') as f:
    arca = json.load(f)
df_arca = pd.DataFrame(arca)

# load available price tables list
lst_path = var_call_Fr7BmlftWmKTW4WkvlHqFvSv
with open(lst_path, 'r') as f:
    tables = json.load(f)
set_tables = set(tables)

# keep only those with price data tables present
df_arca = df_arca[df_arca['symbol'].isin(set_tables)].copy()
syms = sorted(df_arca['symbol'].unique().tolist())

# build UNION ALL query to find max adj close in 2015 for each symbol
parts = []
for s in syms:
    # DuckDB: quote table name with double quotes; quote column "Adj Close" and "Date"
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

union_query = "\nUNION ALL\n".join(parts)

# Return both the query and symbol count to drive next tool call
out = json.dumps({'n_symbols_with_tables': len(syms), 'union_query': union_query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_SfzowiPGo9Cwx7lWlMWFey8F': 'file_storage/call_SfzowiPGo9Cwx7lWlMWFey8F.json', 'var_call_Fr7BmlftWmKTW4WkvlHqFvSv': 'file_storage/call_Fr7BmlftWmKTW4WkvlHqFvSv.json'}

exec(code, env_args)
