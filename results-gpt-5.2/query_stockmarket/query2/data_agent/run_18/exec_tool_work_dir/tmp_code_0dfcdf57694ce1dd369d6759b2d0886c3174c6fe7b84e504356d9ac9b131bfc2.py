code = """import json

path = var_call_YAZ1UBW4wtS43a3iKLtc8A4R
with open(path, 'r') as f:
    etf_syms = [r['symbol'] for r in json.load(f)]

path2 = var_call_KtCAfDmfZykEJa88Eee5Y2tI
with open(path2, 'r') as f:
    price_tables = set(json.load(f))

syms = [s for s in etf_syms if s in price_tables]

# sanitize symbols for duckdb identifiers: only keep those without special chars
safe_syms = [s for s in syms if s.replace('_','').isalnum()]

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'n_safe_syms': len(safe_syms), 'example_unsafe': [s for s in syms if not s.replace('_','').isalnum()][:20]}))"""

env_args = {'var_call_YAZ1UBW4wtS43a3iKLtc8A4R': 'file_storage/call_YAZ1UBW4wtS43a3iKLtc8A4R.json', 'var_call_KtCAfDmfZykEJa88Eee5Y2tI': 'file_storage/call_KtCAfDmfZykEJa88Eee5Y2tI.json', 'var_call_KVfk3Dv7tGpgDdPLXoxjCBaR': {'n_syms': 1435}, 'var_call_XRCU3IQ8FJS0gUfyMrQJq0n2': []}

exec(code, env_args)
