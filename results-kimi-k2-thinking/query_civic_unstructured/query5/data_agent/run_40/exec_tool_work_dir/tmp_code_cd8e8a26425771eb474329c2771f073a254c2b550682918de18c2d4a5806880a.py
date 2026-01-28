code = """import json
import re

civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded files')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_lookup[project_name] = amount

# Find disaster projects that started in 2022
total_funding = 0
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern matching for disaster projects with dates
    # Look for FEMA/CalJPIA/CalOES projects
    patterns = [
        r'([A-Za-z\s\-]+\(FEMA Project\))[^\n]*(?:\n[^\n]*){0,10}?st:[^\n]*2022',
        r'([A-Za-z\s\-]+\(CalJPIA Project\))[^\n]*(?:\n[^\n]*){0,10}?st:[^\n]*2022',
        r'([A-Za-z\s\-]+\(CalOES Project\))[^\n]*(?:\n[^\n]*){0,10}?st:[^\n]*2022',
        r'([A-Za-z\s\-]+FEMA/CalOES[^\n]*Project[^\n]*(?:\n[^\n]*){0,10}?st:[^\n]*2022'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.strip()
            amount = funding_lookup.get(project_name, 0)
            if amount > 0:
                total_funding += amount
                found_projects.append({
                    'name': project_name,
                    'amount': amount
                })

print('\nFound projects:', len(found_projects))
print('Total funding:', total_funding)

for p in found_projects:
    print(f"  {p['name']}: ${p['amount']}")

result = {
    'total_funding': total_funding,
    'project_count': len(found_projects),
    'projects': found_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
