code = """import json
from pathlib import Path

# Load ETF symbols on NYSE Arca
rows = json.loads(Path(var_call_lsVzhsWRcJPMqreLutxe9gCr).read_text())
etf_symbols = sorted({r['Symbol'] for r in rows})

# Load available price tables
price_tables = set(json.loads(Path(var_call_sOPO5ItDyEQ2ND9iPkJlrrQb).read_text()))

symbols = [s for s in etf_symbols if s in price_tables]

def qident(name: str) -> str:
    return '"' + name.replace('"','""') + '"'

# Build UNION ALL query (chunked)
selects = [
    f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {qident(s)} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    for s in symbols
]

chunks = []
chunk = []
max_len = 400000
cur_len = 0
for sel in selects:
    add = len(sel) + (11 if chunk else 0)  # UNION ALL 
    if cur_len + add > max_len and chunk:
        chunks.append(chunk)
        chunk = [sel]
        cur_len = len(sel)
    else:
        chunk.append(sel)
        cur_len += add
if chunk:
    chunks.append(chunk)

print('__RESULT__:')
print(json.dumps({'symbols_with_price_tables': len(symbols), 'chunks': len(chunks), 'example_symbol': symbols[0] if symbols else None}))"""

env_args = {'var_call_lsVzhsWRcJPMqreLutxe9gCr': 'file_storage/call_lsVzhsWRcJPMqreLutxe9gCr.json', 'var_call_sOPO5ItDyEQ2ND9iPkJlrrQb': 'file_storage/call_sOPO5ItDyEQ2ND9iPkJlrrQb.json', 'var_call_i8orDA4VAqo1k3XXAVEWSomT': [{'Symbol': 'SPY'}]}

exec(code, env_args)
