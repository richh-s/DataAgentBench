code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a mapping of project names to funding amounts
project_funding = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    project_funding[project_name] = amount

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for capital improvement projects section
    # Pattern: "Capital Improvement Projects" followed by status in parentheses
    capital_sections = re.split(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', text)
    
    for i in range(1, len(capital_sections), 2):
        status = capital_sections[i]
        section_text = capital_sections[i+1]
        
        # Extract project names (lines that look like project names)
        # Look for patterns like "Project Name\n" followed by updates
        project_matches = re.findall(r'([A-Z][A-Za-z0-9 &\-\(\)/]+)\n\s*\([cC]id:\s*190\)\s*Updates?:', section_text)
        
        for project_name in project_matches:
            # Clean up project name
            project_name = project_name.strip()
            
            # Check if this project has funding > $50,000
            if project_name in project_funding and project_funding[project_name] > 50000:
                extracted_projects.append({
                    'project_name': project_name,
                    'status': status.lower(),
                    'type': 'capital',
                    'funding': project_funding[project_name]
                })
            else:
                # Also check for variations (e.g., with suffixes)
                for funded_name in project_funding:
                    if funded_name.startswith(project_name) and project_funding[funded_name] > 50000:
                        extracted_projects.append({
                            'project_name': funded_name,
                            'status': status.lower(),
                            'type': 'capital',
                            'funding': project_funding[funded_name]
                        })
                        break

# Filter for design status and count
design_projects = [p for p in extracted_projects if p['status'] == 'design']

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(extracted_projects),
    'design_projects': len(design_projects),
    'design_projects_funding_over_50k': len(design_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
