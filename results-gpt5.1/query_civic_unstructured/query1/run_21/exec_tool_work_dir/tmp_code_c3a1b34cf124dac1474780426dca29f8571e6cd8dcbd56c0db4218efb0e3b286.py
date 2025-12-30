code = """import json, pandas as pd, re

# Load full funding > 50000 result
with open(var_call_M5HZ3md0JFeXsBbenvDZ32Ax, 'r') as f:
    funding_projects = json.load(f)

funding_df = pd.DataFrame(funding_projects)

# Get texts from civic docs sample
texts = [d['text'] for d in var_call_iaWisJiTWkJoELyhzZGprdaL]
full_text = '\n'.join(texts)

section_match = re.search(r'Capital Improvement Projects \(Design\)([\s\S]*?)Capital Improvement Projects \(Construction\)', full_text)
project_names_design = set()
if section_match:
    section = section_match.group(1)
    for line in section.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('(') or line.startswith('cid:'):
            continue
        if any(line.startswith(prefix) for prefix in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Page', 'Agenda Item', 'Subject']):
            continue
        if ':' in line:
            continue
        if len(line) < 5:
            continue
        project_names_design.add(line)

funding_names = set(funding_df['Project_Name'].tolist())
matching = [name for name in project_names_design if name in funding_names]

result = {
    'design_capital_projects_funded_over_50000_count': len(matching),
    'matching_project_names': sorted(matching),
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_M5HZ3md0JFeXsBbenvDZ32Ax': 'file_storage/call_M5HZ3md0JFeXsBbenvDZ32Ax.json', 'var_call_iaWisJiTWkJoELyhzZGprdaL': 'file_storage/call_iaWisJiTWkJoELyhzZGprdaL.json'}

exec(code, env_args)
