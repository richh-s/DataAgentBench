code = """import json
import re

d_path = locals()['var_function-call-11529138748773800259']
f_path = locals()['var_function-call-6363168235283738913']

with open(d_path) as f: docs = json.load(f)
with open(f_path) as f: funds = json.load(f)

f_lookup = {x['Project_Name'].strip(): float(x['Amount']) for x in funds}
found = set()

sep = chr(40) + "cid:190" + chr(41)
newline = chr(10)

for d in docs:
    parts = d['text'].split(sep)
    for i in range(1, len(parts)):
        prev = parts[i-1]
        lines = [x.strip() for x in prev.split(newline) if x.strip()]
        
        name = None
        for l in reversed(lines):
            if "Agenda" in l or "Page" in l or "Capital" in l:
                continue
            name = l
            break
        
        if name and "park" in name.lower():
            content = parts[i]
            if "2022" in content:
                # Regex without backslashes if possible, or raw string?
                # \w -> [a-zA-Z0-9_]
                # \s -> [ \t\n\r\f\v]
                # I'll use simple patterns
                # "completed ... 2022"
                # Check for "completed" index and "2022" index
                idx_comp = content.lower().find("completed")
                if idx_comp == -1:
                    idx_comp = content.lower().find("construction:")
                
                if idx_comp != -1:
                    # Check if 2022 follows within reasonable distance
                    sub = content[idx_comp:]
                    idx_2022 = sub.find("2022")
                    if idx_2022 != -1 and idx_2022 < 50:
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
