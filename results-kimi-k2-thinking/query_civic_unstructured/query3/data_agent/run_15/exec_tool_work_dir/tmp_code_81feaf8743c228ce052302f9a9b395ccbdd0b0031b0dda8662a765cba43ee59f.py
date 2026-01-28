code = """import json

# Load funding data
funding_data_path = var_functions.query_db_28
with open(funding_data_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(funding_records), 'funding records')

# Define emergency keywords
emergency_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning', 'siren']
federal_sources = ['federal assistance', 'government grant', 'state development grant']

# Find FEMA/emergency projects
fema_projects = []
for record in funding_records:
    project_name = record['Project_Name'].lower()
    funding_source = record['Funding_Source'].lower()
    
    is_emergency = any(keyword in project_name for keyword in emergency_keywords)
    is_federal = any(source in funding_source for source in federal_sources)
    has_agency = 'caloes' in project_name or 'caljpia' in project_name
    
    if is_emergency or is_federal or has_agency:
        fema_projects.append({
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount'])
        })

print('Found', len(fema_projects), 'FEMA/emergency projects')

# Now load civic docs to get status information
civic_data_path = var_functions.query_db_2
with open(civic_data_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')

# Create a mapping of project names to status
project_status_map = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    for line in lines:
        line = line.strip()
        
        # Look for project headers
        if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
            if (i+1 < len(lines) and 
                ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or 
                 'Project Description:' in lines[i+1])):
                current_project = line
                
                # Check if this is a FEMA/emergency project
                project_lower = current_project.lower()
                is_current_emergency = any(keyword in project_lower for keyword in emergency_keywords)
                
                if is_current_emergency and current_project not in project_status_map:
                    project_status_map[current_project] = 'Unknown'
        
        # Extract status if we have a current project
        if current_project:
            lower_line = line.lower()
            if 'under construction' in lower_line:
                project_status_map[current_project] = 'construction'
            elif 'construction was completed' in lower_line:
                project_status_map[current_project] = 'completed'
            elif 'design:' in lower_line and 'complete' not in lower_line:
                project_status_map[current_project] = 'design'
            elif 'not started' in lower_line:
                project_status_map[current_project] = 'not started'

print('Project status map size:', len(project_status_map))

# Combine funding data with status
final_results = []
for proj in fema_projects:
    project_name = proj['Project_Name']
    status = project_status_map.get(project_name, 'Unknown')
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

# Output in required format
print('\n__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
