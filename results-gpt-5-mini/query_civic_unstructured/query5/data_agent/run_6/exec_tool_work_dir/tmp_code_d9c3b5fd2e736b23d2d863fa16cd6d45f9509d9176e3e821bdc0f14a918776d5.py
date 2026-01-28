code = """import json
import re

# Load data
with open(var_call_90dmcYwBxTb7vQatqrbc7U4G, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_7E8sUjkgBqwcx0vACQAqhl9z, 'r') as f:
    funding = json.load(f)

# Helpers
def normalize(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

disaster_keywords = ["fema", "caloes", "caljpia", "caljpia", "fema/caloes", "fema/", "cal o es", "cal o es", "fema"]
project_title_keywords = ["project","improvements","repairs","repair","resurfacing","renovation","study","facility","playground","phase","road","bridge","culvert","drainage","traffic study","walkway","water treatment","station"]

selected_projects = set()

# Find title-like lines and check nearby lines for 2022 and disaster keywords
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # determine if line looks like a project title by containing one of the title keywords
        low = line_stripped.lower()
        if any(k in low for k in project_title_keywords):
            # look ahead a few lines for '2022'
            window = '\n'.join(lines[i:i+12]).lower()
            has_2022 = '2022' in window
            has_disaster = any(k in window or k in low for k in disaster_keywords)
            if has_2022 and has_disaster:
                selected_projects.add(line_stripped)

# Also capture any explicit parenthetical FEMA/CalOES project names anywhere in docs with nearby 2022
for doc in civic_docs:
    text = doc.get('text','')
    for m in re.finditer(r"([A-Za-z0-9 &\'\-,.()]+\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES|FEMA/CalOES)\)[A-Za-z0-9 &\'\-,.]*)", text, re.IGNORECASE):
        span = m.span()
        snippet_window = text[max(0, span[0]-200):min(len(text), span[1]+200)].lower()
        if '2022' in snippet_window:
            candidate = m.group(0).strip()
            selected_projects.add(candidate)

# Normalize selected project names
selected_norms = [normalize(s) for s in selected_projects]

# Match funding records where project name matches any selected project (substring) OR funding project name contains disaster keywords and project is in 2022 in docs
matched = {}
total = 0
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_norm = normalize(pname)
    matched_flag = False
    for sn in selected_norms:
        if not sn:
            continue
        if sn in pname_norm or pname_norm in sn:
            matched_flag = True
            break
    # also if funding name itself includes disaster keywords and any selected project exists (to be safe)
    if not matched_flag and any(k in pname.lower() for k in disaster_keywords) and selected_norms:
        matched_flag = True
    if matched_flag:
        try:
            amt = int(float(rec.get('Amount',0)))
        except:
            amt = 0
        matched[pname] = amt
        total += amt

result = {"total_funding": total, "matched_projects": matched, "selected_projects": list(selected_projects)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FbCAMFAZTL2Ih3VWgvwFzEcF': ['civic_docs'], 'var_call_90dmcYwBxTb7vQatqrbc7U4G': 'file_storage/call_90dmcYwBxTb7vQatqrbc7U4G.json', 'var_call_aId1Wornd25qzPfcbmiNPMM9': ['Funding'], 'var_call_7E8sUjkgBqwcx0vACQAqhl9z': 'file_storage/call_7E8sUjkgBqwcx0vACQAqhl9z.json'}

exec(code, env_args)
