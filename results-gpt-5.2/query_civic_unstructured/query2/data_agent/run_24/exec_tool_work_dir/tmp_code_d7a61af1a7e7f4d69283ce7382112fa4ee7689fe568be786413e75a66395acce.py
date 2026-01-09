code = """import json, re
from pathlib import Path

# load mongo docs
p = Path(var_call_990QjnLpYNipFGlrpvba9P6S)
docs = json.loads(p.read_text())

# parse projects with a simple line-based heuristic
projects = []
current_section = None  # e.g., 'design','construction','not started'
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    proj = None
    for ln in lines:
        if re.search(r'^Capital Improvement Projects \(Design\)', ln):
            current_section = 'design'
            continue
        if re.search(r'^Capital Improvement Projects \(Construction\)', ln):
            current_section = 'construction'
            continue
        if re.search(r'^Capital Improvement Projects \(Not Started\)', ln):
            current_section = 'not started'
            continue
        if re.search(r'^Disaster Recovery Projects', ln):
            current_section = 'disaster'
            continue

        # project name lines: non-empty, no bullets, not headers
        if ln and not ln.startswith(('(cid', 'Page', 'Agenda Item', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved', 'Date prepared', 'Meeting date', 'Subject:')):
            # detect start of a project when line is followed by a bullet marker in source; here we infer by next lines later.
            # We'll start a project when line has no colon and is Title Case-ish and current_section is set.
            if current_section in ('design','construction','not started'):
                if (':' not in ln) and (len(ln) <= 80) and (not re.search(r'\bProject Schedule\b|\bUpdates\b|\bProject Description\b', ln)):
                    # likely a project title
                    proj = {'Project_Name': ln, 'section': current_section, 'filename': d.get('filename')}
                    projects.append(proj)
                    continue

        if proj is not None:
            # capture completion in updates lines
            m = re.search(r'Construction was completed[^\n]*?(\b\w+\b\s+\d{4})', ln)
            if m:
                proj['completion_text'] = m.group(1)
            m2 = re.search(r'Complete Construction:\s*(.+)$', ln)
            if m2:
                proj['complete_construction'] = m2.group(1).strip()

# determine completed in 2022: any completion_text contains 2022 or complete_construction contains 2022
completed_2022 = []
for pjt in projects:
    comp = (pjt.get('completion_text','') + ' ' + pjt.get('complete_construction','')).strip()
    if '2022' in comp and ('completed' in comp.lower() or pjt.get('completion_text') or pjt.get('complete_construction')):
        completed_2022.append({'Project_Name': pjt['Project_Name'], 'completion_info': comp, 'filename': pjt['filename']})

# park-related: project name contains Park/Playground/Bluffs etc OR we will later intersect with funding? We'll tag by keywords.
park_kw = re.compile(r'\bpark\b|playground|bluffs', re.I)
park_completed_2022 = [x for x in completed_2022 if park_kw.search(x['Project_Name'])]

print('__RESULT__:')
print(json.dumps({'park_completed_2022': park_completed_2022, 'all_completed_2022': completed_2022}, ensure_ascii=False))"""

env_args = {'var_call_bj6z98fjH5u3abeSfc8CTfv8': ['Funding'], 'var_call_XhroUxAsfCyHp0eY88ACVcNh': ['civic_docs'], 'var_call_990QjnLpYNipFGlrpvba9P6S': 'file_storage/call_990QjnLpYNipFGlrpvba9P6S.json'}

exec(code, env_args)
