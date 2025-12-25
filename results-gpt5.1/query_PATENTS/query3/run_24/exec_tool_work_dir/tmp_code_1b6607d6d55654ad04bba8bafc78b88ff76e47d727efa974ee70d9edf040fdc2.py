code = """import json, re
from collections import defaultdict

# Load full result
path = var_call_E7GHQJl1yoltST0tsUzYBZdU
with open(path, 'r') as f:
    records = json.load(f)

# Helper to extract assignee_harmonized and publication numbers from Patents_info
assignee_re = re.compile(r"assignee_harmonized: ([^,.;]+)")
# Common pub number pattern like US-10337029-B2
pub_re = re.compile(r"publication no\. ([A-Z]{2,3}-[0-9A-Z]+-?[A-Z0-9]*)", re.IGNORECASE)
app_pub_re = re.compile(r"publication number ([A-Z]{2,3}-[0-9A-Z]+-?[A-Z0-9]*)", re.IGNORECASE)

# Map publication number -> assignee for all patents
pub_to_assignee = {}

for rec in records:
    pi = rec.get('Patents_info') or ''
    m_assignee = assignee_re.search(pi)
    if not m_assignee:
        continue
    assignee = m_assignee.group(1).strip()
    m_pub = pub_re.search(pi) or app_pub_re.search(pi)
    if not m_pub:
        continue
    pub = m_pub.group(1).strip()
    pub_to_assignee[pub] = assignee

# Identify UNIV CALIFORNIA patents and their pub numbers
uc_pubs = {p for p,a in pub_to_assignee.items() if a.upper().startswith('UNIV CALIFORNIA')}

# For citations, we need to know which citing patents (with any assignee) cite UC patents.
# But our initial query only pulled rows where Patents_info has UC as assignee or citation mentions it.
# Build a set of all possible UC identifiers appearing in Patents_info text snippets
uc_identifiers = set()
for rec in records:
    pi = rec.get('Patents_info') or ''
    if 'UNIV CALIFORNIA' in pi:
        # grab any US-... style numbers as possible UC publications
        for m in re.finditer(r"[A-Z]{2,3}-[0-9A-Z]+-?[A-Z0-9]*", pi):
            uc_identifiers.add(m.group(0))

# Now iterate over all records again to find citing assignees and collect CPC codes used in those citing patents
citing_assignee_to_cpc = defaultdict(set)

for rec in records:
    pi = rec.get('Patents_info') or ''
    cit = rec.get('citation') or ''

    m_assignee = assignee_re.search(pi)
    if not m_assignee:
        continue
    assignee = m_assignee.group(1).strip()

    if assignee.upper().startswith('UNIV CALIFORNIA'):
        continue

    # Check if this record cites any UC patent by looking for UC publication identifiers in citation field
    cites_uc = False
    for ident in uc_identifiers:
        if ident in cit:
            cites_uc = True
            break
    if not cites_uc:
        continue

    # parse CPC JSON-like list
    cpc_raw = rec.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_raw)
        for entry in cpc_list:
            code = entry.get('code')
            if code:
                citing_assignee_to_cpc[assignee].add(code)
    except Exception:
        pass

# Collect all unique CPC symbols
all_cpc_codes = sorted({code for codes in citing_assignee_to_cpc.values() for code in codes})

result = {
    'assignees': sorted(citing_assignee_to_cpc.keys()),
    'cpc_codes': all_cpc_codes,
    'assignee_to_cpc': {a: sorted(list(codes)) for a, codes in citing_assignee_to_cpc.items()}
}

import json as js
out = js.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_E7GHQJl1yoltST0tsUzYBZdU': 'file_storage/call_E7GHQJl1yoltST0tsUzYBZdU.json'}

exec(code, env_args)
