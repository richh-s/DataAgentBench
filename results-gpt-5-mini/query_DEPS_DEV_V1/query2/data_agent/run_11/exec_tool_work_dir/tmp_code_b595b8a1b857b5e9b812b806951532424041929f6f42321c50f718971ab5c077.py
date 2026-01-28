code = """import json
import re
from pathlib import Path

# Load file paths from storage variables
pairs_path = Path(var_call_Cl2PGDtjPTh0xSN30RGJ2iLR)
ppv_path = Path(var_call_x1eNQfSPclUPTzv94gkFbW5f)
pi_path = Path(var_call_C6xE38gBfjBxgBNwUJhwG1UY)

pairs = json.loads(pairs_path.read_text())
ppv = json.loads(ppv_path.read_text())
pi = json.loads(pi_path.read_text())

# Build set of Name-Version pairs
pair_set = {(p['Name'], p['Version']) for p in pairs}

# Filter project_packageversion to those matching our pairs
matched_projects = set()
for r in ppv:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    if key in pair_set:
        pn = r.get('ProjectName')
        if pn:
            matched_projects.add(pn)

# Prepare project_info text list
pi_texts = [item.get('Project_Information','') for item in pi]

results = []
# For each matched project, find a project_info entry that mentions it
for proj in matched_projects:
    found = None
    for text in pi_texts:
        if proj in text:
            found = text
            break
    if not found:
        # try variations: sometimes ProjectName may be 'owner/repo' but info may include repo only
        # fallback: skip
        continue
    # extract fork count
    forks = None
    # pattern: number before 'fork' (e.g., '5782 forks' or '173 forks')
    m = re.search(r"(\d[\d,]*)\s+forks?", found, flags=re.IGNORECASE)
    if m:
        forks = int(m.group(1).replace(',',''))
    else:
        # pattern: 'forked 100 times' or 'been forked 100 times'
        m = re.search(r"forked\s+(\d[\d,]*)", found, flags=re.IGNORECASE)
        if m:
            forks = int(m.group(1).replace(',',''))
        else:
            # pattern: 'forks count of 100' or 'forks count: 100'
            m = re.search(r"forks?\s*(?:count\s*(?:of|:)?\s*)?(\d[\d,]*)", found, flags=re.IGNORECASE)
            if m:
                forks = int(m.group(1).replace(',',''))
    if forks is None:
        forks = 0
    results.append({
        'ProjectName': proj,
        'Forks': forks,
        'Project_Information': found
    })

# Sort by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_5AMYD8MyDFKO01JvVzZWn3eS': ['packageinfo'], 'var_call_BaSR9ijbE3x4QXyQoGOzRPFT': ['project_info', 'project_packageversion'], 'var_call_faxdiIQt980BBkyMR5n1KUWN': 'file_storage/call_faxdiIQt980BBkyMR5n1KUWN.json', 'var_call_Cl2PGDtjPTh0xSN30RGJ2iLR': 'file_storage/call_Cl2PGDtjPTh0xSN30RGJ2iLR.json', 'var_call_8EXA01L6v89sB8AYvZmOyaxs': 'file_storage/call_8EXA01L6v89sB8AYvZmOyaxs.json', 'var_call_uQVDWukcW2PrMS7jAJ235ijj': 'file_storage/call_uQVDWukcW2PrMS7jAJ235ijj.json', 'var_call_x1eNQfSPclUPTzv94gkFbW5f': 'file_storage/call_x1eNQfSPclUPTzv94gkFbW5f.json', 'var_call_C6xE38gBfjBxgBNwUJhwG1UY': 'file_storage/call_C6xE38gBfjBxgBNwUJhwG1UY.json'}

exec(code, env_args)
