code = """import json

# Load funding data
with open('var_function-call-12694910972065598501.json') as f:
    funding_data = json.load(f)

high_funding_names = set()
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            high_funding_names.add(row['Project_Name'].strip())
    except:
        pass

# Load docs
with open('var_function-call-14720826093064389612.json') as f:
    docs = json.load(f)

found_projects = set()
# Debug: list of found names before filtering
debug_found_names = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    start_idx = -1
    for i, line in enumerate(lines):
        if "Capital Improvement Projects (Design)" in line:
            start_idx = i
            break
    
    if start_idx != -1:
        # Collect lines until next section
        section_lines = []
        for i in range(start_idx + 1, len(lines)):
            line = lines[i].strip()
            if "Capital Improvement Projects (" in line or "Disaster Recovery Projects" in line:
                break
            section_lines.append(line)
        
        current_candidate = None
        for line in section_lines:
            if not line:
                continue
            
            # Identify metadata markers
            # Note: (cid:xxx) might be represented differently depending on encoding, but let's look for (cid:
            # Also "Updates:", "Project Schedule:", etc.
            is_metadata = False
            if line.startswith("(cid:") or "Updates:" in line or "Project Schedule" in line or "Estimated Schedule" in line or "Project Description" in line or "Recommended Action" in line:
                is_metadata = True
            
            # Filter out page numbers or agenda items which might appear in the middle
            if line.startswith("Page ") or line.startswith("Agenda Item"):
                continue
                
            if is_metadata:
                if current_candidate:
                    # Clean the candidate name
                    name = current_candidate.strip()
                    # Heuristic: Project names are usually Title Case and reasonably long
                    if len(name) > 3: 
                        found_projects.add(name)
                        debug_found_names.append(name)
                    current_candidate = None
            else:
                # Possible project name
                current_candidate = line

# Find intersection
matches = []
for proj in found_projects:
    if proj in high_funding_names:
        matches.append(proj)

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": matches, "found_names_sample": list(found_projects)[:10]}))"""

env_args = {'var_function-call-12694910972065598501': 'file_storage/function-call-12694910972065598501.json', 'var_function-call-12694910972065599408': 'file_storage/function-call-12694910972065599408.json', 'var_function-call-14720826093064389612': 'file_storage/function-call-14720826093064389612.json'}

exec(code, env_args)
