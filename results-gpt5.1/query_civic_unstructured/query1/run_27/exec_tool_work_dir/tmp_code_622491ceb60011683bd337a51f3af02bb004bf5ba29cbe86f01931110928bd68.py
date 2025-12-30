code = """import re, json
from collections import defaultdict

# Load full civic docs result
path = var_call_zWP5E2i8fTmD4nHEiyLOhZhk
with open(path, 'r') as f:
    civic_records = json.load(f)
texts = [r['text'] for r in civic_records]
full_text = '\n'.join(texts)

section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', full_text, re.S)
projects_in_design = set()
if section_match:
    section_text = section_match.group(1)
    for line in section_text.split('\n'):
        line = line.strip('\r').strip()
        if not line:
            continue
        skip_starts = ['Updates', 'Project Schedule', 'Estimated Schedule', 'Page ', 'Agenda Item']
        if any(line.startswith(p) for p in skip_starts):
            continue
        if line.endswith(':'):
            continue
        if len(line.split()) >= 3 and re.search(r'[A-Za-z]', line):
            projects_in_design.add(line)

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

norm_design = {norm(p) for p in projects_in_design}

funding = var_call_vDoNMCKrh6uVboRSA6PIgUi2
if isinstance(funding, str):
    with open(funding, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding

count = 0
matched_projects = set()
for rec in funding_records:
    pname = rec['Project_Name']
    if norm(pname) in norm_design:
        count += 1
        matched_projects.add(pname)

result = {
    'count_design_funded_over_50000': count,
    'matched_projects': sorted(matched_projects),
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vDoNMCKrh6uVboRSA6PIgUi2': 'file_storage/call_vDoNMCKrh6uVboRSA6PIgUi2.json', 'var_call_zWP5E2i8fTmD4nHEiyLOhZhk': 'file_storage/call_zWP5E2i8fTmD4nHEiyLOhZhk.json'}

exec(code, env_args)
