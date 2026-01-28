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
if 'Amount' in df_funds.columns:
    # convert to int safely
    df_funds['Amount'] = df_funds['Amount'].apply(lambda x: int(x) if x is not None and str(x).strip() != '' else 0)
else:
    df_funds['Amount'] = 0

funded_projects = set(df_funds[df_funds['Amount'] > 50000]['Project_Name'].tolist())

# Parse documents to extract project names under "Capital Improvement Projects (Design)"
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    # case-insensitive search
    low = text.lower()
    marker = 'capital improvement projects (design)'
    start_idx = low.find(marker)
    if start_idx == -1:
        continue
    # find end markers
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    end_idx = len(text)
    for em in end_markers:
        m = low.find(em, start_idx+1)
        if m != -1:
            end_idx = min(end_idx, m)
    section = text[start_idx:end_idx]
    # split into lines
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    # remove the header line
    if lines and lines[0].lower().startswith('capital improvement projects'):
        lines = lines[1:]
    # heuristic: project names are lines that are Title Case and not starting with '(' or containing ':' or 'Updates' or 'Project Schedule' etc.
    skip_tokens = ['updates', 'project schedule', 'project description', 'recommended action', 'discussion', 'agenda', 'page', 'approved by', 'prepared by', 'meeting date']
    for ln in lines:
        lowln = ln.lower()
        if any(tok in lowln for tok in skip_tokens):
            continue
        if ln.startswith('(') or ln.startswith('Item') or ln.endswith(':'):
            continue
        # if line contains words like 'Complete Design' or 'Begin Construction', skip
        if re.search(r'complete design|begin construction|advertise|updates:', lowln):
            continue
        # skip lines that are too short
        if len(ln) < 5:
            continue
        # remove bullets like (cid:131)
        ln_clean = re.sub(r"\(cid:[0-9]+\)", "", ln)
        ln_clean = re.sub(r"\s+", " ", ln_clean).strip()
        # Exclude lines that are clearly sentences (contain verbs)
        if re.search(r'\b(is|are|was|will|have|has|working|submitted|received)\b', lowln):
            continue
        # Final cleanup
        design_projects.add(ln_clean)

# Now find intersection with funded projects > 50000
matched_projects = sorted([p for p in design_projects if p in funded_projects])
count = len(matched_projects)

result = {"count": count, "projects": matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0vg5Fb4iZ2XHFKzqCyioWnmg': 'file_storage/call_0vg5Fb4iZ2XHFKzqCyioWnmg.json', 'var_call_zcrhR2NcXjzG5JIvFd6gjDZK': 'file_storage/call_zcrhR2NcXjzG5JIvFd6gjDZK.json'}

exec(code, env_args)
