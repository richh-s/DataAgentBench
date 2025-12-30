code = """import json
import re

d_path = locals()['var_function-call-11529138748773800259']
f_path = locals()['var_function-call-6363168235283738913']

with open(d_path) as f: docs = json.load(f)
with open(f_path) as f: funds = json.load(f)

f_lookup = {x['Project_Name'].strip(): float(x['Amount']) for x in funds}
found = set()

# Separator construction
sep = chr(40) + "cid:190" + chr(41)

for d in docs:
    parts = d['text'].split(sep)
    for i in range(1, len(parts)):
        prev = parts[i-1]
        lines = [x.strip() for x in prev.split('\n') if x.strip()]
        
        name = None
        for l in reversed(lines):
            # Check for headers without using literals that might break?
            # Agenda, Page, Capital
            if "Agenda" in l or "Page" in l or "Capital" in l:
                continue
            name = l
            break
        
        if name and "park" in name.lower():
            content = parts[i]
            # Check completion
            if "2022" in content:
                # Regex
                if re.search(r"(completed|Construction:)[\w\s,]+2022", content, re.IGNORECASE):
                    found.add(name)

total = 0.0
matches = []
for fname, amt in f_lookup.items():
    for p in found:
        if fname.startswith(p):
            total += amt
            matches.append(fname)
            break

print("__RESULT__:")
print(json.dumps({"matches": matches, "total": total}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully', 'var_function-call-6770345336786910764': "'ovements\\n\\n(cid:190) Updates:\\n\\n(cid:131) '"}

exec(code, env_args)
