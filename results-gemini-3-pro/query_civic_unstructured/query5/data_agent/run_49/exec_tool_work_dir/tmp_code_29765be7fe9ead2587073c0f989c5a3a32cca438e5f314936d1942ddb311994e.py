code = """import json

with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

print("DEBUG: Parsing projects...")
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
        if "Disaster Recovery Projects" in line:
            current_section = "Disaster"
            
        # New project detection
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
                "dates": [],
                "is_disaster": False
            }
            if current_section == "Disaster":
                current_project["is_disaster"] = True
            if "FEMA" in line or "CalOES" in line:
                current_project["is_disaster"] = True
                
        elif current_project:
            # Capture any line with a year in it for debug
            if "2022" in line:
                current_project["dates"].append(line)
            
            if "Begin Construction" in line:
                parts = line.split(":")
                if len(parts) > 1:
                    current_project["st"] = parts[1].strip()
            
            if "FEMA" in line or "CalOES" in line or "Disaster" in line:
                current_project["is_disaster"] = True

    if current_project:
        projects.append(current_project)

print(f"DEBUG: Total projects found: {len(projects)}")
for p in projects:
    if "2022" in str(p["st"]) or "2022" in str(p["dates"]) or p["is_disaster"]:
        print(f"Project: {p['name']}")
        print(f"  Section: {p['section']}")
        print(f"  Is Disaster: {p['is_disaster']}")
        print(f"  Extracted Start: {p['st']}")
        print(f"  Lines with 2022: {p['dates']}")
        print("-" * 20)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json', 'var_function-call-17193814516790891739': {'total': 0, 'projects': [], 'matched': []}}

exec(code, env_args)
