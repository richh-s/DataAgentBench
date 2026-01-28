code = """import json
import pandas as pd

# Load keys
key_funding = 'var_function-call-14443830636332700640'
key_docs = 'var_function-call-14443830636332701107'

funding_path = locals()[key_funding]
docs_path = locals()[key_docs]

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(float)

# Helper to clean names
def clean_name(n):
    if '(' in n:
        parts = n.split('(')
        if parts[-1].strip().endswith(')'):
            return '('.join(parts[:-1]).strip()
    return n.strip()

# Build map
project_map = {}
for i, row in df_funding.iterrows():
    fname = row['Project_Name']
    bname = clean_name(fname)
    if bname not in project_map:
        project_map[bname] = []
    project_map[bname].append(row)

base_names = list(project_map.keys())
all_names = list(df_funding['Project_Name'].unique())

# Parse text
results = []
for doc in docs_data:
    lines = doc['text'].split('\n')
    curr_proj = None
    curr_text = []
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if line is header
        found_name = None
        if line_clean in base_names:
            found_name = line_clean
        elif line_clean in all_names:
            found_name = clean_name(line_clean)
            
        if found_name:
            if curr_proj:
                results.append({'name': curr_proj, 'lines': curr_text})
            curr_proj = found_name
            curr_text = []
        else:
            if curr_proj:
                curr_text.append(line_clean)
                
    if curr_proj:
        results.append({'name': curr_proj, 'lines': curr_text})

# Analyze
qualified_projects = set()
disaster_keys = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Fire', 'Disaster', 'Emergency']

for r in results:
    p_name = r['name']
    lines = r['lines']
    
    # Check 2022 start
    started_2022 = False
    for l in lines:
        l_low = l.lower()
        if 'begin construction' in l_low or 'advertise' in l_low:
            if '2022' in l:
                started_2022 = True
                break
                
    if started_2022:
        # Check disaster
        is_disaster = False
        # Text check
        full_text = ' '.join(lines)
        for k in disaster_keys:
            if k in full_text:
                is_disaster = True
                break
                
        # Funding name check
        if not is_disaster:
            f_recs = project_map.get(p_name, [])
            for fr in f_recs:
                if 'FEMA' in fr['Project_Name'] or 'CalOES' in fr['Project_Name']:
                    is_disaster = True
                    break
        
        if is_disaster:
            qualified_projects.add(p_name)

# Sum
total = 0.0
for qp in qualified_projects:
    recs = project_map.get(qp, [])
    for r in recs:
        total += r['Amount']

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': list(qualified_projects)}))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)
