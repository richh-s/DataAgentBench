code = """import json, pandas as pd
from pathlib import Path

p = Path(var_call_qdLIKDynnEUet9nJTfF5AaTo)
recs = json.loads(p.read_text())
syms = [r['Symbol'] for r in recs]
companies = {r['Symbol']: r['company_name'] for r in recs}

out = {
  'symbols': syms,
  'companies': companies,
  'n': len(syms)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qdLIKDynnEUet9nJTfF5AaTo': 'file_storage/call_qdLIKDynnEUet9nJTfF5AaTo.json'}

exec(code, env_args)
