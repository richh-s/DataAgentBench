code = """import json
import re

# Get the file paths from storage
funding_file_path = locals()['var_functions.query_db:5']
civic_file_path = locals()['var_functions.query_db:6']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup
funding_by_project = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if name:
        funding_by_project[name] = funding_by_project.get(name, 0) + amount

found_projects = []

# Process each document
for doc in civic_data:
    text = doc.get('text', '')
    
    # Look for projects with 2022 Spring dates
    # Pattern: Project name line followed by schedule with 2022 spring/march/april/may
    
    # Find all sections that contain Project Schedule
    schedule_sections = re.split(r'Project Schedule', text)
    
    for i in range(1, len(schedule_sections)):
        section = schedule_sections[i]
        
        # Look back to find the project name
        prev_section = schedule_sections[i-1]
        
        # Check if this schedule has 2022 and Spring/March/April/May
        if '2022' in section and any(x in section.lower() for x in ['spring', 'march', 'april', 'may']):
            
            # Extract project name from previous section (last line)
            prev_lines = [l.strip() for l in prev_section.split('\n') if l.strip()]
            project_name = None
            
            # Look for candidate project names (lines that are not too long and not headers)
            for line in reversed(prev_lines):
                if (len(line) < 100 and 
                    not any(skip in line.lower() for skip in ['page', 'agenda', 'item', 'public works', 'commission']) and
                    not any(keyword in line.lower() for keyword in ['update', 'schedule', 'description'])):
                    
                    project_name = line
                    break
            
            if project_name and project_name not in [p['name'] for p in found_projects]:
                # Extract the date
                date_match = re.search(r'(\d{4}[^\n]*)', section)
                date_str = date_match.group(1).strip()[:50] if date_match else 'Date found'
                
                found_projects.append({
                    'name': project_name,
                    'date': date_str
                })

# Now match with funding
matches = []
total_funding = 0

for proj in found_projects:
    proj_name = proj['name']
    
    # Exact match
    funding = funding_by_project.get(proj_name, 0)
    
    # Try partial match if no exact match
    if funding == 0:
        for funded_name, amount in funding_by_project.items():
            if (proj_name.lower() in funded_name.lower() or 
                funded_name.lower() in proj_name.lower()):
                funding = amount
                break
    
    if funding > 0:
        matches.append({
            'project': proj_name,
            'funding': funding,
            'date': proj['date']
        })
        total_funding += funding

result = {
    'spring_2022_projects_found': len(matches),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
