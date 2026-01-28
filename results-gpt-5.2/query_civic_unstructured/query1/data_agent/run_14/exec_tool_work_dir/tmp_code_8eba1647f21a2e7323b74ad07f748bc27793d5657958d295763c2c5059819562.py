code = """import json, re

fund_path = var_call_nYjJ4kxOjBZ2kYVMCMRSOBrL
with open(fund_path, 'r') as f:
    funding = json.load(f)
fund_projects = {r['Project_Name'] for r in funding}

civic_path = var_call_c8SLOLDsXLD0XVSWokAYJKiQ
with open(civic_path, 'r') as f:
    docs = json.load(f)

sections = []
for d in docs:
    t = d.get('text','')
    patterns = [
        r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)",
        r"Disaster Recovery Projects \(Design\)(.*?)(Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\)|Capital Improvement Projects|$)",
    ]
    for pat in patterns:
        for m in re.finditer(pat, t, flags=re.S|re.I):
            sections.append(m.group(1))

design_text = "\n".join(sections)

matched = set()
for p in fund_projects:
    if re.search(re.escape(p), design_text, flags=re.I):
        matched.add(p)

result = {"count": len(matched)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cOYTFJ37fsmQ6vsv2BI5aIEd': ['Funding'], 'var_call_CoJ4YHLU3kaME3EK9Gh9N7k7': ['civic_docs'], 'var_call_nYjJ4kxOjBZ2kYVMCMRSOBrL': 'file_storage/call_nYjJ4kxOjBZ2kYVMCMRSOBrL.json', 'var_call_c8SLOLDsXLD0XVSWokAYJKiQ': 'file_storage/call_c8SLOLDsXLD0XVSWokAYJKiQ.json'}

exec(code, env_args)
