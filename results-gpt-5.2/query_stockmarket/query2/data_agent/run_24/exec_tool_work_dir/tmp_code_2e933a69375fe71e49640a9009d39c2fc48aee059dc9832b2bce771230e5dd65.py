code = """import json

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

selects = []
for s in common:
    tbl = '"' + s.replace('"','""') + '"'
    sel = "SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s, tbl=tbl)
    selects.append(sel)

chunks = []
chunk = []
max_len = 900000
cur_len = 0
for sel in selects:
    add_len = len(sel) + (11 if chunk else 0)
    if cur_len + add_len > max_len and chunk:
        chunks.append(' UNION ALL '.join(chunk))
        chunk = [sel]
        cur_len = len(sel)
    else:
        if chunk:
            cur_len += 11
        chunk.append(sel)
        cur_len += len(sel)
if chunk:
    chunks.append(' UNION ALL '.join(chunk))

out = {'common_count': len(common), 'n_chunks': len(chunks), 'first_chunk_len': len(chunks[0]) if chunks else 0}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ASxqUidKouxirPTsX6kyMaGX': 'file_storage/call_ASxqUidKouxirPTsX6kyMaGX.json', 'var_call_qDAxo3HVUHPjQPFy7oZgucv5': 'file_storage/call_qDAxo3HVUHPjQPFy7oZgucv5.json'}

exec(code, env_args)
