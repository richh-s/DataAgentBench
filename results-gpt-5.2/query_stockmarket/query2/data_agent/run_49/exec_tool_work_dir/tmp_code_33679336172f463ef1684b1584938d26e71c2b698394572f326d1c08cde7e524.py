code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols on NYSE Arca
p = Path(var_call_lsVzhsWRcJPMqreLutxe9gCr)
rows = json.loads(p.read_text())
etf_symbols = sorted({r['Symbol'] for r in rows})

# Load available price tables
pt = Path(var_call_sOPO5ItDyEQ2ND9iPkJlrrQb)
price_tables = set(json.loads(pt.read_text()))

# Intersect to those with price data tables
symbols = [s for s in etf_symbols if s in price_tables]

# helper to quote table names for DuckDB (double quotes, escape embedded quotes)
def qident(name: str) -> str:
    return '"' + name.replace('"','""') + '"'

# Build one UNION ALL query to compute max Adj Close in 2015 per symbol
selects = []
for s in symbols:
    t = qident(s)
    selects.append(
        f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {t} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )

# Chunk to avoid overly large query strings
chunks = []
chunk = []
max_len = 500000
cur_len = 0
for sel in selects:
    if cur_len + len(sel) + 12 > max_len and chunk:
        chunks.append(chunk)
        chunk = [sel]
        cur_len = len(sel)
    else:
        chunk.append(sel)
        cur_len += len(sel)
if chunk:
    chunks.append(chunk)

out = []
for ch in chunks:
    query = " UNION ALL ".join(ch)
    res = __import__('builtins').globals().get('query_db_result')

print('__RESULT__:')
print(json.dumps({'symbols_with_price_tables': len(symbols), 'chunks': len(chunks)}))"""

env_args = {'var_call_lsVzhsWRcJPMqreLutxe9gCr': 'file_storage/call_lsVzhsWRcJPMqreLutxe9gCr.json', 'var_call_sOPO5ItDyEQ2ND9iPkJlrrQb': 'file_storage/call_sOPO5ItDyEQ2ND9iPkJlrrQb.json'}

exec(code, env_args)
