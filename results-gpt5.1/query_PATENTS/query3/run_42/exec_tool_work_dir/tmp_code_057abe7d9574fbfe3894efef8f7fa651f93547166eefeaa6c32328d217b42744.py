code = """import json, re, pandas as pd, os
from collections import defaultdict

path = var_call_sCChEZqyqN6yj4Ygq1oFYzAA
with open(path, 'r') as f:
    data = json.load(f)

rows = []
for rec in data:
    info = rec.get('Patents_info','')
    m_pub = re.search(r'pub\. number ([A-Z0-9\-]+)', info)
    if not m_pub:
        m_pub = re.search(r'publication number ([A-Z0-9\-]+)', info)
    pubnum = m_pub.group(1) if m_pub else None
    m_ass = re.search(r'assignee_harmonized: ([^;]+)', info)
    assignee = m_ass.group(1).strip() if m_ass else None
    rows.append({'pubnum': pubnum, 'assignee': assignee, 'Patents_info': info})

# citing patents: any record whose citation list includes a publication_number equal to a UC-assigned publication

uc_pubnums = {r['pubnum'] for r in rows if r['pubnum']}

citing_assignees = defaultdict(set)

for rec in data:
    info = rec.get('Patents_info','')
    # extract assignee
    m_ass = re.search(r'assignee_harmonized: ([^;]+)', info)
    assignee = m_ass.group(1).strip() if m_ass else None
    if assignee and 'UNIV CALIFORNIA' in assignee.upper():
        continue
    cit_raw = rec.get('citation','') or '[]'
    try:
        cit_list = json.loads(cit_raw)
    except Exception:
        cit_list = []
    cites_uc = False
    for c in cit_list:
        pn = c.get('publication_number','')
        if pn in uc_pubnums:
            cites_uc = True
            break
    if cites_uc and assignee:
        citing_assignees[assignee].add(rec.get('cpc',''))

# collect unique CPC codes from these citing patents
cpc_codes = set()
for cpcs in citing_assignees.values():
    for cpc_raw in cpcs:
        try:
            arr = json.loads(cpc_raw or '[]')
        except Exception:
            arr = []
        for ent in arr:
            code = ent.get('code')
            if code:
                # primary subclass = strip subgroup after last '/'
                main = code.split('/')[0]
                cpc_codes.add(main)

result = {
    'assignees': {k: sorted(list(cpc_codes)) for k in citing_assignees.keys()},
    'cpc_codes': sorted(list(cpc_codes))
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zg2RF6TKWMwsObsqULUDjS6b': [], 'var_call_ej5s1CFycx38S4PjMvlGG6oX': ['cpc_definition'], 'var_call_sCChEZqyqN6yj4Ygq1oFYzAA': 'file_storage/call_sCChEZqyqN6yj4Ygq1oFYzAA.json'}

exec(code, env_args)
