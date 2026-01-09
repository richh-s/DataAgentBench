code = """import json, pandas as pd

# Load ETF list from stockinfo query result file
path = var_call_yGpAynzIoSqSe9wxFVL88TgL
with open(path, 'r') as f:
    etf_recs = json.load(f)
etf_symbols = sorted({r['Symbol'] for r in etf_recs if r.get('Symbol')})

# Load available trade tables list
path2 = var_call_v5GUXnTyPU6cpGhiSLYg0wi4
with open(path2, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in etf_symbols if s in trade_tables]

# Build a UNION ALL query to find max Adj Close in 2015 per symbol, then filter > 200
parts = []
for s in symbols:
    # Quote table name for duckdb
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# DuckDB has a limit on query length; chunk if necessary
chunks = []
chunk = []
length = 0
for p in parts:
    if length + len(p) + 11 > 900000:  # safety
        chunks.append(chunk)
        chunk = [p]
        length = len(p)
    else:
        chunk.append(p)
        length += len(p)
if chunk:
    chunks.append(chunk)

queries = ["SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(ch) + ") WHERE max_adj_close > 200 ORDER BY symbol" for ch in chunks]

out = {
    'symbols_considered': len(symbols),
    'chunks': len(queries),
    'queries': queries
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a4jDHUOrnVwDbmbC1dsIe3Wg': ['stockinfo'], 'var_call_yGpAynzIoSqSe9wxFVL88TgL': 'file_storage/call_yGpAynzIoSqSe9wxFVL88TgL.json', 'var_call_v5GUXnTyPU6cpGhiSLYg0wi4': 'file_storage/call_v5GUXnTyPU6cpGhiSLYg0wi4.json'}

exec(code, env_args)
