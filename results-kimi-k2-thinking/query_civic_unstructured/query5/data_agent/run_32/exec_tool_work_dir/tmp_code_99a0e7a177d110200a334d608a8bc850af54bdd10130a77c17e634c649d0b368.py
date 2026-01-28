code = """import json, re, sys

# Load data from files
funding_path = '/tmp/tmp_hb9f3fdk.json'
civic_docs_path = '/tmp/tmp_cdv8r04p.json'

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Function to extract projects from text
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project name with status in parentheses
        if '(' in line and ')' in line and i + 4 < len(lines):
            # Extract name and status
            parts = line.rsplit('(', 1)
            if len(parts) == 2:
                name = parts[0].strip()
                status = parts[1].replace(')', '').strip().lower()
                
                # Check next lines for details
                next_lines = lines[i+1:i+5]
                details = {}
                
                for detail_line in next_lines:
                    detail_line = detail_line.strip()
                    if ':' in detail_line:
                        key, value = detail_line.split(':', 1)
                        details[key.strip()] = value.strip()
                
                # Check if we have required fields
                if 'topic' in details and 'type' in details and 'st' in details:
                    projects.append({
                        'name': name,
                        'topic': details['topic'],
                        'type': details['type'],
                        'status': status,
                        'st': details['st'],
                        'et': details.get('et', '')
                    })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    if text:
        projects = extract_projects(text)
        all_projects.extend(projects)

# Filter for disaster projects starting in 2022
filtered_projects = []
fema_pattern = re.compile(r'\((FEMA|CalJPIA|CalOES)\s*Project\)', re.IGNORECASE)

for proj in all_projects:
    if '2022' in proj['st']:
        # Check if it's a disaster project (either explicitly marked or has FEMA suffix)
        if proj['type'] == 'disaster' or fema_pattern.search(proj['name']):
            filtered_projects.append(proj)

# Remove duplicates by project name
unique_projects = {proj['name']: proj for proj in filtered_projects}

# Calculate total funding
total_funding = 0
matched_projects = []

for proj in unique_projects.values():
    proj_name = proj['name']
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        total_funding += amount
        matched_projects.append({
            'project_name': proj_name,
            'amount': amount
        })

result = {
    'total_funding_2022_disaster_projects': total_funding,
    'number_of_projects': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
