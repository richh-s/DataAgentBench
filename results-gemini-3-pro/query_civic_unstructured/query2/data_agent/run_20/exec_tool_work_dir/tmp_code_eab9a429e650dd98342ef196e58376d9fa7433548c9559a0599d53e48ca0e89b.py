code = """import json
import re

# Load data
with open(locals()['var_function-call-11529138748773800259'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6363168235283738913'], 'r') as f:
    funding_data = json.load(f)

funding_lookup = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

matched_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by bullet
    parts = text.split('(cid:190)')
    
    # Identify the first project name
    current_project = None
    if parts[0].strip():
        lines = parts[0].strip().split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        # Filter headers
        headers = ["Capital Improvement Projects", "Agenda Item", "Page ", "Prepared by", "Approved by", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]
        
        # Take the last line that doesn't look like a header
        for line in reversed(lines):
            is_header = False
            for h in headers:
                if h in line:
                    is_header = True
                    break
            if not is_header:
                current_project = line
                break
    
    projects_found = {} # Name -> list of text chunks

    for i in range(1, len(parts)):
        chunk = parts[i]
        
        # Add chunk to current project
        if current_project:
            if current_project not in projects_found:
                projects_found[current_project] = ""
            projects_found[current_project] += " " + chunk
        
        # Determine next project name
        lines = chunk.strip().split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        
        candidate = None
        for line in reversed(lines):
            # Stop if we hit a known content indicator
            if "Updates:" in line or "Schedule:" in line or "Construction:" in line or "Design:" in line:
                break
            if "Agenda Item" in line or "Page " in line or "Capital Improvement Projects" in line:
                continue
            
            # If it looks like a name (not ending in period, reasonably short)
            if not line.endswith('.') and len(line) < 100:
                candidate = line
                break
        
        if candidate:
            current_project = candidate

    # Analyze extracted projects
    for name, content in projects_found.items():
        # Check topic
        if 'park' in name.lower():
            # Check completion in 2022
            # Patterns: "Construction was completed November 2022", "Construction was completed, November 2022", "Complete Construction: November 2022"
            pattern = r"(completed|Construction)[:\s,]+[A-Za-z]+\s+2022"
            if re.search(pattern, content, re.IGNORECASE):
                matched_projects.append(name)

# Deduplicate
matched_projects = list(set(matched_projects))

total_funding = 0
matches_found = []

for proj in matched_projects:
    # Exact match
    if proj in funding_lookup:
        total_funding += funding_lookup[proj]
        matches_found.append(proj)
    else:
        # Fuzzy match
        # Funding DB often has "Project Name (FEMA Project)" etc.
        # So we check if 'proj' is a prefix of funding name?
        # Or if funding name contains 'proj'
        for fname, amount in funding_lookup.items():
            if proj in fname and fname.startswith(proj):
                total_funding += amount
                matches_found.append(fname)

print("__RESULT__:")
print(json.dumps({"matches": matches_found, "total_funding": total_funding}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json'}

exec(code, env_args)
