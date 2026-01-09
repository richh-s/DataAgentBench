code = """import json
path_info = var_call_gKoK14VmHOpdSnLGsEJyjiQI
with open(path_info,'r') as f:
    info=json.load(f)
path_tbls = var_call_bzHgWJ1f135Ch9vkcGJQ06eI
with open(path_tbls,'r') as f:
    tbls=set(json.load(f))
syms=[r['symbol'] for r in info if r['symbol'] in tbls]
print('__RESULT__:')
print(json.dumps({'n':len(syms),'first10':syms[:10]}))"""

env_args = {'var_call_gKoK14VmHOpdSnLGsEJyjiQI': 'file_storage/call_gKoK14VmHOpdSnLGsEJyjiQI.json', 'var_call_bzHgWJ1f135Ch9vkcGJQ06eI': 'file_storage/call_bzHgWJ1f135Ch9vkcGJQ06eI.json'}

exec(code, env_args)
