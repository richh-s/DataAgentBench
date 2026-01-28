code = """import json, pandas as pd

funding = pd.DataFrame(var_call_4guL95goNZzMdKQp4Q1EHJvZ)

from typing import List
texts: List[str] = [d['text'] for d in var_call_3anyV3AH7hUu8mUsbkJN0fc3]
text_all = '\n'.join(texts)

sections = {}
current_section = None
for line in text_all.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    if 'Capital Improvement Projects (Design)' in line_stripped:
        current_section = 'design'
        continue
    if line_stripped.startswith('Capital Improvement Projects (') and 'Design' not in line_stripped:
        current_section = None
        continue
    if current_section == 'design':
        if any(prefix in line_stripped for prefix in ['Updates:', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Project Updates']):
            continue
        if line_stripped and not line_stripped.endswith(':') and not line_stripped.startswith('('):
            sections.setdefault('design_projects', []).append(line_stripped)

projects = sorted(set(sections.get('design_projects', [])))

funding['Amount'] = funding['Amount'].astype(int)
funding_design = funding[funding['Project_Name'].isin(projects)]

result = {
    'design_projects_extracted': projects,
    'count_design_funded_over_50k': int((funding_design['Amount'] > 50000).sum())
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_4guL95goNZzMdKQp4Q1EHJvZ': 'file_storage/call_4guL95goNZzMdKQp4Q1EHJvZ.json', 'var_call_3anyV3AH7hUu8mUsbkJN0fc3': 'file_storage/call_3anyV3AH7hUu8mUsbkJN0fc3.json'}

exec(code, env_args)
