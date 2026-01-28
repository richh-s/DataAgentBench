code = """import json, re, pandas as pd

# Load funding records
path_f = var_call_bsvCGgGs1UKNCyhvSwDM7RI1
with open(path_f, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Load civic docs
path_d = var_call_1cHz8oHf2VudXAUNBQIdKa8v
with open(path_d, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract project blocks from docs that include Disaster Recovery Projects section
projects = {}

# Patterns
header_pat = re.compile(r"^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*(\((Design|Construction|Not Started)\))?\s*$", re.I)
project_line_pat = re.compile(r"^\s*([A-Za-z0-9][^\n]{2,120}?)\s*$")
start_pat = re.compile(r"\b(Start|Begin Construction)\s*:\s*([^\n]+)", re.I)

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
        # project title lines: appear as standalone lines, not bullets, not empty
        if not ln.strip():
            continue
        if ln.strip().startswith(('(cid:', 'Page ', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved', 'Date prepared', 'Meeting date', 'Subject:', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description')):
            continue
        if ln.strip().startswith(('•','-','–','(cid:','\uf0b7')):
            continue
        # Heuristic: treat line as project name if it matches and is not a label with colon
        if ':' in ln:
            # could be schedule lines
            pass
        # detect project name by checking if it exists in funding names (exact)
        cand = ln.strip()
        if any(cand == fr['Project_Name'] for fr in funding):
            current_project = cand
            if current_project not in projects:
                projects[current_project] = {'Project_Name': current_project, 'start_fields': []}
            continue
        # If we have current project, capture start info
        if current_project:
            sm = start_pat.search(ln)
            if sm:
                projects[current_project]['start_fields'].append(sm.group(2).strip())

# Determine projects that started in 2022: any start_fields containing '2022'
started_2022 = set()
for pn, info in projects.items():
    for st in info['start_fields']:
        if '2022' in st:
            started_2022.add(pn)
            break

# Sum funding amounts for these projects
# funding amounts are strings in query result
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
