code = """import json
import pandas as pd
import re

# Load tool results
funding_path = locals()['var_function-call-5441404039575521335']
docs_path = locals()['var_function-call-5441404039575519310']

# Load Funding Data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Filter funding > 50000
# Ensure Amount is treated as int
high_funding_projects = set()
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            high_funding_projects.add(item['Project_Name'].strip())
    except ValueError:
        continue

# Load Civic Docs
with open(docs_path, 'r') as f:
    docs = json.load(f)

extracted_projects = []

# Section Header to find
target_header = "Capital Improvement Projects (Design)"

# Potential Stop Headers
stop_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects",
    "Disaster Recovery Projects (Design)",
    "Disaster Recovery Projects (Construction)",
    "Disaster Recovery Projects (Not Started)",
    "Public Works Commission" # Just in case
]

for doc in docs:
    text = doc['text']
    
    # Find start
    start_idx = text.find(target_header)
    if start_idx == -1:
        continue
    
    # Move past the header
    content_start = start_idx + len(target_header)
    
    # Find end (nearest stop header)
    end_idx = len(text)
    for stop in stop_headers:
        idx = text.find(stop, content_start)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_content = text[content_start:end_idx]
    
    # Parse lines
    lines = section_content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Check for bullets or metadata
        # (cid:190) and (cid:131) are common in the snippet
        if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda Item") or line.startswith("Updates:") or line.startswith("Project Schedule:"):
            continue
        
        # Heuristic: Project names are usually not extremely long sentences
        # And often Title Case (though not always strictly)
        # Assuming lines that remain are project names
        extracted_projects.append(line)

# Match with funding
matches = []
for proj in extracted_projects:
    # Try exact match
    if proj in high_funding_projects:
        matches.append(proj)
    else:
        # Debug: check if there's a near match or if I missed it
        pass

result = {
    "extracted_count": len(extracted_projects),
    "match_count": len(matches),
    "matches": matches,
    "high_funding_sample": list(high_funding_projects)[:5],
    "extracted_sample": extracted_projects[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5441404039575521335': 'file_storage/function-call-5441404039575521335.json', 'var_function-call-5441404039575519310': 'file_storage/function-call-5441404039575519310.json'}

exec(code, env_args)
