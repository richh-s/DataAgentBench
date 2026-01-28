code = """import json

# Load funding data
with open(locals()['var_function-call-6706861510607389059'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-4954927585096532442'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding > 50k
funded_set = set()
for r in funding_data:
    try:
        if float(r['Amount']) > 50000:
            funded_set.add(r['Project_Name'].strip().lower())
    except:
        pass

extracted = set()

for d in civic_docs:
    lines = d['text'].split('\n')
    capturing = False
    
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        
        # Start capture
        if "Capital Improvement Projects" in line and "(Design)" in line:
            capturing = True
            idx += 1
            continue
            
        # Stop capture
        if capturing:
            if "Capital Improvement Projects" in line and "(Design)" not in line:
                capturing = False
            if "Disaster Recovery Projects" in line:
                capturing = False
        
        if capturing and line:
            # Check if valid project line
            # Not a bullet, not empty, not Page X of Y
            if "Page" not in line and "Agenda" not in line and "Updates:" not in line and "Schedule" not in line and not line.startswith("("):
                # Verify
                valid = False
                for offset in range(1, 8):
                    if idx + offset < len(lines):
                        nxt = lines[idx+offset]
                        if "Updates:" in nxt or "Project Description:" in nxt:
                            valid = True
                            break
                if valid:
                    extracted.add(line)
        
        idx += 1

# Count matches
match_count = 0
matches = []

for p in extracted:
    if p.strip().lower() in funded_set:
        match_count += 1
        matches.append(p)

print("__RESULT__:")
print(json.dumps({"count": match_count, "matches": matches}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)
