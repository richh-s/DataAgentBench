code = """import json

civic_docs_data = var_functions.query_db:10
funding_data = var_functions.query_db:7

# Handle file paths or direct data
if isinstance(civic_docs_data, str) and '.json' in civic_docs_data:
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_data

if isinstance(funding_data, str) and '.json' in funding_data:
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

# Create funding map
funding_map = {}
for record in funding_records:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[name] = amount

# Find Spring 2022 projects by looking for specific patterns
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Spring 2022 in the document
    if '2022-Spring' in text or 'Spring 2022' in text or '2022-March' in text or '2022-April' in text or '2022-May' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Project names are typically lines that:
            # 1. Start with capital letters
            # 2. Contain project-related keywords
            # 3. Are not too short
            if (line and line[0].isupper() and 
                any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Drainage', 'Resurfacing']) and
                len(line) > 15):
                spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding data
matched = []
total_funding = 0

for project in spring_projects:
    # Direct match
    if project in funding_map:
        funding = funding_map[project]
        matched.append({'name': project, 'funding': funding})
        total_funding += funding
    else:
        # Check for variations (project name with suffixes removed)
        for funded_name, amount in funding_map.items():
            # Remove common suffixes for comparison
            clean_project = project.replace('Project', '').strip()
            clean_funded = funded_name.replace('Project', '').replace('(FEMA Project)', '').strip()
            
            if clean_project in clean_funded or clean_funded in clean_project:
                if amount > 0:
                    matched.append({'name': project, 'funding': amount})
                    total_funding += amount
                break

# Get unique projects
unique_projects = []
seen = set()
for proj in matched:
    if proj['name'] not in seen:
        unique_projects.append(proj)
        seen.add(proj['name'])

result = {
    'num_projects': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
