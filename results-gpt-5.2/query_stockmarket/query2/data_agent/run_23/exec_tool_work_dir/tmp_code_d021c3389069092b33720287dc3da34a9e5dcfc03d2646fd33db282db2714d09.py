code = """import json, pandas as pd

# Load NYSE Arca ETFs list
p = var_call_L7ddSgvG4pwxWupzI6Jilkxd
if isinstance(p, str):
    with open(p, 'r') as f:
        etfs = json.load(f)
else:
    etfs = p

# Load available price tables
q = var_call_h8spSELnHicwBjN3VuyEck6c
if isinstance(q, str):
    with open(q, 'r') as f:
        tables = json.load(f)
else:
    tables = q

etf_syms = sorted({r['Symbol'] for r in etfs})
table_set = set(tables)
syms = [s for s in etf_syms if s in table_set]

# Build UNION ALL query to find max Adj Close in 2015 per symbol
parts = []
for s in syms:
    # DuckDB identifiers: quote with double quotes; escape any embedded quotes
    ident = '"' + s.replace('"','""') + '"'
    parts.append(
        f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close "
        f"FROM {ident} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )

# If no symbols, return empty
if not parts:
    out = {"etfs": [], "total": 0}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    union_query = " UNION ALL ".join(parts)
    # Store query for next tool call
    print('__RESULT__:')
    print(json.dumps({"query": union_query, "n_syms": len(syms)}))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json'}

exec(code, env_args)
