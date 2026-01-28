code = """import json
import re

# Read the civic documents
civic_docs_file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract projects from text
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('---') or 'Agenda Item' in line or 'Page ' in line:
            continue
        
        # Look for lines that might be project names
        # Not starting with common bullet/list characters, reasonable length
        if (len(line) > 5 and len(line) < 150 and 
            not line[0] in '-*+([{' and
            'PROJECTS' not in line.upper() and
            i < len(lines) - 1):
            
            # Check if next line contains project indicators
            next_line = lines[i+1].strip() if i+1 < len(lines) else ''
            next_next_line = lines[i+2].strip() if i+2 < len(lines) else ''
            
            if ('Updates:' in next_line or 'Project Schedule:' in next_line or 
                'Updates:' in next_next_line or 'Project' in line):
                
                project_name = line
                status = 'unknown'
                completion_date = None
                topics = []
                
                # Look ahead for status and completion info
                for j in range(i+1, min(i+15, len(lines))):
                    check_line = lines[j].strip()
                    
                    # Check for completion
                    if 'completed' in check_line.lower() or 'Complete Construction:' in check_line:
                        status = 'completed'
                        # Extract year
                        year_match = re.search(r'\b202[0-9]\b', check_line)
                        if year_match:
                            completion_date = year_match.group()
                    
                    # Check for construction phase
                    elif 'under construction' in check_line.lower():
                        if status == 'unknown':
                            status = 'construction'
                    
                    # Check for design phase  
                    elif 'Complete Design:' in check_line:
                        if status == 'unknown':
                            status = 'design'
                    
                    # Check for not started
                    elif 'Not Started' in check_line:
                        if status == 'unknown':
                            status = 'not started'
                
                # Determine topics from project name
                project_lower = project_name.lower()
                if 'park' in project_lower:
                    topics.append('park')
                if 'road' in project_lower or 'street' in project_lower:
                    topics.append('road')
                if 'drain' in project_lower:
                    topics.append('drainage')
                if 'fire' in project_lower:
                    topics.append('fire')
                if 'fema' in project_lower:
                    topics.append('FEMA')
                
                # Only add if we found at least one topic
                if topics:
                    projects.append({
                        'Project_Name': project_name,
                        'topics': ','.join(topics),
                        'status': status,
                        'et': completion_date
                    })
    
    return projects

# Extract all projects from documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for project in all_projects:
    if ('park' in project['topics'] and 
        project['status'] == 'completed' and 
        project['et'] and 
        project['et'] == '2022'):
        park_projects_2022.append(project)

# Create lookup for funding
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '').strip()
    funding_lookup[key] = int(item['Amount'])

# Find matching funding
total_funding = 0
matched_projects = []

for project in park_projects_2022:
    project_name = project['Project_Name']
    project_key = project_name.lower().replace(' ', '').strip()
    
    amount = 0
    if project_key in funding_lookup:
        amount = funding_lookup[project_key]
    else:
        # Try without suffixes in parentheses
        clean_key = re.sub(r'\(.*\)', '', project_key).strip()
        if clean_key in funding_lookup:
            amount = funding_lookup[clean_key]
        else:
            # Fuzzy matching
            project_lower = project_name.lower()
            for funding_name, funding_amount in funding_lookup.items():
                if (project_lower in funding_name.lower() or 
                    funding_name.lower() in project_lower):
                    amount = funding_amount
                    break
    
    if amount > 0:
        matched_projects.append({
            'project': project_name,
            'amount': amount
        })
        total_funding += amount

result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
