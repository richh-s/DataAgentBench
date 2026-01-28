code = """import json
import re
import os

# Load civic documents
civic_file_path = locals().get('var_functions.query_db:2', '')
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
fund_file_path = locals().get('var_functions.query_db:0', '')
with open(fund_file_path, 'r') as f:
    funding_data = json.load(f)

print("Parsing %d documents..." % len(civic_docs))

# Extract all design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_match = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)", text, re.DOTALL)
    
    if design_match:
        section = design_match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty and metadata lines
            skip_patterns = ['(', 'Updates:', 'Project Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'cid:']
            if (line and 
                not any(line.startswith(p) for p in skip_patterns) and
                not any(line.lower().startswith(p.lower()) for p in skip_patterns) and
                len(line) > 10):
                design_projects.append(line)

print("Potential projects: %d" % len(design_projects))

# Get unique project names
unique_projects = list(set(design_projects))
print("Unique projects: %d" % len(unique_projects))

# Build funding lookup by project name
funding_lookup = {}
for f in funding_data:
    name = f['Project_Name'].strip().lower()
    amount = int(f['Amount'])
    funding_lookup[name] = amount

# Match with funding
matches = []
for proj in unique_projects:
    proj_lower = proj.lower()
    
    # Check direct match
    if proj_lower in funding_lookup and funding_lookup[proj_lower] > 50000:
        matches.append({'project': proj, 'amount': funding_lookup[proj_lower]})
    else:
        # Check fuzzy match by checking if project is a substring of funding name
        for fund_name, amount in funding_lookup.items():
            if (proj_lower in fund_name or fund_name in proj_lower) and amount > 50000:
                matches.append({'project': proj, 'amount': amount})
                break

print("Projects with >$50K funding: %d" % len(matches))

print('__RESULT__:')
print(json.dumps({
    "total_design_projects": len(unique_projects),
    "final_count": len(matches),
    "examples": matches[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
