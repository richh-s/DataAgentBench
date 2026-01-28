code = """import json, re, pandas as pd

funding_path = var_call_JFNSJn88SwwPbW3ARaj7PbSk
with open(funding_path,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

docs_path = var_call_4NLqzXah9v790slRX2YcYvTs
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

projects = []
for d in docs:
    text = d.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    idxs = [i for i,ln in enumerate(lines) if re.search(r'\bDisaster Recovery Projects\b', ln)]
    if not idxs:
        continue
    start_i = idxs[0]
    sub = [ln for ln in lines[start_i:start_i+500] if ln.strip()]
    current = None
    for ln in sub:
        if ln in ['Updates:', 'Project Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Schedule (pending the MOU extension approval):']:
            continue
        # new project header heuristic
        if not re.search(r'^(\(cid:|[•\-]|\d+\.|Page\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects)', ln) and ':' not in ln:
            if 1 <= len(ln) <= 120 and any(ch.isalpha() for ch in ln):
                if ln.lower() in ['disaster recovery projects','capital improvement projects','construction','design','not started']:
                    continue
                current = {'Project_Name': ln, 'st': None}
                projects.append(current)
                continue
        if current is None:
            continue
        if re.search(r'\bBegin\s+Construction\b', ln, re.I):
            m = re.search(r':\s*(.*)$', ln)
            if m:
                current['st'] = m.group(1).strip()

proj_df = pd.DataFrame(projects)
if proj_df.empty:
    out = {'total_funding': 0, 'project_count': 0, 'projects': []}
else:
    proj_df = proj_df.drop_duplicates(subset=['Project_Name'])
    if 'st' not in proj_df.columns:
        proj_df['st'] = None
    proj_2022 = proj_df[proj_df['st'].fillna('').str.contains('2022')]
    joined = proj_2022.merge(fund_df, on='Project_Name', how='inner')
    total = int(joined['total_amount'].sum())
    out = {
        'total_funding': total,
        'project_count': int(joined.shape[0]),
        'projects': joined[['Project_Name','st','total_amount']].sort_values('Project_Name').to_dict(orient='records')
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JFNSJn88SwwPbW3ARaj7PbSk': 'file_storage/call_JFNSJn88SwwPbW3ARaj7PbSk.json', 'var_call_4NLqzXah9v790slRX2YcYvTs': 'file_storage/call_4NLqzXah9v790slRX2YcYvTs.json'}

exec(code, env_args)
