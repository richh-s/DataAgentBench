code = """import json
from collections import defaultdict
import re

# Read civic documents from file
civic_file_path = locals()['var_functions.query_db:12']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data from file
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[proj_name] = amount

# Extract project information from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    # Pattern to identify projects and their status
    lines = text.split('\n')
    current_section = None
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Identify section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'not started'
            continue
        elif 'Disaster Recovery Projects' in line:
            current_section = 'disaster'
            continue
            
        # Look for project names (typically bold lines or lines without bullet points)
        if current_section and line and not line.startswith('(') and not line.startswith('•') and not line.startswith('▪') and not line.startswith('●'):
            # Skip common non-project lines
            if any(skip in line.lower() for skip in ['updates:', 'schedule:', 'project description:', 'project updates:', 'revised', 'preliminary design phase']):
                continue
                
            # Clean common patterns
            clean_line = re.sub(r'^[^A-Za-z]*', '', line)  # Remove leading non-letters
            clean_line = re.sub(r'\(cid:\d+\)', '', clean_line).strip()  # Remove weird encoding
            
            if len(clean_line) > 10 and not clean_line.startswith('Page') and 'cid:' not in clean_line:
                # This looks like a project name
                project_name = clean_line
                
                # Determine project type
                project_type = 'capital'
                if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
                    project_type = 'disaster'
                
                # Determine status from section
                status_map = {
                    'design': 'design',
                    'construction': 'completed',
                    'not started': 'not started'
                }
                status = status_map.get(current_section, 'unknown')
                
                projects.append({
                    'project_name': project_name,
                    'status': status,
                    'type': project_type,
                    'document': doc.get('filename', '')
                })

# Find projects with design status and funding > $50,000
design_projects_with_funding = []
for proj in projects:
    if proj['status'] == 'design':
        # Check exact match
        if proj['project_name'] in funding_map:
            design_projects_with_funding.append({
                'project_name': proj['project_name'],
                'funding': funding_map[proj['project_name']],
                'status': proj['status'],
                'type': proj['type']
            })
        # Also check for partial matches (clean both names)
        else:
            clean_proj_name = proj['project_name'].lower().replace('project', '').strip()
            for fund_name, amount in funding_map.items():
                if clean_proj_name in fund_name.lower() or fund_name.lower() in clean_proj_name:
                    design_projects_with_funding.append({
                        'project_name': fund_name,
                        'funding': amount,
                        'status': proj['status'],
                        'type': proj['type']
                    })
                    break

# Count unique projects
seen = set()
unique_projects = []
for proj in design_projects_with_funding:
    if proj['project_name'] not in seen:
        seen.add(proj['project_name'])
        unique_projects.append(proj)

# Print results
print('__RESULT__:')
print(json.dumps({
    'total_design_projects_with_funding_gt_50000': len(unique_projects),
    'projects': unique_projects[:10]  # Sample for debugging
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
