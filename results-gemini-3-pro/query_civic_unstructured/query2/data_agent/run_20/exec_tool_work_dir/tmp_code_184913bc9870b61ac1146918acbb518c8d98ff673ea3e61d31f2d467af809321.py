code = """import json
import re

# Load
path_docs = locals()['var_function-call-11529138748773800259']
path_fund = locals()['var_function-call-6363168235283738913']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
with open(path_fund, 'r') as f:
    funding_data = json.load(f)

# Funding Map
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name'].strip()] = float(item['Amount'])

# Logic
matches = set()
bullet = "(cid:190)"

for doc in civic_docs:
    text = doc['text']
    parts = text.split(bullet)
    
    current_proj = None
    
    # Part 0
    p0 = parts[0].strip()
    if p0:
        lines = [l.strip() for l in p0.split('\n') if l.strip()]
        # Get last valid line
        for line in reversed(lines):
            if "Capital" not in line and "Agenda" not in line and "Page" not in line:
                current_proj = line
                break
    
    proj_contents = {}
    
    for i in range(1, len(parts)):
        chunk = parts[i]
        
        # Assign chunk to current project
        if current_proj:
            if current_proj not in proj_contents:
                proj_contents[current_proj] = ""
            proj_contents[current_proj] += " " + chunk
            
        # Find next project
        lines = [l.strip() for l in chunk.strip().split('\n') if l.strip()]
        candidate = None
        for line in reversed(lines):
            # Known content lines
            if "Updates:" in line or "Schedule:" in line or "Construction:" in line or "Design:" in line:
                break
            # Headers
            if "Agenda" in line or "Page" in line:
                continue
            if len(line) < 100 and not line.endswith('.'):
                candidate = line
                break
        
        if candidate:
            current_proj = candidate

    # Check criteria
    for name, content in proj_contents.items():
        if "park" in name.lower():
            # Check 2022 completion
            # Patterns: "completed November 2022", "Complete Construction: ... 2022"
            if re.search(r"completed[\w\s,]+2022", content, re.IGNORECASE):
                matches.add(name)
            elif re.search(r"Complete Construction[\w\s,:]+2022", content, re.IGNORECASE):
                matches.add(name)

# Sum funding
total_funding = 0.0
matched_funding_names = []

# List of matched project names from docs
doc_projects = list(matches)

# Iterate funding DB
for fname, amount in funding_map.items():
    # Check if fname relates to any doc_project
    # e.g. doc_project = "Bluffs Park Shade Structure"
    # fname = "Bluffs Park Shade Structure" or "Bluffs Park Shade Structure (FEMA)"
    
    for dp in doc_projects:
        # Check if dp matches fname (ignoring parens in fname)
        # Or just startswith
        if fname.startswith(dp):
            # Check boundary?
            # If dp is "Park", fname "Parker" -> startswith matches.
            # But dp is "Bluffs Park Shade Structure" -> safe.
            matched_funding_names.append(fname)
            total_funding += amount
            break # Count this funding record once
        elif dp.startswith(fname):
             # fname "Project A", dp "Project A Phase 2"?
             # Usually funding is more granular or has suffixes.
             matched_funding_names.append(fname)
             total_funding += amount
             break

print("__RESULT__:")
print(json.dumps({"projects": matched_funding_names, "total": total_funding}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully', 'var_function-call-6770345336786910764': "'ovements\\n\\n(cid:190) Updates:\\n\\n(cid:131) '"}

exec(code, env_args)
