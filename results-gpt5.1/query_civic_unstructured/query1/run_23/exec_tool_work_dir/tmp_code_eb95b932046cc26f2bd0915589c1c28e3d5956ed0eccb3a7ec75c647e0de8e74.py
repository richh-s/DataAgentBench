code = """import json, re
from collections import defaultdict

# Load funding > 50k
funding = var_call_jPC0AllRpupehbqTvWLoYpOy

funding_names = {row['Project_Name'] for row in funding}

# Parse civic docs text to infer project statuses and types
civic_docs = var_call_OfjFHAj42ztxEm0qbrz5ub29
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

project_info = {}

# Capital Improvement Projects (Design)
cap_design_section = re.search(r'Capital Improvement Projects \(Design\)([\s\S]*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', full_text)
if cap_design_section:
    section_text = cap_design_section.group(1)
    lines = [l.strip() for l in section_text.split('\n') if l.strip()]
    # Project names are lines that are not bullets and not headings
    skip_prefixes = ('Updates:', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Project Updates')
    for i, line in enumerate(lines):
        if any(line.startswith(p) for p in skip_prefixes):
            continue
        if line.startswith('(') and ')' in line[:10]:
            continue
        # heuristic: treat isolated lines without colon as project names
        if ':' in line:
            continue
        # Exclude obvious non-names
        if 'Agenda Item' in line or 'Page ' in line:
            continue
        # Likely project name
        name = re.sub(r'^[\d\)\.]+' , '', line).strip()
        if not name:
            continue
        project_info[name] = {'status': 'design', 'type': 'capital'}

# Also look for explicit phrases like 'Project to be discussed' etc under named headings (already captured by above)

# Some projects explicitly mentioned in design section that may have trailing words like 'Project'
normalized_info = {}
for name, info in project_info.items():
    normalized_info[name] = info

# Merge with funding names by exact match
count = 0
matched_projects = []
for fname in funding_names:
    if fname in normalized_info and normalized_info[fname]['status'] == 'design' and normalized_info[fname]['type'] == 'capital':
        count += 1
        matched_projects.append(fname)

result = {'count': count, 'projects': sorted(matched_projects)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jPC0AllRpupehbqTvWLoYpOy': 'file_storage/call_jPC0AllRpupehbqTvWLoYpOy.json', 'var_call_OfjFHAj42ztxEm0qbrz5ub29': 'file_storage/call_OfjFHAj42ztxEm0qbrz5ub29.json'}

exec(code, env_args)
