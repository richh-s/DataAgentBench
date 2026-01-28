code = """import re, json, pandas as pd

funding = pd.DataFrame(var_call_sYdTHuMzUHSBfqqXZLOaNdIe)

# load civic docs texts
texts = []
if isinstance(var_call_DI1ecJmPINmcXOisb6Ct03qX, str) and var_call_DI1ecJmPINmcXOisb6Ct03qX.endswith('.json'):
    import json as _json
    with open(var_call_DI1ecJmPINmcXOisb6Ct03qX, 'r') as f:
        texts = [d['text'] for d in _json.load(f)]
else:
    texts = [d['text'] for d in var_call_DI1ecJmPINmcXOisb6Ct03qX]

full_text = '\n'.join(texts)

status_map = {}
for name in funding['Project_Name'].unique():
    lname = name.lower()
    if lname in ['discussion', 'recommended action']:
        continue
    pattern = re.escape(name)
    for match in re.finditer(pattern, full_text):
        start = max(0, match.start()-800)
        context = full_text[start:match.start()]
        if re.search('Capital Improvement Projects \(Design\)', context, flags=re.I):
            status_map[name] = 'design'
        elif re.search('Capital Improvement Projects \(Construction\)', context, flags=re.I):
            status_map[name] = 'completed'
        elif re.search('Capital Improvement Projects \(Not Started\)', context, flags=re.I):
            status_map[name] = 'not started'
        elif re.search('finalize the design', context, flags=re.I) or re.search('design plans', context, flags=re.I):
            status_map[name] = 'design'

# treat all named projects as capital for this dataset

real_projects = []
for _, row in funding.iterrows():
    name = row['Project_Name']
    if re.match('project_\d+', name):
        continue
    if status_map.get(name) == 'design':
        real_projects.append(name)

count = len(set(real_projects))

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_sYdTHuMzUHSBfqqXZLOaNdIe': 'file_storage/call_sYdTHuMzUHSBfqqXZLOaNdIe.json', 'var_call_DI1ecJmPINmcXOisb6Ct03qX': 'file_storage/call_DI1ecJmPINmcXOisb6Ct03qX.json'}

exec(code, env_args)
