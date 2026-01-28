code = """import json
import re

# Load data
with open(locals()['var_function-call-10071465858978758167'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-10071465858978756684'], 'r') as f:
    funding_data = json.load(f)

# Build Funding Lookup
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    amount = item['Amount']
    funding_map[name] = amount
    funding_map[name.lower()] = amount

projects_found = {}

# Patterns
# Spring 2022: Spring 2022, March 2022, April 2022, May 2022
# Start keywords: Begin Construction, Start, Estimated Schedule
date_patterns = [
    r"spring 2022",
    r"march 2022",
    r"april 2022",
    r"may 2022",
    r"03/2022",
    r"04/2022",
    r"05/2022"
]

def check_spring_2022(text):
    text = text.lower()
    for pat in date_patterns:
        if pat in text:
            return True
    return False

# Scan documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Check if line is a project name
        # We can check if it exists in funding_map (case insensitive)
        if line.lower() in funding_map:
            current_project = line.strip()
            # If found in funding, use the casing from funding map if possible? 
            # Actually, just keep the text string for now.
        
        elif len(line) > 5 and not line.startswith("(") and "Agenda" not in line and "Page" not in line:
            # Heuristic: if next line is "Updates:" or similar
            if i+1 < len(lines):
                next_l = lines[i+1].strip()
                if "Updates:" in next_l or "Project Schedule" in next_l or "Project Description" in next_l:
                    current_project = line.strip()
            # Or if i+2 has it (sometimes blank line in betweeen)
            elif i+2 < len(lines):
                next_l = lines[i+2].strip()
                if "Updates:" in next_l or "Project Schedule" in next_l or "Project Description" in next_l:
                    current_project = line.strip()

        if current_project:
            # Check for start date in this line
            # Look for "Begin Construction" AND Spring 2022
            if "begin construction" in line.lower() or "start" in line.lower():
                if check_spring_2022(line):
                    projects_found[current_project] = line
            
            # Also, sometimes the date is on the next line after "Begin Construction:"?
            # e.g. "(cid:131) Begin Construction:\nSpring 2022"
            if "begin construction" in line.lower() and ":" in line:
                # check if date is not in line, look at next line
                if not any(char.isdigit() for char in line) and "Spring" not in line and "Fall" not in line:
                     if i+1 < len(lines):
                         next_l = lines[i+1].strip()
                         if check_spring_2022(next_l):
                             projects_found[current_project] = next_l

# Calculate totals
matched_projects = []
total_funding = 0
seen_projects = set()

for proj_name, context in projects_found.items():
    # Normalize name for matching
    # Remove extra spaces
    norm_name = " ".join(proj_name.split())
    
    # Try exact or lower match
    amt = funding_map.get(norm_name)
    if not amt:
        amt = funding_map.get(norm_name.lower())
    
    # If still not found, try fuzzy? 
    # e.g. "Latigo Canyon Road Retaining Wall Repair Project" vs "Latigo Canyon Road Retaining Wall Repair"
    # For now, strict match or print missing
    
    if amt is not None:
        if norm_name not in seen_projects:
            matched_projects.append({"name": norm_name, "amount": amt, "context": context})
            total_funding += amt
            seen_projects.add(norm_name)

print("__RESULT__:")
print(json.dumps({"count": len(matched_projects), "total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-600716714873686583': ['Funding'], 'var_function-call-600716714873684502': 'file_storage/function-call-600716714873684502.json', 'var_function-call-10071465858978756684': 'file_storage/function-call-10071465858978756684.json', 'var_function-call-10071465858978758167': 'file_storage/function-call-10071465858978758167.json'}

exec(code, env_args)
