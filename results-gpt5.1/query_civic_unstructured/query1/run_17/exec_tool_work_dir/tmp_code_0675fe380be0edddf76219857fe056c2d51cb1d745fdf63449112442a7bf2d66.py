code = """import re, json
from collections import defaultdict

funding_records = var_call_ytm6ttfV16j822VrWLI0h2uY
civic_docs = var_call_IlBpye4RpLRD2lb69CV4NLrt

project_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    section = text.split('Capital Improvement Projects (Design)', 1)[1]
    stop_tokens = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for tok in stop_tokens:
        if tok in section:
            section = section.split(tok, 1)[0]
    for line in section.split('\n'):
        s = line.strip()
        if not s:
            continue
        if 'Project Schedule' in s or 'Updates' in s or 'Estimated Schedule' in s or 'Project Description' in s:
            continue
        if len(s.split()) >= 3 and s[0].isupper():
            name = re.sub(r'[^A-Za-z0-9&(),\- ]+', ' ', s).strip()
            project_status[name] = 'design'

capital_design_projects = set(project_status.keys())

count = 0
for rec in funding_records:
    pname = rec['Project_Name']
    if pname in capital_design_projects:
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ytm6ttfV16j822VrWLI0h2uY': 'file_storage/call_ytm6ttfV16j822VrWLI0h2uY.json', 'var_call_IlBpye4RpLRD2lb69CV4NLrt': 'file_storage/call_IlBpye4RpLRD2lb69CV4NLrt.json'}

exec(code, env_args)
