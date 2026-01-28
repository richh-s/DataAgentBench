code = """import json

# Load data
with open(locals()['var_function-call-8970245157857899516'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-8970245157857899203'], 'r') as f:
    funding_data = json.load(f)

# Build funding map
project_funding = {}
for row in funding_data:
    p_name = row['Project_Name'].strip()
    amount = float(row['Amount'])
    key = p_name.lower()
    if key not in project_funding:
        project_funding[key] = 0.0
    project_funding[key] += amount

# Extract projects
all_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    project_starts = []
    
    for i, line in enumerate(lines):
        line_s = line.strip()
        # Use single quotes to avoid JSON escaping hell
        if '(cid:190)' in line_s and ('Updates' in line_s or 'Project Description' in line_s):
            k = i - 1
            while k >= 0:
                if lines[k].strip():
                    name = lines[k].strip()
                    if 'Capital Improvement Projects' not in name:
                        project_starts.append({'line_idx': k, 'name': name})
                    break
                k -= 1
                
    for i in range(len(project_starts)):
        p = project_starts[i]
        start_line = p['line_idx']
        if i < len(project_starts) - 1:
            end_line = project_starts[i+1]['line_idx']
        else:
            end_line = len(lines)
            
        p_text = '\n'.join(lines[start_line:end_line])
        all_projects.append({'name': p['name'], 'text': p_text})

# Filter
completed_park_projects = set()
for p in all_projects:
    name = p['name']
    text_content = p['text'].lower()
    
    if 'park' in name.lower():
        # Check completion in 2022
        if 'construction was completed' in text_content and '2022' in text_content:
             completed_park_projects.add(name)
        elif 'construction completed' in text_content and '2022' in text_content:
             completed_park_projects.add(name)
        elif 'complete construction: november 2022' in text_content:
             completed_park_projects.add(name)

# Sum funding
total_funding = 0.0
matched = []

for p_name in completed_park_projects:
    key = p_name.strip().lower()
    if key in project_funding:
        amount = project_funding[key]
        total_funding += amount
        matched.append({'name': p_name, 'amount': amount})
    else:
        found = False
        for f_key in project_funding:
            # simple substring match
            if key == f_key: 
                amount = project_funding[f_key]
                total_funding += amount
                matched.append({'name': p_name, 'match': f_key, 'amount': amount})
                found = True
        if not found:
            # Try containment
             for f_key in project_funding:
                if key in f_key or f_key in key:
                     amount = project_funding[f_key]
                     total_funding += amount
                     matched.append({'name': p_name, 'match': f_key, 'amount': amount})
                     found = True
                     break

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects': matched}))"""

env_args = {'var_function-call-8970245157857899516': 'file_storage/function-call-8970245157857899516.json', 'var_function-call-8970245157857899203': 'file_storage/function-call-8970245157857899203.json'}

exec(code, env_args)
