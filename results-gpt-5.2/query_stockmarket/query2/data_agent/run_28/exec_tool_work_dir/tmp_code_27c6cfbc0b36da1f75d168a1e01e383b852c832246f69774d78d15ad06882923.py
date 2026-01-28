code = """import json

info_src = var_call_SobbbbZXILGybWnUoxXTVWWx
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        etfs = json.load(f)
else:
    etfs = info_src

trade_tables_src = var_call_QhxtRLpkISLHodfoZTe1ZO6J
if isinstance(trade_tables_src, str):
    with open(trade_tables_src, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_tables_src

etf_syms = sorted({r['symbol'] for r in etfs})
trade_set = set(trade_tables)
syms = [s for s in etf_syms if s in trade_set]

print('__RESULT__:')
print(json.dumps({'n_etf_syms': len(etf_syms), 'n_trade_tables': len(trade_tables), 'n_syms_intersection': len(syms), 'first10': syms[:10]}))"""

env_args = {'var_call_SobbbbZXILGybWnUoxXTVWWx': 'file_storage/call_SobbbbZXILGybWnUoxXTVWWx.json', 'var_call_QhxtRLpkISLHodfoZTe1ZO6J': 'file_storage/call_QhxtRLpkISLHodfoZTe1ZO6J.json', 'var_call_bCxE0YzOOU4Jp5szkT8hBUtj': {'x': 1}}

exec(code, env_args)
