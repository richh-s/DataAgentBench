code = """import json, re
import pandas as pd

# UC-owned records
with open(var_call_E6tbXMkCCY50UNQlzqQSeEjh, 'r', encoding='utf-8') as f:
    uc_recs = json.load(f)

uc_pubs=set()
uc_pub_to_primary_subclass={}
for r in uc_recs:
    pi=r.get('Patents_info') or ''
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi) or re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    pub=m.group(1) if m else None
    if pub:
        uc_pubs.add(pub)
    primary=None
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
        for e in cpcs:
            if isinstance(e, dict) and e.get('first') is True and e.get('code'):
                primary=e['code']
                break
    except Exception:
        primary=None
    if pub and primary:
        uc_pub_to_primary_subclass[pub]=primary[:4]

# Load citing patents set: all rows with non-empty citation (needs whole table; do broad query and filter in python)
# We'll query all Patents_info,citation where citation!='[]'
# This may be large; use sqlite tool output? We'll use existing DB tool by chunking with LIMIT/OFFSET.

import sqlite3
con=sqlite3.connect('file:publication_database?mode=ro', uri=True)
cur=con.cursor()
cur.execute('SELECT COUNT(*) FROM publicationinfo WHERE citation IS NOT NULL AND citation!=\'[]\'')
(total_nonempty,) = cur.fetchone()

chunk=2000
offset=0
rows=[]
while offset<total_nonempty:
    q=f"SELECT Patents_info, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation!='[]' LIMIT {chunk} OFFSET {offset};"
    df=pd.read_sql_query(q, con)
    for _, rr in df.iterrows():
        try:
            cits=json.loads(rr['citation'])
        except Exception:
            continue
        found=False
        for c in cits:
            pn=(c or {}).get('publication_number')
            if pn in uc_pub_to_primary_subclass:
                found=True
                break
        if found:
            rows.append({'Patents_info': rr['Patents_info'], 'citation': rr['citation']})
    offset += chunk
con.close()

citing_df=pd.DataFrame(rows).drop_duplicates()

pairs=[]
for _, rr in citing_df.iterrows():
    pi=rr['Patents_info'] or ''
    am=re.search(r'(?:owned by|assigned to)\s+([^,.]+)', pi) or re.search(r'^([^,]+?)\s+holds', pi)
    assignee=am.group(1).strip() if am else None
    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    try:
        cits=json.loads(rr['citation'])
    except Exception:
        cits=[]
    subclasses=set()
    for c in cits:
        pn=(c or {}).get('publication_number')
        if pn in uc_pub_to_primary_subclass:
            subclasses.add(uc_pub_to_primary_subclass[pn])
    for sc in subclasses:
        pairs.append({'citing_assignee': assignee, 'cpc_subclass': sc})

out_df=pd.DataFrame(pairs).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
print('__RESULT__:')
print(json.dumps(out_df.to_dict(orient='records')))"""

env_args = {'var_call_ky9p28bfw6ZzpdkIpcICy6Ul': ['publicationinfo'], 'var_call_9FjvG9K7GEUQ2jOWlZFfSjSr': ['cpc_definition'], 'var_call_FPczLPUeIyYnvaQzIKLNGXAr': [], 'var_call_E6tbXMkCCY50UNQlzqQSeEjh': 'file_storage/call_E6tbXMkCCY50UNQlzqQSeEjh.json', 'var_call_JuEFYCQ1kR51VnVGUHBz75aP': 'file_storage/call_JuEFYCQ1kR51VnVGUHBz75aP.json'}

exec(code, env_args)
