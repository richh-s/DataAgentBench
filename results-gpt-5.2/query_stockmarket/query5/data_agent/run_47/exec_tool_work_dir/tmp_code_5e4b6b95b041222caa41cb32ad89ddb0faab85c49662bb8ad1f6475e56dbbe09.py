code = """import json
with open(var_call_TQ2qbdhno8m08VxqXsNvkb8Z, 'r') as f:
    info = json.load(f)
with open(var_call_Y0WmHHLLofAkHdC2sAm6zZEb, 'r') as f:
    tables = json.load(f)
syms = sorted(set(r['Symbol'] for r in info) & set(tables))

selects = []
for s in syms:
    t = '"' + s.replace('"','""') + '"'
    selects.append("SELECT '{sym}' AS Symbol, COUNT(*) AS n_days FROM {t} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=s, t=t))

query = "\nUNION ALL\n".join(selects)

print('__RESULT__:')
print(json.dumps({'sql': query, 'n_symbols': len(syms), 'sql_len': len(query)}))"""

env_args = {'var_call_TQ2qbdhno8m08VxqXsNvkb8Z': 'file_storage/call_TQ2qbdhno8m08VxqXsNvkb8Z.json', 'var_call_Y0WmHHLLofAkHdC2sAm6zZEb': 'file_storage/call_Y0WmHHLLofAkHdC2sAm6zZEb.json', 'var_call_K8f8GxAZZ0KBIri208lVZO0H': {'n_filtered_symbols': 86, 'n_trade_tables': 2753, 'n_symbols_to_query': 86, 'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
