code = """import json
import pandas as pd

k_fund = 'var_function-call-13970698935459151877'
k_docs = 'var_function-call-13579203068557831030'

with open(locals()[k_fund], 'r') as f:
    funding_data = json.load(f)
with open(locals()[k_docs], 'r') as f:
    civic_docs = json.load(f)

df = pd.DataFrame(funding_data)
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
df_grp = df.groupby('Project_Name')['Amount'].sum().reset_index()
funded_projects = set(df_grp[df_grp['Amount'] > 50000]['Project_Name'])

design_projects = set()

for doc in civic_docs:
    lines = doc['text'].splitlines()
    active = False
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        if line.startswith('Capital Improvement Projects (Design)'):
            active = True
            continue
        elif line.startswith('Capital Improvement Projects ('):
            active = False
            continue
        elif line.startswith('Disaster Recovery Projects'):
            active = False
            continue
            
        if active:
            if line.startswith('(') or line.startswith('Updates:') or line.startswith('Project Schedule:'): continue
            if line.startswith('Page ') or line.startswith('Agenda Item'): continue
            if line.startswith('Subject:') or line.startswith('Date prepared:'): continue
            if line.startswith('Complete Design') or line.startswith('Advertise') or line.startswith('Begin Construction') or line.startswith('Final Design'): continue
            if 'Project Description' in line or 'Project Updates' in line or 'Estimated Schedule' in line: continue
            
            design_projects.add(line)

matches = design_projects.intersection(funded_projects)
print('__RESULT__:')
print(json.dumps({'count': len(matches), 'matches': list(matches), 'debug_design': list(design_projects)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json', 'var_function-call-2811273710514033903': 276, 'var_function-call-3826532956400393597': 5, 'var_function-call-16108733464645405896': 23}

exec(code, env_args)
