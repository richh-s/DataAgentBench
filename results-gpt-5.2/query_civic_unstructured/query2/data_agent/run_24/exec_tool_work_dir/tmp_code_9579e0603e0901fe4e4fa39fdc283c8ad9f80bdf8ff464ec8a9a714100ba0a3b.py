code = """import json, re
from pathlib import Path

p = Path(var_call_990QjnLpYNipFGlrpvba9P6S)
docs = json.loads(p.read_text())

projects = []
current_section = None
for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    proj = None
    for ln in lines:
        if re.search(r'^Capital Improvement Projects \(Design\)', ln):
            current_section = 'design'; continue
        if re.search(r'^Capital Improvement Projects \(Construction\)', ln):
            current_section = 'construction'; continue
        if re.search(r'^Capital Improvement Projects \(Not Started\)', ln):
            current_section = 'not started'; continue
        if re.search(r'^Disaster Recovery Projects', ln):
            current_section = 'disaster'; continue

        if ln and not ln.startswith(('(cid', 'Page', 'Agenda Item', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved', 'Date prepared', 'Meeting date', 'Subject:')):
            if current_section in ('design','construction','not started'):
                if (':' not in ln) and (len(ln) <= 80) and (not re.search(r'\bProject Schedule\b|\bUpdates\b|\bProject Description\b', ln)):
                    proj = {'Project_Name': ln, 'section': current_section, 'filename': d.get('filename')}
                    projects.append(proj)
                    continue

        if proj is not None:
            m = re.search(r'Construction was completed[^\n]*?(\b\w+\b\s+\d{4})', ln)
            if m:
                proj['completion_text'] = m.group(1)
            m2 = re.search(r'Complete Construction:\s*(.+)$', ln)
            if m2:
                proj['complete_construction'] = m2.group(1).strip()

completed_2022 = []
for pjt in projects:
    comp = (pjt.get('completion_text','') + ' ' + pjt.get('complete_construction','')).strip()
    if '2022' in comp and (pjt.get('completion_text') is not None or pjt.get('complete_construction') is not None):
        completed_2022.append({'Project_Name': pjt['Project_Name'], 'completion_info': comp, 'filename': pjt['filename']})

park_kw = re.compile(r'\bpark\b|playground|bluffs', re.I)
park_completed_2022 = [x for x in completed_2022 if park_kw.search(x['Project_Name'])]

print('__RESULT__:')
print(json.dumps({'park_completed_2022': park_completed_2022, 'all_completed_2022': completed_2022}, ensure_ascii=False))"""

env_args = {'var_call_bj6z98fjH5u3abeSfc8CTfv8': ['Funding'], 'var_call_XhroUxAsfCyHp0eY88ACVcNh': ['civic_docs'], 'var_call_990QjnLpYNipFGlrpvba9P6S': 'file_storage/call_990QjnLpYNipFGlrpvba9P6S.json'}

exec(code, env_args)
