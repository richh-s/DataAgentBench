code = """import re, json
from pathlib import Path

# Load full civic docs result
with open(var_call_BAsnvRD7vOexiKI04VdghO6V, 'r') as f:
    civic_docs = json.load(f)

# Function to heuristically extract project blocks and attributes
projects = []
for doc in civic_docs:
    text = doc['text']
    # Split on double newlines as rough blocks
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        # Only consider blocks that mention FEMA/CalOES or 'Disaster'
        if not re.search(r"FEMA|CalOES|CalJPIA|disaster", block, re.I):
            continue
        # Try to get a project name: first line of the block
        lines = [l.strip() for l in block.split('\n') if l.strip()]
        if not lines:
            continue
        proj_name = lines[0]
        # crude date search for st/et containing 2022
        dates = re.findall(r"(2022[-/A-Za-z0-9 ]*)", block)
        st = dates[0] if dates else ''
        et = dates[1] if len(dates) > 1 else ''
        projects.append({
            'Project_Name': proj_name,
            'block': block,
            'st': st,
            'et': et
        })

# Filter to those with 2022 in st or et
projects_2022 = [p for p in projects if '2022' in p['st'] or '2022' in p['et'] or re.search(r"2022", p['block'])]

# Just collect unique project names for 2022 disaster-related
proj_names_2022 = sorted(set(p['Project_Name'] for p in projects_2022))

result = json.dumps({'project_names_2022_disaster_related': proj_names_2022})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_BAsnvRD7vOexiKI04VdghO6V': 'file_storage/call_BAsnvRD7vOexiKI04VdghO6V.json', 'var_call_Z1hcL4TsObnFcPs2MsyVU5P3': 'file_storage/call_Z1hcL4TsObnFcPs2MsyVU5P3.json'}

exec(code, env_args)
