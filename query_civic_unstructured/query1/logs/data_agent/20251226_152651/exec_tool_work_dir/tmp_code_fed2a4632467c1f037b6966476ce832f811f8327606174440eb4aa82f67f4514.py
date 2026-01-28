code = """import json
with open(var_call_vD4zEmrG487DkCnRuuc8jrW7, 'r') as f:
    funding_projects = json.load(f)
project_names = set([p['Project_Name'] for p in funding_projects])

with open(var_call_lanOkBXfzRQGOCcSYpVNQvY3, 'r') as f:
    civic_texts = [d['text'] for d in json.load(f)]

import re
matching_projects = set()
for text in civic_texts:
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
        elif in_design_section and ('Capital Improvement Projects' in line and '(Design)' not in line):
            in_design_section = False
        if in_design_section:
            m = re.match(r'^([A-Za-z0-9 &\-().]+?)( Updates:|$)', line)
            if m:
                name = m.group(1).strip()
                for fund_name in project_names:
                    if name and name.lower() in fund_name.lower():
                        matching_projects.add(fund_name)
result = len(matching_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
