code = """import json

path = var_call_rtrl8RNO3l8To1mSqWStympT
with open(path, 'r') as f:
    syms = [r['symbol'] for r in json.load(f)]

path2 = var_call_YeDPrvgXGIqbJWv3usn3iXl3
with open(path2, 'r') as f:
    tables = set(json.load(f))

syms_avail = [s for s in syms if s in tables]

# Prepare per-symbol max query without building massive UNION; we'll query each symbol separately later.
out = {"syms_avail": syms_avail, "n_syms_arca_etf": len(syms), "n_syms_avail": len(syms_avail)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rtrl8RNO3l8To1mSqWStympT': 'file_storage/call_rtrl8RNO3l8To1mSqWStympT.json', 'var_call_YeDPrvgXGIqbJWv3usn3iXl3': 'file_storage/call_YeDPrvgXGIqbJWv3usn3iXl3.json'}

exec(code, env_args)
