code = """import re, json
from collections import defaultdict

# Load funding > 50000
funding_records = var_call_u5Y6Md7vn139uNl1NNlLsbzI

# Load civic docs texts
civic_docs = var_call_dm9v833eUHokmhj2EmtnJPjo

# Extract project names and their inferred type/status from civic text.
# We'll use simple heuristics based on section headers like
# 'Capital Improvement Projects (Design)' etc.

project_status = {}
current_type = None
current_status = None

for doc in civic_docs:
    text = doc.get('text', '')
    # Normalize newlines
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for line in lines:
        lower = line.lower()
        # Detect section changes
        if 'capital improvement projects' in lower:
            current_type = 'capital'
            if '(design)' in lower:
                current_status = 'design'
            elif '(construction)' in lower:
                current_status = 'completed'  # treat as not design
            elif '(not started)' in lower:
                current_status = 'not started'
            continue
        # Reset type/status once we hit other big headings
        if lower.startswith('disaster recovery projects'):
            current_type = 'disaster'
            current_status = None
            continue
        # Skip non-project lines when we don't know context
        if current_type == 'capital' and current_status:
            # Heuristic: project name lines are those without colon and not bullets
            if not any(sym in line for sym in [':', 'updates', 'project schedule', 'estimated schedule', 'agenda item', 'page '] ) and len(line.split()) <= 10:
                # Record status for this project
                name = line.strip()
                if name and name.lower() != 'capital improvement projects (design)':
                    project_status[name] = {'type': current_type, 'status': current_status}

# Now join with funding records and count
count = 0

for rec in funding_records:
    pname = rec['Project_Name']
    # Direct match
    info = project_status.get(pname)
    if not info:
        # Try matching without parenthetical suffixes
        base = re.sub(r'\s*\(.*?\)\s*', '', pname).strip()
        info = project_status.get(base)
    if info and info['type'] == 'capital' and info['status'] == 'design':
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_u5Y6Md7vn139uNl1NNlLsbzI': 'file_storage/call_u5Y6Md7vn139uNl1NNlLsbzI.json', 'var_call_dm9v833eUHokmhj2EmtnJPjo': 'file_storage/call_dm9v833eUHokmhj2EmtnJPjo.json'}

exec(code, env_args)
