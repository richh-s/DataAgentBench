code = """import json, re
from collections import defaultdict

path = var_call_QHxp15iX9eGSRda23teyDqEf
with open(path, 'r') as f:
    mongo_records = json.load(f)

texts = [r['text'] for r in mongo_records]

projects = {}
status = 'design'
type_capital = 'capital'

pattern = re.compile(r'^(?!Capital Improvement Projects)(?!Disaster Recovery Projects)([A-Z0-9][^\n]+?)\s*$', re.MULTILINE)

for text in texts:
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    section = text.split('Capital Improvement Projects (Design)',1)[1]
    if 'Capital Improvement Projects (Construction)' in section:
        section = section.split('Capital Improvement Projects (Construction)',1)[0]
    matches = pattern.findall(section)
    for m in matches:
        name = m.strip()
        if len(name.split())<2:
            continue
        projects[name] = {'Project_Name': name, 'status': status, 'type': type_capital}

funding_records = var_call_AgRWbBbH2E98cutRtnhBtEzx

funding_design_capital = []

for fr in funding_records:
    pname = fr['Project_Name']
    if pname in projects and projects[pname]['status']=='design' and projects[pname]['type']=='capital':
        funding_design_capital.append(fr)

result = len(funding_design_capital)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AgRWbBbH2E98cutRtnhBtEzx': 'file_storage/call_AgRWbBbH2E98cutRtnhBtEzx.json', 'var_call_QHxp15iX9eGSRda23teyDqEf': 'file_storage/call_QHxp15iX9eGSRda23teyDqEf.json'}

exec(code, env_args)
