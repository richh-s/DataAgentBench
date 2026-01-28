code = """import json
with open(var_call_vD4zEmrG487DkCnRuuc8jrW7, 'r') as f:
    funding_projects = json.load(f)
funding_names = set(p['Project_Name'].strip().lower() for p in funding_projects)

with open(var_call_lanOkBXfzRQGOCcSYpVNQvY3, 'r') as f:
    civic_docs = json.load(f)

import re
projects_in_design = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        for line in design_section.split('\n'):
            m = re.match(r'^([A-Za-z0-9 &\-().]+?)( Updates:|$)', line)
            if m:
                candidate = m.group(1).strip().lower()
                # Fuzzy match with funded project names
                for f_name in funding_names:
                    if candidate and candidate in f_name:
                        projects_in_design.add(f_name)
            # Stop at the next section header
            if re.match(r'^\s*$', line) or (('Capital Improvement Projects' in line) and not '(Design)' in line):
                break
print('__RESULT__:')
print(json.dumps(len(projects_in_design)))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
