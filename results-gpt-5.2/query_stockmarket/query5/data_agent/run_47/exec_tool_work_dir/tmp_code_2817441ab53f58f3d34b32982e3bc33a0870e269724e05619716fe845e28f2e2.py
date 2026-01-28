code = """import json

# load stockinfo symbols and names
with open(var_call_TQ2qbdhno8m08VxqXsNvkb8Z, 'r') as f:
    info = json.load(f)
info_syms = set(r['Symbol'] for r in info)
name_by_sym = {r['Symbol']: r['company_name'] for r in info}

# load available trade tables
with open(var_call_Y0WmHHLLofAkHdC2sAm6zZEb, 'r') as f:
    tables = json.load(f)
trade_syms = set(tables)

syms = sorted(info_syms & trade_syms)

print('__RESULT__:')
print(json.dumps({'n_filtered_symbols': len(info_syms), 'n_trade_tables': len(trade_syms), 'n_symbols_to_query': len(syms), 'symbols_preview': syms[:20]}))"""

env_args = {'var_call_TQ2qbdhno8m08VxqXsNvkb8Z': 'file_storage/call_TQ2qbdhno8m08VxqXsNvkb8Z.json', 'var_call_Y0WmHHLLofAkHdC2sAm6zZEb': 'file_storage/call_Y0WmHHLLofAkHdC2sAm6zZEb.json'}

exec(code, env_args)
