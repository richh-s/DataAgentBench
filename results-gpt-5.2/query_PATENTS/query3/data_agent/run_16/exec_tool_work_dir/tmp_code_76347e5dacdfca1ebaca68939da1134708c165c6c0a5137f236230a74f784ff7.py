code = """import json, re, pandas as pd
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

uc_recs = load_records(var_call_29sZxqw6esmyTqRimgRWD5oe)

# Map UC publication_number -> set(cpc_first_codes)
uc_pub_to_first_cpc = {}
for r in uc_recs:
    pi = r.get('Patents_info','')
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Za-z-]+)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Za-z-]+)', pi)
    if not m:
        continue
    pub = m.group(1)
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw,str) else (cpc_raw or [])
    except Exception:
        cpcs = []
    first_codes = []
    for c in cpcs:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                first_codes.append(code)
    # dedupe
    uc_pub_to_first_cpc[pub] = sorted(set(first_codes))

uc_pubs = sorted(uc_pub_to_first_cpc.keys())
print('__RESULT__:')
print(json.dumps({'uc_publications': uc_pubs, 'count': len(uc_pubs)}))"""

env_args = {'var_call_WARIrU51ufJzDVMTDu8cN1w8': ['publicationinfo'], 'var_call_QAjMpZ4jD9mwBk4EPKJJhVgl': ['cpc_definition'], 'var_call_zMJEHsIZ0ZXz0lMpwKnP91oh': [], 'var_call_eG8N1uSJihukRzkbf4xtTtS1': 'file_storage/call_eG8N1uSJihukRzkbf4xtTtS1.json', 'var_call_29sZxqw6esmyTqRimgRWD5oe': 'file_storage/call_29sZxqw6esmyTqRimgRWD5oe.json'}

exec(code, env_args)
