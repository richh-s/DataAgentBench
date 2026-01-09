code = """import json, pandas as pd

# Load NYSE Arca ETFs from stockinfo
path_etfs = var_call_M8dVxOKQbT6IQgGKVR7B6Q7a
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

df_etfs = pd.DataFrame(etfs)
etf_symbols = set(df_etfs['Symbol'].astype(str))

# Load available price tables
path_tables = var_call_4OvhmSqRovXB7CTaiTWhMfCL
with open(path_tables, 'r') as f:
    tables = json.load(f)

df_tables = pd.DataFrame(tables)
avail_tables = set(df_tables['table_name'].astype(str))

symbols = sorted(etf_symbols.intersection(avail_tables))

def quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'

# Create batched UNION ALL query to find max Adj Close in 2015 for each symbol

def make_query(batch):
    parts = []
    for sym in batch:
        q = (
            "SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 "
            "FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        ).format(sym=sym, tbl=quote_ident(sym))
        parts.append(q)
    return ' UNION ALL '.join(parts)

batch_size = 150
queries = [make_query(symbols[i:i+batch_size]) for i in range(0, len(symbols), batch_size)]

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'n_batches': len(queries), 'queries': queries}))"""

env_args = {'var_call_VGIN8VJPRkl6MGyAkZCU8mQZ': ['stockinfo'], 'var_call_M8dVxOKQbT6IQgGKVR7B6Q7a': 'file_storage/call_M8dVxOKQbT6IQgGKVR7B6Q7a.json', 'var_call_4OvhmSqRovXB7CTaiTWhMfCL': 'file_storage/call_4OvhmSqRovXB7CTaiTWhMfCL.json'}

exec(code, env_args)
