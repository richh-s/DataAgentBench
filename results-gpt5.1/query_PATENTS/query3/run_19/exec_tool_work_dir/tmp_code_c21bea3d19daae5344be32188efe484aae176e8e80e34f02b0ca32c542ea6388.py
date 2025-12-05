code = """import json, re, pandas as pd
from collections import defaultdict

# Load full result for UNIV CALIFORNIA-assigned patents
path = var_call_HbfT9BjzhP7xXeWPLpJrtcG0
with open(path, 'r') as f:
    uc_patents = json.load(f)

# Helper to extract publication numbers from citation JSON string
def extract_pub_numbers(cit_str):
    if not cit_str:
        return []
    try:
        data = json.loads(cit_str)
    except Exception:
        return []
    pubs = []
    for c in data:
        pn = c.get('publication_number') or ''
        if pn:
            pubs.append(pn)
    return pubs

# Get set of cited publication numbers (normalized) for UC patents
cited_pns = set()
for rec in uc_patents:
    for pn in extract_pub_numbers(rec.get('citation')):
        m = re.match(r"([A-Z]{2}-[0-9A-Z]+)/?", pn)
        norm = m.group(1) if m else pn.split('-')[0] if '-' in pn else pn
        cited_pns.add(norm)

# Now find publications whose publication number matches these cited ones, and get their assignees & CPCs
# We don't know schema field for publication number; it's inside Patents_info text like "publication number US-11081687-B2" or "pub. number US-11081687-B2".

all_rows = var_call_Jz8AOE2Tf5zfq22MGv4M3DVc  # just to get structure; but we actually need full table, which may be large.

# We'll query DB in chunks later; for now, just prepare cited_pns list to return.

result = list(cited_pns)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_R4WXCjPHwFKCqiwH8iAkCVXn': [], 'var_call_Jz8AOE2Tf5zfq22MGv4M3DVc': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_HbfT9BjzhP7xXeWPLpJrtcG0': 'file_storage/call_HbfT9BjzhP7xXeWPLpJrtcG0.json'}

exec(code, env_args)
