code = """import json, re
from collections import defaultdict

funding_records = var_call_pRUj9a82rmsVUyx3EyEFd0gA
civic_docs = var_call_2nuLhwW6sadTEG5zvzqimHxl

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

pattern = r'Capital Improvement Projects \(Design\)([\s\S]*?)(?:Capital Improvement Projects \(|Capital Improvement Projects\s*\(|$)'
m = re.search(pattern, full_text)
design_block = m.group(1) if m else ''

project_lines = []
for line in design_block.split('\n'):
    line = line.strip('\r ')
    if not line:
        continue
    lower = line.lower()
    if lower.startswith('updates') or lower.startswith('project') or lower.startswith('estimated') or lower.startswith('page '):
        continue
    if line.startswith('('):
        continue
    if ':' in line:
        continue
    if len(line.split()) >= 2:
        project_lines.append(line)

design_projects = sorted(set(project_lines))

funding_design_projects = []
for rec in funding_records:
    name = rec['Project_Name']
    if name in design_projects:
        funding_design_projects.append(name)

count = len(set(funding_design_projects))

result = {
    'design_project_names_detected': design_projects,
    'design_projects_with_funding_gt_50000_count': count,
    'matched_project_names': sorted(set(funding_design_projects)),
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_pRUj9a82rmsVUyx3EyEFd0gA': 'file_storage/call_pRUj9a82rmsVUyx3EyEFd0gA.json', 'var_call_2nuLhwW6sadTEG5zvzqimHxl': 'file_storage/call_2nuLhwW6sadTEG5zvzqimHxl.json'}

exec(code, env_args)
