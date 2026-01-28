code = """import json
import re
import pandas as pd

# Load previous tool results from storage file paths
with open(var_call_0vg5Fb4iZ2XHFKzqCyioWnmg, 'r') as f:
    docs = json.load(f)
with open(var_call_zcrhR2NcXjzG5JIvFd6gjDZK, 'r') as f:
    funds = json.load(f)

# Prepare funding DataFrame and set of funded project names with Amount > 50000
df_funds = pd.DataFrame(funds)
# Ensure Amount is integer
if 'Amount' in df_funds.columns:
    df_funds['Amount'] = df_funds['Amount'].astype(int)
else:
    df_funds['Amount'] = 0

funded_projects = set(df_funds[df_funds['Amount'] > 50000]['Project_Name'].tolist())

# Parse documents to extract project names under "Capital Improvement Projects (Design)"
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        # try lowercase variant
        start_idx = text.find('Capital Improvement Projects (design)')
    if start_idx == -1:
        continue
    # find end of the design section
    end_idx = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Construction)']:
        m = text.find(marker, start_idx + 1)
        if m != -1:
            end_idx = min(end_idx, m)
    section = text[start_idx:end_idx]
    # Split section into paragraphs by two or more newlines
    paras = re.split(r'\n{2,}', section)
    for p in paras:
        p = p.strip()
        if not p:
            continue
        # take first line
        first_line = p.splitlines()[0].strip()
        if not first_line:
            continue
        if first_line == 'Capital Improvement Projects (Design)':
            continue
        # filter out lines that are not project names
        skip_indicators = ['Updates', 'Project Schedule', 'Project Description', 'RECOMMENDED ACTION', 'DISCUSSION', 'Agenda', 'Page', 'Approved by', 'Prepared by', 'Meeting date']
        if any(ind in first_line for ind in skip_indicators):
            continue
        if first_line.startswith('(') or first_line.startswith('Item') or first_line.endswith(':'):
            continue
        if len(first_line) < 5:
            continue
        # Clean up whitespace
        clean_name = re.sub(r'\s+', ' ', first_line).strip()
        design_projects.add(clean_name)

# Now find intersection with funded projects > 50000
matched_projects = sorted([p for p in design_projects if p in funded_projects])
count = len(matched_projects)

result = {"count": count, "projects": matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0vg5Fb4iZ2XHFKzqCyioWnmg': 'file_storage/call_0vg5Fb4iZ2XHFKzqCyioWnmg.json', 'var_call_zcrhR2NcXjzG5JIvFd6gjDZK': 'file_storage/call_zcrhR2NcXjzG5JIvFd6gjDZK.json'}

exec(code, env_args)
