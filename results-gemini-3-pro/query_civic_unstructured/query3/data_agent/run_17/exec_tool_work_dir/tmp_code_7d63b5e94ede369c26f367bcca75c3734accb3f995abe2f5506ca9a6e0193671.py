code = """import json
import pandas as pd

funding_path = locals()['var_function-call-5188433826363097598']
docs_path = locals()['var_function-call-7088797317398377498']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.splitlines()
    status = None
    curr = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if 'Capital Improvement Projects (Design)' in line:
            status = 'design'
            continue
        if 'Capital Improvement Projects (Construction)' in line:
            status = 'construction'
            continue
        if 'Capital Improvement Projects (Not Started)' in line:
            status = 'not started'
            continue
            
        is_bullet = line.startswith('(') or line.startswith('-')
        is_k = line.startswith('Updates:') or line.startswith('Project Schedule:') or line.startswith('Estimated Schedule:') or line.startswith('Project Description:')
        
        next_l = ''
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                next_l = lines[j].strip()
                break
        
        is_start = False
        if status and not is_bullet and not is_k:
            if next_l.startswith('(') or next_l.startswith('Updates:') or next_l.startswith('Project Description:') or next_l.startswith('Project Updates:'):
                is_start = True
                if 'Page' in line and 'of' in line: is_start = False
                if 'Agenda Item' in line: is_start = False
                if 'Public Works' in line and 'Commission' in line: is_start = False
        
        if is_start:
            if curr: projects.append(curr)
            curr = {'Project_Name': line, 'status': status, 'lines': [], 'st': None, 'et': None}
        elif curr:
            curr['lines'].append(line)
            
    if curr: projects.append(curr)

final = []
for p in projects:
    full = ' '.join(p['lines'])
    s = p['status']
    if 'Construction was completed' in full or 'Notice of completion filed' in full:
        s = 'completed'
    
    st = None
    et = None
    for l in p['lines']:
        ll = l.lower()
        if 'begin construction' in ll and ':' in l:
            st = l.split(':', 1)[1].strip()
        if 'complete construction' in ll and ':' in l:
            et = l.split(':', 1)[1].strip()
            
    p['st'] = st
    p['et'] = et
    p['status'] = s
    
    related = False
    if 'EMERGENCY' in p['Project_Name'].upper() or 'FEMA' in p['Project_Name'].upper():
        related = True
    elif 'EMERGENCY' in full.upper() or 'FEMA' in full.upper():
        related = True
    
    if related:
        final.append(p)

df = pd.DataFrame(final)
res = []
if not df.empty:
    merged = pd.merge(df, funding_df, on='Project_Name', how='inner')
    res = merged[['Project_Name', 'Funding_Source', 'Amount', 'status', 'st', 'et']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-1936795018027182717': ['Funding'], 'var_function-call-1936795018027181912': 'file_storage/function-call-1936795018027181912.json', 'var_function-call-5188433826363097598': 'file_storage/function-call-5188433826363097598.json', 'var_function-call-7088797317398377498': 'file_storage/function-call-7088797317398377498.json'}

exec(code, env_args)
