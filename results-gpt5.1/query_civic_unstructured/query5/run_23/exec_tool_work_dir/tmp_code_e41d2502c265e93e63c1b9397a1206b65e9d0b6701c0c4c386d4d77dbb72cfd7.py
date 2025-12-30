code = """import re, json, pandas as pd

# Load full civic docs
path = var_call_BBeyA5jBPnLs16ha5eUqLUTz
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = ' '.join(d['text'] for d in civic_docs)

# Heuristic: disaster projects mentioned with 2022 in same sentence/line
projects_2022_disaster = set()
for line in texts.split('\n'):
    if '2022' in line and re.search(r'(FEMA|CalOES|CalJPIA|Woolsey|Disaster Recovery)', line, re.I):
        name = line.strip()
        if name:
            projects_2022_disaster.add(name)

# Also capture lines that look like project titles with 2022 and typical suffixes
for line in texts.split('\n'):
    if '2022' in line and re.search(r'(Improvements|Repairs|Project)', line):
        if re.search(r'(FEMA|CalOES|CalJPIA)', line):
            projects_2022_disaster.add(line.strip())

# Normalize by just keeping project name before first bullet/paren
normalized = set()
for p in projects_2022_disaster:
    p2 = re.split(r'[-:\u2022]', p)[0]
    p2 = p2.strip()
    normalized.add(p2)

projects_2022_disaster = normalized

# Load funding table
path_f = var_call_rzIMnrNOIShmkg8kW5IpJkXV
with open(path_f, 'r') as f:
    funding = json.load(f)

# Identify disaster-type projects by name suffix and assume all years, then filter by 2022 start from docs using substring 2022 in some inferred date field.
# Since we don't have structured dates, approximate: any disaster-style project whose name contains '2022' is 2022-start, plus any match from extracted set.

disaster_keywords = ['(FEMA Project)', '(FEMA/CalOES Project)', '(CalOES Project)', '(CalJPIA Project)', '(FEMA)', '(CalOES)']

total = 0
used = []
for row in funding:
    name = row['Project_Name']
    is_disaster = any(k in name for k in disaster_keywords)
    if not is_disaster:
        continue
    # 2022 start proxy: name has 2022 or is in extracted set by prefix match
    if '2022' in name:
        total += int(row['Amount'])
        used.append(name)
        continue
    for p in projects_2022_disaster:
        if name.startswith(p):
            total += int(row['Amount'])
            used.append(name)
            break

result = {'total_funding_2022_disaster_projects': total, 'matched_projects': used}

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_BBeyA5jBPnLs16ha5eUqLUTz': 'file_storage/call_BBeyA5jBPnLs16ha5eUqLUTz.json', 'var_call_rzIMnrNOIShmkg8kW5IpJkXV': 'file_storage/call_rzIMnrNOIShmkg8kW5IpJkXV.json'}

exec(code, env_args)
