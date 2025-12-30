code = """import json

# Load funding data
with open(locals()['var_function-call-6706861510607389059'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-4954927585096532442'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding > 50k
funded_projects_high = set()
for rec in funding_data:
    try:
        if float(rec['Amount']) > 50000:
            funded_projects_high.add(rec['Project_Name'].strip().lower())
    except:
        pass

extracted_projects = set()

for doc in civic_docs:
    lines = doc['text'].split('\n')
    capture = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect Start of Section
        if "Capital Improvement Projects (Design)" in line:
            capture = True
            i += 1
            continue
            
        # Detect End of Section (other sections)
        if capture:
            if "Capital Improvement Projects (" in line and "Design" not in line:
                capture = False
            elif "Disaster Recovery Projects" in line:
                capture = False
                
        if capture and line:
            # Heuristic to identify project name line
            # It shouldn't be a metadata line
            if not line.startswith("(") and not line.startswith("Page") and "Agenda Item" not in line and "Updates:" not in line and "Project Schedule" not in line and "Estimated Schedule" not in line:
                # Look ahead to confirm it is a project title
                # usually followed (eventually) by "(cid:190) Updates:" or similar
                is_project = False
                for offset in range(1, 10): # look ahead up to 10 lines
                    if i + offset < len(lines):
                        nxt = lines[i+offset].strip()
                        if "Updates:" in nxt or "Project Description:" in nxt or "(cid:190)" in nxt:
                            is_project = True
                            break
                        # If we hit another likely project name or section header, stop
                        # But this is hard to distinguish from just text.
                        # However, the structure is usually Title -> Updates.
                
                if is_project:
                    extracted_projects.add(line.strip())
        
        i += 1

# Matching
# We compare extracted names (lower case) with funded names (lower case)
count = 0
matched_list = []

for proj in extracted_projects:
    p_lower = proj.lower()
    # Direct match check
    if p_lower in funded_projects_high:
        count += 1
        matched_list.append(proj)
    else:
        # Check for partial match / fuzzy?
        # The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
        # So we should expect exact matches or very close.
        # Let's check if the project name from text is contained in funding db or vice versa?
        # "Birdview Avenue Improvements" vs "Birdview Avenue Improvements"
        pass

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "matches": matched_list,
    "extracted_preview": list(extracted_projects),
    "funded_preview": list(funded_projects_high)[:10]
}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)
