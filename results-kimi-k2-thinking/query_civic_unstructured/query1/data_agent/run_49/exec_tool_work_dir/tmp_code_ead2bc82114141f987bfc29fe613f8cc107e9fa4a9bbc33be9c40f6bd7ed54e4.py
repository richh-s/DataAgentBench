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

print("Analyzing %d civic documents..." % len(civic_docs))

# Parse documents to extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    # Pattern: look for project names followed by design status
    design_pattern = r"Capital Improvement Projects \(Design\)(.*?)\n\s*\n"
    design_section = re.search(design_pattern, text, re.DOTALL)
    
    if design_section:
        section_text = design_section.group(1)
        # Extract project names - lines that look like project names
        # Typically start with project name, then have status/updates
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common patterns
            if (line and 
                not line.startswith('(') and 
                not line.lower().startswith('updates') and
                not line.lower().startswith('project schedule') and
                not line.lower().startswith('complete design') and
                not line.lower().startswith('advertise') and
                not line.lower().startswith('begin construction') and
                len(line) > 5):
                
                # This looks like a project name
                project_name = line.strip()
                if project_name and not project_name.startswith('cid:'):
                    design_projects.append({
                        'project_name': project_name,
                        'status': 'design',
                        'type': 'capital'
                    })

print("Found %d potential design projects" % len(design_projects))

# Get unique project names
unique_design_projects = list({p['project_name']: p for p in design_projects}.values())
print("Unique design projects: %d" % len(unique_design_projects))

for p in unique_design_projects[:10]:
    print("- %s" % p['project_name'])

# Map funding data by project name (lowercase)
funding_by_project = {}
for fund in funding_data:
    name = fund['Project_Name'].lower().strip()
    amount = int(fund['Amount'])
    funding_by_project[name] = amount

# Match design projects with funding > $50,000
matched_projects = []
for project in unique_design_projects:
    proj_name = project['project_name'].lower().strip()
    
    # Also check without suffixes like "(FEMA Project)"
    base_name = re.sub(r'\s*\([^)]*\)$', '', proj_name)
    
    # Check if funding exists
    amount = None
    if proj_name in funding_by_project:
        amount = funding_by_project[proj_name]
    elif base_name in funding_by_project:
        amount = funding_by_project[base_name]
    
    if amount is not None and amount > 50000:
        matched_projects.append({
            'project_name': project['project_name'],
            'funding': amount
        })

print("\nProjects with funding > $50,000: %d" % len(matched_projects))
for p in matched_projects:
    print("- %s: $%d" % (p['project_name'], p['funding']))

print('__RESULT__:')
print(json.dumps({
    "design_projects_found": len(unique_design_projects),
    "funded_projects_count": len(matched_projects),
    "sample_matches": matched_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
