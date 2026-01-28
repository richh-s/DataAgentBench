code = """import json

key_f = locals()["var_function-call-6706861510607389059"]
key_d = locals()["var_function-call-4954927585096532442"]

with open(key_f, "r") as f:
    fd = json.load(f)

with open(key_d, "r") as f:
    cd = json.load(f)

funded = set()
for r in fd:
    try:
        if float(r["Amount"]) > 50000:
            funded.add(r["Project_Name"].strip().lower())
    except:
        pass

extracted = set()
newline = chr(10)
for d in cd:
    lines = d["text"].split(newline)
    active = False
    idx = 0
    while idx < len(lines):
        ln = lines[idx].strip()
        
        if "Capital Improvement Projects" in ln and "Design" in ln:
            active = True
            idx += 1
            continue
        
        if active:
            if "Capital Improvement Projects" in ln and "Design" not in ln:
                active = False
            if "Disaster" in ln:
                active = False
        
        if active and ln:
            if "Page" not in ln and "Agenda" not in ln and "Updates" not in ln and "Schedule" not in ln:
                valid = False
                for k in range(1, 6):
                    if idx + k < len(lines):
                        nxt = lines[idx+k]
                        if "Updates" in nxt or "Description" in nxt:
                            valid = True
                            break
                if valid:
                    extracted.add(ln)
        idx += 1

cnt = 0
matches = []
for p in extracted:
    if p.lower().strip() in funded:
        cnt += 1
        matches.append(p)

print("__RESULT__:")
print(json.dumps({"count": cnt, "matches": matches}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)
