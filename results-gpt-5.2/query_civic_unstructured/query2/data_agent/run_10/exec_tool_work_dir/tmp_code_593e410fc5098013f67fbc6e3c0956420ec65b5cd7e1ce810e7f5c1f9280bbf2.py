code = """import json, re

# Load mongo docs (may be a path)
docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Heuristic parser for project blocks in agenda reports
# We'll detect lines that look like project headings, then parse following lines for status and schedule.
project_records = []

heading_re = re.compile(r'^[A-Z0-9][A-Za-z0-9\-\&\,\'\(\)\./ ]{3,}$')
status_completed_re = re.compile(r'\b(completed|complete(?:d)? construction|construction was completed)\b', re.I)

for d in docs:
    text = d.get('text','') or ''
    # focus docs containing 'Park' keyword to reduce noise
    if 'Park' not in text and 'park' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    # remove empty
    lines = [ln for ln in lines if ln]

    # find headings: lines that are not bullet lines and not too long
    headings = []
    for i, ln in enumerate(lines):
        if len(ln) > 120: 
            continue
        if ln.startswith(('(cid', 'Page ', 'Agenda', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject:', 'RECOMMENDED', 'DISCUSSION', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Capital Improvement', 'Disaster Recovery')):
            continue
        if ln.lower().startswith(('staff', 'city', 'consultant', 'plans', 'project', 'notice of completion', 'advertise', 'begin construction', 'complete design', 'final design')):
            continue
        if heading_re.match(ln) and ('project' in ln.lower() or 'park' in ln.lower() or 'playground' in ln.lower() or 'bluffs' in ln.lower() or 'walkway' in ln.lower() or 'shade' in ln.lower()):
            headings.append((i, ln))

    # for each heading, look ahead 25 lines for completed and dates containing 2022
    for idx, name in headings:
        window = "\n".join(lines[idx: idx+30])
        if not status_completed_re.search(window):
            continue
        # look for any mention of 2022 near completion
        completed_2022 = False
        for m in re.finditer(r'(?:completed|complete(?:d)? construction|construction was completed)[^\n]{0,80}', window, flags=re.I):
            snippet = m.group(0)
            if '2022' in snippet:
                completed_2022 = True
        # also allow pattern 'completed <Month> 2022'
        if re.search(r'\b(completed|construction was completed)\b.*\b2022\b', window, flags=re.I|re.S):
            completed_2022 = True
        if not completed_2022:
            continue
        # park-related? name/window contains park/playground/bluffs
        topic = None
        park_related = bool(re.search(r'\bpark\b|playground|bluffs', name, re.I)) or bool(re.search(r'\bpark\b|playground|bluffs', window, re.I))
        if not park_related:
            continue
        project_records.append({'Project_Name': name, 'source_file': d.get('filename')})

# Deduplicate by Project_Name
uniq = {}
for r in project_records:
    uniq[r['Project_Name']] = r
projects_2022 = sorted(uniq.keys())

print('__RESULT__:')
print(json.dumps({'projects_completed_2022_park_related': projects_2022, 'count': len(projects_2022)}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json'}

exec(code, env_args)
