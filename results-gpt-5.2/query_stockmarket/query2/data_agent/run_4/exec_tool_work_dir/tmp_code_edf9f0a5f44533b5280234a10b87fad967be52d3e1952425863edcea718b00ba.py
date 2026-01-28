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

batch_size = 120
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]

DQUOTE = chr(34)

def quote_ident(name):
    return DQUOTE + name.replace(DQUOTE, DQUOTE + DQUOTE) + DQUOTE

adj_col = DQUOTE + 'Adj Close' + DQUOTE

queries = []
for batch in batches:
    parts = []
    for sym in batch:
        q = "SELECT '{sym}' AS Symbol, MAX({adj}) AS max_adj_close_2015 FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(
            sym=sym,
            adj=adj_col,
            tbl=quote_ident(sym)
        )
        parts.append(q)
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'n_batches': len(queries), 'batch0_len': len(batches[0]), 'query0_prefix': queries[0][:200]}))"""

env_args = {'var_call_VGIN8VJPRkl6MGyAkZCU8mQZ': ['stockinfo'], 'var_call_M8dVxOKQbT6IQgGKVR7B6Q7a': 'file_storage/call_M8dVxOKQbT6IQgGKVR7B6Q7a.json', 'var_call_4OvhmSqRovXB7CTaiTWhMfCL': 'file_storage/call_4OvhmSqRovXB7CTaiTWhMfCL.json', 'var_call_6BdRJPKJ5EqpDGoJMmdeufid': {'test': 'ok'}, 'var_call_p0Vilhyhy7EGUlhAo6trR3mP': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_2vMrtbvYy4gkbmITODD6Hsgg': {'n_etfs': 1435, 'n_tables': 2753}, 'var_call_swY5ifcQBIC0Cp6V6QcwkH4L': {'symbols5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'n_symbols': 1435}, 'var_call_qPlR1I3Y089soRh7q3gFHLmc': [{'Symbol': 'AAAU', 'max_AAAU': 'nan', 'max_AADR': '39.58057403564453'}], 'var_call_hGyunXrstZZpREiNtLIY5KTC': {'a': 'x'}, 'var_call_J8JvU7UMW6Fru5kqE3WZdnwX': 'hello', 'var_call_GFnELtGEvNEyMKePNbck080G': {'s': 'MAX(Adj Close)'}, 'var_call_g8fl1jWimn262p1hDO25thwq': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_MhIlH6PuFqJcWAjf2BELs63x': {'s': '"Adj Close"'}}

exec(code, env_args)
