code = """import json
import re

p_docs = locals()['var_function-call-11529138748773800259']
p_fund = locals()['var_function-call-6363168235283738913']

with open(p_docs, 'r') as f:
    docs = json.load(f)
with open(p_fund, 'r') as f:
    funds = json.load(f)

f_map = {x['Project_Name'].strip(): float(x['Amount']) for x in funds}

found = set()
sep = "(cid:190)"

for d in docs:
    txt = d['text']
    chunks = txt.split(sep)
    
    # Simple parser: just look for 'Park' in the chunk preceding completion info?
    # No, name is in chunk i-1, info in chunk i.
    
    # Loop chunks
    for i in range(1, len(chunks)):
        prev = chunks[i-1]
        curr = chunks[i]
        
        # Extract name from prev
        # Last non-empty line
        ls = [x.strip() for x in prev.split('\n') if x.strip()]
        if not ls: continue
        
        # Filter headers from ls reversed
        name = None
        for l in reversed(ls):
            if 'Agenda' in l or 'Page' in l or 'Capital' in l:
                continue
            name = l
            break
        
        if not name: continue
        
        # Check Park
        if 'park' in name.lower():
            # Check completion in curr
            # pattern: completed ... 2022
            if '2022' in curr:
                if re.search(r'(completed|Construction:)[\w\s,]+2022', curr, re.IGNORECASE):
                    found.add(name)

total = 0.0
matched = []
for f_name, amt in f_map.items():
    # check against found
    for p in found:
        if f_name.startswith(p):
            total += amt
            matched.append(f_name)
            break

print('__RESULT__:')
print(json.dumps({'projects': matched, 'total': total}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully', 'var_function-call-6770345336786910764': "'ovements\\n\\n(cid:190) Updates:\\n\\n(cid:131) '"}

exec(code, env_args)
