code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_a3J5UCGacpNITPno4TYl6FQE)
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = "\n".join(texts)

# Heuristic: disaster projects contain FEMA/CalOES/CalJPIA or words like 'Disaster Recovery Projects'
# Extract project lines around those markers with years/dates
projects = {}
for line in full_text.split('\n'):
    l = line.strip()
    if not l:
        continue
    if any(k in l for k in ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster Recovery Projects']):
        # Consider this a project name line
        name = l
        projects.setdefault(name, {})
    # Also collect lines that look like project headings with a year and road/park/etc
    if re.search(r'\b20[0-3][0-9]\b', l) and any(w in l for w in ['Project','Improvements','Repairs','Warning','Park','Bridge','Drain','Slope','Road','Canyon','Beach']):
        projects.setdefault(l, {})

# Now search for start time lines near each project by scanning windows in text
lines = full_text.split('\n')
for i, line in enumerate(lines):
    for pname in list(projects.keys()):
        if pname.strip() == line.strip():
            window = " ".join(lines[i:i+8])
            m = re.search(r'(Begin Construction|Start|Project Schedule)[^\.]*?(20[0-3][0-9])', window)
            if m:
                projects[pname]['st_year'] = m.group(2)

# Collect project names that are disaster-type and start year 2022
selected_names = set()
for pname, info in projects.items():
    text_lower = pname.lower()
    is_disaster = any(k in pname for k in ['(FEMA', '(CalOES', '(CalJPIA']) or 'disaster' in text_lower or 'recovery' in text_lower
    if not is_disaster:
        continue
    if info.get('st_year') == '2022':
        selected_names.add(pname)

# But Funding table uses cleaned project names; map by containment/overlap heuristics
funding = pd.DataFrame(var_call_vGDJRYxEHmcds85eUElyGBYZ)
funding['Amount'] = funding['Amount'].astype(int)

def is_disaster_project_name(n):
    return any(k in n for k in ['(FEMA', '(CalOES', '(CalJPIA']) or 'disaster' in n.lower() or 'recovery' in n.lower()

# Assume disaster projects generally those with FEMA/CalOES/CalJPIA tags in Funding
funding['is_disaster'] = funding['Project_Name'].apply(is_disaster_project_name)

# We don't have reliable st_year from docs mapping, approximate: disaster projects that likely started in 2022 have '2022' in name
funding['has_2022_in_name'] = funding['Project_Name'].str.contains('2022')

# Additionally, try matching against selected_names by substring
if selected_names:
    sel_lower = [s.lower() for s in selected_names]
    def match_selected(n):
        nl = n.lower()
        return any(sl in nl or nl in sl for sl in sel_lower)
    funding['matches_selected'] = funding['Project_Name'].apply(match_selected)
else:
    funding['matches_selected'] = False

mask = funding['is_disaster'] & (funding['has_2022_in_name'] | funding['matches_selected'])

total_amount = int(funding.loc[mask, 'Amount'].sum())

result = {"total_disaster_funding_2022_start_projects": total_amount}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_a3J5UCGacpNITPno4TYl6FQE': 'file_storage/call_a3J5UCGacpNITPno4TYl6FQE.json', 'var_call_vGDJRYxEHmcds85eUElyGBYZ': 'file_storage/call_vGDJRYxEHmcds85eUElyGBYZ.json'}

exec(code, env_args)
