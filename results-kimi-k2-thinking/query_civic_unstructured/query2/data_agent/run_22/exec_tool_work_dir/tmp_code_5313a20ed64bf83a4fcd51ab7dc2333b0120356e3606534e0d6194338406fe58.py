code = """import json
import re

# Read all civic documents
filepath = locals()['var_functions.query_db:6']
with open(filepath, 'r') as f:
    civic_docs = json.load(f)

# Read all funding data  
filepath2 = locals()['var_functions.query_db:8']
with open(filepath2, 'r') as f:
    funding_data = json.load(f)

# Now extract projects from civic documents with status "completed" and date containing 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for project pattern: project name followed by details
    # Match projects followed by status indicators and dates
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if this is a project name line (not bullet point, not update/status line)
        if (line and 
            not line.startswith('(cid:') and 
            not line.startswith('(') and 
            not line.startswith('•') and
            not any(keyword in line.lower() for keyword in ['updates:', 'project schedule:', 'project description:']):
            
            # Check if it has project-like characteristics
            if len(line) > 5 and len(line) < 150:
                current_project = line
        
        # If we have a current project, check for completion and dates
        if current_project:
            # Check for completion status and 2022 date
            if ('completed' in line.lower() and '2022' in line):
                # Extract end date (et) if present
                # Look for common patterns
                date_match = re.search(r'(\w+\s+)?2022', line)
                if date_match:
                    date_str = date_match.group(0)
                    
                    # Check if this is a park-related project
                    if 'park' in current_project.lower():
                        park_projects_completed_2022.append({
                            'project_name': current_project,
                            'status': 'completed',
                            'date_info': line,
                            'year': '2022'
                        })

# Filter funding records that match park projects completed in 2022
matching_funding = []

for project in park_projects_completed_2022:
    project_name = project['project_name']
    
    # Look for matching funding records
    for fund in funding_data:
        fund_project_name = fund['Project_Name']
        
        # Check if project names match (accounting for slight variations)
        if (fund_project_name.lower().replace(' project', '') == project_name.lower().replace(' project', '') or
            fund_project_name.lower().startswith(project_name.lower()) or
            project_name.lower().startswith(fund_project_name.lower())):
            
            matching_funding.append({
                'project': project_name,
                'funding_id': fund['Funding_ID'],
                'amount': int(fund['Amount']),
                'funding_source': fund['Funding_Source']
            })

# Calculate total funding
total_funding = sum(f['amount'] for f in matching_funding)

result = {
    'park_projects_completed_2022': park_projects_completed_2022,
    'matching_funding_records': matching_funding,
    'total_funding': total_funding,
    'count_projects': len(park_projects_completed_2022),
    'count_funding_records': len(matching_funding)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
