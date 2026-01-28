code = """import json
import re
from collections import defaultdict

# Open and read the civic documents file
with open('var_functions.query_db:20.json', 'r') as f:
    civic_docs = json.load(f)

# Open and read the funding data file  
with open('var_functions.query_db:12.json', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Extract project information with Spring 2022 start dates
spring_2022_projects = defaultdict(dict)

# Create a funding lookup by project name
funding_lookup = {record['Project_Name'].lower(): int(record['Amount']) for record in funding_data}

# Pattern to find projects with Spring 2022 dates
# Spring is March, April, May
spring_patterns = [
    r'(?i)(spring\s+2022)',
    r'(?i)(march\s+2022|april\s+2022|may\s+2022)',
    r'(?i)(2022-03|2022-04|2022-05)',
    r'(?i)(2022-spring)'
]

# Look for project names and their schedules in the text
for doc in civic_docs:
    text = doc['text']
    
    # Find all project schedules mentioning Spring 2022
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        # Look for project name patterns (capitalized titles, often with keywords)
        if re.match(r'^\s*[A-Z][a-zA-Z\s]+(?:\s+[A-Z][a-zA-Z\s]+)*\s*$', line.strip()) and len(line.strip()) > 10:
            # Skip common headers
            if not any(header in line.lower() for header in ['page', 'agenda item', 'capital improvement', 'disaster project', 'project schedule', 'project description']):
                current_project = line.strip()
        
        # Check if this line mentions Spring 2022 for construction/start
        if re.search(r'(?i)(begin construction|construction|construction:|advertise|award contract|complete design|design:|begin design|start)', line):
            for pattern in spring_patterns:
                if re.search(pattern, line):
                    if current_project:
                        spring_2022_projects[current_project]['mentioned_in'] = doc['filename']
                        spring_2022_projects[current_project]['line'] = line.strip()
                        break

print(f"\nFound {len(spring_2022_projects)} potential Spring 2022 projects")

# Display projects found
for i, (project, info) in enumerate(spring_2022_projects.items(), 1):
    print(f"{i}. {project}")
    if 'line' in info:
        print(f"   {info['line']}")

# Map projects to funding
print("\n" + "="*60)
print("MATCHING PROJECTS TO FUNDING:")
print("="*60)

matched_projects = []
total_funding = 0

for project_name in spring_2022_projects.keys():
    # Try exact match first
    amount = funding_lookup.get(project_name.lower())
    
    # Try common variations if no exact match
    if not amount:
        # Try without suffixes
        base_name = re.sub(r'\s*\(.*?\)\s*$', '', project_name)
        amount = funding_lookup.get(base_name.lower())
        
        # Try with different suffixes
        if not amount:
            suffixes = [' (FEMA Project)', ' (CalJPIA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)', ' Project']
            for suffix in suffixes:
                alt_name = base_name + suffix
                amount = funding_lookup.get(alt_name.lower())
                if amount:
                    break
    
    if amount:
        matched_projects.append({
            'project_name': project_name,
            'amount': amount,
            'info': spring_2022_projects[project_name]
        })
        total_funding += amount
        print(f"✓ {project_name}: ${amount:,}")
    else:
        print(f"✗ {project_name}: No funding match found")

print("\n" + "="*60)
print(f"SUMMARY:")
print(f"Total Spring 2022 projects: {len(matched_projects)}")
print(f"Total funding: ${total_funding:,}")
print("="*60)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
