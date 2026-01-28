code = """import json, re
from collections import defaultdict

# Load all rows with citations
path = var_call_bikrzAw6eZSC1YQu0kHbrdd4
with open(path,'r',encoding='utf-8') as f:
    rows = json.load(f)

# Get UC publications list from earlier CALIFORNIA query rows
uc_path = var_call_NETCgiRx70xDGMqzp64VWVxg
with open(uc_path,'r',encoding='utf-8') as f:
    cal_rows = json.load(f)
uc_pubs=set()
for r in cal_rows:
    pi=r.get('Patents_info','')
    if 'UNIV CALIFORNIA' in pi:
        m=re.search(r'pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
        if not m:
            m=re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
        if m:
            uc_pubs.add(m.group(1))

# Helper parse assignee from Patents_info
assignee_patterns=[
    r'^(.*?) holds the',
    r'is owned by (.*?) and has',
    r'is assigned to (.*?) and has',
    r'owned by (.*?), with publication',
    r'assigned to (.*?), with publication',
]

def extract_assignee(pi:str):
    pi=pi.strip()
    # remove leading country phrase
    pi=re.sub(r'^In [A-Z]{2},\s*','',pi)
    for pat in assignee_patterns:
        m=re.search(pat, pi)
        if m:
            return m.group(1).strip().strip(',')
    return None

citing_assignees=set()
for r in rows:
    cit=r.get('citation')
    if not cit:
        continue
    try:
        cits=json.loads(cit)
    except Exception:
        continue
    cited_pubs=set()
    for c in cits:
        pn=c.get('publication_number','')
        if pn:
            cited_pubs.add(pn)
    if cited_pubs & uc_pubs:
        ass=extract_assignee(r.get('Patents_info',''))
        if ass and ass!='UNIV CALIFORNIA':
            citing_assignees.add(ass)

print('__RESULT__:')
print(json.dumps(sorted(citing_assignees)))"""

env_args = {'var_call_YJidZmBvU5MTPVYW57hU6WF7': ['publicationinfo'], 'var_call_LRepTdXnPvuewKZleMJeYEt0': ['cpc_definition'], 'var_call_89qb0KndyOtUX3EZVb5EyOw1': [], 'var_call_EpTAmg0Qd8RR0QwpJzsoYOy4': [], 'var_call_orSJcL9REVmx7crexoGaa75w': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_u13kdrbYze9McgMf77J8ZfqV': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'], 'var_call_NETCgiRx70xDGMqzp64VWVxg': 'file_storage/call_NETCgiRx70xDGMqzp64VWVxg.json', 'var_call_hIW3RERYBuL0XZdQDDqC03yH': {'uc_publications_count': 24, 'primary_subclasses': ['A61H', 'A61K', 'A61L', 'A61P', 'B82B', 'C07C', 'C07D', 'C07H', 'C07K', 'C08G', 'C09J', 'C12N', 'C12Q', 'C30B', 'E04H', 'F25B', 'G01N', 'G01T', 'G01V']}, 'var_call_bikrzAw6eZSC1YQu0kHbrdd4': 'file_storage/call_bikrzAw6eZSC1YQu0kHbrdd4.json'}

exec(code, env_args)
