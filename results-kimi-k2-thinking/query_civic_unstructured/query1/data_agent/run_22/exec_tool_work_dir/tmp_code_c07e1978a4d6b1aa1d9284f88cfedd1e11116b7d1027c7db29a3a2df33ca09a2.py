code = """import json
import re

# Read the data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents with their status and type
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital projects sections with different statuses
    # Pattern: Capital Improvement Projects (Design)
    # Pattern: Capital Improvement Projects (Construction)
    # Pattern: Capital Improvement Projects (Not Started)
    
    # Split by sections to identify project groups
    sections = re.split(r'\n(?=Capital Improvement Projects|Disaster Recovery Projects)', text)
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Determine status from section header
        status = None
        if '(Design)' in section:
            status = 'design'
        elif '(Construction)' in section:
            status = 'completed'
        elif '(Not Started)' in section:
            status = 'not started'
        
        # Determine type
        p_type = 'capital' if 'Capital Improvement' in section else 'disaster' if 'Disaster Recovery' in section else None
        
        if status and p_type:
            # Extract project names - look for lines that start with project names
            lines = section.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                # Skip empty lines or update/schedule lines
                if not line or line.startswith('(') or line.startswith('•') or line.startswith('▪') or line.startswith('▲'):
                    continue
                if 'Updates:' in line or 'Project Schedule' in line or 'Estimated Schedule' in line:
                    continue
                if line.startswith('Project Description:') or line.startswith('To:') or line.startswith('Prepared by:'):
                    continue
                if line.startswith('RECOMMENDED ACTION') or line.startswith('DISCUSSION:'):
                    continue
                if 'Page' in line and 'of' in line:
                    continue
                if 'Agenda Item' in line:
                    continue
                    
                # Look for project names (typically first line of a project description)
                # Check if this looks like a project name (not a bullet/update line)
                if len(line) > 5 and not line.startswith('(') and ':' not in line[:30]:
                    # This might be a project name
                    project_name = line
                    
                    # Clean up the name (remove trailing spaces, etc.)
                    project_name = re.sub(r'\s+', ' ', project_name).strip()
                    
                    # Avoid capturing section headers or generic text
                    if (project_name and 'Capital Improvement' not in project_name and 
                        'Disaster Recovery' not in project_name and
                        'Project Description' not in project_name and
                        len(project_name) < 200):  # Reasonable length
                        
                        projects.append({
                            'Project_Name': project_name,
                            'status': status,
                            'type': p_type
                        })

# Now merge with funding data
projects_with_funding = []

for project in projects:
    if project['status'] == 'design' and project['type'] == 'capital':
        # Find matching funding records (amount > 50000)
        for fund in funding_data:
            if int(fund['Amount']) > 50000:
                # Check if project names match (exact or close match)
                fund_name = fund['Project_Name'].lower().strip()
                project_name = project['Project_Name'].lower().strip()
                
                # Direct match or project name contained in funding name
                if (project_name == fund_name or 
                    project_name in fund_name or 
                    fund_name in project_name):
                    projects_with_funding.append({
                        'Project_Name': project['Project_Name'],
                        'Funding_Project_Name': fund['Project_Name'],
                        'Amount': int(fund['Amount']),
                        'status': project['status'],
                        'type': project['type']
                    })

# Count unique projects
count = len(set(p['Project_Name'] for p in projects_with_funding))

result = {
    'count': count,
    'matching_projects': projects_with_funding[:10]  # First 10 for inspection
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
