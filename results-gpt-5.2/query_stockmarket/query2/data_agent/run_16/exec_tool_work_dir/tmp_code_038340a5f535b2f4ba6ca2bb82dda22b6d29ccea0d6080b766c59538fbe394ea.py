code = """import json

path_etfs = var_call_GhhqzigemFWLhVImnohWlQBL
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

path_tables = var_call_LJHghFAAPNKl9yp5GcEObROY
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

candidates = [t for t in tickers if t in tables]

# build query chunks
chunk_size = 150
queries = []
for i in range(0, len(candidates), chunk_size):
    chunk = candidates[i:i+chunk_size]
    parts = []
    for t in chunk:
        tbl = '"' + t.replace('"','""') + '"'
        parts.append(
            "SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose2015 FROM {tbl} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(
                sym=t, tbl=tbl
            )
        )
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps({'queries': queries, 'chunks': len(queries), 'chunk_size': chunk_size}))"""

env_args = {'var_call_GhhqzigemFWLhVImnohWlQBL': 'file_storage/call_GhhqzigemFWLhVImnohWlQBL.json', 'var_call_LJHghFAAPNKl9yp5GcEObROY': 'file_storage/call_LJHghFAAPNKl9yp5GcEObROY.json', 'var_call_0t51cMFLwAcam0YT0XAWnZZc': {'candidates_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
