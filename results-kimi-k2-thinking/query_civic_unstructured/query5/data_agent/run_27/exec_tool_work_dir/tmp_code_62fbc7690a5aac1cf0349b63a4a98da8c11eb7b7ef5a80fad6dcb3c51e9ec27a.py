code = """import json
import re

# Load all funding data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load all civic documents
with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

# Create funding map (project name -> amount)
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Extract disaster projects that started in 2022
disaster_projects_2022 = []

# Patterns to identify disaster projects
disaster_markers = [
    '(FEMA Project)',
    '(CalOES Project)', 
    '(CalJPIA Project)',
    'FEMA/CalOES Project',
    'FEMA/CalJPIA Project',
    'CalOES Project',
    'CalJPIA Project'
]

# Keywords that indicate disaster recovery
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency warning', 'Woolsey Fire']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5:
            continue
        
        # Check if this line is a project name (usually doesn't start with bullet/arrow, reasonable length)
        # Project names are typically not too long and start with capital letters
        is_likely_project_name = (
            len(line) < 150 and 
            line[0].isupper() and
            not line.startswith('-') and
            not line.startswith('•') and
            not line.startswith('(')
        )
        
        if is_likely_project_name:
            # Check if it's a disaster project
            is_disaster = False
            
            # Check for explicit markers
            for marker in disaster_markers:
                if marker in line:
                    is_disaster = True
                    break
            
            # Check for keywords if not already marked
            if not is_disaster:
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        is_disaster = True
                        break
            
            if is_disaster:
                # Check if it started in 2022
                # Look in the project name itself
                if '2022' in line:
                    disaster_projects_2022.append(line)
                else:
                    # Look in surrounding context (next 10 lines)
                    context_start = max(0, i-2)
                    context_end = min(len(lines), i+15)
                    context = '\n'.join(lines[context_start:context_end])
                    
                    # Check for 2022 references in context
                    if '2022' in context:
                        # Check for schedule/update lines that mention 2022
                        if any(phrase in context for phrase in ['2022-', '2022 Spring', '2022 Fall', '2022 Summer', '2022 Winter']):
                            disaster_projects_2022.append(line)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

# Now match with funding data
total_funding = 0
matched_projects = []

for project in disaster_projects_2022:
    # Direct match
    if project in funding_map:
        amount = funding_map[project]
        total_funding += amount
        matched_projects.append((project, amount))
    else:
        # Try partial matching
        for funding_name, amount in funding_map.items():
            # Check if one contains the other
            if (project in funding_name or funding_name in project) and len(project) > 10:
                total_funding += amount
                matched_projects.append((funding_name, amount))
                break

# Get all FEMA/Disaster type projects from funding data that might not be captured above
fema_funding_projects = []
for project_name, amount in funding_map.items():
    if any(marker in project_name for marker in disaster_markers):
        fema_funding_projects.append((project_name, amount))

# Combine and deduplicate
all_disaster_funding = {}
for project, amount in matched_projects:
    all_disaster_funding[project] = amount

for project, amount in fema_funding_projects:
    if project not in all_disaster_funding:
        # Check if this project mentions 2022 in its name
        if '2022' in project:
            all_disaster_funding[project] = amount

# Calculate final total
total_funding = sum(all_disaster_funding.values())

# Prepare results
result = {
    "disaster_projects_found": len(disaster_projects_2022),
    "matched_funding_projects": len(all_disaster_funding),
    "total_funding": total_funding,
    "project_details": list(all_disaster_funding.items())
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'funding_count': 500, 'civic_count': 19, 'sample': ['2021 Annual Street Maintenance', 24000]}}

exec(code, env_args)
