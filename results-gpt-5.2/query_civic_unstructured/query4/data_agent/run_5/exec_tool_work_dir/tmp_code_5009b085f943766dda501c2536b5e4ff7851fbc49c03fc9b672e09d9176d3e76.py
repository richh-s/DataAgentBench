code = """import json, re
import pandas as pd

# Load mongo docs from json file path
path = var_call_bFT0LzLw79r9xBgBKESnVmpw
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# heuristic: in these agenda reports, project names appear as standalone lines.
# We'll locate lines followed soon by a "Project Schedule" block that contains "Begin Construction:" or "Advertise:" with "Spring 2022".

def extract_projects_started_spring_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = set()
    for i, ln in enumerate(lines):
        if not ln or len(ln) < 4:
            continue
        # candidate project name: not bullet, not label
        if any(ln.lower().startswith(x) for x in ['(cid', 'updates', 'project schedule', 'estimated schedule', 'project description', 'capital improvement projects', 'disaster recovery projects', 'page ', 'agenda item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'staff will provide', 'city will', 'complete design', 'advertise', 'begin construction', 'complete construction']):
            continue
        if ':' in ln and len(ln.split())<6:
            continue
        # look ahead window for spring 2022 start signals
        window = '\n'.join(lines[i:i+40]).lower()
        if ('spring 2022' in window) and (('begin construction' in window) or ('start construction' in window) or ('begin design' in window) or ('start' in window) or ('advertise' in window)):
            # ensure spring 2022 is tied to begin construction or start, not just complete design
            if re.search(r'begin\s+construction\s*:\s*spring\s+2022', window) or re.search(r'begin\s+design\s*:\s*spring\s+2022', window) or re.search(r'advertise\s*:\s*spring\s+2022', window):
                projects.add(ln)
    return sorted(projects)

projects = []
for d in docs:
    ps = extract_projects_started_spring_2022(d.get('text',''))
    for p in ps:
        projects.append({'filename': d.get('filename'), 'Project_Name': p})

# dedupe by Project_Name
unique_projects = sorted(set([p['Project_Name'] for p in projects]))

print('__RESULT__:')
print(json.dumps({'unique_projects': unique_projects, 'count': len(unique_projects), 'examples': projects[:10]}, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json'}

exec(code, env_args)
