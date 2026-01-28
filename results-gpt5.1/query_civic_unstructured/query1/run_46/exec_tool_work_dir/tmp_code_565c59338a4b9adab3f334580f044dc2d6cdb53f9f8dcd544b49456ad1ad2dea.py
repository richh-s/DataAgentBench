code = """import re, json
from collections import defaultdict

# Load full civic docs result
import os, json as jsonlib
path = var_call_8Fd6e4eTOsGPJXdL0LMB95MN
with open(path, 'r') as f:
    civic_docs = jsonlib.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

section_pattern = re.compile(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)', re.S)
match = section_pattern.search(texts)

design_projects = []
if match:
    block = match.group(1)
    lines = [l.strip() for l in block.split('\n') if l.strip()]
    for line in lines:
        if len(line.split())>2 and not line.endswith(':') and 'Updates' not in line and 'Project Schedule' not in line and 'Estimated Schedule' not in line:
            if not line.startswith('(') and 'Agenda Item' not in line and 'Page ' not in line:
                if not any(kw in line for kw in ['Updates', 'Schedule', 'Project Description']):
                    if re.match(r'[A-Z].*[a-z]', line):
                        design_projects.append(line)

design_projects = sorted(set(design_projects))

# Now filter to capital projects with status design implicitly; we'll join by name with funding >50000 set
funding = var_call_6hebe4n4IRxjkeGdenvMBx8y
funding_names = {row['Project_Name'] for row in funding}

count = sum(1 for name in design_projects if name in funding_names)

result = {"design_capital_projects_over_50000_count": count, "design_projects_matched": sorted([name for name in design_projects if name in funding_names])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6hebe4n4IRxjkeGdenvMBx8y': 'file_storage/call_6hebe4n4IRxjkeGdenvMBx8y.json', 'var_call_8Fd6e4eTOsGPJXdL0LMB95MN': 'file_storage/call_8Fd6e4eTOsGPJXdL0LMB95MN.json'}

exec(code, env_args)
