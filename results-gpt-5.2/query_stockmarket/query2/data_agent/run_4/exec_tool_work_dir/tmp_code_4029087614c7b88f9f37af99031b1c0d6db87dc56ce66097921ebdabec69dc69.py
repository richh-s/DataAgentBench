code = """import json, pandas as pd

# Build all batch queries (same as before)
with open(var_call_M8dVxOKQbT6IQgGKVR7B6Q7a,'r') as f:
    etfs=json.load(f)
with open(var_call_4OvhmSqRovXB7CTaiTWhMfCL,'r') as f:
    tables=json.load(f)

df_etfs=pd.DataFrame(etfs)
df_tables=pd.DataFrame(tables)
meta = df_etfs[['Symbol','company_description']].copy()
meta['Symbol']=meta['Symbol'].astype(str)

symbols=sorted(set(meta['Symbol']).intersection(set(df_tables['table_name'].astype(str))))

DQUOTE=chr(34)
adj_col=DQUOTE+'Adj Close'+DQUOTE

def quote_ident(name):
    return DQUOTE + name.replace(DQUOTE, DQUOTE + DQUOTE) + DQUOTE

batch_size=120
queries=[]
for i in range(0,len(symbols),batch_size):
    batch=symbols[i:i+batch_size]
    parts=[]
    for sym in batch:
        parts.append("SELECT '{sym}' AS Symbol, MAX({adj}) AS max_adj_close_2015 FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=sym, adj=adj_col, tbl=quote_ident(sym)))
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'queries': queries}))"""

env_args = {'var_call_VGIN8VJPRkl6MGyAkZCU8mQZ': ['stockinfo'], 'var_call_M8dVxOKQbT6IQgGKVR7B6Q7a': 'file_storage/call_M8dVxOKQbT6IQgGKVR7B6Q7a.json', 'var_call_4OvhmSqRovXB7CTaiTWhMfCL': 'file_storage/call_4OvhmSqRovXB7CTaiTWhMfCL.json', 'var_call_6BdRJPKJ5EqpDGoJMmdeufid': {'test': 'ok'}, 'var_call_p0Vilhyhy7EGUlhAo6trR3mP': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_2vMrtbvYy4gkbmITODD6Hsgg': {'n_etfs': 1435, 'n_tables': 2753}, 'var_call_swY5ifcQBIC0Cp6V6QcwkH4L': {'symbols5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'n_symbols': 1435}, 'var_call_qPlR1I3Y089soRh7q3gFHLmc': [{'Symbol': 'AAAU', 'max_AAAU': 'nan', 'max_AADR': '39.58057403564453'}], 'var_call_hGyunXrstZZpREiNtLIY5KTC': {'a': 'x'}, 'var_call_J8JvU7UMW6Fru5kqE3WZdnwX': 'hello', 'var_call_GFnELtGEvNEyMKePNbck080G': {'s': 'MAX(Adj Close)'}, 'var_call_g8fl1jWimn262p1hDO25thwq': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_MhIlH6PuFqJcWAjf2BELs63x': {'s': '"Adj Close"'}, 'var_call_Hl7eyz0vZYC4YJY2fgWpGJcZ': {'n_symbols': 1435, 'n_batches': 12, 'batch0_len': 120, 'query0_prefix': 'SELECT \'AAAU\' AS Symbol, MAX("Adj Close") AS max_adj_close_2015 FROM "AAAU" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' UNION ALL SELECT \'AADR\' AS Symbol, MAX("Adj Close") AS max_adj_close_201'}, 'var_call_wIKtkcTPJMWG62r9Ufoce4v3': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}, {'Symbol': 'AADR', 'max_adj_close_2015': '39.58057403564453'}], 'var_call_2Q5RDuxLLzbzAqityNXdPmuo': {'n_batches': 12, 'batch_sizes': [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 115]}, 'var_call_xRen4vt87csrcaXE1rePZT6X': [{'Symbol': 'AAAU', 'max_adj_close_2015': 'nan'}, {'Symbol': 'AADR', 'max_adj_close_2015': '39.58057403564453'}, {'Symbol': 'ABEQ', 'max_adj_close_2015': 'nan'}, {'Symbol': 'ACSG', 'max_adj_close_2015': 'nan'}, {'Symbol': 'ACWF', 'max_adj_close_2015': '23.251304626464844'}]}

exec(code, env_args)
