code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_wO38ZjGimh1uwB8txz3OP2RP, 'r') as f:
    civic_docs = json.load(f)

# Simple heuristic: project lines often end with 'Project' or 'Improvements' etc.; dates like '2022-Spring' in text
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    # Find patterns like 'Project Schedule' blocks with seasons/years
    for line in text.split('\n'):
        line_strip = line.strip()
        if not line_strip:
            continue
        # Capture project name: lines that look like a title (no colon, reasonable length)
        # Collect nearby date info is too complex; instead, search globally for '2022-Spring' etc.
    # Global search for st patterns
    # Assume formats shortened like '2022-Spring', 'Spring 2022', '2022-March', 'March 2022'
    # For this synthetic dataset, we'll search explicit tokens

# Since actual structured st/et are not present, approximate by keyword search for 'Spring 2022'
projects_spring_2022 = set()
for doc in civic_docs:
    text = doc.get('text','')
    # Find project headings: lines surrounded by blank lines that are Title Case
    lines = text.split('\n')
    for i,line in enumerate(lines):
        if 'Spring 2022' in line or '2022-Spring' in line or '2022 March' in line or 'March 2022' in line or 'April 2022' in line or 'May 2022' in line:
            # look backwards for a likely project name (previous non-empty line)
            j = i-1
            while j>=0 and not lines[j].strip():
                j-=1
            if j>=0:
                name = lines[j].strip()
                # filter out generic headings
                if len(name.split())>1 and not name.endswith(':'):
                    projects_spring_2022.add(name)

# Load funding table
funding = var_call_ZXPtfJt8g3NwUStm2Ba5qIIR

# If funding is stored directly as list
if isinstance(funding, list):
    funding_records = funding
else:
    # It's a path
    with open(funding, 'r') as f:
        funding_records = json.load(f)

# Match funding project names approximately: exact or containment both ways
started_projects = []
for fr in funding_records:
    fname = fr.get('Project_Name','')
    for pname in projects_spring_2022:
        if fname==pname or fname in pname or pname in fname:
            started_projects.append(fr)
            break

# Aggregate
total_projects = len({fr['Project_Name'] for fr in started_projects})
total_funding = sum(int(fr['Amount']) for fr in started_projects)

result = {"projects_started_spring_2022": total_projects, "total_funding": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wO38ZjGimh1uwB8txz3OP2RP': 'file_storage/call_wO38ZjGimh1uwB8txz3OP2RP.json', 'var_call_ZXPtfJt8g3NwUStm2Ba5qIIR': 'file_storage/call_ZXPtfJt8g3NwUStm2Ba5qIIR.json'}

exec(code, env_args)
