code = """import json, re
from collections import defaultdict

# Load funding records (already filtered to Amount > 50000)
funding_records = var_call_pRUj9a82rmsVUyx3EyEFd0gA

# Load civic docs texts
civic_docs = var_call_2nuLhwW6sadTEG5zvzqimHxl
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic: extract project names under "Capital Improvement Projects (Design)" section
# We'll look for that header and then capture subsequent lines until next "Capital Improvement Projects" header

sections = re.split(r"Capital Improvement Projects \((?:Design|Construction|Not Started)\)", full_text)
# After split, sections[1] should correspond to text after first such header; but we need the part for Design specifically.
# Instead, explicitly find the Design section with regex groups.

m = re.search(r"Capital Improvement Projects \(Design\)([\s\S]*?)(?:Capital Improvement Projects \(|Capital Improvement Projects\s*\(|$)", full_text)
design_block = m.group(1) if m else ''

# Candidate project names in design_block: lines that look like title-case phrases, not starting with bullets or parentheses.
project_lines = []
for line in design_block.split('\n'):
    line = line.strip('\r ')
    if not line:
        continue
    # Skip lines that are clearly not project names
    if line.startswith('(') or line.startswith('Updates') or line.startswith('Project') or line.startswith('Estimated') or line.startswith('Page '):
        continue
    if ':' in line:
        continue
    # Heuristic: must contain at least one space and be mostly letters & spaces & punctuation
    if len(line.split()) >= 2:
        project_lines.append(line)

# Clean duplicates
design_projects = sorted(set(project_lines))

# Now match these project names against funding records by exact string match (case-sensitive) on Project_Name
funding_design_projects = []
for rec in funding_records:
    name = rec['Project_Name']
    if name in design_projects:
        funding_design_projects.append(name)

count = len(set(funding_design_projects))

result = {
    'design_project_names_detected': design_projects,
    'design_projects_with_funding_gt_50000_count': count,
    'matched_project_names': sorted(set(funding_design_projects)),
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_pRUj9a82rmsVUyx3EyEFd0gA': 'file_storage/call_pRUj9a82rmsVUyx3EyEFd0gA.json', 'var_call_2nuLhwW6sadTEG5zvzqimHxl': 'file_storage/call_2nuLhwW6sadTEG5zvzqimHxl.json'}

exec(code, env_args)
