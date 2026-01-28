code = """import json
from pathlib import Path

res_path = Path(var_call_0mQglWcsWaS71wSJDfJpPg8m)
res = json.loads(res_path.read_text())
# Filter results to only those where project name or funding source or status mention 'fema' or 'emergency'
out = []
for r in res:
    pname = (r.get('Project_Name') or '').lower()
    psource = (r.get('Funding_Source') or '').lower()
    status = (r.get('Status') or '').lower()
    if 'fema' in pname or 'fema' in psource or 'fema' in status or 'emergency' in pname or 'emergency' in psource or 'emergency' in status:
        out.append(r)
# also include ones with '(FEMA' in name
for r in res:
    if '(fema' in (r.get('Project_Name') or '').lower() and r not in out:
        out.append(r)

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json', 'var_call_aYt4NsGlTLq0WSd9YxToc5f3': {'civic_var': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'funding_var': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}, 'var_call_0mQglWcsWaS71wSJDfJpPg8m': 'file_storage/call_0mQglWcsWaS71wSJDfJpPg8m.json'}

exec(code, env_args)
