code = """import json
import re

# Load funding data from file
funding_file = var_functions.query_db:4
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:4

# Load civic docs from file
civic_file = var_functions.query_db:5
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:5

# Filter funding > $50,000
high_funding = [f for f in funding_data if isinstance(f, dict) and int(f.get('Amount', 0)) > 50000]

# Process civic documents to extract project info
projects = []

for doc in civic_docs:
    if not isinstance(doc, dict):
        continue
        
    text = doc.get('text', '')
    if not text:
        continue
    
    # Parse through text to find project patterns
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Look for patterns that indicate project names with status
        # Common patterns: 
        # - Project Name (indented, often with status keywords)
        # - Lines with schedule info
        
        # Try to extract project name from lines that are likely project names
        if line and len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
            # Skip header lines
            skip_keywords = ['Public Works', 'Commission', 'Agenda', 'Date', 'To:', 'From:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Capital Improvement', 'Disaster Recovery']
            if any(skip in line for skip in skip_keywords):
                continue
            
            # Look for lines that end without colon and seem like project names
            if not line.endswith(':') and not line.startswith('-'):
                # Check if next lines contain status info
                project_name = line
                
                # Clean up project name
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                # Skip if it's just a page number or similar
                if re.match(r'^(Page|Agenda Item|cid:|\\|/|\d+)', project_name):
                    continue
                
                projects.append({
                    'Project_Name': project_name,
                    'doc_id': doc.get('_id'),
                    'filename': doc.get('filename')
                })

# Now try to extract status from text for each unique project
project_info = {}

for project in projects:
    name = project['Project_Name']
    
    # Search in the original text for status information about this project
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Check if this project appears in the text
        if name in text:
            # Look for status indicators near the project name
            # Status: "design", "completed", "not started"
            # Type: "capital", "disaster"
            
            status = None
            project_type = None
            
            # Look for section headers that indicate type
            if 'Capital Improvement Projects (Design)' in text:
                project_type = 'capital'
                if name in text.split('Capital Improvement Projects (Design)')[-1].split('Capital Improvement Projects (Construction)')[0]:
                    status = 'design'
            elif 'Capital Improvement Projects (Construction)' in text:
                project_type = 'capital'
                if name in text.split('Capital Improvement Projects (Construction)')[-1].split('Capital Improvement Projects (Not Started)')[0]:
                    status = 'completed'  # Projects in construction section are likely completed or underway
            elif 'Capital Improvement Projects (Not Started)' in text:
                project_type = 'capital'
                if name in text.split('Capital Improvement Projects (Not Started)')[-1]:
                    status = 'not started'
            elif 'Disaster Recovery Projects' in text:
                project_type = 'disaster'
            
            # Check for FEMA-related names to identify disaster projects
            if 'FEMA' in name.upper() or 'CalOES' in name or 'CalJPIA' in name:
                project_type = 'disaster'
            
            # If we found info, store it
            if status or project_type:
                project_info[name] = {
                    'Project_Name': name,
                    'status': status,
                    'type': project_type
                }

# Join with funding data
funding_by_project = {f['Project_Name']: f for f in high_funding}

# Count capital projects with 'design' status and funding > $50,000
count = 0
results = []

for name, info in project_info.items():
    if info.get('type') == 'capital' and info.get('status') == 'design':
        if name in funding_by_project:
            count += 1
            results.append({
                'Project_Name': name,
                'Funding': int(funding_by_project[name]['Amount']),
                'Source': funding_by_project[name]['Funding_Source']
            })

# Also check for projects in funding data that might not have been extracted perfectly
# Try pattern matching to find more projects
for funding in high_funding:
    f_name = funding['Project_Name']
    
    # Skip if we already have it
    if f_name in [r['Project_Name'] for r in results]:
        continue
    
    # Try to find partial matches in project_info
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Check if project name appears (with or without FEMA suffix)
        base_name = f_name.split(' (')[0]  # Remove suffixes like (FEMA Project)
        
        if base_name in text:
            # Determine status based on section
            status = None
            project_type = None
            
            if 'Capital Improvement Projects (Design)' in text:
                design_section = text.split('Capital Improvement Projects (Design)')[-1].split('Capital Improvement Projects (Construction)')[0]
                if base_name in design_section:
                    status = 'design'
                    project_type = 'capital'
            elif 'Capital Improvement Projects (Construction)' in text:
                construction_section = text.split('Capital Improvement Projects (Construction)')[-1].split('Capital Improvement Projects (Not Started)')[0]
                if base_name in construction_section:
                    status = 'completed'
                    project_type = 'capital'
            elif 'Capital Improvement Projects (Not Started)' in text:
                not_started_section = text.split('Capital Improvement Projects (Not Started)')[-1]
                if base_name in not_started_section:
                    status = 'not started'
                    project_type = 'capital'
            
            if status == 'design' and project_type == 'capital':
                count += 1
                results.append({
                    'Project_Name': f_name,
                    'Funding': int(funding['Amount']),
                    'Source': funding['Funding_Source']
                })
                break

result = {
    'count': count,
    'projects': results
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
