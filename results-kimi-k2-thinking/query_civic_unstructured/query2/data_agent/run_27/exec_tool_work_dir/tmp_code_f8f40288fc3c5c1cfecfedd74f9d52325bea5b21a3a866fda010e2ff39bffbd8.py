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
                    break
            
            if project_name:
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
    if 'park' in name_lower:
        park_projects.append(project)

print('Found ' + str(len(park_projects)) + ' park-related projects completed in 2022')

# List the park projects found
if park_projects:
    for p in park_projects:
        print('Park project: ' + p['project_name'])

# Now match with funding data
print('Matching with funding data...')
total_funding = 0
funded_parks = []

for park in park_projects:
    park_name = park['project_name']
    
    # Look for matching funding records
    for funding in funding_data:
        funding_name = funding['Project_Name']
        
        # Check for exact match or similar names
        if (park_name.lower() in funding_name.lower() or 
            funding_name.lower() in park_name.lower()):
            
            amount = int(funding['Amount'])
            total_funding += amount
            funded_parks.append({
                'project': park_name,
                'funded_as': funding_name,
                'amount': amount
            })

print('Found ' + str(len(funded_parks)) + ' funded park projects')
print('Total funding: $' + str(total_funding))

# Show detailed results
for fp in funded_parks:
    print(fp['project'] + ' -> ' + fp['funded_as'] + ': $' + str(fp['amount']))

# Final result
result = {
    'total_funding': total_funding,
    'funded_park_projects': funded_parks
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
