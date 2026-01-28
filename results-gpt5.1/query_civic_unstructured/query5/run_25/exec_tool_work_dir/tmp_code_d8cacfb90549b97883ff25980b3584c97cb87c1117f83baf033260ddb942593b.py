code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_a3J5UCGacpNITPno4TYl6FQE)
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = "\n".join(texts)

projects = {}
for line in full_text.split('\n'):
    l = line.strip()
    if not l:
        continue
    if ('(FEMA' in l) or ('(CalOES' in l) or ('(CalJPIA' in l) or ('Disaster Recovery Projects' in l):
        name = l
        projects.setdefault(name, {})
    if (re.search(r"\b20[0-3][0-9]\b", l) is not None) and any(w in l for w in ['Project','Improvements','Repairs','Warning','Park','Bridge','Drain','Slope','Road','Canyon','Beach']):
        projects.setdefault(l, {})

lines = full_text.split('\n')
for i, line in enumerate(lines):
    for pname in list(projects.keys()):
        if pname.strip() == line.strip():
            window = " ".join(lines[i:i+8])
            m = re.search(r"(Begin Construction|Start|Project Schedule)[^\.]*?(20[0-3][0-9])", window)
            if m:
                projects[pname]['st_year'] = m.group(2)

selected_names = set()
for pname, info in projects.items():
    text_lower = pname.lower()
    is_disaster = ('(FEMA' in pname) or ('(CalOES' in pname) or ('(CalJPIA' in pname) or ('disaster' in text_lower) or ('recovery' in text_lower)
    if not is_disaster:
        continue
    if info.get('st_year') == '2022':
        selected_names.add(pname)

funding = pd.DataFrame(var_call_vGDJRYxEHmcds85eUElyGBYZ)
funding['Amount'] = funding['Amount'].astype(int)

def is_disaster_project_name(n):
    nl = n.lower()
    return ('(FEMA' in n) or ('(CalOES' in n) or ('(CalJPIA' in n) or ('disaster' in nl) or ('recovery' in nl)

funding['is_disaster'] = funding['Project_Name'].apply(is_disaster_project_name)
funding['has_2022_in_name'] = funding['Project_Name'].str.contains('2022')

if selected_names:
    sel_lower = [s.lower() for s in selected_names]
    def match_selected(n):
        nl = n.lower()
        return any((sl in nl) or (nl in sl) for sl in sel_lower)
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
