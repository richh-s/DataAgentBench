code = """import json
import re
from collections import defaultdict

# Access the stored results
civic_docs_var = globals()['var_functions_query_db_0']
funding_var = globals()['var_functions_query_db_5']

# Load civic documents
civic_docs = json.loads(json.dumps(civic_docs_var)) if not isinstance(civic_docs_var, list) else civic_docs_var

# Load funding data
funding_data = json.loads(json.dumps(funding_var)) if not isinstance(funding_var, list) else funding_var

print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_data)} funding records')

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Common patterns: project names followed by schedules
    lines = text.split('\n')
    
    current_project = None
    project_schedule = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically bolded or followed by updates)
        if line and not line.startswith('(') and not line.startswith('cid:') and len(line) > 10:
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement', 'facility', 'structure']):
                if current_project:
                    # Save previous project
                    projects.append({
                        'project_name': current_project,
                        'schedule': project_schedule,
                        'source_file': filename
                    })
                current_project = line
                project_schedule = {}
        
        # Look for schedule information
        if 'Schedule:' in line or 'schedule:' in line:
            # Next few lines might contain dates
            continue
            
        # Look for specific date patterns
        if any(pattern in line for pattern in ['Begin', 'Start', 'Complete', 'Advertise']):
            # Extract year and season/month
            year_match = re.search(r'(20\d{2})', line)
            if year_match:
                year = year_match.group(1)
                if 'Spring' in line or 'March' in line or 'April' in line or 'May' in line:
                    project_schedule['st'] = f'{year}-Spring'
                elif 'Summer' in line or 'June' in line or 'July' in line or 'August' in line:
                    project_schedule['et'] = f'{year}-Summer'
                elif 'Fall' in line or 'September' in line or 'October' in line or 'November' in line:
                    project_schedule['et'] = f'{year}-Fall'
    
    # Add last project
    if current_project:
        projects.append({
            'project_name': current_project,
            'schedule': project_schedule,
            'source_file': filename
        })

# More robust extraction using regex patterns for projects
project_patterns = [
    r'([A-Z][^.\n]{10,}?(?:Project|Improvements|Repairs|Replacement|Facility|Structure)[^.\n]*)',
    r'([A-Z][^.\n]{15,}?(?:Road|Park|Drain|Bridge|Building)[^.\n]*)'
]

# Extract dates more carefully
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all potential project names
    for pattern in project_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            project_name = match.strip()
            if len(project_name) > 15 and len(project_name) < 200:
                # Look for schedule info near this project name
                project_pos = text.find(project_name)
                context = text[project_pos:project_pos + 500]
                
                # Check for Spring 2022 or 2022 Spring
                if re.search(r'2022[-\s]Spring|Spring[-\s]2022', context, re.IGNORECASE) or \
                   re.search(r'2022[-\s](March|April|May)', context, re.IGNORECASE):
                    spring_2022_projects.append({
                        'project_name': project_name,
                        'start_date': '2022-Spring',
                        'source': doc.get('filename')
                    })

# Clean up project names (remove common suffixes and prefixes)
cleaned_projects = []
for proj in spring_2022_projects:
    name = proj['project_name']
    # Remove common prefixes
    name = re.sub(r'^(cid:\d+\s*)+', '', name)
    name = re.sub(r'^[\-\*\•\d\.\s]+', '', name)
    name = name.strip()
    
    if name and len(name) > 10:
        proj['project_name_clean'] = name
        cleaned_projects.append(proj)

print(f'Found {len(cleaned_projects)} potential Spring 2022 projects')

# Show sample projects
for i, proj in enumerate(cleaned_projects[:10]):
    print(f"{i+1}. {proj['project_name_clean']}")

# Get unique project names
unique_projects = {}
for proj in cleaned_projects:
    name = proj['project_name_clean']
    if name not in unique_projects:
        unique_projects[name] = proj

spring_projects = list(unique_projects.values())
print(f'Unique Spring 2022 projects: {len(spring_projects)}')

print('__RESULT__:')
print(json.dumps({
    'spring_projects': spring_projects,
    'count': len(spring_projects),
    'sample_projects': [p['project_name_clean'] for p in spring_projects[:5]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}}

exec(code, env_args)
