code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-7721797773547696454'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11187982915613525112'], 'r') as f:
    civic_docs = json.load(f)

# Create a set of funded projects > 50000
funded_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        continue

print(f"DEBUG: Found {len(funded_projects)} projects with funding > 50,000.")

extracted_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        # We are looking for "Capital Improvement Projects (Design)"
        # Note: The text might have extra spaces or be split.
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        
        # Stop if we hit another section
        # "Capital Improvement Projects (Construction)"
        # "Capital Improvement Projects (Not Started)"
        # "Disaster Recovery Projects"
        if in_design_section:
            if "Capital Improvement Projects" in line and "(Design)" not in line:
                in_design_section = False
            elif "Disaster Recovery Projects" in line:
                in_design_section = False
        
        if in_design_section:
            # Extract potential project names
            # Heuristic: 
            # - Not a page number "Page X of Y"
            # - Not an update line "(cid:190)" or starting with bullet
            # - Not "Agenda Item"
            # - Not "To:", "From:", "Subject:", "Date"
            # - Not "Updates:", "Project Schedule:"
            
            if line.startswith("(cid:") or line.startswith("\u2022") or line.startswith("-"):
                continue
            if line.lower().startswith("page ") or "agenda item" in line.lower():
                continue
            if line.startswith("To:") or line.startswith("From:") or line.startswith("Subject:"):
                continue
            if "Updates:" in line or "Project Schedule:" in line or "Estimated Schedule:" in line:
                continue
            if "Complete Design:" in line or "Begin Construction:" in line or "Advertise:" in line:
                continue
            
            # This line is likely a project name
            extracted_design_projects.append(line)

# Remove duplicates if any
extracted_design_projects = list(set(extracted_design_projects))

print(f"DEBUG: Extracted {len(extracted_design_projects)} potential design projects.")
print("DEBUG: Sample extracted:", extracted_design_projects[:5])

# Count matches
match_count = 0
matches = []
for proj in extracted_design_projects:
    # Exact match check
    if proj in funded_projects:
        match_count += 1
        matches.append(proj)
    else:
        # Check for near match?
        # Maybe the project name in text is slightly different?
        pass

print("__RESULT__:")
print(json.dumps({"count": match_count, "matches": matches, "extracted": extracted_design_projects}))"""

env_args = {'var_function-call-10821165667219444455': ['Funding'], 'var_function-call-10821165667219446426': ['civic_docs'], 'var_function-call-7721797773547696454': 'file_storage/function-call-7721797773547696454.json', 'var_function-call-7721797773547696997': 'file_storage/function-call-7721797773547696997.json', 'var_function-call-11187982915613525112': 'file_storage/function-call-11187982915613525112.json'}

exec(code, env_args)
