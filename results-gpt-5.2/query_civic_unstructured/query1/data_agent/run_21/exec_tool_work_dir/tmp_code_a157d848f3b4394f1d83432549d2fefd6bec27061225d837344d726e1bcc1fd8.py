code = """import json, re, pandas as pd

# load funding > 50000
fund_path = var_call_wPuywgwAi6U2yzb1vhODm8Sp
with open(fund_path, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_projects = {r['Project_Name'] for r in fund}

# load civic docs
civic_path = var_call_88GaOK77FtOdfo63Nml4Nuqr
with open(civic_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Determine which funded projects are in 'design' status by searching for design sections
# Heuristic: if project name appears in a document and within 4000 chars after a header containing 'Design' or in a section titled 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)'

def is_design_in_text(proj, text):
    lt = text.lower()
    p = re.escape(proj.lower())
    # direct 'proj ... design' nearby
    m = re.search(p, lt)
    if not m:
        return False
    idx = m.start()
    window = lt[max(0, idx-1500): idx+1500]
    if 'design' in window:
        # avoid cases like '(design)' in project name only? still indicates design status generally
        return True
    # check for design header before project listing
    prior = lt[max(0, idx-4000):idx]
    if re.search(r'\(design\)', prior) or 'projects (design)' in prior or 'under design' in prior or 'design phase' in prior:
        return True
    return False

# compute design projects
found_design = set()
for d in docs:
    text = d.get('text','')
    for proj in list(fund_projects - found_design):
        if is_design_in_text(proj, text):
            found_design.add(proj)

result = {"count": len(found_design), "projects": sorted(found_design)[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wPuywgwAi6U2yzb1vhODm8Sp': 'file_storage/call_wPuywgwAi6U2yzb1vhODm8Sp.json', 'var_call_88GaOK77FtOdfo63Nml4Nuqr': 'file_storage/call_88GaOK77FtOdfo63Nml4Nuqr.json'}

exec(code, env_args)
