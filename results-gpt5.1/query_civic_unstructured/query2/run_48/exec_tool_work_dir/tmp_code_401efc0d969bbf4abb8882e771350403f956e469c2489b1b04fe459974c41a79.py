code = """import re, json, pandas as pd

path = var_call_AzxNLzQYErCuP7tasW38dzUp
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = [d.get('text','') for d in civic_docs]
full_text = '\n'.join(texts)

blocks = re.split(r'\n\n+', full_text)
projects = []
for block in blocks:
    first_line = block.strip().split('\n')[0].strip()
    if not first_line:
        continue
    if re.search(r'(Project|Park|Playground|Shade|Walkway)', first_line):
        topics = []
        for kw in ['park','playground','shade','walkway','road','bridge','storm drain','drainage']:
            if re.search(kw, block, re.IGNORECASE):
                topics.append(kw)
        status = None
        if re.search(r'Construction was completed,? (November )?2022', block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r'Construction was completed November 2022', block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r'Notice of completion', block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r'project is currently under construction', block, re.IGNORECASE):
            status = 'design'
        et = None
        m = re.search(r'Construction was completed,? ([A-Za-z]+ 2022|2022)', block, re.IGNORECASE)
        if m:
            et = m.group(1)
        m2 = re.search(r'Construction was completed ([A-Za-z]+ 2022)', block, re.IGNORECASE)
        if m2:
            et = m2.group(1)
        projects.append({
            'Project_Name': first_line,
            'topic': ','.join(sorted(set(topics))) if topics else '',
            'status': status or '',
            'et': et or ''
        })

park_projects_2022 = [p for p in projects if 'park' in p.get('topic','') and p.get('status')=='completed' and '2022' in p.get('et','')]

funding = pd.DataFrame(var_call_QE590y2beo7xdcETCshsds0E)
funding['Amount'] = funding['Amount'].astype(int)
proj_names = [p['Project_Name'] for p in park_projects_2022]
matched = funding[funding['Project_Name'].isin(proj_names)]

result = {
    'projects': park_projects_2022,
    'matched_funding_records': matched.to_dict(orient='records'),
    'total_funding': int(matched['Amount'].sum()) if not matched.empty else 0
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AzxNLzQYErCuP7tasW38dzUp': 'file_storage/call_AzxNLzQYErCuP7tasW38dzUp.json', 'var_call_QE590y2beo7xdcETCshsds0E': 'file_storage/call_QE590y2beo7xdcETCshsds0E.json'}

exec(code, env_args)
