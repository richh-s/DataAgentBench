code = """import json

d_path = locals()['var_function-call-11529138748773800259']
f_path = locals()['var_function-call-6363168235283738913']

with open(d_path) as f: docs = json.load(f)
with open(f_path) as f: funds = json.load(f)

f_lookup = {x['Project_Name'].strip(): float(x['Amount']) for x in funds}
candidates = []

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
        
        if name:
            content = parts[i]
            c_lower = content.lower()
            
            # Check completion in 2022
            idx = c_lower.find("completed")
            if idx == -1:
                idx = c_lower.find("construction:")
            
            if idx != -1:
                sub = c_lower[idx:idx+50]
                if "2022" in sub:
                    # Found a completed project. Check if park related.
                    is_park = "park" in name.lower() or "park" in c_lower
                    candidates.append({"name": name, "is_park": is_park, "context": sub})

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully', 'var_function-call-6770345336786910764': "'ovements\\n\\n(cid:190) Updates:\\n\\n(cid:131) '", 'var_function-call-10634271001682805926': {'matches': ['Bluffs Park Shade Structure'], 'total': 21000.0}}

exec(code, env_args)
