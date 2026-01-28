code = """import re, json, os, json as jsonlib
from collections import defaultdict

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
        if len(line.split())>2 and not line.endswith(':') and 'Updates' not in line and 'Project Schedule' not in line and 'Estimated Schedule' not in line and 'Project Description' not in line and 'Agenda Item' not in line and not line.startswith('Page '):
            design_projects.append(line)

funding = var_call_6hebe4n4IRxjkeGdenvMBx8y
funding_names = {row['Project_Name'] for row in funding}

count = sum(1 for name in set(design_projects) if name in funding_names)

result = {"design_capital_projects_over_50000_count": count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6hebe4n4IRxjkeGdenvMBx8y': 'file_storage/call_6hebe4n4IRxjkeGdenvMBx8y.json', 'var_call_8Fd6e4eTOsGPJXdL0LMB95MN': 'file_storage/call_8Fd6e4eTOsGPJXdL0LMB95MN.json'}

exec(code, env_args)
