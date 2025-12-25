code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_JppVdCCwNCSD1uNjh6Tuwnv6
with open(path, 'r') as f:
    records = json.load(f)

# Build map from publication_number -> assignee and CPC primary subclass (first code's subclass)
pub_to_assignee = {}
pub_to_primary_cpc = {}

for rec in records:
    info = rec.get('Patents_info','')
    m_pub = re.search(r'pub\. number ([A-Z0-9\-]+)', info)
    pub_num = m_pub.group(1) if m_pub else None
    m_assignee = re.search(r'owned by ([^.,]+)|assigned to ([^.,]+)|holds the .*? filing .*?, with', info)
    assignee = None
    if m_assignee:
        assignee = m_assignee.group(1) or m_assignee.group(2)
    if not assignee:
        m_assignee2 = re.search(r'is assigned to ([^.,]+)', info)
        if m_assignee2:
            assignee = m_assignee2.group(1)
    if not assignee:
        continue
    assignee = assignee.strip()
    if pub_num:
        pub_to_assignee[pub_num] = assignee
    # parse CPC and take first code as primary subclass code (up to first "/" for subclass)
    cpc_raw = rec.get('cpc')
    if cpc_raw and pub_num:
        try:
            cpcs = json.loads(cpc_raw)
            if cpcs:
                code = cpcs[0].get('code')
                if code:
                    # subclass is up to first "/" or full if none
                    subclass = code.split('/')[0]
                    pub_to_primary_cpc[pub_num] = subclass
        except Exception:
            pass

# Now we need all patents (any assignee) that cite these UNIV CALIFORNIA patents.
# First, get list of publication_numbers we just mapped.
univ_pubs = set(pub_to_assignee.keys())

# Load all publications to find citations
all_path = path  # already all UNIV CALIFORNIA only; we actually need whole DB but we don't have it here
# We only have UNIV CALIFORNIA subset, so cannot find other assignees citing them.

result = {
  'univ_publications_count': len(univ_pubs),
  'note': 'Need full publicationinfo table to find external citations; current subset only has UNIV CALIFORNIA-owned patents.'
}

import json as _j
print("__RESULT__:")
print(_j.dumps(result))"""

env_args = {'var_call_D4H6szc3cfh7BI796k773VCb': [], 'var_call_JppVdCCwNCSD1uNjh6Tuwnv6': 'file_storage/call_JppVdCCwNCSD1uNjh6Tuwnv6.json'}

exec(code, env_args)
