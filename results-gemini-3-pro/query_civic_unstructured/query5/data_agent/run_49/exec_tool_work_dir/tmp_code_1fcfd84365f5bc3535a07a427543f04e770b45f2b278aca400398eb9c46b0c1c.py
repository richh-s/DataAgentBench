code = """import json

with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    lines = doc.get('text', '').splitlines()
    current_section = "Unknown"
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        if "Capital Improvement Projects" in line:
            current_section = "Capital"
        elif "Disaster Recovery Projects" in line:
            current_section = "Disaster"
            
        is_new = False
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            if "Updates:" in nxt or "Project Description:" in nxt:
                if len(line) < 150 and "Page" not in line:
                    is_new = True
        
        if is_new:
            if current_project:
                projects.append(current_project)
            current_project = {
                "name": line,
                "section": current_section,
                "st": None,
                "raw_text_dates": [],
                "is_disaster": False
            }
            if current_section == "Disaster":
                current_project["is_disaster"] = True
            if "FEMA" in line or "CalOES" in line:
                current_project["is_disaster"] = True
                
        elif current_project:
            # Check for dates
            if "Begin Construction" in line:
                current_project["st"] = line
            
            if "2022" in line:
                current_project["raw_text_dates"].append(line)
                
            if "FEMA" in line or "CalOES" in line:
                current_project["is_disaster"] = True

    if current_project:
        projects.append(current_project)

# Summary
summary = []
for p in projects:
    summary.append({
        "name": p["name"],
        "section": p["section"],
        "is_disaster": p["is_disaster"],
        "st": p["st"],
        "dates_2022": p["raw_text_dates"]
    })

print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json', 'var_function-call-17193814516790891739': {'total': 0, 'projects': [], 'matched': []}, 'var_function-call-2668714204962722020': 'Done'}

exec(code, env_args)
