code = """import json, pandas as pd

# Load ETF list from file if needed
etf_var = var_call_ASxqUidKouxirPTsX6kyMaGX
if isinstance(etf_var, str):
    with open(etf_var, 'r') as f:
        etfs = json.load(f)
else:
    etfs = etf_var

trade_tables_var = var_call_qDAxo3HVUHPjQPFy7oZgucv5
if isinstance(trade_tables_var, str):
    with open(trade_tables_var, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_tables_var

etf_symbols = sorted({r['Symbol'] for r in etfs})
trade_set = set(trade_tables)
common = [s for s in etf_symbols if s in trade_set]

# Build a single UNION ALL query to test max Adj Close in 2015 for each symbol
# Quote table names because some may contain special chars like '#'
selects = []
for s in common:
    tbl = '"' + s.replace('"','""') + '"'
    selects.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")

# Chunk to avoid overly large SQL strings
chunks = []
chunk = []
max_len = 900000  # conservative
cur_len = 0
for sel in selects:
    if cur_len + len(sel) + 11 > max_len and chunk:
        chunks.append(chunk)
        chunk = [sel]
        cur_len = len(sel)
    else:
        chunk.append(sel)
        cur_len += len(sel)
if chunk:
    chunks.append(chunk)

out = {
    'common_count': len(common),
    'chunks': [' UNION ALL '.join(c) for c in chunks],
    'symbol_to_desc': {r['Symbol']: r.get('company_description') for r in etfs}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ASxqUidKouxirPTsX6kyMaGX': 'file_storage/call_ASxqUidKouxirPTsX6kyMaGX.json', 'var_call_qDAxo3HVUHPjQPFy7oZgucv5': 'file_storage/call_qDAxo3HVUHPjQPFy7oZgucv5.json'}

exec(code, env_args)
