code = """# Load the full funding data
import json
import re

# Read funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic docs path
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Convert amount to integer for proper comparison
funding_df = []
for item in funding_data:
    funding_df.append({
        'Funding_ID': item['Funding_ID'],
        'Project_Name': item['Project_Name'],
        'Funding_Source': item['Funding_Source'],
        'Amount': int(item['Amount'])
    })

# Filter funding > 50000
high_funding = [f for f in funding_df if f['Amount'] > 50000]

# Extract projects from civic docs
projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for project sections with status indicators
    # Pattern: Section headers like "Capital Improvement Projects (Design)"
    
    # Find all project sections
    capital_design_matches = re.finditer(r'Capital Improvement Projects \(Design\).*?(?=\n\n[A-Z]|\Z)', text, re.DOTALL)
    
    for match in capital_design_matches:
        section_text = match.group(0)
        
        # Extract project names - look for patterns like project names followed by markers
        # Projects appear to be listed with bullet points or just name lines
        lines = section_text.split('\n')
        
        current_project = None
        for line in lines:
            line = line.strip()
            
            # Skip empty lines, headers, and bullet content
            if not line or line.startswith('(') or line.startswith('cid:') or \
               'Updates:' in line or 'Schedule:' in line or \
               'Complete Design:' in line or 'Advertise:' in line or \
               'Begin Construction:' in line or 'Capital Improvement' in line:
                continue
                
            # If line looks like a project name (reasonable length, not a status line)
            if len(line) > 5 and len(line) < 200 and \
               not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'complete', 'advertise', 'begin', 'spring', 'summer', 'fall', 'winter', '2023', '2024']):
                
                # Clean up the project name
                project_name = line.strip()
                if project_name and project_name not in ['RECOMMENDED ACTION', 'DISCUSSION']:
                    projects.append({
                        'Project_Name': project_name,
                        'Status': 'design',
                        'Type': 'capital',
                        'Document_Filename': doc['filename']
                    })

# Also check for Disaster Recovery projects with design status
disaster_design_matches = re.finditer(r'Disaster Recovery Projects \(Design\).*?(?=\n\n[A-Z]|\Z)', text, re.DOTALL)

for match in disaster_design_matches:
    section_text = match.group(0)
    lines = section_text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line or line.startswith('(') or line.startswith('cid:') or \
           'Updates:' in line or 'Schedule:' in line or \
           'Complete Design:' in line or 'Advertise:' in line or \
           'Begin Construction:' in line or 'Disaster Recovery' in line:
            continue
            
        if len(line) > 5 and len(line) < 200 and \
           not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'complete', 'advertise', 'begin', 'spring', 'summer', 'fall', 'winter', '2023', '2024']):
            
            project_name = line.strip()
            if project_name and project_name not in ['RECOMMENDED ACTION', 'DISCUSSION']:
                projects.append({
                    'Project_Name': project_name,
                    'Status': 'design',
                    'Type': 'disaster',
                    'Document_Filename': doc['filename']
                })

# Debug: Print projects we found
print("Found design projects:", len(projects))
for p in projects[:10]:  # Show first 10
    print(f"  - {p['Project_Name']}")

# Now join with funding data
# Need to match project names - handle variations like suffixes
matched_projects = []

for project in projects:
    proj_name = project['Project_Name'].strip()
    
    # Look for direct match or project name as substring
    for funding in high_funding:
        fund_name = funding['Project_Name'].strip()
        
        # Check if project name matches (direct or as substring)
        if proj_name == fund_name or \
           fund_name.startswith(proj_name + ' ') or \
           fund_name.startswith(proj_name + '(') or \
           proj_name in fund_name:
            
            matched_projects.append({
                'Project_Name': proj_name,
                'Status': project['Status'],
                'Type': project['Type'],
                'Funding_Amount': funding['Amount'],
                'Funding_Source': funding['Funding_Source']
            })
            break

# Filter for capital projects only
capital_design_projects = [p for p in matched_projects if p['Type'] == 'capital']

# Count them
count = len(capital_design_projects)

print(f"__RESULT__: {count}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
