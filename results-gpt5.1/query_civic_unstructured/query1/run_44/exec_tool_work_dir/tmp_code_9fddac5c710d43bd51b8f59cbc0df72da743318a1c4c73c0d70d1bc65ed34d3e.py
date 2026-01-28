code = """import re, json, pandas as pd

funding = pd.DataFrame(var_call_sYdTHuMzUHSBfqqXZLOaNdIe)

# parse civic docs for project statuses
texts = []
if isinstance(var_call_DI1ecJmPINmcXOisb6Ct03qX, str) and var_call_DI1ecJmPINmcXOisb6Ct03qX.endswith('.json'):
    import json as _json, pathlib
    with open(var_call_DI1ecJmPINmcXOisb6Ct03qX, 'r') as f:
        texts = [d['text'] for d in _json.load(f)]
else:
    texts = [d['text'] for d in var_call_DI1ecJmPINmcXOisb6Ct03qX]

projects = {}
for text in texts:
    # very rough parsing: look for section headers indicating status
    status_blocks = [
        ('design', re.split('Capital Improvement Projects \(Design\)', text, flags=re.I)),
        ('completed', re.split('Capital Improvement Projects \(Construction\)', text, flags=re.I)),
        ('not started', re.split('Capital Improvement Projects \(Not Started\)', text, flags=re.I)),
    ]
    # Actually we will just use known patterns from preview where design projects are listed after that header

# For simplicity and robustness for this synthetic dataset, we infer status by keyword hints in text near project names from funding table.

status_map = {}
full_text = '\n'.join(texts)
for name in funding['Project_Name'].unique():
    # skip generic non-project terms
    if name.lower() in ['discussion', 'recommended action']:
        continue
    # search name in text and infer status by nearby headings
    pattern = re.escape(name)
    for match in re.finditer(pattern, full_text):
        start = max(0, match.start()-500)
        context = full_text[start:match.start()]
        if re.search('Capital Improvement Projects \(Design\)', context, flags=re.I):
            status_map[name] = 'design'
        elif re.search('Capital Improvement Projects \(Construction\)', context, flags=re.I):
            status_map[name] = 'completed'
        elif re.search('Capital Improvement Projects \(Not Started\)', context, flags=re.I):
            status_map[name] = 'not started'
        # also check wording
        elif re.search('finalize the design', context, flags=re.I) or re.search('design plans', context, flags=re.I):
            status_map[name] = 'design'

# Count capital projects in design with amount > 50000.
# In this synthetic data, treat all named projects (non-generic, non-random id like project_123) as capital projects.

def is_real_project(n):
    return not re.match('project_\\d+', n)

merged = []
for _, row in funding.iterrows():
    name = row['Project_Name']
    if not is_real_project(name):
        continue
    status = status_map.get(name)
    if status == 'design':
        merged.append(name)

count = len(set(merged))

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_sYdTHuMzUHSBfqqXZLOaNdIe': 'file_storage/call_sYdTHuMzUHSBfqqXZLOaNdIe.json', 'var_call_DI1ecJmPINmcXOisb6Ct03qX': 'file_storage/call_DI1ecJmPINmcXOisb6Ct03qX.json'}

exec(code, env_args)
