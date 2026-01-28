code = """import json
import re

# Load the funding data from storage
with open('/tmp/tmps2y9r5zk.json', 'r') as f:
    funding_data = json.load(f)

# Load the civic documents from storage  
with open('/tmp/tmpq5n1lx3u.json', 'r') as f:
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
            'Amount': record.get('Amount', 0)
        })

print(f"Found {len(fema_projects)} FEMA/emergency-related projects in funding data")
for proj in fema_projects[:10]:
    print(f"  - {proj['Project_Name']}")

# Parse civic documents to extract project status information
def extract_project_status(text):
    """Extract project information from text document"""
    projects = []
    
    # Split by common project name patterns
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically bolded or starting with bullet points)
        # Pattern: project name followed by status section
        if line and not line.startswith('(') and len(line) > 10:
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'repairs', 'improvements', 'drainage', 'road', 'bridge']):
                # Could be a project name
                current_project = line
        
        # Look for status indicators
        if current_project:
            lower_line = line.lower()
            status = None
            
            if 'design' in lower_line or 'in design' in lower_line:
                status = 'design'
            elif 'completed' in lower_line or 'construction was completed' in lower_line:
                status = 'completed'
            elif 'not started' in lower_line:
                status = 'not started'
            elif 'construction' in lower_line and ('under construction' in lower_line or 'begin construction' in lower_line):
                # Projects under construction are effectively in progress, map to design status
                status = 'design'
            
            if status:
                projects.append({
                    'Project_Name': current_project,
                    'Status': status
                })
                current_project = None
    
    return projects

# Extract projects from all documents
all_extracted_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_project_status(text)
    all_extracted_projects.extend(projects)

print(f"\nExtracted {len(all_extracted_projects)} projects from civic documents")
for proj in all_extracted_projects[:10]:
    print(f"  - {proj['Project_Name']}: {proj['Status']}")

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

# Filter for projects with "FEMA" or "emergency" in the name
filtered_results = []
for result in final_results:
    project_name = result['Project_Name']
    if 'FEMA' in project_name or 'fema' in project_name or 'emergency' in project_name.lower():
        filtered_results.append(result)

print(f"\nFinal results count: {len(filtered_results)}")

# Format the output as JSON
result_json = json.dumps(filtered_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
