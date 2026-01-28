code = """import json
import re

# Get the file paths using locals()
civic_docs_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:20']

# Load the data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_dict = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_dict[project_name] = funding_dict.get(project_name, 0) + amount

# Function to extract projects with dates
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    capturing = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip headers
        if any(hdr in line for hdr in ['Capital Improvement', 'Disaster Recovery', 'Projects (', 'Page ']):
            if current_project:
                projects.append(current_project)
                current_project = None
            capturing = False
            continue
        
        # Look for project name pattern (standalone title-like line)
        if (len(line) < 100 and
            not line.startswith('(') and
            not line.startswith('cid:') and
            not any(label in line for label in ['Updates:', 'Schedule:', 'To:', 'From:', 'Subject:', 'Date:']) and
            not line.isupper()):
            
            # Check if next lines contain project indicators
            next_lines = [l.strip() for l in lines[lines.index(line)+1:lines.index(line)+4] if l.strip()]
            if any('Updates:' in nl or 'Schedule:' in nl or '(cid:' in nl for nl in next_lines):
                if current_project:
                    projects.append(current_project)
                current_project = {'name': line, 'dates': []}
                capturing = True
                continue
        
        # Capture dates if we're in a project section
        if capturing and current_project:
            # Look for date patterns
            date_patterns = [
                r'(?:Begin|Start|Construction|Design|Advertise|Complete)[\s\w]*:\s*([A-Za-z\s]+(?:\d{4}|\d{2}))',
                r'(?:Spring|Fall|Summer|Winter)\s+\d{4}',
                r'(?:January|February|March|April|May|June|July|August|September|October|November|December)[\s\d-]+'
            ]
            
            for pattern in date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        current_project['dates'].append(match.strip() if isinstance(match, str) else match[0].strip())
    
    if current_project:
        projects.append(current_project)
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

# Find Spring 2022 projects
spring_2022_names = set()
for project in all_projects:
    for date_str in project['dates']:
        if '2022' in date_str:
            if any(season in date_str.lower() for season in ['spring', 'march', 'april', 'may']):
                spring_2022_names.add(project['name'])
                break

# Match with funding
matched_projects = {}
for project_name in spring_2022_names:
    for funded_name in funding_dict:
        # Simple matching - check if one contains the other
        if (project_name.lower() in funded_name.lower() or 
            funded_name.lower() in project_name.lower() or
            any(part.lower() in funded_name.lower() for part in project_name.split() if len(part) > 5)):
            matched_projects[project_name] = funding_dict[funded_name]
            break

# Result
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

result = {
    "total_projects": total_projects,
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
