code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-13970698935459151877'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)
df_funding_grouped = df_funding.groupby('Project_Name')['Amount'].sum().reset_index()
funded_projects = set(df_funding_grouped[df_funding_grouped['Amount'] > 50000]['Project_Name'])

# Load civic docs
with open(locals()['var_function-call-13579203068557831030'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    in_capital_design = False
    
    for line in lines:
        stripped = line.strip()
        
        if 'Capital Improvement Projects (Design)' in stripped:
            in_capital_design = True
            continue
        elif 'Capital Improvement Projects (' in stripped and 'Design' not in stripped:
            in_capital_design = False
            continue
        elif 'Disaster Recovery Projects' in stripped:
            in_capital_design = False
            continue
        
        if in_capital_design:
            if not stripped: continue
            # Filter noise
            if stripped.startswith('(cid:') or stripped.startswith('Updates:') or stripped.startswith('Project Schedule:'): continue
            if stripped.startswith('Page ') or stripped.startswith('Agenda Item') or stripped.startswith('Subject:') or stripped.startswith('Date prepared:'): continue
            if stripped.startswith('Complete Design') or stripped.startswith('Advertise') or stripped.startswith('Begin Construction') or stripped.startswith('Final Design'): continue
            if 'Project Description' in stripped or 'Project Updates' in stripped or 'Estimated Schedule' in stripped: continue
            
            # Additional heuristic: Project name shouldn't be too long or contain many params
            # But let's trust the structure first
            capital_design_projects.add(stripped)

result_projects = capital_design_projects.intersection(funded_projects)
count = len(result_projects)

print('__RESULT__:')
print(json.dumps({'count': count, 'matches': list(result_projects), 'found_design': list(capital_design_projects)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
