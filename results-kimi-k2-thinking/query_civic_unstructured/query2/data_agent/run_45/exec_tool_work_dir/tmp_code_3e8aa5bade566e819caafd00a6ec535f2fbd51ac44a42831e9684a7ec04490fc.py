code = """import json

# Load data from the JSON files that contain our query results
with open('/tmp/tmpq0c3uww8.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmphv6u7l7_.json', 'r') as f:
    funding_data = json.load(f)

print('Loaded civic documents and funding data')

# Search for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    if 'completed' not in text.lower():
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith(('(', '•', '-')):
            continue
        
        line_lower = line.lower()
        if 'park' in line_lower and ('project' in line_lower or 'improvements' in line_lower or 'repairs' in line_lower):
            # Check if completed in 2022
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j]
                if '2022' in next_line and ('completed' in next_line.lower() or 'completion' in next_line.lower()):
                    park_projects_2022.append(line)
                    break

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))
print('Found', len(unique_park_projects), 'unique park projects completed in 2022')

# Build funding lookup dictionary
funding_lookup = {}
for fund in funding_data:
    project_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[project_name] = amount

# Match projects and calculate total funding
total_funding = 0
projects_matched = 0

for project in unique_park_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        projects_matched += 1
    else:
        # Try partial string matching
        project_words = set(project.lower().split())
        for fund_name, amount in funding_lookup.items():
            fund_words = set(fund_name.lower().split())
            overlap = project_words.intersection(fund_words)
            if len(overlap) >= 2:  # At least 2 words match
                total_funding += amount
                projects_matched += 1
                break

print('Total funding for park projects completed in 2022:', total_funding)
print('Projects matched with funding:', projects_matched)

# Return result in required format
result = str(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
