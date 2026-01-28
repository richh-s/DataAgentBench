code = """import json
import re

# Load data from files
with open(locals()['var_functions.query_db:0'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:2'], 'r') as f:
    civic_docs = json.load(f)

# Build funding map by project name (normalized)
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip().lower()
    amount = int(item['Amount'])
    funding_map[name] = amount

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for the "Capital Improvement Projects (Design)" section
    # Use case-insensitive search and capture until next major heading
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)', 
                             text, re.IGNORECASE | re.DOTALL)
    
    if design_match:
        section = design_match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and metadata
            if (line and 
                not line.startswith('(') and 
                not line.lower().startswith('updates') and
                not line.lower().startswith('project schedule') and
                not line.lower().startswith('complete design') and
                not line.lower().startswith('advertise') and
                not line.lower().startswith('begin construction') and
                not line.startswith('cid:') and
                len(line) > 10):
                
                # Normalize project name
                normalized = line.lower().strip()
                capital_design_projects.append(normalized)

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))

print("Capital design projects found: %d" % len(capital_design_projects))

# Count matches with funding > $50,000
matched_count = 0
matched_details = []

for project in capital_design_projects:
    # Check exact match
    if project in funding_map and funding_map[project] > 50000:
        matched_count += 1
        matched_details.append({"project": project, "funding": funding_map[project]})
    else:
        # Try without parenthetical suffixes
        base_name = re.sub(r'\s*\([^)]*\)$', '', project).strip()
        if base_name in funding_map and funding_map[base_name] > 50000:
            matched_count += 1
            matched_details.append({"project": project, "funding": funding_map[base_name]})

print("Projects with funding > $50K: %d" % matched_count)

print('__RESULT__:')
print(json.dumps({
    "total_design_projects": len(capital_design_projects),
    "count_over_50k": matched_count,
    "sample_matches": matched_details[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
