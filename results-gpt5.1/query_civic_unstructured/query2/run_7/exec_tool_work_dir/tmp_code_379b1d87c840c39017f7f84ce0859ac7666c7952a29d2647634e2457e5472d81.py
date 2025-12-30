code = """import re, json
from collections import defaultdict

# Load full civic docs
import pandas as pd

path = var_call_GnX6xt7hY3INOHf23HF6PI6N
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d['text'] for d in civic_docs)

# Heuristic: find project-like lines and attach simple attributes by regex
lines = [l.strip() for l in texts.split('\n') if l.strip()]
projects = []
for line in lines:
    if len(line) > 3 and any(k in line.lower() for k in ['park']):
        projects.append(line)

# Approximate project names with year or capitalized phrases around 'Park'
project_names = set()
for p in projects:
    project_names.add(p)

# Filter for those mentioning completion in 2022
completed_2022_names = set()
for line in lines:
    if '2022' in line and 'completed' in line.lower():
        # grab previous line as project name heuristic
        idx = lines.index(line)
        if idx>0:
            name = lines[idx-1].strip()
            if 'park' in name.lower():
                completed_2022_names.add(name)

# Also look for 'Park' projects with 'Construction was completed, November 2022' pattern
for i,line in enumerate(lines):
    if 'Construction was completed' in line and '2022' in line:
        # search upwards for nearest line with 'Park'
        for j in range(i-1, max(-1,i-5), -1):
            if 'park' in lines[j].lower():
                completed_2022_names.add(lines[j].strip())
                break

completed_2022_names = list(completed_2022_names)

# Load funding
path2 = var_call_5hDBo3TBIgrWNiqKfckgM8Dr
with open(path2, 'r') as f:
    funding = json.load(f)

# naive join by substring matching
total = 0
matched = []
for rec in funding:
    pname = rec['Project_Name']
    for cname in completed_2022_names:
        # substring either direction
        if pname.lower() in cname.lower() or cname.lower() in pname.lower():
            amt = int(rec['Amount'])
            total += amt
            matched.append({'civic_name': cname, 'fund_name': pname, 'Amount': amt})
            break

result = {'completed_2022_park_projects': completed_2022_names, 'matches': matched, 'total_funding': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GnX6xt7hY3INOHf23HF6PI6N': 'file_storage/call_GnX6xt7hY3INOHf23HF6PI6N.json', 'var_call_5hDBo3TBIgrWNiqKfckgM8Dr': 'file_storage/call_5hDBo3TBIgrWNiqKfckgM8Dr.json'}

exec(code, env_args)
