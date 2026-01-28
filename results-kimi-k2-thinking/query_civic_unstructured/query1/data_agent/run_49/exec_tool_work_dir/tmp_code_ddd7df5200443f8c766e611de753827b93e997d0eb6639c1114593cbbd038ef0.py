code = """import json
import re
import os

# Load funding data - projects with Amount > 50000
funding_path = locals().get('var_functions.query_db:36', '')
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals().get('var_functions.query_db:37', '')
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_records)} funding records and {len(civic_docs)} civic documents")

# Build funding lookup map: normalized project name -> amount
funding_map = {}
for record in funding_records:
    proj_name = record['Project_Name'].strip().lower()
    amount = int(record['Amount'])
    funding_map[proj_name] = amount

print(f"Funding map contains {len(funding_map)} projects")

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the "Capital Improvement Projects (Design)" section
    # The pattern looks for this heading and captures content until next major heading or double newline
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n\s*[A-Z][A-Z]|$)'
    design_match = re.search(design_pattern, text, re.IGNORECASE | re.DOTALL)
    
    if design_match:
        section_text = design_match.group(1)
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and metadata lines
            if (line and 
                not line.startswith('(') and 
                not line.lower().startswith('updates') and
                not line.lower().startswith('project schedule') and
                not line.lower().startswith('complete design') and
                not line.lower().startswith('advertise') and
                not line.lower().startswith('begin construction') and
                not line.startswith('cid:') and
                len(line) > 10):  # Reasonable length for a project name
                
                # Normalize project name
                normalized = line.strip().lower()
                capital_design_projects.append(normalized)

# Remove duplicates while preserving order seen
seen = set()
unique_design_projects = []
for proj in capital_design_projects:
    if proj not in seen:
        seen.add(proj)
        unique_design_projects.append(proj)

print(f"Found {len(unique_design_projects)} unique capital design projects")

# Match with funding data > $50,000
matched_projects = []
for project in unique_design_projects:
    # Check exact match
    if project in funding_map:
        amount = funding_map[project]
        if amount > 50000:
            matched_projects.append({
                'project_name': project,
                'funding_amount': amount
            })
    else:
        # Try without parenthetical suffixes like "(FEMA Project)"
        base_name = re.sub(r'\s*\([^)]*\)$', '', project).strip()
        if base_name in funding_map:
            amount = funding_map[base_name]
            if amount > 50000:
                matched_projects.append({
                    'project_name': project,
                    'funding_amount': amount
                })

print(f"Matched {len(matched_projects)} projects with funding > $50,000")

print('__RESULT__:')
print(json.dumps({
    'capital_design_projects_found': len(unique_design_projects),
    'projects_with_funding_over_50k': len(matched_projects),
    'sample_matches': matched_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
