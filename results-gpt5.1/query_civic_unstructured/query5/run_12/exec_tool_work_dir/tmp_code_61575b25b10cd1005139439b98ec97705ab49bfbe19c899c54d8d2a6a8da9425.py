code = """import json, re, pandas as pd

# Load full civic docs
path = var_call_YtiM3HZD3AfptUlZQhMyHWxR
with open(path, 'r') as f:
    civic_docs = json.load(f)

# Heuristic: disaster projects are those with FEMA/CalOES/CalJPIA in name or containing 'Disaster Recovery'
# Need projects that started in 2022 based on text patterns like '2022' near project names.

text_all = ' '.join(d['text'] for d in civic_docs)

# Extract lines containing 2022 and FEMA/CalOES/CalJPIA or 'Disaster Recovery'
lines = re.split(r'\n+', text_all)
relevant_projects = set()
for line in lines:
    if '2022' in line and (re.search(r'FEMA|CalOES|CalJPIA|Disaster Recovery', line, re.I)):
        # crude project name: the whole line stripped
        name = line.strip()
        if name:
            relevant_projects.add(name)

# Additionally, from agenda style lists, many project names include year at start, like '2022 Morning View Resurfacing & Storm Drain Improvements'
for line in lines:
    m = re.match(r'\s*(2022[^\n]+)', line)
    if m:
        relevant_projects.add(m.group(1).strip())

relevant_projects_list = sorted(relevant_projects)

print('__RESULT__:')
print(json.dumps(relevant_projects_list))"""

env_args = {'var_call_YtiM3HZD3AfptUlZQhMyHWxR': 'file_storage/call_YtiM3HZD3AfptUlZQhMyHWxR.json', 'var_call_wHli7EZTdU0PuSIFJAmDOKrr': 'file_storage/call_wHli7EZTdU0PuSIFJAmDOKrr.json'}

exec(code, env_args)
