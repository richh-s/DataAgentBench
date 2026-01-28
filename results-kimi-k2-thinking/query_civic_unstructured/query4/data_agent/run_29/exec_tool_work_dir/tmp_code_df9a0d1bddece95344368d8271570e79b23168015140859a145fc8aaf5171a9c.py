code = """import json
import re
from collections import defaultdict

# Load funding data
funding_file = "functions.query_db_28"
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = "functions.query_db_24"
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print("=== DATA LOADED ===")
print("Funding records: " + str(len(funding_data)))
print("Civic documents: " + str(len(civic_data)))

# Create a dictionary for funding lookup
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

print("Funding dictionary created with " + str(len(funding_dict)) + " projects")

# Search for Spring 2022 projects in civic documents
spring_2022_patterns = [
    r'2022[-\s]Spring',
    r'2022[-\s]March',
    r'2022[-\s]April', 
    r'2022[-\s]May',
    r'Spring\s+2022',
    r'March\s+2022',
    r'April\s+2022',
    r'May\s+2022'
]

spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('Page ') or 'Agenda Item' in line:
            continue
            
        # Check if this looks like a project name (title case, reasonable length)
        if len(line) > 10 and (line.istitle() or (line[0].isupper() and len(line.split()) > 2)):
            
            # Look ahead for date patterns
            context_window = '\n'.join(lines[i:i+5])
            
            for pattern in spring_2022_patterns:
                if re.search(pattern, context_window, re.IGNORECASE):
                    project_name = line
                    # Avoid duplicates
                    if project_name not in [p['name'] for p in spring_projects]:
                        spring_projects.append({
                            'name': project_name,
                            'context': context_window[:200]
                        })
                    break

print("\n=== SPRING 2022 PROJECTS ===")
print("Found " + str(len(spring_projects)) + " potential projects")

# Match with funding data
matched_projects = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    
    # Direct match
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched_projects.append({
            'name': project_name,
            'funding': amount,
            'match_type': 'exact'
        })
        total_funding += amount
        print("MATCH: " + project_name + " - $" + str(amount))
    else:
        # Try partial matching
        for funded_name, amount in funding_dict.items():
            if (project_name.lower() in funded_name.lower() or 
                funded_name.lower() in project_name.lower()):
                matched_projects.append({
                    'name': project_name,
                    'funding': amount,
                    'match_type': 'partial',
                    'matched_with': funded_name
                })
                total_funding += amount
                print("PARTIAL MATCH: " + project_name + " -> " + funded_name + " - $" + str(amount))
                break

# Create result
result = {
    "project_count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
