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
print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_data)}")

# Create a dictionary for funding lookup
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

print(f"\nFunding dictionary created with {len(funding_dict)} projects")

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
    
    # Look for project sections in the text
    # Common patterns: project names are often on their own line or followed by updates
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('Page ') or 'Agenda Item' in line:
            continue
            
        # Check if this line might be a project name (typically title case, not too short)
        if len(line) > 10 and (line.istitle() or (line[0].isupper() and len(line.split()) > 2)):
            
            # Look ahead for date patterns
            context_window = '\n'.join(lines[i:i+5])
            
            for pattern in spring_2022_patterns:
                if re.search(pattern, context_window, re.IGNORECASE):
                    # This project started in Spring 2022
                    project_name = line
                    if project_name not in [p['name'] for p in spring_projects]:
                        spring_projects.append({
                            'name': project_name,
                            'context': context_window[:200]
                        })
                    break

print(f"\n=== PROJECTS STARTING IN SPRING 2022 ===")
print(f"Found {len(spring_projects)} potential projects:")

for i, proj in enumerate(spring_projects, 1):
    print(f"{i}. {proj['name']}")
    print(f"   Context: {proj['context'][:100]}...")
    print()

# Now match with funding data
print("=== MATCHING WITH FUNDING DATA ===")
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
        print(f"✓ Exact match: {project_name} - ${amount:,}")
    else:
        # Try partial matching
        for funded_name, amount in funding_dict.items():
            # Check if one is contained in the other
            if (project_name.lower() in funded_name.lower() or 
                funded_name.lower() in project_name.lower()):
                matched_projects.append({
                    'name': project_name,
                    'funding': amount,
                    'match_type': 'partial',
                    'matched_with': funded_name
                })
                total_funding += amount
                print(f"✓ Partial match: {project_name}")
                print(f"  -> Matched with: {funded_name} - ${amount:,}")
                break

print(f"\n=== SUMMARY ===")
print(f"Total Spring 2022 projects found: {len(spring_projects)}")
print(f"Projects with funding data: {len(matched_projects)}")
print(f"Total funding: ${total_funding:,}")

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
