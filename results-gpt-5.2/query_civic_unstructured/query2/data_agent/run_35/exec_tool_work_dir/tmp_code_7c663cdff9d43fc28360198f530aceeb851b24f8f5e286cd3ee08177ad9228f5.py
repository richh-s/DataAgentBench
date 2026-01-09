code = """import re, json
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

recs = load_records(var_call_xaBtDyrvLf2HBp16vz21aGew)

# Extract project lines with completion in 2022 and park-related keywords
park_kw = re.compile(r"\b(park|playground|bluffs|skate)\b", re.I)

projects = {}
current = None
for rec in recs:
    text = rec.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for ln in lines:
        if not ln:
            continue
        # detect project name lines (heuristic): not bullets and reasonably short
        if len(ln) < 120 and not ln.startswith(('(', '(cid', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital', 'Storm', 'City', 'Public')):
            # Many project names appear as standalone lines; capture those containing park keywords
            if park_kw.search(ln):
                current = ln
                projects.setdefault(current, {'completed_2022': False, 'evidence': []})
                continue
        if current and 'completed' in ln.lower() and '2022' in ln:
            projects[current]['completed_2022'] = True
            projects[current]['evidence'].append(ln)
        # reset current when blank handled; keep otherwise

completed_park_projects = sorted([p for p,v in projects.items() if v['completed_2022']])

print('__RESULT__:')
print(json.dumps({'completed_park_projects': completed_park_projects, 'count': len(completed_park_projects)}))"""

env_args = {'var_call_BS3mWapbppeBGys41aMraj6f': ['Funding'], 'var_call_3GqwVynV65vRLEHoYdkLXplO': ['civic_docs'], 'var_call_xaBtDyrvLf2HBp16vz21aGew': 'file_storage/call_xaBtDyrvLf2HBp16vz21aGew.json'}

exec(code, env_args)
