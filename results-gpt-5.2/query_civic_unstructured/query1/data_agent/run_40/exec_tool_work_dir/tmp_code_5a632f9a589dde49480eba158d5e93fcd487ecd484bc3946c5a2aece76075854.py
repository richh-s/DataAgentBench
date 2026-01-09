code = """import json, re
import pandas as pd

# Load funding project names > 50000
proj_src = var_call_96XYcpyozNNIlQEfcVVT74N9
if isinstance(proj_src, str):
    with open(proj_src, 'r', encoding='utf-8') as f:
        proj_src = json.load(f)
projects = sorted({r['Project_Name'] for r in proj_src if r.get('Project_Name')})

# Load civic docs
civic = var_call_P3OAu5oMAVeNPOfjYe1YfCRO
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)
texts = [d.get('text','') for d in civic]
full = "\n".join(texts)
full_lc = full.lower()

# Determine which funded projects are capital and design based on presence under 'Capital Improvement Projects (Design)'
# Heuristic: find the section heading and take subsequent lines until next 'Capital Improvement Projects (Construction)' or '(Not Started)' or 'Disaster Recovery Projects'

def extract_design_section(text):
    t = text
    m = re.search(r"Capital Improvement Projects\s*\(Design\)", t, flags=re.IGNORECASE)
    if not m:
        return ""
    start = m.end()
    # end at next major section
    m2 = re.search(r"Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects|Disaster\s+Recovery\s+Projects", t[start:], flags=re.IGNORECASE)
    end = start + (m2.start() if m2 else len(t[start:]))
    return t[start:end]

sections = [extract_design_section(t) for t in texts]
section_join = "\n".join(sections)
section_lc = section_join.lower()

# count projects whose name appears in design section and also has type capital implied by being in capital section
hits = []
for p in projects:
    pl = p.lower()
    if pl in section_lc:
        hits.append(p)

result = {"count": len(sorted(set(hits))), "projects": sorted(set(hits))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0OOLA3zH2bqIsJ6coifOC5qC': [{'cnt': '276'}], 'var_call_P3OAu5oMAVeNPOfjYe1YfCRO': 'file_storage/call_P3OAu5oMAVeNPOfjYe1YfCRO.json', 'var_call_96XYcpyozNNIlQEfcVVT74N9': 'file_storage/call_96XYcpyozNNIlQEfcVVT74N9.json'}

exec(code, env_args)
