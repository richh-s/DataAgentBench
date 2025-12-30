code = """import json

funding_key = 'var_function-call-3513875169581502759'
civic_key = 'var_function-call-3513875169581504334'

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for record in funding_data:
    name = record['Project_Name'].strip()
    try:
        amount = float(record['Amount'])
    except:
        amount = 0.0
    if name not in funding_map:
        funding_map[name] = 0.0
    funding_map[name] += amount

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Capital Improvement Projects (Design)" in line:
            current_section = "DESIGN"
            i += 1
            continue
        
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            current_section = None
        
        if current_section == "DESIGN":
            if not line:
                i += 1
                continue
            
            # Skip noise
            if line.startswith("Page ") or "Agenda Item" in line:
                i += 1
                continue
            if "(cid:" in line:
                i += 1
                continue
            if "Updates:" in line or "Project Schedule:" in line:
                i += 1
                continue
            
            # Look ahead to confirm it is a project
            is_valid = False
            for offset in range(1, 6):
                if i + offset >= len(lines):
                    break
                nxt = lines[i+offset].strip()
                if not nxt:
                    continue
                if "(cid:" in nxt:
                    if "Updates" in nxt or "Description" in nxt or "Project" in nxt or "Schedule" in nxt:
                        is_valid = True
                    break
                else:
                    if "Agenda Item" in nxt or "Page " in nxt:
                        continue
                    break
            
            if is_valid:
                capital_design_projects.add(line)
        
        i += 1

count = 0
matches = []
for proj in capital_design_projects:
    if proj in funding_map:
        if funding_map[proj] > 50000:
            count += 1
            matches.append(proj)

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted": list(capital_design_projects)}))"""

env_args = {'var_function-call-3513875169581502759': 'file_storage/function-call-3513875169581502759.json', 'var_function-call-3513875169581504334': 'file_storage/function-call-3513875169581504334.json'}

exec(code, env_args)
