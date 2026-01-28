code = """import re, json, pandas as pd

path_docs = var_call_rw3mILjLc7tXWSaw2jRbUfuM
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

lines = [l.strip() for l in full_text.split('\n')]
proj_lines = []
keywords = ['road','park','project','improvements','repairs','storm','drain','playground','facility','study','warning','median','crosswalk','walkway','shade','roof','hvac','biofilter','culvert','bridge','guardrail','traffic','water','resurfacing','maintenance','treatment','slope','retaining wall','skate','signals','benches','arbors']
for l in lines:
    if not l:
        continue
    if ':' in l:
        continue
    if len(l.split()) > 12:
        continue
    low = l.lower()
    if any(k in low for k in ['agenda','report','item','updates','project schedule','estimated schedule','project description']):
        continue
    if any(k in low for k in keywords):
        proj_lines.append(l)

proj_names = sorted(set(proj_lines))

spring_patterns = [
    re.compile(r'Begin Construction:\s*Spring\s*2022', re.I),
    re.compile(r'Advertise:\s*Spring\s*2022', re.I),
    re.compile(r'2022-0[3-5]'),
    re.compile(r'(March|April|May)\s+2022', re.I),
    re.compile(r'Spring\s+2022', re.I),
]

lines_with_idx = list(enumerate(lines))

spring_projects = set()
for pname in proj_names:
    for idx, l in lines_with_idx:
        if l.strip() == pname:
            window = '\n'.join(x for _, x in lines_with_idx[idx:idx+25])
            if any(p.search(window) for p in spring_patterns):
                spring_projects.add(pname)
                break

path_fund = var_call_pNrwAvR3IlQ54Kfa0jjVvLJa
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

spring_projects_list = sorted(list(spring_projects))
mask = fund_df['Project_Name'].isin(spring_projects_list)
matched = fund_df[mask]

result = {
    'spring_2022_project_names_from_docs': spring_projects_list,
    'matched_funded_projects': matched['Project_Name'].tolist(),
    'count_projects_started_spring_2022': int(mask.sum()),
    'total_funding_for_these_projects': int(matched['Amount'].sum()),
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_rw3mILjLc7tXWSaw2jRbUfuM': 'file_storage/call_rw3mILjLc7tXWSaw2jRbUfuM.json', 'var_call_pNrwAvR3IlQ54Kfa0jjVvLJa': 'file_storage/call_pNrwAvR3IlQ54Kfa0jjVvLJa.json'}

exec(code, env_args)
