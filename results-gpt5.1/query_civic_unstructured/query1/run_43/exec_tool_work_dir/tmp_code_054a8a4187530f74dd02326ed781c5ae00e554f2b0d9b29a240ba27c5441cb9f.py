code = """import re, json, os
from collections import defaultdict

funding_records = var_call_aWXHrDQQUf81FCBRaRJ7h8IJ
funding_projects = {rec['Project_Name'] for rec in funding_records if int(rec['Amount']) > 50000}

civic_data = var_call_Qs94OMR5gYtC2IDDwUZOajyx
if isinstance(civic_data, str):
    civic_data = json.load(open(civic_data, 'r'))

texts = [d['text'] for d in civic_data]
full_text = "\n".join(texts)

norm_text = re.sub(r"\r", "", full_text)

design_sections = []
pattern = r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|$)"
for m in re.finditer(pattern, norm_text, flags=re.S):
    design_sections.append(m.group(1))

design_projects = set()
for sec in design_sections:
    for line in sec.split("\n"):
        line = line.strip()
        if not line:
            continue
        if any(line.startswith(prefix) for prefix in ("Updates", "Project", "Estimated", "Advertise", "Begin", "Complete", "City ", "Staff ", "Page ", "Agenda Item", "(")):
            continue
        if len(line.split()) >= 2 and re.search(r"[A-Z]", line):
            design_projects.add(line)

for m in re.finditer(r"\n([^\n]+?)\s*\(Design\)", norm_text):
    name = m.group(1).strip()
    if len(name.split()) >= 2:
        design_projects.add(name)

capital_design_with_funding = {name for name in design_projects if name in funding_projects}

result_count = len(capital_design_with_funding)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_aWXHrDQQUf81FCBRaRJ7h8IJ': 'file_storage/call_aWXHrDQQUf81FCBRaRJ7h8IJ.json', 'var_call_Qs94OMR5gYtC2IDDwUZOajyx': 'file_storage/call_Qs94OMR5gYtC2IDDwUZOajyx.json'}

exec(code, env_args)
