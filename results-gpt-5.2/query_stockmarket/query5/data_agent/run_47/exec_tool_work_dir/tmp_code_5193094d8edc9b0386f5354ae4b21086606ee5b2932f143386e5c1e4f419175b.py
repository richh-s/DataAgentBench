code = """import json
with open(var_call_TQ2qbdhno8m08VxqXsNvkb8Z, 'r') as f:
    info = json.load(f)
with open(var_call_Y0WmHHLLofAkHdC2sAm6zZEb, 'r') as f:
    tables = json.load(f)
syms = sorted(set(r['Symbol'] for r in info) & set(tables))

# build union query in chunks of 25
chunks=[]
chunk_size=25
for i in range(0,len(syms),chunk_size):
    sub=syms[i:i+chunk_size]
    selects=[]
    for s in sub:
        t='"'+s.replace('"','""')+'"'
        selects.append("SELECT '"+s+"' AS Symbol, COUNT(*) AS n_days FROM "+t+" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2")
    chunks.append(" UNION ALL ".join(selects))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunks), 'chunk0_sql': chunks[0], 'chunk0_len': len(chunks[0]), 'total_syms': len(syms)}))"""

env_args = {'var_call_TQ2qbdhno8m08VxqXsNvkb8Z': 'file_storage/call_TQ2qbdhno8m08VxqXsNvkb8Z.json', 'var_call_Y0WmHHLLofAkHdC2sAm6zZEb': 'file_storage/call_Y0WmHHLLofAkHdC2sAm6zZEb.json', 'var_call_K8f8GxAZZ0KBIri208lVZO0H': {'n_filtered_symbols': 86, 'n_trade_tables': 2753, 'n_symbols_to_query': 86, 'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_2X7WN0vg5Vq0psFO8g8Eme6O': [{'Symbol': 'AGMH', 'n_days': '13'}, {'Symbol': 'BHAT', 'n_days': '10'}, {'Symbol': 'BIOC', 'n_days': '21'}]}

exec(code, env_args)
