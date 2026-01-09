code = """import json

etf_path = var_call_ASxqUidKouxirPTsX6kyMaGX
trade_path = var_call_qDAxo3HVUHPjQPFy7oZgucv5
with open(etf_path,'r') as f:
    etfs = json.load(f)
with open(trade_path,'r') as f:
    trade_tables = json.load(f)

etf_symbols = sorted({r['Symbol'] for r in etfs})
common = [s for s in etf_symbols if s in set(trade_tables)]

# build chunked union all queries
selects = []
for s in common:
    tbl = '"' + s.replace('"','""') + '"'
    selects.append("SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s, tbl=tbl))

chunks=[]
chunk=[]
max_len=700000
cur=0
for sel in selects:
    add=len(sel) + (11 if chunk else 0)
    if cur+add>max_len and chunk:
        chunks.append(' UNION ALL '.join(chunk))
        chunk=[sel]
        cur=len(sel)
    else:
        if chunk:
            cur += 11
        chunk.append(sel)
        cur += len(sel)
if chunk:
    chunks.append(' UNION ALL '.join(chunk))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunks), 'chunk_lens': [len(c) for c in chunks[:5]]}))"""

env_args = {'var_call_ASxqUidKouxirPTsX6kyMaGX': 'file_storage/call_ASxqUidKouxirPTsX6kyMaGX.json', 'var_call_qDAxo3HVUHPjQPFy7oZgucv5': 'file_storage/call_qDAxo3HVUHPjQPFy7oZgucv5.json', 'var_call_tVCECwffNXINpFAgd099c7UH': [{'x': 'DUMMY'}], 'var_call_91jccmvZMcEWEuAJAsaVFqm0': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}], 'var_call_fPP4wsWWGtNhqAp74CX0913q': {'ok': True}, 'var_call_OeauaWLzzwAZ4VeVCRjyphIK': {'type': "<class 'str'>", 'is_str': True}, 'var_call_QaMBbeQYGGpHjYpVDuLX7TjV': {'type': "<class 'str'>", 'is_str': True}, 'var_call_N9JLKv5YcLKDVMKDPDKyL9HG': {'etf_count': 1435, 'common_count': 1435}}

exec(code, env_args)
