code = """import json

# keys
key_funding = locals()['var_function-call-6706861510607389059']
key_docs = locals()['var_function-call-4954927585096532442']

with open(key_funding, 'r') as f:
    funding = json.load(f)

with open(key_docs, 'r') as f:
    docs = json.load(f)

# Funding > 50k
valid_funding = set()
for x in funding:
    try:
        if float(x['Amount']) > 50000:
            valid_funding.add(x['Project_Name'].strip().lower())
    except:
        pass

# Parse
found_projects = []
for d in docs:
    txt = d['text']
    lines = txt.split('\n')
    mode = 0 # 0: scan, 1: capture
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check markers
        if 'Capital Improvement Projects (Design)' in line:
            mode = 1
            i += 1
            continue
            
        if mode == 1:
            # Check exit
            if 'Capital Improvement Projects' in line and '(Design)' not in line:
                mode = 0
            elif 'Disaster Recovery Projects' in line:
                mode = 0
        
        if mode == 1 and line:
            # Check if project
            # exclusions
            if 'Page ' not in line and 'Agenda Item' not in line and 'Updates:' not in line:
                # confirm
                is_p = False
                for k in range(1, 6):
                    if i + k < len(lines):
                        nx = lines[i+k]
                        if 'Updates:' in nx or 'Project Description:' in nx:
                            is_p = True
                            break
                if is_p:
                    found_projects.append(line)
        i += 1

# Count
cnt = 0
matched = []
unique_found = set(found_projects)
for p in unique_found:
    if p.lower().strip() in valid_funding:
        cnt += 1
        matched.append(p)

print('__RESULT__:')
print(json.dumps({'count': cnt, 'matches': matched}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)
