code = """import json, re
import pandas as pd

# Load full UC-assignee publications
path = var_call_D8KOFXg6SsoYmdwmDXj91rd5
with open(path, 'r', encoding='utf-8') as f:
    uc_recs = json.load(f)

uc_pubnums=set()
for r in uc_recs:
    pi=r.get('Patents_info','')
    m=re.search(r'pub\.? number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\.', pi)
    if m:
        uc_pubnums.add(m.group(1))

# Find citing patents: those whose citation list contains any UC publication_number
citing=[]
for r in uc_recs:
    pass

# Need all patents to search citations; query whole table citations+Patents_info+cpc
print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubnums)}))"""

env_args = {'var_call_6r9kRKlWpAnxGL0RQggEq1u2': ['publicationinfo'], 'var_call_E96U2H3Ln095YkOv6QIGX04g': ['cpc_definition'], 'var_call_tPdPyr8N8C3FwSeXzne8Nu8v': [], 'var_call_d2oOELDTbDWpa9VNRi39QqwN': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_D8KOFXg6SsoYmdwmDXj91rd5': 'file_storage/call_D8KOFXg6SsoYmdwmDXj91rd5.json'}

exec(code, env_args)
