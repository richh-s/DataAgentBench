code = """import json, re
import pandas as pd

# load records
src = var_call_QlDCLePqJogYQ2wyYP5FHfsg
if isinstance(src, str) and src.endswith('.json'):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

uc_pub_to_primary = {}
uc_pubs = set()
for r in recs:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-\d{7,}-[A-Z]\d?)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-\d{7,}-[A-Z]\d?)', pi)
    pub = m.group(1) if m else None
    if pub:
        uc_pubs.add(pub)
    cpc_raw = r.get('cpc')
    primary = None
    if cpc_raw:
        try:
            cpcs = json.loads(cpc_raw)
        except Exception:
            cpcs = []
        # primary = first==true; take subclass (e.g., F25B21/00 -> F25B)
        for e in cpcs:
            if isinstance(e, dict) and e.get('first') is True:
                code = e.get('code')
                if isinstance(code, str):
                    code = code.strip()
                    primary = code
                    break
    if pub and primary:
        # normalize to subclass symbol: 4 chars after section+class? CPC subclass is like F25B, C12Q
        m2 = re.match(r'^([A-HY]\d{2}[A-Z])', primary)
        subclass = m2.group(1) if m2 else primary
        uc_pub_to_primary[pub] = subclass

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs), 'mapped_primary_count': len(uc_pub_to_primary), 'sample': list(uc_pub_to_primary.items())[:5]}))"""

env_args = {'var_call_WHv1lmPSfKcTdS8wJQw8DFVx': ['publicationinfo'], 'var_call_9FObhEdTKcKZY57NsI47GeTw': ['cpc_definition'], 'var_call_C0tsT6udBqwTfDYCy6wmqC6T': [], 'var_call_QlDCLePqJogYQ2wyYP5FHfsg': 'file_storage/call_QlDCLePqJogYQ2wyYP5FHfsg.json'}

exec(code, env_args)
