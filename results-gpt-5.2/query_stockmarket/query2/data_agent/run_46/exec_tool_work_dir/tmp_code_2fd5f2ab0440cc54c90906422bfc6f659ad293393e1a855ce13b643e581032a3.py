code = """import json, pandas as pd

# load NYSE Arca ETFs
path = var_call_8BRy2xXU5qjQcBQIHostXyf0
with open(path, 'r') as f:
    etfs = json.load(f)
syms = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

# load available price tables
pt_path = var_call_sNc7LSyyo3Q8oR8uQ2zyBJlI
with open(pt_path, 'r') as f:
    price_tables = set(json.load(f))

syms_in_db = [s for s in syms if s in price_tables]

# build a UNION ALL query to find max Adj Close in 2015 per symbol
# quote table names in case of special chars
parts = []
for s in syms_in_db:
    t = '"' + s.replace('"','""') + '"'
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {t} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# If no symbols, return empty
union_query = " UNION ALL ".join(parts) if parts else "SELECT NULL AS Symbol, NULL AS max_adj_close_2015 WHERE FALSE"

result = {
    "symbols_in_metadata": len(syms),
    "symbols_with_price_table": len(syms_in_db),
    "union_query": union_query
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8BRy2xXU5qjQcBQIHostXyf0': 'file_storage/call_8BRy2xXU5qjQcBQIHostXyf0.json', 'var_call_sNc7LSyyo3Q8oR8uQ2zyBJlI': 'file_storage/call_sNc7LSyyo3Q8oR8uQ2zyBJlI.json'}

exec(code, env_args)
