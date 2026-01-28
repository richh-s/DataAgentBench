code = """import json, re

# Load mongo docs
res = var_call_MIofTe0n8KOLSWwt31iMnvsM
if isinstance(res, str):
    import pathlib
    p = pathlib.Path(res)
    docs = json.loads(p.read_text())
else:
    docs = res

projects = []

# Patterns
status_pat = re.compile(r'^(?P<name>.+?)\n\n\(cid:190\) Updates:\s*(?P<updates>.*?)(?=\n\n[A-Z][^\n]*\n|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\Z)', re.S|re.M)
completed_pat = re.compile(r'(?i)\b(completed|construction was completed)\b')
park_pat = re.compile(r'(?i)\bpark\b')
y2022_pat = re.compile(r'(?i)\b(2022)\b')

for d in docs:
    text = d.get('text','')
    for m in status_pat.finditer(text):
        name = m.group('name').strip()
        block = m.group(0)
        updates = m.group('updates')
        if not completed_pat.search(updates):
            continue
        if not park_pat.search(name) and not park_pat.search(block):
            continue
        # completed in 2022: look for 'November 2022' etc near completion phrase
        if not re.search(r'(?i)completed\s+(in\s+)?(\w+\s+)?2022', block) and not re.search(r'(?i)completed\s*,?\s*(\w+\s+)?2022', block) and not re.search(r'(?i)completed\s+\w+\s+2022', block):
            # fallback: any 2022 in same block
            if not y2022_pat.search(block):
                continue
        projects.append({'Project_Name': name})

# Deduplicate
seen=set(); uniq=[]
for p in projects:
    n=p['Project_Name']
    if n not in seen:
        seen.add(n); uniq.append(p)

print('__RESULT__:')
print(json.dumps(uniq))"""

env_args = {'var_call_1mgfrIM9pU0UjpbLFEUhUinP': ['Funding'], 'var_call_4IxugqawmZ4fkQ7HkP3qZkcJ': ['civic_docs'], 'var_call_MIofTe0n8KOLSWwt31iMnvsM': 'file_storage/call_MIofTe0n8KOLSWwt31iMnvsM.json'}

exec(code, env_args)
