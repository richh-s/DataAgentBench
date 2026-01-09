code = """import json

path_etfs = var_call_GhhqzigemFWLhVImnohWlQBL
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

path_tables = var_call_LJHghFAAPNKl9yp5GcEObROY
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

candidates = [t for t in tickers if t in tables]

parts = []
for t in candidates:
    table_ident = '"' + t.replace('"','""') + '"'
    q = "SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose2015 FROM {tbl} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=t, tbl=table_ident)
    parts.append(q)

chunk_size = 200
queries = []
for i in range(0, len(parts), chunk_size):
    queries.append(" UNION ALL ".join(parts[i:i+chunk_size]))

result = {'candidates_count': len(candidates), 'queries': queries}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GhhqzigemFWLhVImnohWlQBL': 'file_storage/call_GhhqzigemFWLhVImnohWlQBL.json', 'var_call_LJHghFAAPNKl9yp5GcEObROY': 'file_storage/call_LJHghFAAPNKl9yp5GcEObROY.json'}

exec(code, env_args)
