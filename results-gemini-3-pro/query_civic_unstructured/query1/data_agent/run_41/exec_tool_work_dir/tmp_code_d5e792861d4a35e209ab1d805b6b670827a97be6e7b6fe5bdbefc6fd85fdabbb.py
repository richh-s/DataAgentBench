code = """import json

# Load funding data
with open(locals()['var_function-call-11382907056012316849'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11382907056012318432'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()
debug_log = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    in_design_section = False
    design_marker = "Capital Improvement Projects (Design)"
    stop_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Agenda Item"
    ]
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if design_marker in line:
            in_design_section = True
            i += 1
            continue
            
        if in_design_section:
            if any(marker in line for marker in stop_markers):
                in_design_section = False
                break
            
            if not line:
                i += 1
                continue
            
            # Skip metadata/bullets
            if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda") or line.startswith("Subject:") or line.startswith("Date prepared:"):
                i += 1
                continue
            
            # Look ahead for "Updates:" or bullet
            is_project = False
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if not next_line:
                    j += 1
                    continue
                if next_line.startswith("(cid:") or "Updates:" in next_line:
                    is_project = True
                break
            
            if is_project:
                capital_design_projects.add(line.strip())
        
        i += 1

# Filter funding
funded_high = {}
for item in funding_data:
    try:
        amt = float(item['Amount'])
    except:
        amt = 0
    if amt > 50000:
        funded_high[item['Project_Name']] = amt

# Matching
matches = []
# Try direct match
for proj in capital_design_projects:
    if proj in funded_high:
        matches.append(proj)
    else:
        # Check for fuzzy
        # Check if any db project is a substring of extracted project or vice versa
        found = False
        for db_proj in funded_high:
            if db_proj == proj:
                matches.append(proj)
                found = True
                break
            # Logic: if the DB name is "Clover Heights Storm Drain" and text is "Clover Heights Storm Drainage Improvements",
            # then DB name is contained in Text name (mostly).
            # But "Storm Drain" is in "Storm Drainage".
            # Let's check if the main words overlap?
            # Or simplified: if one is substring of other
            if db_proj in proj and len(db_proj) > 10: # avoid short matches
                matches.append(db_proj) # Add the DB name to matches
                found = True
                break
            if proj in db_proj and len(proj) > 10:
                matches.append(db_proj)
                found = True
                break
        if not found:
            debug_log.append(f"Unmatched extracted: {proj}")

print("__RESULT__:")
print(json.dumps({
    "extracted_projects": list(capital_design_projects),
    "matches": list(set(matches)),
    "match_count": len(set(matches)),
    "unmatched": debug_log
}))"""

env_args = {'var_function-call-11382907056012316849': 'file_storage/function-call-11382907056012316849.json', 'var_function-call-11382907056012318432': 'file_storage/function-call-11382907056012318432.json'}

exec(code, env_args)
