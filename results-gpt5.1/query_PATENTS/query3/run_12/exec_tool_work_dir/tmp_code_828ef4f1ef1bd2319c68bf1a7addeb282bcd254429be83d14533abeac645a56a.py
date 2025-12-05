code = """import json, pandas as pd, re, os
from collections import defaultdict

path = var_call_1pfrSWFeOT6sj3gYqeHp896E
with open(path) as f:
    data = json.load(f)

# Build mapping from publication_number -> assignee and CPC codes
pub_assignee = {}
pub_cpc = {}

for rec in data:
    info = rec.get('Patents_info','')
    # extract publication_number like US-2022074631-A1
    m_pub = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    if not m_pub:
        m_pub = re.search(r'publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    pubno = m_pub.group(1) if m_pub else None
    m_ass = re.search(r'assignee_harmonized: ([^;]+)', info)
    if not m_ass:
        m_ass = re.search(r'owned by ([^.;]+)', info)
    if not m_ass:
        m_ass = re.search(r'helds? the [A-Z]{2} patent filing .* is (?:owned by|assigned to) ([^.;]+)', info)
    assignee = m_ass.group(1).strip() if m_ass else None
    try:
        cpcs = json.loads(rec.get('cpc') or '[]')
    except Exception:
        cpcs = []
    codes = sorted(set([c['code'] for c in cpcs if 'code' in c]))
    if pubno:
        pub_assignee[pubno] = assignee
        pub_cpc[pubno] = codes

# Collect citations to build reverse map: cited pub -> set of citing assignees
cited_to_citers = defaultdict(set)

for rec in data:
    info = rec.get('Patents_info','')
    # identify citing publication number
    m_pub = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    if not m_pub:
        m_pub = re.search(r'publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    citing_pub = m_pub.group(1) if m_pub else None
    m_ass = re.search(r'assignee_harmonized: ([^;]+)', info)
    if not m_ass:
        m_ass = re.search(r'owned by ([^.;]+)', info)
    assignee = m_ass.group(1).strip() if m_ass else None

    try:
        cits = json.loads(rec.get('citation') or '[]')
    except Exception:
        cits = []
    for c in cits:
        cpub = c.get('publication_number')
        if cpub and assignee and assignee != 'UNIV CALIFORNIA':
            cited_to_citers[cpub].add(assignee)

# Now we want cited patents whose assignee is UNIV CALIFORNIA
result_pairs = []  # (assignee, cpc_code)
for cited_pub, assigs in cited_to_citers.items():
    if pub_assignee.get(cited_pub) == 'UNIV CALIFORNIA':
        for a in assigs:
            for code in pub_cpc.get(cited_pub, []):
                # reduce to primary CPC subclass: take up to main group, e.g., C09D11/00 -> C09D11/00; keep as-is
                result_pairs.append((a, code))

# unique codes
unique_codes = sorted(set(code for _, code in result_pairs))

out = {
  'assignee_cpc_pairs': sorted(list({(a,c) for a,c in result_pairs})),
  'unique_cpc_codes': unique_codes
}

j = json.dumps(out)
print("__RESULT__:")
print(j)"""

env_args = {'var_call_oa6AsXxiXSObpRPJv5ypO7NX': [], 'var_call_fgpTHTcfjBuJYtk11VJRy3P9': ['cpc_definition'], 'var_call_1pfrSWFeOT6sj3gYqeHp896E': 'file_storage/call_1pfrSWFeOT6sj3gYqeHp896E.json'}

exec(code, env_args)
