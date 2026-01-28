code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-13808490642390448201'], 'r') as f:
    funding_data = json.load(f)

# Create a set of funded project names (Amount > 50000)
# The query already filtered > 50000, but let's double check/ensure uniqueness
funded_projects = set()
for item in funding_data:
    if float(item['Amount']) > 50000:
        funded_projects.add(item['Project_Name'].strip())

# Load Civic Docs
with open(locals()['var_function-call-4985696884690537041'], 'r') as f:
    civic_docs = json.load(f)

extracted_design_projects = []

for doc in civic_docs:
    text = doc['text']
    # Find the Design section
    # Use regex to find the section and capture text until the next section
    # Pattern: "Capital Improvement Projects (Design)" ... until "Capital Improvement Projects (" or end
    
    # Normalize newlines
    text = text.replace('\r\n', '\n')
    
    pattern = r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|$)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section_text = match.group(1)
        lines = [line.strip() for line in section_text.split('\n') if line.strip()]
        
        # Identify project names
        # Logic: A line is a project name if the *next* line starts with "(cid:" or contains "Updates:"
        for i in range(len(lines) - 1):
            current_line = lines[i]
            next_line = lines[i+1]
            
            # Skip noise
            if "Page " in current_line or "Agenda Item" in current_line:
                continue
            
            # Check if next line looks like the start of updates
            if "(cid:" in next_line or "Updates:" in next_line or "Project Schedule" in next_line:
                # current_line is likely the project name
                # Clean up
                p_name = current_line
                extracted_design_projects.append(p_name)

# Deduplicate extracted projects
extracted_design_projects = list(set(extracted_design_projects))

# Count matches
matches = []
misses = []

for p in extracted_design_projects:
    if p in funded_projects:
        matches.append(p)
    else:
        # Try fuzzy match?
        # Check if p is in funded_projects or vice versa
        found = False
        for fp in funded_projects:
            if p == fp:
                matches.append(p)
                found = True
                break
            # substring check - be careful
            # if fp in p or p in fp:
            #     matches.append(fp) # Count the funded one
            #     found = True
            #     break
        if not found:
            misses.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": len(matches),
    "matches": matches,
    "misses": misses,
    "funded_sample": list(funded_projects)[:5]
}))"""

env_args = {'var_function-call-13808490642390448090': ['Funding'], 'var_function-call-13808490642390448201': 'file_storage/function-call-13808490642390448201.json', 'var_function-call-13808490642390448312': 'file_storage/function-call-13808490642390448312.json', 'var_function-call-4985696884690537041': 'file_storage/function-call-4985696884690537041.json'}

exec(code, env_args)
