code = """import json, pandas as pd

# load nasdaq capital market tickers
obj = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(obj, str):
    with open(obj, 'r') as f:
        symbols = json.load(f)
else:
    symbols = obj
sym_df = pd.DataFrame(symbols)
capital_tickers = set(sym_df['Symbol'].dropna().unique())

# load available trade tables
obj2 = var_call_sB1dlFjC01RJNrtqfKeMDI7e
if isinstance(obj2, str):
    with open(obj2, 'r') as f:
        tables = json.load(f)
else:
    tables = obj2
trade_tables = set(pd.DataFrame(tables)['table_name'].dropna().unique())

common = sorted(capital_tickers.intersection(trade_tables))

# chunk the union query into multiple queries if needed
chunks = []
chunk_size = 150  # keep query length reasonable
for i in range(0, len(common), chunk_size):
    chunk = common[i:i+chunk_size]
    parts = []
    for t in chunk:
        safe_t = t.replace('"','""')
        parts.append(
            f"SELECT '{safe_t}' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM \"{safe_t}\" "
            f"WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2"
        )
    q = "\nUNION ALL\n".join(parts)
    chunks.append(q)

print('__RESULT__:')
print(json.dumps({'n_capital_tickers': len(capital_tickers), 'n_trade_tables': len(trade_tables), 'n_common': len(common), 'first10_common': common[:10], 'n_chunks': len(chunks), 'chunk0_query': chunks[0] if chunks else ''}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json', 'var_call_sB1dlFjC01RJNrtqfKeMDI7e': 'file_storage/call_sB1dlFjC01RJNrtqfKeMDI7e.json'}

exec(code, env_args)
