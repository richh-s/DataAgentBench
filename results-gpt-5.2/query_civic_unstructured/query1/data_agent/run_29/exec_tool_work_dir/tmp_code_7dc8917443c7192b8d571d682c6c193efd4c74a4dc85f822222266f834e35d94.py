code = """import json, re
import pandas as pd

# Load funding project names (>50k)
proj_path = var_call_EdjbYaO2yoaSnpToAwG19q3w
with open(proj_path, 'r', encoding='utf-8') as f:
    proj_records = json.load(f)
projects = [r.get('Project_Name') for r in proj_records if r.get('Project_Name')]
projects = sorted(set(projects))

# Load civic docs
civic_path = var_call_pxRUHJ44pPjnHOSb2hezHWgd
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
texts = [d.get('text','') for d in civic_docs]

# Identify which projects appear under a "Capital Improvement Projects (Design)" section
# Approach: for each document, extract the section after that header until next "Capital Improvement Projects (" header
# then check if project name appears as a standalone line/substring.

design_capital_projects = set()

for text in texts:
    if not text:
        continue
    # normalize
    t = text
    # Find all section starts
    header = r"Capital Improvement Projects \(Design\)"
    for m in re.finditer(header, t, flags=re.IGNORECASE):
        start = m.end()
        # find next header that begins with Capital Improvement Projects ( or Disaster Recovery Projects
        next_m = re.search(r"\n\s*(Capital Improvement Projects \(|Disaster Recovery Projects\b)", t[start:], flags=re.IGNORECASE)
        end = start + next_m.start() if next_m else len(t)
        section = t[start:end]
        # For faster lookup, lowercase section
        section_l = section.lower()
        for p in projects:
            if p and p.lower() in section_l:
                design_capital_projects.add(p)

result = {"count": len(design_capital_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OURQGnOXuxAqd3DLCd9cu1t0': [{'cnt': '276'}], 'var_call_pxRUHJ44pPjnHOSb2hezHWgd': 'file_storage/call_pxRUHJ44pPjnHOSb2hezHWgd.json', 'var_call_EdjbYaO2yoaSnpToAwG19q3w': 'file_storage/call_EdjbYaO2yoaSnpToAwG19q3w.json'}

exec(code, env_args)
