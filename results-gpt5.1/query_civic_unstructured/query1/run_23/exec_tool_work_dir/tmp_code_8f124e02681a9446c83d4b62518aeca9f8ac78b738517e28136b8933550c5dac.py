code = """import json, re
from collections import defaultdict

funding = var_call_jPC0AllRpupehbqTvWLoYpOy
civic_docs = var_call_OfjFHAj42ztxEm0qbrz5ub29

funding_names = {row['Project_Name'] for row in funding}
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

project_info = {}
pattern = r'Capital Improvement Projects \(Design\)([\s\S]*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)'
cap_design_section = re.search(pattern, full_text)
if cap_design_section:
    section_text = cap_design_section.group(1)
    lines = [l.strip() for l in section_text.split('\n') if l.strip()]
    skip_prefixes = ('Updates:', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Project Updates')
    for line in lines:
        if any(line.startswith(p) for p in skip_prefixes):
            continue
        if ':' in line:
            continue
        if 'Agenda Item' in line or 'Page ' in line:
            continue
        if line.startswith('(cid:'):
            continue
        name = re.sub(r'^[0-9\)\.]+', '', line).strip()
        if not name:
            continue
        project_info[name] = {'status': 'design', 'type': 'capital'}

count = 0
for fname in funding_names:
    if fname in project_info and project_info[fname]['status'] == 'design' and project_info[fname]['type'] == 'capital':
        count += 1

print("__RESULT__:")
print(json.dumps({'count': count}))"""

env_args = {'var_call_jPC0AllRpupehbqTvWLoYpOy': 'file_storage/call_jPC0AllRpupehbqTvWLoYpOy.json', 'var_call_OfjFHAj42ztxEm0qbrz5ub29': 'file_storage/call_OfjFHAj42ztxEm0qbrz5ub29.json'}

exec(code, env_args)
