code = """import json
import re

d_path = locals()['var_function-call-11529138748773800259']
f_path = locals()['var_function-call-6363168235283738913']

with open(d_path) as f: docs = json.load(f)
with open(f_path) as f: funds = json.load(f)

f_lookup = {x['Project_Name'].strip(): x['Amount'] for x in funds}
found_projects = set()

for d in docs:
    parts = d['text'].split('(cid:190)')
    for i in range(1, len(parts)):
        # Name is in previous part
        prev_lines = parts[i-1].strip().split('\n')
        name = "Unknown"
        # Find last line that isn't a header
        for l in reversed(prev_lines):
            l = l.strip()
            if not l: continue
            # Avoid headers
            if l.startswith('Capital') or l.startswith('Agenda') or l.startswith('Page'):
                continue
            name = l
            break
        
        content = parts[i]
        # Check park
        if 'park' in name.lower():
            # Check completion 2022
            if '2022' in content and ('completed' in content.lower() or 'construction:' in content.lower()):
                 # stricter check
                 if re.search(r'(completed|Construction:)[\w\s,]+2022', content, re.IGNORECASE):
                     found_projects.add(name)

total = 0.0
matches = []
for fname, amt in f_lookup.items():
    for p in found_projects:
        # Match logic: fname starts with p
        if fname.startswith(p):
            total += float(amt)
            matches.append(fname)
            break

print('__RESULT__:')
print(json.dumps({'p': matches, 't': total}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully', 'var_function-call-6770345336786910764': "'ovements\\n\\n(cid:190) Updates:\\n\\n(cid:131) '"}

exec(code, env_args)
