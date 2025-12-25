code = """import json, re, os
from collections import defaultdict

path = var_call_gTBh6mfJs1y6Mviwn7UH1a8s
if isinstance(path, str) and os.path.isfile(path):
    with open(path, 'r') as f:
        data = json.load(f)
else:
    data = var_call_gTBh6mfJs1y6Mviwn7UH1a8s

pub_to_assignee = {}
for rec in data:
    info = rec.get('Patents_info','')
    m_pub = re.search(r'pub\. number\s+([A-Z0-9\-]+)', info)
    pub = m_pub.group(1) if m_pub else None
    assignee = None
    m_ass = re.search(r'owned by ([^,]+)', info)
    if m_ass:
        assignee = m_ass.group(1)
    m_ass2 = re.search(r'assigned to ([^,]+)', info)
    if not assignee and m_ass2:
        assignee = m_ass2.group(1)
    if 'holds the' in info and 'UNIV CALIFORNIA' in info and not assignee:
        assignee = 'UNIV CALIFORNIA'
    if pub and assignee:
        pub_to_assignee[pub] = assignee.strip()

citing_assignee_to_codes = defaultdict(set)
for rec in data:
    info = rec.get('Patents_info','')
    assignee = None
    m_ass = re.search(r'owned by ([^,]+)', info)
    if m_ass:
        assignee = m_ass.group(1)
    m_ass2 = re.search(r'assigned to ([^,]+)', info)
    if not assignee and m_ass2:
        assignee = m_ass2.group(1)
    if 'holds the' in info and 'UNIV CALIFORNIA' in info and not assignee:
        assignee = 'UNIV CALIFORNIA'
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    citations = rec.get('citation','')
    try:
        cites = json.loads(citations) if citations else []
    except Exception:
        continue
    cites_univ = False
    for c in cites:
        pub = c.get('publication_number')
        if pub and pub_to_assignee.get(pub) == 'UNIV CALIFORNIA':
            cites_univ = True
            break
    if not cites_univ:
        continue
    cpc_raw = rec.get('cpc','')
    try:
        cpcs = json.loads(cpc_raw) if cpc_raw else []
    except Exception:
        cpcs = []
    primary_codes = [e['code'] for e in cpcs if e.get('first')]
    for code in primary_codes:
        subclass = code.split('/')[0] if '/' in code else code
        citing_assignee_to_codes[assignee].add(subclass)

result = {assignee: sorted(list(codes)) for assignee, codes in citing_assignee_to_codes.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SvnaiGgIo6WyeDZa416wh3HL': [], 'var_call_gTBh6mfJs1y6Mviwn7UH1a8s': 'file_storage/call_gTBh6mfJs1y6Mviwn7UH1a8s.json'}

exec(code, env_args)
