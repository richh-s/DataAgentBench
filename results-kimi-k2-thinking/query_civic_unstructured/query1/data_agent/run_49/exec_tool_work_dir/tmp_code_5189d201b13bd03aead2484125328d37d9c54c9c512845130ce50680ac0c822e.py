code = """import json
import re

# Load funding data
funding_path = locals().get('var_functions.query_db:0', '')
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals().get('var_functions.query_db:2', '')
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup map (project name -> amount)
funding_map = {}
for record in funding_records:
    name = record['Project_Name'].strip().lower()
    amount = int(record['Amount'])
    funding_map[name] = amount

# Extract capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    # The section ends when we hit another heading or double newline
    design_section = re.search(
        r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n\s*[A-Z][A-Z]|$)',
        text, 
        re.DOTALL
    )
    
    if design_section:
        section_text = design_section.group(1)
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and lines that are clearly not project names
            if (line and 
                not line.startswith('(') and 
                not line.lower().startswith('updates') and
                not line.lower().startswith('project schedule') and
                not line.lower().startswith('complete design') and
                not line.lower().startswith('advertise') and
                not line.lower().startswith('begin construction') and
                not line.startswith('cid:')):
                
                # This should be a project name
                if len(line) > 5:  # reasonable length check
                    # Normalize the name
                    normalized = line.strip().lower()
                    design_projects.add(normalized)

# Match with funding
matched_count = 0
matched_projects = []

for proj_name in design_projects:
    # Check exact match
    if proj_name in funding_map and funding_map[proj_name] > 50000:
        matched_count += 1
        matched_projects.append({
            'name': proj_name,
            'amount': funding_map[proj_name]
        })
    else:
        # Try without parenthetical suffixes like (FEMA Project)
        base_name = re.sub(r'\s*\([^)]*\)$', '', proj_name)
        if base_name in funding_map and funding_map[base_name] > 50000:
            matched_count += 1
            matched_projects.append({
                'name': proj_name,
                'amount': funding_map[base_name]
            })

# Output results
print('__RESULT__:')
print(json.dumps({
    'total_design_projects': len(design_projects),
    'funded_projects_over_50k': matched_count,
    'sample_matches': matched_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
