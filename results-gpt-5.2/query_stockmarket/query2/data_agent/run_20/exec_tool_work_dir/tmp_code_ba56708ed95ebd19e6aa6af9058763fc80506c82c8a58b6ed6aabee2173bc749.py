code = """import json

arca_etfs = var_call_LB1ZbwPPcY0PzkOXrLj7u8zh
if isinstance(arca_etfs, str):
    with open(arca_etfs, 'r') as f:
        arca_etfs = json.load(f)

trade_tables = var_call_v7Kx9fKHDfirqP6JfQmY5K9t
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

arca_symbols = [r['Symbol'] for r in arca_etfs]
trade_set = set(trade_tables)
symbols = sorted([s for s in arca_symbols if s in trade_set])

chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]
queries = []
for ch in chunks:
    parts = []
    for s in ch:
        parts.append("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"" + s + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    queries.append(" UNION ALL ".join(parts))

out = {'symbols_considered': len(symbols), 'n_queries': len(queries), 'queries': queries}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LB1ZbwPPcY0PzkOXrLj7u8zh': 'file_storage/call_LB1ZbwPPcY0PzkOXrLj7u8zh.json', 'var_call_v7Kx9fKHDfirqP6JfQmY5K9t': 'file_storage/call_v7Kx9fKHDfirqP6JfQmY5K9t.json'}

exec(code, env_args)
