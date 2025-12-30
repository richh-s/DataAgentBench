code = """import json
import pandas as pd

# Load Funding
with open(locals()['var_function-call-4014968237340428108'], 'r') as f:
    funding = json.load(f)
df = pd.DataFrame(funding)
names = set(df['Project_Name'].unique())

# Load Docs
with open(locals()['var_function-call-4014968237340429633'], 'r') as f:
    docs = json.load(f)

# Parse
projects = []
for d in docs:
    lines = d['text'].split('\n')
    curr = None
    buf = []
    
    for line in lines:
        l = line.strip()
        if not l: continue
        
        # Identification
        found = None
        for n in names:
            if n.lower() == l.lower():
                found = n
                break
        
        if found:
            if curr:
                projects.append({'name': curr, 'data': " ".join(buf)})
            curr = found
            buf = []
        elif curr:
            buf.append(l)
            
    if curr:
        projects.append({'name': curr, 'data': " ".join(buf)})

# Filter
final = []
for p in projects:
    n = p['name']
    d = p['data'].lower()
    
    # Topic
    if 'park' not in n.lower() and 'park' not in d:
        continue
        
    # Completion
    # Check for "completed" and "2022"
    if 'completed' in d and '2022' in d:
        # Refine to avoid Design completion
        if 'construction' in d:
            if 'construction was completed' in d or 'complete construction' in d:
                 final.append(n)
        else:
            # If construction word not present, assume completed refers to project
            final.append(n)

final = list(set(final))

total = 0
recs = []
for n in final:
    sub = df[df['Project_Name'] == n]
    amt = sub['Amount'].sum()
    total += amt
    recs.append({'name': n, 'amt': amt})

print("__RESULT__:")
print(json.dumps({'projects': recs, 'total': int(total)}))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json'}

exec(code, env_args)
