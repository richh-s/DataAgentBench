code = """import json
import re

# Access the stored results
funding_data = locals()['var_functions.query_db:2']
civic_docs = locals()['var_functions.query_db:0']

# For large results that are stored as file paths, read them
if isinstance(funding_data, str) and '.json' in funding_data:
    with open(funding_data.replace('/tmp/', '/'), 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs, str) and '.json' in civic_docs:
    with open(civic_docs.replace('/tmp/', '/'), 'r') as f:
        civic_docs = json.load(f)

print(f"Found {len(funding_data)} funding records and {len(civic_docs)} civic documents")

# Look for FEMA/emergency projects in funding data
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name or 'fema' in project_name or 'emergency' in project_name.lower():
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        })

print(f"Found {len(fema_projects)} FEMA/emergency-related projects in funding data")

# Parse civic documents to extract project status information
def extract_project_status(text):
    """Extract project information from text document"""
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names followed by status indicators
        # Common patterns in the documents
        lower_line = line.lower()
        
        # Check if this line might be a project name
        is_potential_project = False
        if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
            # Check for project keywords
            project_keywords = ['project', 'repairs', 'improvements', 'drainage', 'road', 'bridge', 'sirens', 'warning', 'structure']
            if any(keyword in lower_line for keyword in project_keywords):
                is_potential_project = True
        
        if is_potential_project:
            # Look ahead for status indicators
            status = None
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].lower()
                
                if 'design' in next_line or 'in design' in next_line:
                    status = 'design'
                    break
                elif 'completed' in next_line or 'construction was completed' in next_line:
                    status = 'completed'
                    break
                elif 'not started' in next_line:
                    status = 'not started'
                    break
                elif 'construction' in next_line and ('under construction' in next_line or 'begin construction' in next_line):
                    status = 'design'
                    break
            
            if status:
                projects.append({
                    'Project_Name': line,
                    'Status': status
                })
    
    return projects

# Extract projects from all documents
all_extracted_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_project_status(text)
    all_extracted_projects.extend(projects)

print(f"Extracted {len(all_extracted_projects)} projects from civic documents")

# Match funding data with extracted project statuses
final_results = []

for funding_proj in fema_projects:
    project_name = funding_proj['Project_Name']
    status = 'Unknown'
    
    # Try to find matching project in extracted data
    for extracted in all_extracted_projects:
        extracted_name = extracted['Project_Name']
        
        # Simple matching: check if extracted name is contained in funding name or vice versa
        if (project_name.lower() in extracted_name.lower() or 
            extracted_name.lower() in project_name.lower()):
            status = extracted['Status']
            break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status
    })

print(f"\nFinal results count: {len(final_results)}")
for result in final_results:
    print(f"  - {result['Project_Name']}: ${result['Amount']:,} ({result['Status']})")

# Format the output as JSON
result_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
