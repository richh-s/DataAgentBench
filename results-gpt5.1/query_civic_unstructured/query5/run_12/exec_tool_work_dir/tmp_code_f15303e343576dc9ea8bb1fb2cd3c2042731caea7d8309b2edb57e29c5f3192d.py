code = """import json, re, pandas as pd
path = var_call_YtiM3HZD3AfptUlZQhMyHWxR
with open(path, 'r') as f:
    civic_docs = json.load(f)
text_all = ' '.join(d['text'] for d in civic_docs)
lines = re.split(r'\n+', text_all)
relevant_projects = set()
for line in lines:
    if '2022' in line and (re.search(r'FEMA|CalOES|CalJPIA|Disaster Recovery', line, re.I)):
        name = line.strip()
        if name:
            relevant_projects.add(name)
for line in lines:
    m = re.match(r'\s*(2022[^\n]+)', line)
    if m:
        relevant_projects.add(m.group(1).strip())
relevant_projects_list = sorted(relevant_projects)
print('__RESULT__:')
print(json.dumps(relevant_projects_list))"""

env_args = {'var_call_YtiM3HZD3AfptUlZQhMyHWxR': 'file_storage/call_YtiM3HZD3AfptUlZQhMyHWxR.json', 'var_call_wHli7EZTdU0PuSIFJAmDOKrr': 'file_storage/call_wHli7EZTdU0PuSIFJAmDOKrr.json'}

exec(code, env_args)
