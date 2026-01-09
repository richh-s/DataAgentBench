code = """import json, pandas as pd

path_etfs = var_call_M8dVxOKQbT6IQgGKVR7B6Q7a
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

df_etfs = pd.DataFrame(etfs)
etf_symbols = set(df_etfs['Symbol'].astype(str))

path_tables = var_call_4OvhmSqRovXB7CTaiTWhMfCL
with open(path_tables, 'r') as f:
    tables = json.load(f)

df_tables = pd.DataFrame(tables)
avail_tables = set(df_tables['table_name'].astype(str))

symbols = sorted(etf_symbols.intersection(avail_tables))

batch_size = 80
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]

def quote_ident(name):
    return '"' + name.replace('"','""') + '"'

def make_query(batch):
    cols = []
    for sym in batch:
        sub = "(SELECT MAX(\"Adj Close\") FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') AS {col}".format(
            tbl=quote_ident(sym),
            col='max_' + sym.replace('#','_').replace('-','_')
        )
        cols.append(sub)
    q = 'SELECT ' + ', '.join(cols) + ';'
    return q

queries = [make_query(b) for b in batches]

print('__RESULT__:')
print(json.dumps({'n_batches': len(queries), 'first_query': queries[0], 'first_batch': batches[0]}))"""

env_args = {'var_call_VGIN8VJPRkl6MGyAkZCU8mQZ': ['stockinfo'], 'var_call_M8dVxOKQbT6IQgGKVR7B6Q7a': 'file_storage/call_M8dVxOKQbT6IQgGKVR7B6Q7a.json', 'var_call_4OvhmSqRovXB7CTaiTWhMfCL': 'file_storage/call_4OvhmSqRovXB7CTaiTWhMfCL.json', 'var_call_6BdRJPKJ5EqpDGoJMmdeufid': {'test': 'ok'}, 'var_call_p0Vilhyhy7EGUlhAo6trR3mP': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_2vMrtbvYy4gkbmITODD6Hsgg': {'n_etfs': 1435, 'n_tables': 2753}, 'var_call_swY5ifcQBIC0Cp6V6QcwkH4L': {'symbols5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'n_symbols': 1435}, 'var_call_qPlR1I3Y089soRh7q3gFHLmc': [{'Symbol': 'AAAU', 'max_AAAU': 'nan', 'max_AADR': '39.58057403564453'}]}

exec(code, env_args)
