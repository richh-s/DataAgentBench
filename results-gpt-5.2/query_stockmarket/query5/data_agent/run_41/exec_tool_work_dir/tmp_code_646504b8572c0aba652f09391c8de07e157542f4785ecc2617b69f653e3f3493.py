code = """import json, pandas as pd

obj = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(obj, str):
    with open(obj, 'r') as f:
        symbols = json.load(f)
else:
    symbols = obj
sym_df = pd.DataFrame(symbols)
capital_tickers = set(sym_df['Symbol'].dropna().unique())

obj2 = var_call_sB1dlFjC01RJNrtqfKeMDI7e
if isinstance(obj2, str):
    with open(obj2, 'r') as f:
        tables = json.load(f)
else:
    tables = obj2
trade_tables = set(pd.DataFrame(tables)['table_name'].dropna().unique())

common = sorted(capital_tickers.intersection(trade_tables))

chunk_size = 150
chunks = []
for i in range(0, len(common), chunk_size):
    chunk = common[i:i+chunk_size]
    parts = []
    for t in chunk:
        safe_t = t.replace('"','""')
        parts.append(
            f"SELECT '{safe_t}' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM \"{safe_t}\" "
            f"WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2"
        )
    chunks.append("\nUNION ALL\n".join(parts))

print('__RESULT__:')
print(json.dumps({'n_common': len(common), 'n_chunks': len(chunks)}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json', 'var_call_sB1dlFjC01RJNrtqfKeMDI7e': 'file_storage/call_sB1dlFjC01RJNrtqfKeMDI7e.json'}

exec(code, env_args)
