code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

pub_recs = load_records(var_call_5dYnMvBJZnQfC9UIf2YHeLOD)
cpcdef_recs = load_records(var_call_j5D3GOcOU4a7SxvX6LAidKH9)

# Build lookup for CPC symbols -> titleFull
cpc_title = {r['symbol']: r.get('titleFull') for r in cpcdef_recs if r.get('symbol')}

# Helper: extract assignee from Patents_info
assignee_pat = re.compile(r"owned by ([^,]+?) and has pub\.")
assignee_pat2 = re.compile(r"is assigned to ([^,]+?) and has")
assignee_pat3 = re.compile(r"holds the [A-Z]{2} patent filing .*? is (?:owned by|assigned to) ([^,]+?)(?: and|\.)")

def extract_assignee(pinfo: str):
    for pat in (assignee_pat, assignee_pat2, assignee_pat3):
        m = pat.search(pinfo or '')
        if m:
            return m.group(1).strip()
    # fallback: last occurrence
    if pinfo and 'UNIV CALIFORNIA' in pinfo:
        return 'UNIV CALIFORNIA'
    return None

# collect UC publication numbers
uc_pubnums = set()
for r in pub_recs:
    pinfo = r.get('Patents_info','')
    if 'pub. number' in pinfo:
        m = re.search(r"pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pinfo)
        if m:
            uc_pubnums.add(m.group(1))

# build map from cited publication_number -> set(uc_publication_record_index)
# and primary CPC subclass (first==true) per UC patent
uc_primary_subclass = {}  # uc_pubnum -> set(subclass codes)

def parse_jsonish(s):
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        return []

for r in pub_recs:
    pinfo = r.get('Patents_info','')
    assignee = extract_assignee(pinfo)
    if assignee != 'UNIV CALIFORNIA':
        continue
    m = re.search(r"pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pinfo)
    if not m:
        continue
    uc_pub = m.group(1)
    cpcs = parse_jsonish(r.get('cpc'))
    primary = [c.get('code') for c in cpcs if c.get('first') is True and c.get('code')]
    # convert to subclass = first 4 chars + '/' + group? In CPC, subclass is first 4 chars (e.g., C12Q)
    subclasses = set([code[:4] for code in primary])
    uc_primary_subclass[uc_pub] = subclasses

# Now find citing patents: those whose citation list includes a UC pubnum
# Need all publicationinfo rows (not just UC). We only queried UC rows. Can't find citing assignees.
result = {"error":"Insufficient data: only UC-assigned records were queried. Need full publicationinfo (or at least records that cite UC patents) to identify citing assignees."}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5dYnMvBJZnQfC9UIf2YHeLOD': 'file_storage/call_5dYnMvBJZnQfC9UIf2YHeLOD.json', 'var_call_j5D3GOcOU4a7SxvX6LAidKH9': 'file_storage/call_j5D3GOcOU4a7SxvX6LAidKH9.json'}

exec(code, env_args)
