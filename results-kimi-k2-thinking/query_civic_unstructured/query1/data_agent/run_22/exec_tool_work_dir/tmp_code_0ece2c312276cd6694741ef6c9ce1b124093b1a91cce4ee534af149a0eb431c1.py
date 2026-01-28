code = """import json
import re

# Read the data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract projects from text
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_status = None
    current_type = None
    
    for line in lines:
        line = line.strip()
        
        # Detect section headers for status
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
            current_type = 'capital'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'completed'
            current_type = 'capital'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            current_type = 'capital'
            continue
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
            # Try to find status in the same line
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'completed'
            elif '(Not Started)' in line:
                current_status = 'not started'
            continue
        
        # Skip empty lines or lines that are obviously not project names
        if not line or len(line) < 5:
            continue
        if line.startswith('(') or line.startswith('▪') or line.startswith('▲') or line.startswith('•'):
            continue
        if any(keyword in line for keyword in ['Updates:', 'Project Schedule', 'Estimated Schedule', 
                                              'Project Description:', 'To:', 'Prepared by:', 'Approved by:',
                                              'RECOMMENDED ACTION', 'DISCUSSION:', 'Page', 'Agenda Item',
                                               'Subject:', 'Date prepared:', 'Meeting date:']):
            continue
            
        # If we have a status and type, this line might be a project name
        if current_status and current_type:
            # Clean the line
            project_name = re.sub(r'\s+', ' ', line).strip()
            
            # Skip if it's too long (probably not a project name)
            if len(project_name) > 150:
                continue
                
            # Skip common headers
            if any(header in project_name for header in ['Capital Improvement', 'Disaster Recovery', 
                                                        'Public Works', 'City Council', 'Commission']):
                continue
            
            projects.append({
                'Project_Name': project_name,
                'status': current_status,
                'type': current_type
            })

# Filter for design capital projects and match with funding
design_capital_projects = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']

# Match with funding data (amount > 50000)
matches = []
project_names_seen = set()

for project in design_capital_projects:
    for fund in funding_data:
        amount = int(fund['Amount'])
        if amount > 50000:
            fund_name = fund['Project_Name'].lower().strip()
            project_name = project['Project_Name'].lower().strip()
            
            # Check for match
            if project_name == fund_name or project_name in fund_name or fund_name in project_name:
                if project['Project_Name'] not in project_names_seen:
                    project_names_seen.add(project['Project_Name'])
                    matches.append({
                        'Project_Name': project['Project_Name'],
                        'Funding_Project_Name': fund['Project_Name'],
                        'Amount': amount
                    })

result = {
    'count': len(matches),
    'projects': matches[:5]  # Sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
