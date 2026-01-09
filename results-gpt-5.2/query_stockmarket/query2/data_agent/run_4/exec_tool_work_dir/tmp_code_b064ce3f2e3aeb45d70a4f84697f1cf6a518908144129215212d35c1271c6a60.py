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

# limit to first 5 symbols
symbols5 = symbols[:5]

print('__RESULT__:')
print(json.dumps({'symbols5': symbols5, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_VGIN8VJPRkl6MGyAkZCU8mQZ': ['stockinfo'], 'var_call_M8dVxOKQbT6IQgGKVR7B6Q7a': 'file_storage/call_M8dVxOKQbT6IQgGKVR7B6Q7a.json', 'var_call_4OvhmSqRovXB7CTaiTWhMfCL': 'file_storage/call_4OvhmSqRovXB7CTaiTWhMfCL.json', 'var_call_6BdRJPKJ5EqpDGoJMmdeufid': {'test': 'ok'}, 'var_call_p0Vilhyhy7EGUlhAo6trR3mP': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_2vMrtbvYy4gkbmITODD6Hsgg': {'n_etfs': 1435, 'n_tables': 2753}}

exec(code, env_args)
