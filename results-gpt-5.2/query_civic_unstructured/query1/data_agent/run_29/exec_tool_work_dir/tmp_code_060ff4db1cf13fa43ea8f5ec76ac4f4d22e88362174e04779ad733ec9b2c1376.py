code = """import json, re

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
texts = [d.get('text','') or '' for d in civic_docs]

# Determine which funded projects appear in a Capital Improvement Projects (Design) section

design_capital_projects = set()
header_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", flags=re.IGNORECASE)
next_header_re = re.compile(r"\n\s*(Capital Improvement Projects\s*\(|Disaster Recovery Projects\b)", flags=re.IGNORECASE)

for t in texts:
    if not t:
        continue
    for m in header_re.finditer(t):
        start = m.end()
        m2 = next_header_re.search(t, pos=start)
        end = m2.start() if m2 else len(t)
        section_l = t[start:end].lower()
        for p in projects:
            pl = p.lower()
            if pl in section_l:
                design_capital_projects.add(p)

result = {"count": len(design_capital_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OURQGnOXuxAqd3DLCd9cu1t0': [{'cnt': '276'}], 'var_call_pxRUHJ44pPjnHOSb2hezHWgd': 'file_storage/call_pxRUHJ44pPjnHOSb2hezHWgd.json', 'var_call_EdjbYaO2yoaSnpToAwG19q3w': 'file_storage/call_EdjbYaO2yoaSnpToAwG19q3w.json'}

exec(code, env_args)
