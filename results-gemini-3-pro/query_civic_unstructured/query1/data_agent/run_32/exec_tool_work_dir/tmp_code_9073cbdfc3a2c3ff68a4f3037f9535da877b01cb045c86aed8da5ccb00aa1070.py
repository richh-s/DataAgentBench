code = """import json
import sqlite3
import pandas as pd

# Load funding data
with open(locals()['var_function-call-4570374009180656928'], 'r') as f:
    funding_data = json.load(f)

# Filter funding data for > 50000
# Note: Amount is string in the JSON output, need to convert to int.
high_funding_projects = []
for item in funding_data:
    try:
        if int(item['Amount']) > 50000:
            high_funding_projects.append(item['Project_Name'])
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function-call-13689454801406461365'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Normalize text slightly for easier searching (optional, but keep original for extraction)
    # Find the "Capital Improvement Projects (Design)" section
    # We look for the header.
    
    # We need to find the start and end of the Design section.
    # Potential headers based on observation
    start_header = "Capital Improvement Projects (Design)"
    
    # Potential end headers
    end_headers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Staff has also prepared" # End of the list in one doc
    ]
    
    start_idx = text.find(start_header)
    if start_idx == -1:
        continue
        
    # Find the earliest end header that appears AFTER the start_header
    end_idx = len(text)
    for end_h in end_headers:
        idx = text.find(end_h, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    design_section = text[start_idx:end_idx]
    
    # Now check for project names in this section
    for proj_name in high_funding_projects:
        # Check if project name is in the section
        # We strip the project name to be sure
        clean_proj_name = proj_name.strip()
        
        # Simple substring match
        # To avoid matching "Park" in "Parker", we could look for boundary, 
        # but project names are usually multi-word and specific.
        if clean_proj_name in design_section:
            found_projects.add(clean_proj_name)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json'}

exec(code, env_args)
