code = """import json
import re
from collections import defaultdict

# Load the stored query results from files
with open(var_call_D4rq9cs4gFNTl4lSdqgfzKOa, 'r', encoding='utf-8') as f:
    unc_rows = json.load(f)
with open(var_call_IItaqV0SEoPNDJAoMxeGoSEA, 'r', encoding='utf-8') as f:
    all_rows = json.load(f)

# Helper to extract publication number from Patents_info
pub_patterns = [r'pub\. number\s*([A-Z0-9\-\._]+)', r'publication number\s*([A-Z0-9\-\._]+)', r'with pub\. number\s*([A-Z0-9\-\._]+)', r'with publication number\s*([A-Z0-9\-\._]+)']
unc_pubnums = set()
for r in unc_rows:
    info = r.get('Patents_info','')
    found = None
    for p in pub_patterns:
        m = re.search(p, info, flags=re.IGNORECASE)
        if m:
            found = m.group(1).strip()
            break
    if not found:
        # try to find patterns like 'publication number .*?([A-Z0-9\-]+)'
        m = re.search(r'([A-Z]{1,3}-\d{4,}|US-\d+|WO-\d+|JP-\w+|TW-\d+|FR-\d+|EP-\d+|CN-\d+)', info)
        if m:
            found = m.group(0)
    if found:
        unc_pubnums.add(found)

# Parse citations of all_rows to find those that cite any UNC publication numbers
# Also extract assignee from Patents_info and primary CPC codes
assignee_to_codes = defaultdict(set)
records_citing = []

for r in all_rows:
    citation_raw = r.get('citation', '[]')
    try:
        citations = json.loads(citation_raw)
    except Exception:
        citations = []
    cites_unc = False
    for c in citations:
        pubnum = c.get('publication_number','')
        if pubnum in unc_pubnums:
            cites_unc = True
            break
    if cites_unc:
        info = r.get('Patents_info','')
        # extract assignee using patterns
        assignee = None
        # common phrases
        patterns = [r'^(.*?)\s+holds\b', r'^(.*?)\s+holds the\b', r'^(.*?)\s+is assigned to\b', r'^(.*?)\s+is owned by\b', r'^(.*?)\s+holds the US', r'^(.*?)\s+has the US', r'^(.*?)\s+owns the', r'^(.*?)\s+filed the']
        for p in patterns:
            m = re.search(p, info, flags=re.IGNORECASE)
            if m:
                assignee = m.group(1).strip()
                break
        if not assignee:
            # try to capture leading uppercase sequence
            m = re.match(r'^([A-Z0-9 &,\.\-]+)', info)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            assignee = info.strip().split(' ')[0]
        # normalize
        assignee = assignee.strip().upper()
        if 'UNIV CALIFORNIA' in assignee:
            continue
        # extract primary CPC codes
        cpc_raw = r.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_raw)
        except Exception:
            cpc_list = []
        primary_codes = [entry.get('code') for entry in cpc_list if entry.get('first')]
        if not primary_codes and cpc_list:
            primary_codes = [cpc_list[0].get('code')]
        for code in primary_codes:
            if code:
                assignee_to_codes[assignee].add(code)

# Convert sets to sorted lists
assignee_codes_out = {a: sorted(list(codes)) for a, codes in assignee_to_codes.items()}

result = []
for a, codes in assignee_codes_out.items():
    result.append({'assignee': a, 'primary_cpc_codes': codes})

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_D4rq9cs4gFNTl4lSdqgfzKOa': 'file_storage/call_D4rq9cs4gFNTl4lSdqgfzKOa.json', 'var_call_IItaqV0SEoPNDJAoMxeGoSEA': 'file_storage/call_IItaqV0SEoPNDJAoMxeGoSEA.json'}

exec(code, env_args)
