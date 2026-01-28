code = """import re, json
from pathlib import Path

funding_records = var_call_n8nzxdQh9Pe0cse40ECASpU8
if isinstance(funding_records, str) and funding_records.endswith('.json'):
    funding_records = json.loads(Path(funding_records).read_text())

funded_projects = {rec['Project_Name'] for rec in funding_records}

civic_result = var_call_AE2EPGTGVzbJM9JHanzn0m5g
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    civic_result = json.loads(Path(civic_result).read_text())
texts = [d['text'] for d in civic_result]

projects = []
for text in texts:
    for line in text.split('\n'):
        line = line.strip('\ufeff').strip()
        if not line:
            continue
        if any(k in line for k in ['Agenda', 'Project Description', 'Project Updates', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Subject:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Page ']):
            continue
        if re.search(r'Project|Road|Park|PCH|Drain|Improvements|Canyon|Facility|Skate', line):
            projects.append(line)

projects = list(dict.fromkeys(projects))

project_info = {}
for text in texts:
    lower = text.lower()
    for name in projects:
        if name in project_info:
            continue
        idx = text.find(name)
        if idx == -1:
            continue
        window = lower[max(0, idx-400): idx+400]
        status = None
        if 'capital improvement projects (design)' in lower or 'finalize the design' in window or 'complete design' in window or 'design phase' in window:
            status = 'design'
        elif 'currently under construction' in window or 'begin construction' in window or 'construction was completed' in window:
            status = 'completed'
        elif 'not started' in window:
            status = 'not started'
        ptype = None
        if 'disaster recovery projects' in lower or 'fema' in window or 'caloes' in name.lower() or 'fema' in name.lower():
            ptype = 'disaster'
        if ptype is None:
            ptype = 'capital'
        project_info[name] = {'status': status, 'type': ptype}

count = 0
for name, info in project_info.items():
    if info['type'] == 'capital' and info['status'] == 'design' and name in funded_projects:
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_n8nzxdQh9Pe0cse40ECASpU8': 'file_storage/call_n8nzxdQh9Pe0cse40ECASpU8.json', 'var_call_AE2EPGTGVzbJM9JHanzn0m5g': 'file_storage/call_AE2EPGTGVzbJM9JHanzn0m5g.json'}

exec(code, env_args)
