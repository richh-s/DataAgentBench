code = """import json
import re

# Load data
with open(locals()['var_function-call-8970245157857899516'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-8970245157857899203'], 'r') as f:
    funding_data = json.load(f)

# Build funding map
project_funding = {}
for row in funding_data:
    p_name = row['Project_Name'].strip()
    amount = float(row['Amount'])
    key = p_name.lower()
    if key not in project_funding:
        project_funding[key] = 0.0
    project_funding[key] += amount

# Extract projects
completed_park_projects = set()
debug_log = []

# Regex: Name line, followed by newlines, followed by (cid:190) Updates/Project Description
# We use \\n for newlines in regex string within this python code
pattern_str = r'(?P<name>[^\n]+)\s*\n+\(cid:190\)\s*(?:Updates|Project Description)'
marker_pattern = re.compile(pattern_str, re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    matches = list(marker_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        raw_name = match.group('name').strip()
        
        start_idx = match.start()
        if i < len(matches) - 1:
            end_idx = matches[i+1].start()
            block = text[start_idx:end_idx]
        else:
            block = text[start_idx:]
        
        # Check park
        if "park" in raw_name.lower():
            # Check completed 2022
            # "Construction was completed... 2022"
            if re.search(r'construction (was )?completed.*?2022', block, re.IGNORECASE):
                completed_park_projects.add(raw_name)

total_funding = 0.0
matched_projects = []

for p_name in completed_park_projects:
    key = p_name.strip().lower()
    if key in project_funding:
        amount = project_funding[key]
        total_funding += amount
        matched_projects.append({"name": p_name, "amount": amount})
    else:
        # Check if we can find it by loose match
        # e.g. "Bluffs Park Shade Structure" vs "Bluffs Park Shade Structure "
        pass

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-8970245157857899516': 'file_storage/function-call-8970245157857899516.json', 'var_function-call-8970245157857899203': 'file_storage/function-call-8970245157857899203.json'}

exec(code, env_args)
