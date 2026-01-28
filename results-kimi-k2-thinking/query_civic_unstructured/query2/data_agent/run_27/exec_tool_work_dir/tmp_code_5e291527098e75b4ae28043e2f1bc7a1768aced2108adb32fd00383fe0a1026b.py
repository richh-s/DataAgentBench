code = """import json
import re

# Get the file paths from storage and read the data
civic_docs_path = locals()['var_functions.query_db:16']
funding_data_path = locals()['var_functions.query_db:17']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Initialize project list
projects = []

# Extract project information from civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Look for completion status with 2022
        if 'completed' in line_lower and '2022' in line:
            # Find project name - usually in previous lines
            project_name = None
            for j in range(i-1, max(0, i-10), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                    # Clean project name
                    project_name = prev_line.replace('•', '').replace('◦', '').strip()
                    if project_name and 'project' not in project_name.lower()[:30]:
                        break
            
            if project_name:
                projects.append({
                    'project_name': project_name,
                    'completion_date': '2022',
                    'status': 'completed'
                })
        
        # Also look for "Complete Construction: [Month] 2022"
        if 'complete construction' in line_lower and '2022' in line:
            project_name = None
            for j in range(i-1, max(0, i-10), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                    project_name = prev_line.replace('•', '').replace('◦', '').strip()
                    if project_name:
                        break
            
            if project_name and 'project' not in project_name.lower()[:30]:
                projects.append({
                    'project_name': project_name,
                    'completion_date': '2022',
                    'status': 'completed'
                })

print('Found ' + str(len(projects)) + ' projects completed in 2022')

# Check which ones are park-related
park_projects = []
for project in projects:
    name_lower = project['project_name'].lower()
    if 'park' in name_lower or 'playground' in name_lower:
        park_projects.append(project)

print('Found ' + str(len(park_projects)) + ' park-related projects completed in 2022')
if park_projects:
    print('Park projects: ' + str([p['project_name'] for p in park_projects]))

# Now match with funding data
print('\nMatching with funding data...')
total_funding = 0
funded_parks = []

for park in park_projects:
    park_name = park['project_name']
    
    # Look for matching funding records
    for funding in funding_data:
        funding_name = funding['Project_Name']
        
        # Check for exact match or similar names
        if (park_name.lower() in funding_name.lower() or 
            funding_name.lower() in park_name.lower() or
            park_name.lower().replace(' ', '') in funding_name.lower().replace(' ', '')):
            
            amount = int(funding['Amount'])
            total_funding += amount
            funded_parks.append({
                'project': park_name,
                'funded_as': funding_name,
                'amount': amount
            })
            break

print('Found ' + str(len(funded_parks)) + ' funded park projects')
print('Total funding: $' + str(total_funding))
print('Details: ' + str(funded_parks))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
