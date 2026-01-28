code = """import json
import re

# Read the filtered civic documents that contain Spring 2022
civic_file = locals()['var_functions.query_db:26']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Read all funding data
funding_file = locals()['var_functions.query_db:24']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Documents with Spring 2022:', len(civic_docs))
print('Total funding records:', len(funding_records))

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec['Project_Name'].lower().strip()
    amt = int(rec['Amount'])
    funding_map[name] = amt

# Extract project names from documents
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split into sections
    parts = re.split(r'(?:_|cid:|cid:131)', text)
    
    for part in parts:
        part = part.strip()
        if len(part) < 50:
            continue
        
        # Check for Spring 2022 construction start
        if re.search(r'(?i)begin[^\n]*spring[^\n]*2022', part):
            # Get project name from preceding text or first line
            lines = part.split('\n')
            for line in lines[:3]:
                line = line.strip()
                if line and not line.startswith('(') and len(line) < 100:
                    spring_projects.append(line.lower())
                    break

print('Projects with Spring 2022 start:', len(spring_projects))

# Find funding matches
matches = []
matched_names = set()

for proj_name in spring_projects:
    if proj_name in funding_map:
        amount = funding_map[proj_name]
        if proj_name not in matched_names:
            matches.append({
                'name': proj_name,
                'funding': amount
            })
            matched_names.add(proj_name)

# Calculate totals
total_funding = sum(m['funding'] for m in matches)

print('Matched projects:', len(matches))
print('Total funding:', total_funding)

result = {
    'project_count': len(matches),
    'total_funding': total_funding,
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
