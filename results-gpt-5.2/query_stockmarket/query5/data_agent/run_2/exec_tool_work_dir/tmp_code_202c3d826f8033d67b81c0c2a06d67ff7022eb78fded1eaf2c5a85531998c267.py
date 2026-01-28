code = """import json, pandas as pd
from pathlib import Path

# load symbols list
p = Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh)
records = json.loads(p.read_text())
syms = [r['Symbol'] for r in records]
companies = {r['Symbol']: r['company_name'] for r in records}

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'symbols': syms[:50]}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json'}

exec(code, env_args)
