code = """import re, json, pandas as pd
path = var_call_BBeyA5jBPnLs16ha5eUqLUTz
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = ' '.join(d['text'] for d in civic_docs)
projects_2022_disaster = set()
for line in texts.split('\n'):
    if '2022' in line and re.search(r'(FEMA|CalOES|CalJPIA|Woolsey|Disaster Recovery)', line, re.I):
        name = line.strip()
        if name:
            projects_2022_disaster.add(name)
for line in texts.split('\n'):
    if '2022' in line and re.search(r'(Improvements|Repairs|Project)', line):
        if re.search(r'(FEMA|CalOES|CalJPIA)', line):
            projects_2022_disaster.add(line.strip())
normalized = set()
for p in projects_2022_disaster:
    p2 = re.split(r'[-:•]', p)[0]
    p2 = p2.strip()
    normalized.add(p2)
projects_2022_disaster = normalized
path_f = var_call_rzIMnrNOIShmkg8kW5IpJkXV
with open(path_f, 'r') as f:
    funding = json.load(f)
disaster_keywords = ['(FEMA Project)', '(FEMA/CalOES Project)', '(CalOES Project)', '(CalJPIA Project)', '(FEMA)', '(CalOES)']
civic_lines_2022 = [l for l in texts.split('\n') if '2022' in l]

total = 0
used = []
for row in funding:
    name = row['Project_Name']
    is_disaster = any(k in name for k in disaster_keywords)
    if not is_disaster:
        continue
    if '2022' in name:
        total += int(row['Amount'])
        used.append(name)
        continue
    base = name.split('(')[0].strip()
    for l in civic_lines_2022:
        if base in l:
            total += int(row['Amount'])
            used.append(name)
            break
result = {'total_funding_2022_disaster_projects': total, 'matched_projects': used}
res_json = json.dumps(result)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_BBeyA5jBPnLs16ha5eUqLUTz': 'file_storage/call_BBeyA5jBPnLs16ha5eUqLUTz.json', 'var_call_rzIMnrNOIShmkg8kW5IpJkXV': 'file_storage/call_rzIMnrNOIShmkg8kW5IpJkXV.json'}

exec(code, env_args)
