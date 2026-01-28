code = """import json
import pandas as pd

k1 = 'var_function-call-13970698935459151877'
k2 = 'var_function-call-13579203068557831030'

with open(locals()[k1], 'r') as f:
    funding_data = json.load(f)

with open(locals()[k2], 'r') as f:
    civic_docs = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)
df_funding_grouped = df_funding.groupby('Project_Name')['Amount'].sum().reset_index()
funded_projects = set(df_funding_grouped[df_funding_grouped['Amount'] > 50000]['Project_Name'])

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        s = line.strip()
        
        if 'Capital Improvement Projects (Design)' in s:
            in_design = True
            continue
        if 'Capital Improvement Projects (' in s and 'Design' not in s:
            in_design = False
            continue
        if 'Disaster Recovery Projects' in s:
            in_design = False
            continue
            
        if in_design:
            if not s: continue
            if s.startswith('(cid:') or s.startswith('Updates:') or s.startswith('Project Schedule:'): continue
            if s.startswith('Page ') or s.startswith('Agenda Item'): continue
            if 'Project Description' in s: continue
            
            capital_design_projects.add(s)

matches = capital_design_projects.intersection(funded_projects)

print('__RESULT__:')
print(json.dumps({'count': len(matches), 'matches': list(matches)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
