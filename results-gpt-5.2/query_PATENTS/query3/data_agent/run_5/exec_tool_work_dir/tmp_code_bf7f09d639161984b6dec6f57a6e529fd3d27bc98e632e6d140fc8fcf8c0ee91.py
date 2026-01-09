code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

# UC patents set from earlier query (UC-only)
uc_recs = load_records(var_call_5dYnMvBJZnQfC9UIf2YHeLOD)
all_citing_recs = load_records(var_call_El1OwxXrwjUoghDJwjkxAMnx)
cpcdef_recs = load_records(var_call_j5D3GOcOU4a7SxvX6LAidKH9)

cpc_title = {r['symbol']: r.get('titleFull') for r in cpcdef_recs if r.get('symbol')}

# Extract UC publication numbers
uc_pubnums = set()
for r in uc_recs:
    pinfo = r.get('Patents_info','')
    m = re.search(r"pub\.? (?:number|no\.) ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pinfo)
    if m:
        uc_pubnums.add(m.group(1))

# Map UC pubnum -> primary CPC subclass symbols (e.g., C12Q)

def parse_jsonish(s):
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        return []

uc_to_subclasses = {}
for r in uc_recs:
    pinfo = r.get('Patents_info','')
    m = re.search(r"pub\.? (?:number|no\.) ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pinfo)
    if not m:
        continue
    uc_pub = m.group(1)
    cpcs = parse_jsonish(r.get('cpc'))
    primary_codes = [c.get('code') for c in cpcs if c.get('first') is True and c.get('code')]
    subclasses = sorted(set([code[:4] for code in primary_codes]))
    uc_to_subclasses[uc_pub] = subclasses

# Extract citing assignee from Patents_info (best-effort)
patterns = [
    re.compile(r"^(.+?) holds the"),
    re.compile(r"^The [A-Z]{2} application .*? is belonging to (.+?) and has"),
    re.compile(r"^In [A-Z]{2}, the application .*? is owned by (.+?) and has"),
    re.compile(r"is assigned to (.+?) and has"),
    re.compile(r"is owned by (.+?) and has"),
]

def extract_assignee(pinfo):
    for pat in patterns:
        m = pat.search(pinfo or '')
        if m:
            return m.group(1).strip()
    return None

rows = []
for r in all_citing_recs:
    citing_pinfo = r.get('Patents_info','')
    citing_assignee = extract_assignee(citing_pinfo)
    if not citing_assignee:
        continue
    if citing_assignee.strip().upper() == 'UNIV CALIFORNIA':
        continue
    citations = parse_jsonish(r.get('citation'))
    cited_pubnums = [c.get('publication_number') for c in citations if isinstance(c, dict)]
    cited_uc = [p for p in cited_pubnums if p in uc_pubnums]
    if not cited_uc:
        continue
    for uc_pub in cited_uc:
        for subclass in uc_to_subclasses.get(uc_pub, []):
            title = cpc_title.get(subclass)
            if title:
                rows.append({"citing_assignee": citing_assignee, "cpc_subclass": subclass, "cpc_subclass_title": title})

if rows:
    df = pd.DataFrame(rows).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
    out = df.to_dict(orient='records')
else:
    out = []

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5dYnMvBJZnQfC9UIf2YHeLOD': 'file_storage/call_5dYnMvBJZnQfC9UIf2YHeLOD.json', 'var_call_j5D3GOcOU4a7SxvX6LAidKH9': 'file_storage/call_j5D3GOcOU4a7SxvX6LAidKH9.json', 'var_call_ZvoUZHBY7Qc1kHaQvUQacJCe': {'error': 'Insufficient data: only UC-assigned records were queried. Need full publicationinfo (or at least records that cite UC patents) to identify citing assignees.'}, 'var_call_iGN1nsH0ZdjB9Y0d3VeOXdgk': 'file_storage/call_iGN1nsH0ZdjB9Y0d3VeOXdgk.json', 'var_call_El1OwxXrwjUoghDJwjkxAMnx': 'file_storage/call_El1OwxXrwjUoghDJwjkxAMnx.json'}

exec(code, env_args)
