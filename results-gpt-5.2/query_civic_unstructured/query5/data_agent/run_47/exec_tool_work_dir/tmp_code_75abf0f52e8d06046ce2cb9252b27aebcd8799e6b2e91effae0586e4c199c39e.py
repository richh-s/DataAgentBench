code = """import json, re

path_f = var_call_bsvCGgGs1UKNCyhvSwDM7RI1
with open(path_f, 'r', encoding='utf-8') as f:
    funding = json.load(f)

path_d = var_call_1cHz8oHf2VudXAUNBQIdKa8v
with open(path_d, 'r', encoding='utf-8') as f:
    docs = json.load(f)

funding_names = set(fr['Project_Name'] for fr in funding)

projects = {}
header_pat = re.compile(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*(\((Design|Construction|Not Started)\))?\s*$', re.I)
start_pat = re.compile(r'\b(Start|Begin Construction)\s*:\s*([^\n]+)', re.I)

for doc in docs:
    text = doc.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.rstrip() for ln in text.splitlines()]
    section = None
    current_project = None
    for ln in lines:
        m = header_pat.match(ln)
        if m:
            section = m.group(1).strip().lower()
            current_project = None
            continue
        if section != 'disaster recovery projects':
            continue
        if not ln.strip():
            continue
        s = ln.strip()
        # skip obvious non-project lines
        skip_prefixes = ('(cid:', 'Page ', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved',
                         'Date prepared', 'Meeting date', 'Subject:', 'Updates', 'Project Schedule', 'Estimated Schedule',
                         'Project Description')
        if s.startswith(skip_prefixes):
            continue
        if s.startswith(('•','-','–','\uf0b7')):
            continue
        # project line: exact match with Funding table project name
        if s in funding_names:
            current_project = s
            projects.setdefault(current_project, {'Project_Name': current_project, 'start_fields': []})
            continue
        if current_project:
            sm = start_pat.search(s)
            if sm:
                projects[current_project]['start_fields'].append(sm.group(2).strip())

started_2022 = set()
for pn, info in projects.items():
    if any('2022' in st for st in info['start_fields']):
        started_2022.add(pn)

fund_sum = 0
for fr in funding:
    if fr['Project_Name'] in started_2022:
        try:
            fund_sum += int(fr['Amount'])
        except Exception:
            pass

result = {'total_funding': fund_sum, 'project_count': len(started_2022), 'projects': sorted(started_2022)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bsvCGgGs1UKNCyhvSwDM7RI1': 'file_storage/call_bsvCGgGs1UKNCyhvSwDM7RI1.json', 'var_call_1cHz8oHf2VudXAUNBQIdKa8v': 'file_storage/call_1cHz8oHf2VudXAUNBQIdKa8v.json'}

exec(code, env_args)
