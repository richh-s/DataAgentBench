code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

recs = load_records(var_call_L8fDs73ZbOWv1aufcn7fQYRG)

def parse_pubnum(s):
    return s.strip() if isinstance(s, str) else None

# Build mapping: cited_pub -> set(uc_pub)
uc_pubs = set()
uc_cited = set()
for r in recs:
    pi = r.get('Patents_info','')
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[^\s\.,]*)', pi)
    if not m:
        m = re.search(r'pub\. number\s+([A-Z]{2}\s*[0-9]+[^\s\.,]*)', pi)
    uc_pub = m.group(1) if m else None
    if uc_pub:
        uc_pubs.add(uc_pub)
    cit = r.get('citation')
    try:
        cit_list = json.loads(cit) if isinstance(cit, str) and cit.strip().startswith('[') else []
    except Exception:
        cit_list = []
    for c in cit_list:
        pn = parse_pubnum(c.get('publication_number'))
        if pn:
            uc_cited.add(pn)

# Now find all publications that cite any UC publication number
# use SQL LIKE for each prefix? We'll just fetch rows where citation contains 'US-' etc and filter in python
print('__RESULT__:')
print(json.dumps({'uc_publications_count': len(uc_pubs), 'unique_cited_pubnums_in_uc_patents': len(uc_cited), 'sample_uc_pubnums': sorted(list(uc_pubs))[:10]}))"""

env_args = {'var_call_23VvrFdA40JcWZBuqH9jRbLo': ['publicationinfo'], 'var_call_7lw1L8BPzvfVu1w1VqgpeU3c': ['cpc_definition'], 'var_call_kiOeirk9Z6qjJK8KB6oCKo89': [], 'var_call_L8fDs73ZbOWv1aufcn7fQYRG': 'file_storage/call_L8fDs73ZbOWv1aufcn7fQYRG.json'}

exec(code, env_args)
