code = """import json, re, pandas as pd
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x,'r',encoding='utf-8'))
    return x

recs = load_records(var_call_qRWQTJABX8lc4IPA6CVXZtuH)

# helper to extract publication_number and assignee_harmonized from Patents_info
pub_re = re.compile(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', re.I)
assg_re = re.compile(r'owned by\s+([^\.]+)', re.I)
assg2_re = re.compile(r'assigned to\s+([^\.]+)', re.I)
assg3_re = re.compile(r'holds the\s+[A-Z]{2}\s+patent filing.*?owned by\s+([^,\.]+)', re.I)

rows=[]
for r in recs:
    pi = r.get('Patents_info') or ''
    m = pub_re.search(pi)
    if not m:
        continue
    pub = m.group(1).upper()
    # normalize pub format already like US-2022074631-A1
    assg=None
    for rx in (assg_re, assg2_re, assg3_re):
        mm = rx.search(pi)
        if mm:
            assg = mm.group(1).strip()
            break
    if not assg:
        # fallback: contains 'UNIV CALIFORNIA holds'
        if 'UNIV CALIFORNIA' in pi.upper():
            assg='UNIV CALIFORNIA'
    rows.append({'uc_pub':pub,'uc_patents_info':pi,'uc_assignee':assg,'uc_cpc_raw':r.get('cpc')})

uc_df = pd.DataFrame(rows).drop_duplicates(subset=['uc_pub'])

# Build a set of UC publication_numbers for matching in citations
uc_pubs = set(uc_df['uc_pub'].tolist())

# Now find all citing publications that cite any UC publication
# Need to scan all records with citations and see if any cited publication_number in uc_pubs
# Query all with citation not null and not empty

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs)}))"""

env_args = {'var_call_BqFBih7gQaqIxBlVRthiRuTU': ['publicationinfo'], 'var_call_jto7NMN8HlbGcKqShFKjzGug': ['cpc_definition'], 'var_call_qRWQTJABX8lc4IPA6CVXZtuH': 'file_storage/call_qRWQTJABX8lc4IPA6CVXZtuH.json'}

exec(code, env_args)
