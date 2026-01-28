code = """import json

key_f = locals()['var_function-call-6706861510607389059']
key_d = locals()['var_function-call-4954927585096532442']

with open(key_f, 'r') as f:
    fd = json.load(f)

with open(key_d, 'r') as f:
    cd = json.load(f)

funded = set()
for r in fd:
    if float(r['Amount']) > 50000:
        funded.add(r['Project_Name'].strip().lower())

extracted = set()
for d in cd:
    lines = d['text'].split('\n')
    active = False
    idx = 0
    while idx < len(lines):
        ln = lines[idx].strip()
        
        # Check start
        # breaking string to avoid parse error
        s1 = 'Capital Improvement Projects'
        s2 = 'Design'
        if s1 in ln and s2 in ln:
            active = True
            idx += 1
            continue
            
        if active:
            if s1 in ln and s2 not in ln:
                active = False
            if 'Disaster' in ln:
                active = False
                
        if active and ln:
            # filters
            if 'Page' not in ln and 'Agenda' not in ln and 'Updates' not in ln:
                # check ahead
                valid = False
                for k in range(1, 8):
                    if idx + k < len(lines):
                        nxt = lines[idx+k]
                        if 'Updates' in nxt or 'Description' in nxt:
                            valid = True
                            break
                if valid:
                    extracted.add(ln)
        idx += 1

cnt = 0
for p in extracted:
    if p.lower().strip() in funded:
        cnt += 1

print('__RESULT__:')
print(json.dumps({'count': cnt, 'extracted': list(extracted)}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)
