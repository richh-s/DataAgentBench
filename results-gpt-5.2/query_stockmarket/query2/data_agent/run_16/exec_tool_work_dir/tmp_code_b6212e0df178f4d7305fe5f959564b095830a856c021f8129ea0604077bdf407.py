code = """import json, pandas as pd

# load NYSE Arca ETFs
path_etfs = var_call_GhhqzigemFWLhVImnohWlQBL
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

# load available price tables
path_tables = var_call_LJHghFAAPNKl9yp5GcEObROY
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

# intersect
candidates = [t for t in tickers if t in tables]

# build a UNION ALL query to compute max adj close in 2015 per ticker
# quote table names that contain special characters
parts = []
for t in candidates:
    table_ident = '"' + t.replace('"','""') + '"'
    parts.append(
        f"SELECT '{t}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose2015 FROM {table_ident} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )

# chunk to avoid overly long query
chunk_size = 200
chunks = [parts[i:i+chunk_size] for i in range(0, len(parts), chunk_size)]
queries = [" UNION ALL ".join(ch) for ch in chunks]

result = {
    'candidates_count': len(candidates),
    'queries': queries
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GhhqzigemFWLhVImnohWlQBL': 'file_storage/call_GhhqzigemFWLhVImnohWlQBL.json', 'var_call_LJHghFAAPNKl9yp5GcEObROY': 'file_storage/call_LJHghFAAPNKl9yp5GcEObROY.json'}

exec(code, env_args)
