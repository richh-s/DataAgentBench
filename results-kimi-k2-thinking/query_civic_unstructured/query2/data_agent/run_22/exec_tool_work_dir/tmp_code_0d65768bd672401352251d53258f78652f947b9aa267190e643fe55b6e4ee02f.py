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

# Extract park-related projects completed in 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if not line:
            continue
            
        # Detect project name (lines that are likely project titles)
        if (line and 
            not line.startswith('(cid:') and 
            not line.startswith('(') and 
            not any(keyword in line.lower() for keyword in ['updates:', 'project schedule:', 'project description:', 'recommended action:', 'discussion:']) and
            len(line) > 5 and len(line) < 150 and
            not line.startswith('Page') and
            not line.startswith('Agenda')):
            
            current_project = line
        
        # Check if current project has completion in 2022
        if current_project:
            # Look for completion patterns
            if ('Construction was completed' in line or 'construction was completed' in line) and '2022' in line:
                if 'park' in current_project.lower():
                    park_projects_completed_2022.append({
                        'project_name': current_project,
                        'status': 'completed',
                        'date_info': line,
                        'year': '2022'
                    })

# Match with funding data
matching_funding_records = []

for project in park_projects_completed_2022:
    project_name = project['project_name'].lower().strip()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower().strip()
        
        # Check for exact or partial match
        if fund_name == project_name.lower() or project_name.lower() == fund_name:
            matching_funding_records.append({
                'project': project['project_name'],
                'funding_id': fund['Funding_ID'],
                'amount': int(fund['Amount']),
                'funding_source': fund['Funding_Source']
            })

# Calculate total funding
total_funding = sum(f['amount'] for f in matching_funding_records)

result = {
    'total_funding': total_funding,
    'count_park_projects': len(park_projects_completed_2022),
    'count_funding_matches': len(matching_funding_records)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
