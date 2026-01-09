code = """import json, re

path = var_call_bFT0LzLw79r9xBgBKESnVmpw
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_projects_started_spring_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = set()
    for i, ln in enumerate(lines):
        if not ln or len(ln) < 4:
            continue
        low = ln.lower()
        skip_prefixes = [
            '(cid', 'updates', 'project schedule', 'estimated schedule', 'project description',
            'capital improvement projects', 'disaster recovery projects', 'page ', 'agenda item',
            'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject',
            'recommended action', 'discussion'
        ]
        if any(low.startswith(x) for x in skip_prefixes):
            continue
        if low in ['recommended action', 'discussion']:
            continue
        # look ahead window for explicit start markers in Spring 2022
        window = '\n'.join(lines[i:i+50]).lower()
        if 'spring 2022' not in window:
            continue
        if re.search(r'begin\s+construction\s*:\s*spring\s+2022', window) or \
           re.search(r'begin\s+design\s*:\s*spring\s+2022', window) or \
           re.search(r'advertise\s*:\s*spring\s+2022', window):
            projects.add(ln)
    return sorted(projects)

unique = set()
for d in docs:
    for p in extract_projects_started_spring_2022(d.get('text','')):
        unique.add(p)

result = {'projects_started_spring_2022': sorted(unique), 'count': len(unique)}
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json'}

exec(code, env_args)
