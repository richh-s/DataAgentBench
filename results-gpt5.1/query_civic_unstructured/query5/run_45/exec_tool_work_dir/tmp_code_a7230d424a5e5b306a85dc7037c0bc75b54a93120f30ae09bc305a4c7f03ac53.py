code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_yL94HGQiKFWbhMgCL4V0jVfp)
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

lines = [l.strip() for l in texts.split('\n') if l.strip()]
projects = []
current = None
for line in lines:
    if re.match(r'.*Project', line) or re.match(r'.*Improvements', line) or re.match(r'.*Repairs', line) or ('Warning Sirens' in line) or ('Warning Signs' in line):
        if len(line.split()) <= 2:
            continue
        current = {'Project_Name': line, 'st': None, 'et': None, 'type': None}
        projects.append(current)
    if current and (('Begin Construction' in line) or ('Begin construction' in line) or ('Project Schedule' in line) or ('Estimated Schedule' in line)):
        if 'Begin' in line:
            current['st'] = line
    if current and (('Project Description' in line) or ('FEMA' in line) or ('CalOES' in line) or ('CalJPIA' in line) or ('Woolsey' in line) or ('Disaster' in line)):
        if ('FEMA' in line) or ('CalOES' in line) or ('CalJPIA' in line) or ('Woolsey' in line) or ('Disaster' in line):
            current['type'] = 'disaster'

for p in projects:
    if p['st'] is not None:
        m = re.search(r'20\d{2}', p['st'])
        if m:
            p['year'] = m.group(0)
        else:
            p['year'] = None
    else:
        p['year'] = None

proj_2022 = {p['Project_Name'] for p in projects if (p['type'] == 'disaster') and (p.get('year') == '2022')}

funding_df = pd.DataFrame(var_call_5MtKHcJvjOfSwn1chlyXO3Ma)
funding_df['Amount'] = funding_df['Amount'].astype(int)

mask = funding_df['Project_Name'].isin(proj_2022)
sel = funding_df[mask]

result = {
    'projects_2022_disaster': list(proj_2022),
    'matched_funding_records': sel.to_dict(orient='records'),
    'total_funding_2022_disaster': int(sel['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yL94HGQiKFWbhMgCL4V0jVfp': 'file_storage/call_yL94HGQiKFWbhMgCL4V0jVfp.json', 'var_call_5MtKHcJvjOfSwn1chlyXO3Ma': 'file_storage/call_5MtKHcJvjOfSwn1chlyXO3Ma.json'}

exec(code, env_args)
