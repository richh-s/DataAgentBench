code = """import json, pandas as pd, re, os
path = var_call_09M6hbFwQJRldz97tYKCZCt3
with open(path, 'r') as f:
    data = json.load(f)
# Build lookup of pub number -> assignee, cpc for all patents
rows = []
for rec in data:
    info = rec['Patents_info']
    m_pub = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    pubnum = m_pub.group(1) if m_pub else None
    m_app = re.search(r'application \(number ([A-Z]{2}-[0-9A-Z]+-[A-Z])\)', info)
    assignee_match = re.search(r'owned by (.+?) and has pub\. number', info)
    if not assignee_match:
        assignee_match = re.search(r'assigned to (.+?) and has publication number', info)
    if not assignee_match:
        assignee_match = re.search(r'holds the .*? filing .*?, with pub\. number', info)
    assignee = assignee_match.group(1) if assignee_match else None
    cpcs = [e['code'] for e in json.loads(rec['cpc'])] if rec['cpc'] else []
    cites = [c['publication_number'] for c in json.loads(rec['citation'])] if rec['citation'] else []
    rows.append({'pubnum': pubnum, 'assignee': assignee, 'cpcs': cpcs, 'cited_pubnums': cites})
# identify UC patents' pubnums
uc_pubnums = set(r['pubnum'] for r in rows if r['assignee'] and 'UNIV CALIFORNIA' in r['assignee'])
# now need full database to find citing patents where citation includes a UC pubnum
# can't access full DB, so approximate within UC-owned subset
citing_assignees = {}
for r in rows:
    if not r['cited_pubnums'] or not r['assignee']:
        continue
    if 'UNIV CALIFORNIA' in r['assignee']:
        continue
    if any(c in uc_pubnums for c in r['cited_pubnums']):
        citing_assignees.setdefault(r['assignee'], set()).update(r['cpcs'])
result = [{'assignee': a, 'cpc_codes': sorted(list(codes))} for a, codes in citing_assignees.items()]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_69nShL88Fyb6t19WVHEwy3HU': [], 'var_call_09M6hbFwQJRldz97tYKCZCt3': 'file_storage/call_09M6hbFwQJRldz97tYKCZCt3.json'}

exec(code, env_args)
